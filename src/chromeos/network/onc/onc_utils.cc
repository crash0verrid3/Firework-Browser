// Copyright (c) 2012 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#include "chromeos/network/onc/onc_utils.h"

#include "base/base64.h"
#include "base/json/json_reader.h"
#include "base/logging.h"
#include "base/metrics/histogram.h"
#include "base/strings/string_number_conversions.h"
#include "base/strings/string_util.h"
#include "base/values.h"
#include "chromeos/network/network_event_log.h"
#include "chromeos/network/onc/onc_mapper.h"
#include "chromeos/network/onc/onc_signature.h"
#include "chromeos/network/onc/onc_utils.h"
#include "chromeos/network/onc/onc_validator.h"
#include "components/device_event_log/device_event_log.h"
#include "components/proxy_config/proxy_config_dictionary.h"
#include "crypto/encryptor.h"
#include "crypto/hmac.h"
#include "crypto/symmetric_key.h"
#include "net/base/host_port_pair.h"
#include "net/cert/pem_tokenizer.h"
#include "net/cert/x509_certificate.h"
#include "net/proxy/proxy_bypass_rules.h"
#include "net/proxy/proxy_config.h"
#include "net/proxy/proxy_server.h"
#include "url/url_constants.h"

using namespace ::onc;

namespace chromeos {
namespace onc {

namespace {

const char kUnableToDecrypt[] = "Unable to decrypt encrypted ONC";
const char kUnableToDecode[] = "Unable to decode encrypted ONC";

}  // namespace

const char kEmptyUnencryptedConfiguration[] =
    "{\"Type\":\"UnencryptedConfiguration\",\"NetworkConfigurations\":[],"
    "\"Certificates\":[]}";

scoped_ptr<base::DictionaryValue> ReadDictionaryFromJson(
    const std::string& json) {
  std::string error;
  base::Value* root = base::JSONReader::DeprecatedReadAndReturnError(
      json, base::JSON_ALLOW_TRAILING_COMMAS, nullptr, &error);

  base::DictionaryValue* dict_ptr = nullptr;
  if (!root || !root->GetAsDictionary(&dict_ptr)) {
    NET_LOG(ERROR) << "Invalid JSON Dictionary: " << error;
    delete root;
  }

  return make_scoped_ptr(dict_ptr);
}

scoped_ptr<base::DictionaryValue> Decrypt(const std::string& passphrase,
                                          const base::DictionaryValue& root) {
  const int kKeySizeInBits = 256;
  const int kMaxIterationCount = 500000;
  std::string onc_type;
  std::string initial_vector;
  std::string salt;
  std::string cipher;
  std::string stretch_method;
  std::string hmac_method;
  std::string hmac;
  int iterations;
  std::string ciphertext;

  if (!root.GetString(encrypted::kCiphertext, &ciphertext) ||
      !root.GetString(encrypted::kCipher, &cipher) ||
      !root.GetString(encrypted::kHMAC, &hmac) ||
      !root.GetString(encrypted::kHMACMethod, &hmac_method) ||
      !root.GetString(encrypted::kIV, &initial_vector) ||
      !root.GetInteger(encrypted::kIterations, &iterations) ||
      !root.GetString(encrypted::kSalt, &salt) ||
      !root.GetString(encrypted::kStretch, &stretch_method) ||
      !root.GetString(toplevel_config::kType, &onc_type) ||
      onc_type != toplevel_config::kEncryptedConfiguration) {
    NET_LOG(ERROR) << "Encrypted ONC malformed.";
    return nullptr;
  }

  if (hmac_method != encrypted::kSHA1 ||
      cipher != encrypted::kAES256 ||
      stretch_method != encrypted::kPBKDF2) {
    NET_LOG(ERROR) << "Encrypted ONC unsupported encryption scheme.";
    return nullptr;
  }

  // Make sure iterations != 0, since that's not valid.
  if (iterations == 0) {
    NET_LOG(ERROR) << kUnableToDecrypt;
    return nullptr;
  }

  // Simply a sanity check to make sure we can't lock up the machine
  // for too long with a huge number (or a negative number).
  if (iterations < 0 || iterations > kMaxIterationCount) {
    NET_LOG(ERROR) << "Too many iterations in encrypted ONC";
    return nullptr;
  }

  if (!base::Base64Decode(salt, &salt)) {
    NET_LOG(ERROR) << kUnableToDecode;
    return nullptr;
  }

  scoped_ptr<crypto::SymmetricKey> key(
      crypto::SymmetricKey::DeriveKeyFromPassword(crypto::SymmetricKey::AES,
                                                  passphrase,
                                                  salt,
                                                  iterations,
                                                  kKeySizeInBits));

  if (!base::Base64Decode(initial_vector, &initial_vector)) {
    NET_LOG(ERROR) << kUnableToDecode;
    return nullptr;
  }
  if (!base::Base64Decode(ciphertext, &ciphertext)) {
    NET_LOG(ERROR) << kUnableToDecode;
    return nullptr;
  }
  if (!base::Base64Decode(hmac, &hmac)) {
    NET_LOG(ERROR) << kUnableToDecode;
    return nullptr;
  }

  crypto::HMAC hmac_verifier(crypto::HMAC::SHA1);
  if (!hmac_verifier.Init(key.get()) ||
      !hmac_verifier.Verify(ciphertext, hmac)) {
    NET_LOG(ERROR) << kUnableToDecrypt;
    return nullptr;
  }

  crypto::Encryptor decryptor;
  if (!decryptor.Init(key.get(), crypto::Encryptor::CBC, initial_vector))  {
    NET_LOG(ERROR) << kUnableToDecrypt;
    return nullptr;
  }

  std::string plaintext;
  if (!decryptor.Decrypt(ciphertext, &plaintext)) {
    NET_LOG(ERROR) << kUnableToDecrypt;
    return nullptr;
  }

  scoped_ptr<base::DictionaryValue> new_root =
      ReadDictionaryFromJson(plaintext);
  if (!new_root) {
    NET_LOG(ERROR) << "Property dictionary malformed.";
    return nullptr;
  }

  return new_root.Pass();
}

std::string GetSourceAsString(ONCSource source) {
  switch (source) {
    case ONC_SOURCE_UNKNOWN:
      return "unknown";
    case ONC_SOURCE_NONE:
      return "none";
    case ONC_SOURCE_DEVICE_POLICY:
      return "device policy";
    case ONC_SOURCE_USER_POLICY:
      return "user policy";
    case ONC_SOURCE_USER_IMPORT:
      return "user import";
  }
  NOTREACHED() << "unknown ONC source " << source;
  return "unknown";
}

void ExpandField(const std::string& fieldname,
                 const StringSubstitution& substitution,
                 base::DictionaryValue* onc_object) {
  std::string user_string;
  if (!onc_object->GetStringWithoutPathExpansion(fieldname, &user_string))
    return;

  std::string login_id;
  if (substitution.GetSubstitute(substitutes::kLoginIDField, &login_id)) {
    base::ReplaceSubstringsAfterOffset(&user_string, 0,
                                       substitutes::kLoginIDField,
                                       login_id);
  }

  std::string email;
  if (substitution.GetSubstitute(substitutes::kEmailField, &email)) {
    base::ReplaceSubstringsAfterOffset(&user_string, 0,
                                       substitutes::kEmailField,
                                       email);
  }

  onc_object->SetStringWithoutPathExpansion(fieldname, user_string);
}

void ExpandStringsInOncObject(
    const OncValueSignature& signature,
    const StringSubstitution& substitution,
    base::DictionaryValue* onc_object) {
  if (&signature == &kEAPSignature) {
    ExpandField(eap::kAnonymousIdentity, substitution, onc_object);
    ExpandField(eap::kIdentity, substitution, onc_object);
  } else if (&signature == &kL2TPSignature ||
             &signature == &kOpenVPNSignature) {
    ExpandField(vpn::kUsername, substitution, onc_object);
  }

  // Recurse into nested objects.
  for (base::DictionaryValue::Iterator it(*onc_object); !it.IsAtEnd();
       it.Advance()) {
    base::DictionaryValue* inner_object = nullptr;
    if (!onc_object->GetDictionaryWithoutPathExpansion(it.key(), &inner_object))
      continue;

    const OncFieldSignature* field_signature =
        GetFieldSignature(signature, it.key());
    if (!field_signature)
      continue;

    ExpandStringsInOncObject(*field_signature->value_signature,
                             substitution, inner_object);
  }
}

void ExpandStringsInNetworks(const StringSubstitution& substitution,
                             base::ListValue* network_configs) {
  for (base::Value* entry : *network_configs) {
    base::DictionaryValue* network = nullptr;
    entry->GetAsDictionary(&network);
    DCHECK(network);
    ExpandStringsInOncObject(
        kNetworkConfigurationSignature, substitution, network);
  }
}

void FillInHexSSIDFieldsInOncObject(const OncValueSignature& signature,
                                    base::DictionaryValue* onc_object) {
  if (&signature == &kWiFiSignature)
    FillInHexSSIDField(onc_object);

  // Recurse into nested objects.
  for (base::DictionaryValue::Iterator it(*onc_object); !it.IsAtEnd();
       it.Advance()) {
    base::DictionaryValue* inner_object = nullptr;
    if (!onc_object->GetDictionaryWithoutPathExpansion(it.key(), &inner_object))
      continue;

    const OncFieldSignature* field_signature =
        GetFieldSignature(signature, it.key());
    if (!field_signature)
      continue;

    FillInHexSSIDFieldsInOncObject(*field_signature->value_signature,
                                   inner_object);
  }
}

void FillInHexSSIDField(base::DictionaryValue* wifi_fields) {
  std::string ssid_string;
  if (wifi_fields->HasKey(::onc::wifi::kHexSSID) ||
      !wifi_fields->GetStringWithoutPathExpansion(::onc::wifi::kSSID,
                                                  &ssid_string)) {
    return;
  }
  if (ssid_string.empty()) {
    NET_LOG(ERROR) << "Found empty SSID field.";
    return;
  }
  wifi_fields->SetStringWithoutPathExpansion(
      ::onc::wifi::kHexSSID,
      base::HexEncode(ssid_string.c_str(), ssid_string.size()));
}

namespace {

class OncMaskValues : public Mapper {
 public:
  static scoped_ptr<base::DictionaryValue> Mask(
      const OncValueSignature& signature,
      const base::DictionaryValue& onc_object,
      const std::string& mask) {
    OncMaskValues masker(mask);
    bool unused_error;
    return masker.MapObject(signature, onc_object, &unused_error);
  }

