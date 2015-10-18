// Copyright 2015 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#ifndef CHROME_BROWSER_ANDROID_SHORTCUT_INFO_H_
#define CHROME_BROWSER_ANDROID_SHORTCUT_INFO_H_

#include "base/strings/string16.h"
#include "content/public/common/manifest.h"
#include "third_party/WebKit/public/platform/modules/screen_orientation/WebScreenOrientationLockType.h"
#include "url/gurl.h"

// Information needed to create a shortcut via ShortcutHelper.
struct ShortcutInfo {

  // This enum is used to back a UMA histogram, and must be treated as
  // append-only.
  enum Source {
    SOURCE_UNKNOWN = 0,
    SOURCE_ADD_TO_HOMESCREEN = 1,
    SOURCE_APP_BANNER = 2,
    SOURCE_COUNT = 3
  };

  ShortcutInfo();
  explicit ShortcutInfo(const GURL& shortcut_url);

  // Updates the info based on the given |manifest|.
  void UpdateFromManifest(const content::Manifest& manifest);

  // Updates the source of the shortcut.
  void UpdateSource(const Source source);

  GURL url;
  base::string16 title;
  content::Manifest::DisplayMode display;
  blink::WebScreenOrientationLockType orientation;
  Source source;
};

#endif  // CHROME_BROWSER_ANDROID_SHORTCUT_INFO_H_
