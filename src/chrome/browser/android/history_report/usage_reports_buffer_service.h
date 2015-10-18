// Copyright 2015 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#ifndef CHROME_BROWSER_ANDROID_HISTORY_REPORT_USAGE_REPORTS_BUFFER_SERVICE_H_
#define CHROME_BROWSER_ANDROID_HISTORY_REPORT_USAGE_REPORTS_BUFFER_SERVICE_H_

#include <string>
#include <vector>

#include "base/memory/scoped_ptr.h"
#include "base/threading/sequenced_worker_pool.h"

namespace base {
class FilePath;
}  // namespace base

namespace history_report {

class UsageReport;
class UsageReportsBufferBackend;

// This class is intended to be created once and not destroyed until process is
// killed. |backend_| is assumed to be a long lived pointer.
class UsageReportsBufferService {
 public:
  explicit UsageReportsBufferService(const base::FilePath& dir);
  ~UsageReportsBufferService();

  // Init buffer. All calls to buffer before it's initialized are ignored. It's
  // asynchronous.
  void Init();

  // Add report about page visit to the buffer. It's asynchronous.
  void AddVisit(const std::string& id, int64 timestamp_ms, bool typed_visit);

  // Get a batch of usage reports of size up to |batch_size|. It's synchronous.
  scoped_ptr<std::vector<UsageReport> > GetUsageReportsBatch(int32 batch_size);

  // Remove given usage reports from buffer. It's synchronous.
  void Remove(const std::vector<std::string>& report_ids);

  // Clears buffer by removing all usage reports from it.
  void Clear();

  // Dumps internal state to string.
  std::string Dump();

 private:
  // Token used to serialize buffer operations.
  base::SequencedWorkerPool::SequenceToken worker_pool_token_;
  // Non thread safe backend.
  scoped_ptr<UsageReportsBufferBackend> backend_;

  DISALLOW_COPY_AND_ASSIGN(UsageReportsBufferService);
};

}  // namespace history_report

#endif  // CHROME_BROWSER_ANDROID_HISTORY_REPORT_USAGE_REPORTS_BUFFER_SERVICE_H_
