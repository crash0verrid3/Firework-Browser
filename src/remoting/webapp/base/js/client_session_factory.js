// Copyright 2015 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

/** @suppress {duplicate} */
var remoting = remoting || {};

(function() {

'use strict';

/**
 * @param {Element} container parent element for the plugin to be created.
 * @param {Array<string>} capabilities capabilities required by this
 *     application.
 * @constructor
 */
remoting.ClientSessionFactory = function(container, capabilities) {
  /** @private */
  this.container_ = /** @type {HTMLElement} */ (container);

  /** @private {Array<string>} */
  this.requiredCapabilities_ = [
    remoting.ClientSession.Capability.SEND_INITIAL_RESOLUTION,
    remoting.ClientSession.Capability.RATE_LIMIT_RESIZE_REQUESTS,
    remoting.ClientSession.Capability.VIDEO_RECORDER,
    remoting.ClientSession.Capability.TOUCH_EVENTS
  ];

  // Append the app-specific capabilities.
  this.requiredCapabilities_.push.apply(this.requiredCapabilities_,
                                        capabilities);
};

/**
 * Creates a session.
 *
 * @param {remoting.ClientSession.EventHandler} listener
 * @param {boolean=} opt_useApiaryForLogging
 * @return {Promise<!remoting.ClientSession>} Resolves with the client session
 *     if succeeded or rejects with remoting.Error on failure.
 */
remoting.ClientSessionFactory.prototype.createSession =
    function(listener, opt_useApiaryForLogging) {
  var that = this;
  /** @type {string} */
  var token;
  /** @type {remoting.SignalStrategy} */
  var signalStrategy;
  /** @type {remoting.ClientPlugin} */
  var clientPlugin;
  var useApiaryForLogging = Boolean(opt_useApiaryForLogging);

  function OnError(/** remoting.Error */ error) {
    base.dispose(signalStrategy);
    base.dispose(clientPlugin);
    throw error;
  }

  var promise = remoting.identity.getToken().then(
    function(/** string */ authToken) {
    token = authToken;
    return remoting.identity.getUserInfo();
  }).then(function(/** {email: string, name: string} */ userInfo) {
    return connectSignaling(userInfo.email, token);
  }).then(function(/** remoting.SignalStrategy */ strategy) {
    signalStrategy = strategy;
    return createPlugin(that.container_, that.requiredCapabilities_);
  }).then(function(/** remoting.ClientPlugin */ plugin) {
    clientPlugin = plugin;
    return new remoting.ClientSession(
        plugin, signalStrategy, useApiaryForLogging, listener);
  }).catch(
    remoting.Error.handler(OnError)
  );

  return /** @type {Promise<!remoting.ClientSession>} */ (promise);
};

/**
 * @param {string} email
 * @param {string} token
 * @return {Promise<!remoting.SignalStrategy>}
 */
function connectSignaling(email, token) {
  var signalStrategy = remoting.SignalStrategy.create();
  var deferred = new base.Deferred();
  function onSignalingState(/** remoting.SignalStrategy.State */ state) {
    switch (state) {
      case remoting.SignalStrategy.State.CONNECTED:
        deferred.resolve(signalStrategy);
        break;

      case remoting.SignalStrategy.State.FAILED:
        var error = signalStrategy.getError();
        signalStrategy.dispose();
        deferred.reject(error);
        break;
    }
  }
  signalStrategy.setStateChangedCallback(onSignalingState);
  signalStrategy.connect(remoting.settings.XMPP_SERVER, email, token);
  return deferred.promise();
}

/**
 * Creates the plugin.
 * @param {HTMLElement} container parent element for the plugin.
 * @param {Array<string>} capabilities capabilities required by this
 *     application.
 * @return {Promise<!remoting.ClientPlugin>}
 */
function createPlugin(container, capabilities) {
  var plugin = remoting.ClientPlugin.factory.createPlugin(
      container, capabilities);
  var deferred = new base.Deferred();

  function onInitialized(/** boolean */ initialized) {
    if (!initialized) {
      console.error('ERROR: remoting plugin not loaded');
      plugin.dispose();
      deferred.reject(new remoting.Error(remoting.Error.Tag.MISSING_PLUGIN));
      return;
    }

    if (!plugin.isSupportedVersion()) {
      console.error('ERROR: bad plugin version');
      plugin.dispose();
      deferred.reject(
          new remoting.Error(remoting.Error.Tag.BAD_PLUGIN_VERSION));
      return;
    }
    deferred.resolve(plugin);
  }
  plugin.initialize(onInitialized);
  return deferred.promise();
}

})();