 protected:
  explicit OncMaskValues(const std::string& mask)
      : mask_(mask) {
  }

  scoped_ptr<base::Value> MapField(const std::string& field_name,
                                   const OncValueSignature& object_signature,
                                   const base::Value& onc_value,
                                   bool* found_unknown_field,
                                   bool* error) override {
    if (FieldIsCredential(object_signature, field_name)) {
      return scoped_ptr<base::Value>(new base::StringValue(mask_));
    } else {
      return Mapper::MapField(field_name, object_signature, onc_value,
                              found_unknown_field, error);
    }
  }

  // Mask to insert in place of the sensitive values.
  std::string mask_;
};

}  // namespace

scoped_ptr<base::DictionaryValue> MaskCredentialsInOncObject(
    const OncValueSignature& signature,
    const base::DictionaryValue& onc_object,
    const std::string& mask) {
  return OncMaskValues::Mask(signature, onc_object, mask);
}

namespace {

std::string DecodePEM(const std::string& pem_encoded) {
  // The PEM block header used for DER certificates
  const char kCertificateHeader[] = "CERTIFICATE";

  // This is an older PEM marker for DER certificates.
  const char kX509CertificateHeader[] = "X509 CERTIFICATE";

  std::vector<std::string> pem_headers;
  pem_headers.push_back(kCertificateHeader);
  pem_headers.push_back(kX509CertificateHeader);

  net::PEMTokenizer pem_tokenizer(pem_encoded, pem_headers);
  std::string decoded;
  if (pem_tokenizer.GetNext()) {
    decoded = pem_tokenizer.data();
  } else {
    // If we failed to read the data as a PEM file, then try plain base64 decode
    // in case the PEM marker strings are missing. For this to work, there has
    // to be no white space, and it has to only contain the base64-encoded data.
    if (!base::Base64Decode(pem_encoded, &decoded)) {
      LOG(ERROR) << "Unable to base64 decode X509 data: " << pem_encoded;
      return std::string();
    }
  }
  return decoded;
}

CertPEMsByGUIDMap GetServerAndCACertsByGUID(
    const base::ListValue& certificates) {
  CertPEMsByGUIDMap certs_by_guid;
  for (const base::Value* entry : certificates) {
    const base::DictionaryValue* cert = nullptr;
    entry->GetAsDictionary(&cert);

    std::string guid;
    cert->GetStringWithoutPathExpansion(certificate::kGUID, &guid);
    std::string cert_type;
    cert->GetStringWithoutPathExpansion(certificate::kType, &cert_type);
    if (cert_type != certificate::kServer &&
        cert_type != certificate::kAuthority) {
      continue;
    }
    std::string x509_data;
    cert->GetStringWithoutPathExpansion(certificate::kX509, &x509_data);

    std::string der = DecodePEM(x509_data);
    std::string pem;
    if (der.empty() || !net::X509Certificate::GetPEMEncodedFromDER(der, &pem)) {
      LOG(ERROR) << "Certificate with GUID " << guid
                 << " is not in PEM encoding.";
      continue;
    }
    certs_by_guid[guid] = pem;
  }

  return certs_by_guid;
}

void FillInHexSSIDFieldsInNetworks(base::ListValue* network_configs) {
  for (base::Value* entry : *network_configs) {
    base::DictionaryValue* network = nullptr;
    entry->GetAsDictionary(&network);
    DCHECK(network);
    FillInHexSSIDFieldsInOncObject(kNetworkConfigurationSignature, network);
  }
}

}  // namespace

bool ParseAndValidateOncForImport(const std::string& onc_blob,
                                  ONCSource onc_source,
                                  const std::string& passphrase,
                                  base::ListValue* network_configs,
                                  base::DictionaryValue* global_network_config,
                                  base::ListValue* certificates) {
  network_configs->Clear();
  global_network_config->Clear();
  certificates->Clear();
  if (onc_blob.empty())
    return true;

  scoped_ptr<base::DictionaryValue> toplevel_onc =
      ReadDictionaryFromJson(onc_blob);
  if (!toplevel_onc) {
    LOG(ERROR) << "ONC loaded from " << GetSourceAsString(onc_source)
               << " is not a valid JSON dictionary.";
    return false;
  }

  // Check and see if this is an encrypted ONC file. If so, decrypt it.
  std::string onc_type;
  toplevel_onc->GetStringWithoutPathExpansion(toplevel_config::kType,
                                              &onc_type);
  if (onc_type == toplevel_config::kEncryptedConfiguration) {
    toplevel_onc = Decrypt(passphrase, *toplevel_onc);
    if (!toplevel_onc) {
      LOG(ERROR) << "Couldn't decrypt the ONC from "
                 << GetSourceAsString(onc_source);
      return false;
    }
  }

  bool from_policy = (onc_source == ONC_SOURCE_USER_POLICY ||
                      onc_source == ONC_SOURCE_DEVICE_POLICY);

  // Validate the ONC dictionary. We are liberal and ignore unknown field
  // names and ignore invalid field names in kRecommended arrays.
  Validator validator(false,  // Ignore unknown fields.
                      false,  // Ignore invalid recommended field names.
                      true,   // Fail on missing fields.
                      from_policy);
  validator.SetOncSource(onc_source);

  Validator::Result validation_result;
  toplevel_onc = validator.ValidateAndRepairObject(
      &kToplevelConfigurationSignature,
      *toplevel_onc,
      &validation_result);

  if (from_policy) {
    UMA_HISTOGRAM_BOOLEAN("Enterprise.ONC.PolicyValidation",
                          validation_result == Validator::VALID);
  }

  bool success = true;
  if (validation_result == Validator::VALID_WITH_WARNINGS) {
    LOG(WARNING) << "ONC from " << GetSourceAsString(onc_source)
                 << " produced warnings.";
    success = false;
  } else if (validation_result == Validator::INVALID || !toplevel_onc) {
    LOG(ERROR) << "ONC from " << GetSourceAsString(onc_source)
               << " is invalid and couldn't be repaired.";
    return false;
  }

  base::ListValue* validated_certs = nullptr;
  if (toplevel_onc->GetListWithoutPathExpansion(toplevel_config::kCertificates,
                                                &validated_certs)) {
    certificates->Swap(validated_certs);
  }

  base::ListValue* validated_networks = nullptr;
  if (toplevel_onc->GetListWithoutPathExpansion(
          toplevel_config::kNetworkConfigurations, &validated_networks)) {
    FillInHexSSIDFieldsInNetworks(validated_networks);

    CertPEMsByGUIDMap server_and_ca_certs =
        GetServerAndCACertsByGUID(*certificates);

    if (!ResolveServerCertRefsInNetworks(server_and_ca_certs,
                                         validated_networks)) {
      LOG(ERROR) << "Some certificate references in the ONC policy for source "
                 << GetSourceAsString(onc_source) << " could not be resolved.";
      success = false;
    }

    network_configs->Swap(validated_networks);
  }

  base::DictionaryValue* validated_global_config = nullptr;
  if (toplevel_onc->GetDictionaryWithoutPathExpansion(
          toplevel_config::kGlobalNetworkConfiguration,
          &validated_global_config)) {
    global_network_config->Swap(validated_global_config);
  }

  return success;
}

scoped_refptr<net::X509Certificate> DecodePEMCertificate(
    const std::string& pem_encoded) {
  std::string decoded = DecodePEM(pem_encoded);
  scoped_refptr<net::X509Certificate> cert =
      net::X509Certificate::CreateFromBytes(decoded.data(), decoded.size());
  LOG_IF(ERROR, !cert.get()) << "Couldn't create certificate from X509 data: "
                             << decoded;
  return cert;
}

namespace {

bool GUIDRefToPEMEncoding(const CertPEMsByGUIDMap& certs_by_guid,
                          const std::string& guid_ref,
                          std::string* pem_encoded) {
  CertPEMsByGUIDMap::const_iterator it = certs_by_guid.find(guid_ref);
  if (it == certs_by_guid.end()) {
    LOG(ERROR) << "Couldn't resolve certificate reference " << guid_ref;
    return false;
  }
  *pem_encoded = it->second;
  if (pem_encoded->empty()) {
    LOG(ERROR) << "Couldn't PEM-encode certificate with GUID " << guid_ref;
    return false;
  }
  return true;
}

bool ResolveSingleCertRef(const CertPEMsByGUIDMap& certs_by_guid,
                          const std::string& key_guid_ref,
                          const std::string& key_pem,
                          base::DictionaryValue* onc_object) {
  std::string guid_ref;
  if (!onc_object->GetStringWithoutPathExpansion(key_guid_ref, &guid_ref))
    return true;

  std::string pem_encoded;
  if (!GUIDRefToPEMEncoding(certs_by_guid, guid_ref, &pem_encoded))
    return false;

  onc_object->RemoveWithoutPathExpansion(key_guid_ref, nullptr);
  onc_object->SetStringWithoutPathExpansion(key_pem, pem_encoded);
  return true;
}

bool ResolveCertRefList(const CertPEMsByGUIDMap& certs_by_guid,
                        const std::string& key_guid_ref_list,
                        const std::string& key_pem_list,
                        base::DictionaryValue* onc_object) {
  const base::ListValue* guid_ref_list = nullptr;
  if (!onc_object->GetListWithoutPathExpansion(key_guid_ref_list,
                                               &guid_ref_list)) {
    return true;
  }

  scoped_ptr<base::ListValue> pem_list(new base::ListValue);
  for (const base::Value* entry : *guid_ref_list) {
    std::string guid_ref;
    entry->GetAsString(&guid_ref);

    std::string pem_encoded;
    if (!GUIDRefToPEMEncoding(certs_by_guid, guid_ref, &pem_encoded))
      return false;

    pem_list->AppendString(pem_encoded);
  }

  onc_object->RemoveWithoutPathExpansion(key_guid_ref_list, nullptr);
  onc_object->SetWithoutPathExpansion(key_pem_list, pem_list.release());
  return true;
}

bool ResolveSingleCertRefToList(const CertPEMsByGUIDMap& certs_by_guid,
                                const std::string& key_guid_ref,
                                const std::string& key_pem_list,
                                base::DictionaryValue* onc_object) {
  std::string guid_ref;
  if (!onc_object->GetStringWithoutPathExpansion(key_guid_ref, &guid_ref))
    return true;

  std::string pem_encoded;
  if (!GUIDRefToPEMEncoding(certs_by_guid, guid_ref, &pem_encoded))
    return false;

  scoped_ptr<base::ListValue> pem_list(new base::ListValue);
  pem_list->AppendString(pem_encoded);
  onc_object->RemoveWithoutPathExpansion(key_guid_ref, nullptr);
  onc_object->SetWithoutPathExpansion(key_pem_list, pem_list.release());
  return true;
}

// Resolves the reference list at |key_guid_refs| if present and otherwise the
// single reference at |key_guid_ref|. Returns whether the respective resolving
// was successful.
bool ResolveCertRefsOrRefToList(const CertPEMsByGUIDMap& certs_by_guid,
                                const std::string& key_guid_refs,
                                const std::string& key_guid_ref,
                                const std::string& key_pem_list,
                                base::DictionaryValue* onc_object) {
  if (onc_object->HasKey(key_guid_refs)) {
    if (onc_object->HasKey(key_guid_ref)) {
      LOG(ERROR) << "Found both " << key_guid_refs << " and " << key_guid_ref
                 << ". Ignoring and removing the latter.";
      onc_object->RemoveWithoutPathExpansion(key_guid_ref, nullptr);
    }
    return ResolveCertRefList(
        certs_by_guid, key_guid_refs, key_pem_list, onc_object);
  }

  // Only resolve |key_guid_ref| if |key_guid_refs| isn't present.
  return ResolveSingleCertRefToList(
      certs_by_guid, key_guid_ref, key_pem_list, onc_object);
}

bool ResolveServerCertRefsInObject(const CertPEMsByGUIDMap& certs_by_guid,
                                   const OncValueSignature& signature,
                                   base::DictionaryValue* onc_object) {
  if (&signature == &kCertificatePatternSignature) {
    if (!ResolveCertRefList(certs_by_guid,
                            client_cert::kIssuerCARef,
                            client_cert::kIssuerCAPEMs,
                            onc_object)) {
      return false;
    }
  } else if (&signature == &kEAPSignature) {
    if (!ResolveCertRefsOrRefToList(certs_by_guid,
                                    eap::kServerCARefs,
                                    eap::kServerCARef,
                                    eap::kServerCAPEMs,
                                    onc_object)) {
      return false;
    }
  } else if (&signature == &kIPsecSignature) {
    if (!ResolveCertRefsOrRefToList(certs_by_guid,
                                    ipsec::kServerCARefs,
                                    ipsec::kServerCARef,
                                    ipsec::kServerCAPEMs,
                                    onc_object)) {
      return false;
    }
  } else if (&signature == &kIPsecSignature ||
             &signature == &kOpenVPNSignature) {
    if (!ResolveSingleCertRef(certs_by_guid,
                              openvpn::kServerCertRef,
                              openvpn::kServerCertPEM,
                              onc_object) ||
        !ResolveCertRefsOrRefToList(certs_by_guid,
                                    openvpn::kServerCARefs,
                                    openvpn::kServerCARef,
                                    openvpn::kServerCAPEMs,
                                    onc_object)) {
      return false;
    }
  }

  // Recurse into nested objects.
  for (base::DictionaryValue::Iterator it(*onc_object); !it.IsAtEnd();
       it.Advance()) {
    base::DictionaryValue* inner_object = nullptr;
    if (!onc_object->GetDictionaryWithoutPathExpansion(it.key(), &inner_object))
      continue;

    const OncFieldSignature* field_signature =
        GetFieldSignature(signature, it.key());
    if (!field_signature)
      continue;

    if (!ResolveServerCertRefsInObject(certs_by_guid,
                                       *field_signature->value_signature,
                                       inner_object)) {
      return false;
    }
  }
  return true;
}

}  // namespace

bool ResolveServerCertRefsInNetworks(const CertPEMsByGUIDMap& certs_by_guid,
                                     base::ListValue* network_configs) {
  bool success = true;
  for (base::ListValue::iterator it = network_configs->begin();
       it != network_configs->end(); ) {
    base::DictionaryValue* network = nullptr;
    (*it)->GetAsDictionary(&network);
    if (!ResolveServerCertRefsInNetwork(certs_by_guid, network)) {
      std::string guid;
      network->GetStringWithoutPathExpansion(network_config::kGUID, &guid);
      // This might happen even with correct validation, if the referenced
      // certificate couldn't be imported.
      LOG(ERROR) << "Couldn't resolve some certificate reference of network "
                 << guid;
      it = network_configs->Erase(it, nullptr);
      success = false;
      continue;
    }
    ++it;
  }
  return success;
}

bool ResolveServerCertRefsInNetwork(const CertPEMsByGUIDMap& certs_by_guid,
                                    base::DictionaryValue* network_config) {
  return ResolveServerCertRefsInObject(certs_by_guid,
                                       kNetworkConfigurationSignature,
                                       network_config);
}

NetworkTypePattern NetworkTypePatternFromOncType(const std::string& type) {
  if (type == ::onc::network_type::kAllTypes)
    return NetworkTypePattern::Default();
  if (type == ::onc::network_type::kCellular)
    return NetworkTypePattern::Cellular();
  if (type == ::onc::network_type::kEthernet)
    return NetworkTypePattern::Ethernet();
  if (type == ::onc::network_type::kVPN)
    return NetworkTypePattern::VPN();
  if (type == ::onc::network_type::kWiFi)
    return NetworkTypePattern::WiFi();
  if (type == ::onc::network_type::kWimax)
    return NetworkTypePattern::Wimax();
  if (type == ::onc::network_type::kWireless)
    return NetworkTypePattern::Wireless();
  NOTREACHED() << "Unrecognized ONC type: " << type;
  return NetworkTypePattern::Default();
}

bool IsRecommendedValue(const base::DictionaryValue* onc,
                        const std::string& property_key) {
  std::string property_basename, recommended_property_key;
  size_t pos = property_key.find_last_of('.');
  if (pos != std::string::npos) {
    // 'WiFi.AutoConnect' -> 'AutoConnect', 'WiFi.Recommended'
    property_basename = property_key.substr(pos + 1);
    recommended_property_key =
        property_key.substr(0, pos + 1) + ::onc::kRecommended;
  } else {
    // 'Name' -> 'Name', 'Recommended'
    property_basename = property_key;
    recommended_property_key = ::onc::kRecommended;
  }

  const base::ListValue* recommended_keys = nullptr;
  return (onc->GetList(recommended_property_key, &recommended_keys) &&
          recommended_keys->Find(base::StringValue(property_basename)) !=
          recommended_keys->end());
}

namespace {

const char kDirectScheme[] = "direct";
const char kQuicScheme[] = "quic";
const char kSocksScheme[] = "socks";
const char kSocks4Scheme[] = "socks4";
const char kSocks5Scheme[] = "socks5";

net::ProxyServer ConvertOncProxyLocationToHostPort(
    net::ProxyServer::Scheme default_proxy_scheme,
    const base::DictionaryValue& onc_proxy_location) {
  std::string host;
  onc_proxy_location.GetStringWithoutPathExpansion(::onc::proxy::kHost, &host);
  // Parse |host| according to the format [<scheme>"://"]<server>[":"<port>].
  net::ProxyServer proxy_server =
      net::ProxyServer::FromURI(host, default_proxy_scheme);
  int port = 0;
  onc_proxy_location.GetIntegerWithoutPathExpansion(::onc::proxy::kPort, &port);

  // Replace the port parsed from |host| by the provided |port|.
  return net::ProxyServer(
      proxy_server.scheme(),
      net::HostPortPair(proxy_server.host_port_pair().host(),
                        static_cast<uint16>(port)));
}

void AppendProxyServerForScheme(const base::DictionaryValue& onc_manual,
                                const std::string& onc_scheme,
                                std::string* spec) {
  const base::DictionaryValue* onc_proxy_location = nullptr;
  if (!onc_manual.GetDictionaryWithoutPathExpansion(onc_scheme,
                                                    &onc_proxy_location)) {
    return;
  }

  net::ProxyServer::Scheme default_proxy_scheme = net::ProxyServer::SCHEME_HTTP;
  std::string url_scheme;
  if (onc_scheme == ::onc::proxy::kFtp) {
    url_scheme = url::kFtpScheme;
  } else if (onc_scheme == ::onc::proxy::kHttp) {
    url_scheme = url::kHttpScheme;
  } else if (onc_scheme == ::onc::proxy::kHttps) {
    url_scheme = url::kHttpsScheme;
  } else if (onc_scheme == ::onc::proxy::kSocks) {
    default_proxy_scheme = net::ProxyServer::SCHEME_SOCKS4;
    url_scheme = kSocksScheme;
  } else {
    NOTREACHED();
  }

  net::ProxyServer proxy_server = ConvertOncProxyLocationToHostPort(
      default_proxy_scheme, *onc_proxy_location);

  ProxyConfigDictionary::EncodeAndAppendProxyServer(url_scheme, proxy_server,
                                                    spec);
}

net::ProxyBypassRules ConvertOncExcludeDomainsToBypassRules(
    const base::ListValue& onc_exclude_domains) {
  net::ProxyBypassRules rules;
  for (base::ListValue::const_iterator it = onc_exclude_domains.begin();
       it != onc_exclude_domains.end(); ++it) {
    std::string rule;
    (*it)->GetAsString(&rule);
    rules.AddRuleFromString(rule);
  }
  return rules;
}

std::string SchemeToString(net::ProxyServer::Scheme scheme) {
  switch (scheme) {
    case net::ProxyServer::SCHEME_DIRECT:
      return kDirectScheme;
    case net::ProxyServer::SCHEME_HTTP:
      return url::kHttpScheme;
    case net::ProxyServer::SCHEME_SOCKS4:
      return kSocks4Scheme;
    case net::ProxyServer::SCHEME_SOCKS5:
      return kSocks5Scheme;
    case net::ProxyServer::SCHEME_HTTPS:
      return url::kHttpsScheme;
    case net::ProxyServer::SCHEME_QUIC:
      return kQuicScheme;
    case net::ProxyServer::SCHEME_INVALID:
      break;
  }
  NOTREACHED();
  return "";
}

void SetProxyForScheme(const net::ProxyConfig::ProxyRules& proxy_rules,
                       const std::string& scheme,
                       const std::string& onc_scheme,
                       base::DictionaryValue* dict) {
  const net::ProxyList* proxy_list = nullptr;
  if (proxy_rules.type == net::ProxyConfig::ProxyRules::TYPE_SINGLE_PROXY) {
    proxy_list = &proxy_rules.single_proxies;
  } else if (proxy_rules.type ==
             net::ProxyConfig::ProxyRules::TYPE_PROXY_PER_SCHEME) {
    proxy_list = proxy_rules.MapUrlSchemeToProxyList(scheme);
  }
  if (!proxy_list || proxy_list->IsEmpty())
    return;
  const net::ProxyServer& server = proxy_list->Get();
  scoped_ptr<base::DictionaryValue> url_dict(new base::DictionaryValue);
  std::string host = server.host_port_pair().host();

  // For all proxy types except SOCKS, the default scheme of the proxy host is
  // HTTP.
  net::ProxyServer::Scheme default_scheme =
      (onc_scheme == ::onc::proxy::kSocks) ? net::ProxyServer::SCHEME_SOCKS4
                                           : net::ProxyServer::SCHEME_HTTP;
  // Only prefix the host with a non-default scheme.
  if (server.scheme() != default_scheme)
    host = SchemeToString(server.scheme()) + "://" + host;
  url_dict->SetStringWithoutPathExpansion(::onc::proxy::kHost, host);
  url_dict->SetIntegerWithoutPathExpansion(::onc::proxy::kPort,
                                           server.host_port_pair().port());
  dict->SetWithoutPathExpansion(onc_scheme, url_dict.release());
}

}  // namespace

scoped_ptr<base::DictionaryValue> ConvertOncProxySettingsToProxyConfig(
    const base::DictionaryValue& onc_proxy_settings) {
  std::string type;
  onc_proxy_settings.GetStringWithoutPathExpansion(::onc::proxy::kType, &type);
  scoped_ptr<base::DictionaryValue> proxy_dict;

  if (type == ::onc::proxy::kDirect) {
    proxy_dict.reset(ProxyConfigDictionary::CreateDirect());
  } else if (type == ::onc::proxy::kWPAD) {
    proxy_dict.reset(ProxyConfigDictionary::CreateAutoDetect());
  } else if (type == ::onc::proxy::kPAC) {
    std::string pac_url;
    onc_proxy_settings.GetStringWithoutPathExpansion(::onc::proxy::kPAC,
                                                     &pac_url);
    GURL url(pac_url);
    DCHECK(url.is_valid()) << "Invalid URL in ProxySettings.PAC";
    proxy_dict.reset(ProxyConfigDictionary::CreatePacScript(url.spec(), false));
  } else if (type == ::onc::proxy::kManual) {
    const base::DictionaryValue* manual_dict = nullptr;
    onc_proxy_settings.GetDictionaryWithoutPathExpansion(::onc::proxy::kManual,
                                                         &manual_dict);
    std::string manual_spec;
    AppendProxyServerForScheme(*manual_dict, ::onc::proxy::kFtp, &manual_spec);
    AppendProxyServerForScheme(*manual_dict, ::onc::proxy::kHttp, &manual_spec);
    AppendProxyServerForScheme(*manual_dict, ::onc::proxy::kSocks,
                               &manual_spec);
    AppendProxyServerForScheme(*manual_dict, ::onc::proxy::kHttps,
                               &manual_spec);

    const base::ListValue* exclude_domains = nullptr;
    net::ProxyBypassRules bypass_rules;
    if (onc_proxy_settings.GetListWithoutPathExpansion(
            ::onc::proxy::kExcludeDomains, &exclude_domains)) {
      bypass_rules.AssignFrom(
          ConvertOncExcludeDomainsToBypassRules(*exclude_domains));
    }
    proxy_dict.reset(ProxyConfigDictionary::CreateFixedServers(
        manual_spec, bypass_rules.ToString()));
  } else {
    NOTREACHED();
  }
  return proxy_dict.Pass();
}

scoped_ptr<base::DictionaryValue> ConvertProxyConfigToOncProxySettings(
    const base::DictionaryValue& proxy_config_value) {
  // Create a ProxyConfigDictionary from the DictionaryValue.
  scoped_ptr<ProxyConfigDictionary> proxy_config(
      new ProxyConfigDictionary(&proxy_config_value));

  // Create the result DictionaryValue and populate it.
  scoped_ptr<base::DictionaryValue> proxy_settings(new base::DictionaryValue);
  ProxyPrefs::ProxyMode mode;
  if (!proxy_config->GetMode(&mode))
    return nullptr;
  switch (mode) {
    case ProxyPrefs::MODE_DIRECT: {
      proxy_settings->SetStringWithoutPathExpansion(::onc::proxy::kType,
                                                    ::onc::proxy::kDirect);
      break;
    }
    case ProxyPrefs::MODE_AUTO_DETECT: {
      proxy_settings->SetStringWithoutPathExpansion(::onc::proxy::kType,
                                                    ::onc::proxy::kWPAD);
      break;
    }
    case ProxyPrefs::MODE_PAC_SCRIPT: {
      proxy_settings->SetStringWithoutPathExpansion(::onc::proxy::kType,
                                                    ::onc::proxy::kPAC);
      std::string pac_url;
      proxy_config->GetPacUrl(&pac_url);
      proxy_settings->SetStringWithoutPathExpansion(::onc::proxy::kPAC,
                                                    pac_url);
      break;
    }
    case ProxyPrefs::MODE_FIXED_SERVERS: {
      proxy_settings->SetString(::onc::proxy::kType, ::onc::proxy::kManual);
      scoped_ptr<base::DictionaryValue> manual(new base::DictionaryValue);
      std::string proxy_rules_string;
      if (proxy_config->GetProxyServer(&proxy_rules_string)) {
        net::ProxyConfig::ProxyRules proxy_rules;
        proxy_rules.ParseFromString(proxy_rules_string);
        SetProxyForScheme(proxy_rules, url::kFtpScheme, ::onc::proxy::kFtp,
                          manual.get());
        SetProxyForScheme(proxy_rules, url::kHttpScheme, ::onc::proxy::kHttp,
                          manual.get());
        SetProxyForScheme(proxy_rules, url::kHttpsScheme, ::onc::proxy::kHttps,
                          manual.get());
        SetProxyForScheme(proxy_rules, kSocksScheme, ::onc::proxy::kSocks,
                          manual.get());
      }
      proxy_settings->SetWithoutPathExpansion(::onc::proxy::kManual,
                                              manual.release());

      // Convert the 'bypass_list' string into dictionary entries.
      std::string bypass_rules_string;
      if (proxy_config->GetBypassList(&bypass_rules_string)) {
        net::ProxyBypassRules bypass_rules;
        bypass_rules.ParseFromString(bypass_rules_string);
        scoped_ptr<base::ListValue> exclude_domains(new base::ListValue);
        for (const net::ProxyBypassRules::Rule* rule : bypass_rules.rules())
          exclude_domains->AppendString(rule->ToString());
        if (!exclude_domains->empty()) {
          proxy_settings->SetWithoutPathExpansion(::onc::proxy::kExcludeDomains,
                                                  exclude_domains.release());
        }
      }
      break;
    }
    default: {
      LOG(ERROR) << "Unexpected proxy mode in Shill config: " << mode;
      return nullptr;
    }
  }
  return proxy_settings.Pass();
}

}  // namespace onc
}  // namespace chromeos
