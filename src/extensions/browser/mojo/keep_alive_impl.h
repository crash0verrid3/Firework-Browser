// Copyright 2014 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#ifndef EXTENSIONS_BROWSER_MOJO_KEEP_ALIVE_IMPL_H_
#define EXTENSIONS_BROWSER_MOJO_KEEP_ALIVE_IMPL_H_

#include "base/callback.h"
#include "extensions/common/mojo/keep_alive.mojom.h"
#include "third_party/mojo/src/mojo/public/cpp/bindings/interface_request.h"
#include "third_party/mojo/src/mojo/public/cpp/bindings/strong_binding.h"

namespace content {
class BrowserContext;
}

namespace extensions {
class Extension;

// An RAII mojo service implementation for extension keep alives. This adds a
// keep alive on construction and removes it on destruction.
class KeepAliveImpl : public KeepAlive {
 public:
  // Create a keep alive for |extension| running in |context| and connect it to
  // |request|. When the requester closes its pipe, the keep alive ends.
  static void Create(content::BrowserContext* context,
                     const Extension* extension,
                     mojo::InterfaceRequest<KeepAlive> request);

 private:
  KeepAliveImpl(content::BrowserContext* context,
                const Extension* extension,
                mojo::InterfaceRequest<KeepAlive> request);
  ~KeepAliveImpl() override;

  content::BrowserContext* context_;
  const Extension* extension_;
  mojo::StrongBinding<KeepAlive> binding_;

  DISALLOW_COPY_AND_ASSIGN(KeepAliveImpl);
};

}  // namespace extensions

#endif  // EXTENSIONS_BROWSER_MOJO_KEEP_ALIVE_IMPL_H_
