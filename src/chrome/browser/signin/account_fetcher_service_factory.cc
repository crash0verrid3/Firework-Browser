// Copyright 2015 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#include "chrome/browser/signin/account_fetcher_service_factory.h"

#include "chrome/browser/profiles/profile.h"
#include "chrome/browser/signin/account_tracker_service_factory.h"
#include "chrome/browser/signin/chrome_signin_client_factory.h"
#include "chrome/browser/signin/profile_oauth2_token_service_factory.h"
#include "components/keyed_service/content/browser_context_dependency_manager.h"
#include "components/pref_registry/pref_registry_syncable.h"
#include "components/signin/core/browser/account_fetcher_service.h"
#include "components/signin/core/browser/profile_oauth2_token_service.h"

AccountFetcherServiceFactory::AccountFetcherServiceFactory()
    : BrowserContextKeyedServiceFactory(
        "AccountFetcherServiceFactory",
        BrowserContextDependencyManager::GetInstance()) {
  DependsOn(AccountTrackerServiceFactory::GetInstance());
  DependsOn(ChromeSigninClientFactory::GetInstance());
  DependsOn(ProfileOAuth2TokenServiceFactory::GetInstance());
}

AccountFetcherServiceFactory::~AccountFetcherServiceFactory() {}

// static
AccountFetcherService* AccountFetcherServiceFactory::GetForProfile(
    Profile* profile) {
  return static_cast<AccountFetcherService*>(
      GetInstance()->GetServiceForBrowserContext(profile, true));
}

// static
AccountFetcherServiceFactory* AccountFetcherServiceFactory::GetInstance() {
  return Singleton<AccountFetcherServiceFactory>::get();
}

void AccountFetcherServiceFactory::RegisterProfilePrefs(
    user_prefs::PrefRegistrySyncable* registry) {
  registry->RegisterInt64Pref(AccountFetcherService::kLastUpdatePref, 0);
}

KeyedService* AccountFetcherServiceFactory::BuildServiceInstanceFor(
    content::BrowserContext* context) const {
  Profile* profile = static_cast<Profile*>(context);
  AccountFetcherService* service = new AccountFetcherService();
  service->Initialize(ChromeSigninClientFactory::GetForProfile(profile),
                      ProfileOAuth2TokenServiceFactory::GetForProfile(profile),
                      AccountTrackerServiceFactory::GetForProfile(profile));
  return service;
}
