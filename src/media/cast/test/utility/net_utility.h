// Copyright 2014 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#include "net/base/ip_endpoint.h"

namespace media {
namespace cast {
namespace test {

// Determine a unused UDP port for the in-process receiver to listen on.
// Method: Bind a UDP socket on port 0, and then check which port the
// operating system assigned to it.
net::IPEndPoint GetFreeLocalPort();

}  // namespace test
}  // namespace cast
}  // namespace media
