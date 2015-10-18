// Copyright 2013 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#ifndef CHROME_RENDERER_PEPPER_PNACL_TRANSLATION_RESOURCE_HOST_H_
#define CHROME_RENDERER_PEPPER_PNACL_TRANSLATION_RESOURCE_HOST_H_

#include <map>

#include "base/callback.h"
#include "ipc/ipc_platform_file.h"
#include "ipc/message_filter.h"
#include "ppapi/c/pp_bool.h"
#include "ppapi/c/pp_instance.h"
#include "ppapi/c/private/pp_file_handle.h"

namespace base {
class SingleThreadTaskRunner;
}

namespace nacl {
struct PnaclCacheInfo;
}

// A class to keep track of requests made to the browser for resources that the
// PNaCl translator needs (e.g. descriptors for the translator nexes, temp
// files, and cached translations).

// "Resource" might not be the best name for the various things that pnacl
// needs from the browser since "Resource" is a Pepper thing...
class PnaclTranslationResourceHost : public IPC::MessageFilter {
 public:
  typedef base::Callback<void(int32_t, bool, PP_FileHandle)>
          RequestNexeFdCallback;

  explicit PnaclTranslationResourceHost(
      scoped_refptr<base::SingleThreadTaskRunner> io_task_runner);
  void RequestNexeFd(int render_view_id,
                     PP_Instance instance,
                     const nacl::PnaclCacheInfo& cache_info,
                     RequestNexeFdCallback callback);
  void ReportTranslationFinished(PP_Instance instance, PP_Bool success);

 protected:
  ~PnaclTranslationResourceHost() override;

 private:
  // Maps the instance with an outstanding cache request to the info
  // about that request.
  typedef std::map<PP_Instance, RequestNexeFdCallback> CacheRequestInfoMap;

  // IPC::MessageFilter implementation.
  bool OnMessageReceived(const IPC::Message& message) override;
  void OnFilterAdded(IPC::Sender* sender) override;
  void OnFilterRemoved() override;
  void OnChannelClosing() override;

  void SendRequestNexeFd(int render_view_id,
                         PP_Instance instance,
                         const nacl::PnaclCacheInfo& cache_info,
                         RequestNexeFdCallback callback);
  void SendReportTranslationFinished(PP_Instance instance,
                                     PP_Bool success);
  void OnNexeTempFileReply(PP_Instance instance,
                           bool is_hit,
                           IPC::PlatformFileForTransit file);
  void CleanupCacheRequests();

  scoped_refptr<base::SingleThreadTaskRunner> io_task_runner_;

  // Should be accessed on the io thread.
  IPC::Sender* sender_;
  CacheRequestInfoMap pending_cache_requests_;
  DISALLOW_COPY_AND_ASSIGN(PnaclTranslationResourceHost);
};

#endif  // CHROME_RENDERER_PEPPER_PNACL_TRANSLATION_RESOURCE_HOST_H_
