// Copyright (c) 2012 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#ifndef SYNC_TEST_NULL_DIRECTORY_CHANGE_DELEGATE_H_
#define SYNC_TEST_NULL_DIRECTORY_CHANGE_DELEGATE_H_

#include "base/compiler_specific.h"
#include "sync/syncable/directory_change_delegate.h"

namespace syncer {
namespace syncable {

// DirectoryChangeDelegate that does nothing in all delegate methods.
class NullDirectoryChangeDelegate : public DirectoryChangeDelegate {
 public:
  ~NullDirectoryChangeDelegate() override;

  void HandleCalculateChangesChangeEventFromSyncApi(
      const ImmutableWriteTransactionInfo& write_transaction_info,
      BaseTransaction* trans,
      std::vector<int64>* entries_changed) override;
  void HandleCalculateChangesChangeEventFromSyncer(
      const ImmutableWriteTransactionInfo& write_transaction_info,
      BaseTransaction* trans,
      std::vector<int64>* entries_changed) override;
  ModelTypeSet HandleTransactionEndingChangeEvent(
      const ImmutableWriteTransactionInfo& write_transaction_info,
      BaseTransaction* trans) override;
  void HandleTransactionCompleteChangeEvent(
      ModelTypeSet models_with_changes) override;
};

}  // namespace syncable
}  // namespace syncer

#endif  // SYNC_TEST_NULL_DIRECTORY_CHANGE_DELEGATE_H_
