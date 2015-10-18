// Copyright (c) 2015 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#include <sstream>

#include "ppapi/cpp/input_event.h"
#include "ppapi/cpp/instance.h"
#include "ppapi/cpp/module.h"
#include "ppapi/cpp/var.h"
#include "ppapi/cpp/var_dictionary.h"

namespace remoting {

class KeyTesterInstance : public pp::Instance {
 public:
  explicit KeyTesterInstance(PP_Instance instance) : pp::Instance(instance) {
    RequestFilteringInputEvents(PP_INPUTEVENT_CLASS_KEYBOARD);
  }

  virtual ~KeyTesterInstance() {}

  virtual bool HandleInputEvent(const pp::InputEvent& event) {
    switch (event.GetType()) {
      case PP_INPUTEVENT_TYPE_KEYDOWN:
      case PP_INPUTEVENT_TYPE_KEYUP:
      case PP_INPUTEVENT_TYPE_CHAR: {
        HandleKeyboardEvent(pp::KeyboardInputEvent(event));
        break;
      }
      default:
        break;
    }
    return true;
  }

 private:
  void HandleKeyboardEvent(const pp::KeyboardInputEvent& event) {
    pp::VarDictionary out;
    out.Set("type", EventTypeToString(event.GetType()));
    out.Set("modifiers", (double)event.GetModifiers());
    out.Set("keyCode", (double)event.GetKeyCode());
    out.Set("characterText", event.GetCharacterText());
    out.Set("code", event.GetCode());
    PostMessage(out);
  }

  std::string EventTypeToString(PP_InputEvent_Type t) {
    switch (t) {
      case PP_INPUTEVENT_TYPE_UNDEFINED:
        return "UNDEFINED";
      case PP_INPUTEVENT_TYPE_MOUSEDOWN:
        return "MOUSEDOWN";
      case PP_INPUTEVENT_TYPE_MOUSEUP:
        return "MOUSEUP";
      case PP_INPUTEVENT_TYPE_MOUSEMOVE:
        return "MOUSEMOVE";
      case PP_INPUTEVENT_TYPE_MOUSEENTER:
        return "MOUSEENTER";
      case PP_INPUTEVENT_TYPE_MOUSELEAVE:
        return "MOUSELEAVE";
      case PP_INPUTEVENT_TYPE_WHEEL:
        return "WHEEL";
      case PP_INPUTEVENT_TYPE_RAWKEYDOWN:
        return "RAWKEYDOWN";
      case PP_INPUTEVENT_TYPE_KEYDOWN:
        return "KEYDOWN";
      case PP_INPUTEVENT_TYPE_KEYUP:
        return "KEYUP";
      case PP_INPUTEVENT_TYPE_CHAR:
        return "CHAR";
      case PP_INPUTEVENT_TYPE_CONTEXTMENU:
        return "CONTEXTMENU";
      case PP_INPUTEVENT_TYPE_IME_COMPOSITION_START:
        return "IME_COMPOSITION_START";
      case PP_INPUTEVENT_TYPE_IME_COMPOSITION_UPDATE:
        return "IME_COMPOSITION_UPDATE";
      case PP_INPUTEVENT_TYPE_IME_COMPOSITION_END:
        return "IME_COMPOSITION_END";
      case PP_INPUTEVENT_TYPE_IME_TEXT:
        return "IME_TEXT";
      case PP_INPUTEVENT_TYPE_TOUCHSTART:
        return "TOUCHSTART";
      case PP_INPUTEVENT_TYPE_TOUCHMOVE:
        return "TOUCHMOVE";
      case PP_INPUTEVENT_TYPE_TOUCHEND:
        return "TOUCHEND";
      case PP_INPUTEVENT_TYPE_TOUCHCANCEL:
        return "TOUCHCANCEL";
      default:
        return "[UNRECOGNIZED]";
    }
  }
};

class KeyTesterModule : public pp::Module {
 public:
  KeyTesterModule() : pp::Module() {}
  virtual ~KeyTesterModule() {}

  virtual pp::Instance* CreateInstance(PP_Instance instance) {
    return new KeyTesterInstance(instance);
  }
};

}  // namespace remoting

namespace pp {

Module* CreateModule() {
  return new remoting::KeyTesterModule();
}

}  // namespace pp
