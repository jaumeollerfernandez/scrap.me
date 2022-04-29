!function(){"use strict";var t={5329:function(){Array.from||(Array.from=function(){var t=Object.prototype.toString,e=function(e){return"function"===typeof e||"[object Function]"===t.call(e)},o=Math.pow(2,53)-1,n=function(t){var e=function(t){var e=Number(t);return isNaN(e)?0:0!==e&&isFinite(e)?(e>0?1:-1)*Math.floor(Math.abs(e)):e}(t);return Math.min(Math.max(e,0),o)};return function(t){var o=this,r=Object(t);if(null==t)throw new TypeError("Array.from requires an array-like object - not null or undefined");var i,s=arguments.length>1?arguments[1]:void 0;if("undefined"!==typeof s){if(!e(s))throw new TypeError("Array.from: when provided, the second argument must be a function");arguments.length>2&&(i=arguments[2])}for(var a,c=n(r.length),u=e(o)?Object(new o(c)):new Array(c),d=0;d<c;)a=r[d],u[d]=s?"undefined"===typeof i?s(a,d):s.call(i,a,d):a,d+=1;return u.length=c,u}}())},9762:function(){"function"!==typeof Object.assign&&(Object.assign=function(t){if(null===t)throw new TypeError("Cannot convert undefined or null to object");t=Object(t);for(var e=1;e<arguments.length;e++){var o=arguments[e];if(null!==o)for(var n in o)Object.prototype.hasOwnProperty.call(o,n)&&(t[n]=o[n])}return t})},1314:function(){String.prototype.startsWith||(String.prototype.startsWith=function(t,e){return e=e||0,this.substr(e,t.length)===t})}},e={};function o(n){var r=e[n];if(void 0!==r)return r.exports;var i=e[n]={exports:{}};return t[n](i,i.exports,o),i.exports}!function(){o(9762),o(1314),o(5329);var t,e="Smartlook could not be initialized.",n="Missing",r=function(){function t(){}return t.check=function(o){var r=window;if(function(){try{var t=0,e=/MSIE (\d+\.\d+);/.test(navigator.userAgent),o=!!navigator.userAgent.match(/Trident\/7.0/),n=navigator.userAgent.indexOf("rv:11.0");return e&&(t=new Number(RegExp.$1)),-1!==navigator.appVersion.indexOf("MSIE 10")&&(t=10),o&&-1!==n&&(t=11),!!t}catch(r){return!1}}())return o.warn(e,"IE not supported."),!1;if(!r.MutationObserver)return o.warn(e,n,"mutation Observer."),!1;if(!Array.from||!Array.prototype.filter||!Array.prototype.map||!Array.prototype.forEach)return o.warn(e,n,"one of array from, filter, map, forEach."),!1;try{if(!t.__isStorageSupported(window.localStorage))return o.warn(e,n,"local Storage."),!1;if(!t.__isStorageSupported(window.sessionStorage))return o.warn(e,n,"session Storage."),!1}catch(i){return o.warn(e,n,"local Storage."),!1}return!!window.navigator||(o.warn(e,n,"navigator."),!1)},t.__isStorageSupported=function(t){if(!t)return!1;var e="__b61b7e6555c65__";try{return t.setItem(e,e),t.removeItem(e),!0}catch(o){return!1}},t}(),i=function(t){try{return JSON.stringify(t,function(){if("function"===typeof WeakSet){var t=new WeakSet;return function(e,o){if("object"===typeof o&&null!==o){if(t.has(o))return;t.add(o)}return o}}}())}catch(e){return null}},s=function(t){try{var e=window,o=e.Prototype,n=e.MooTools;if(o&&o.Version<"1.7"&&Array.prototype.toJSON&&Object.toJSON)return Object.toJSON(t);if(n&&JSON&&JSON.encode&&Array.prototype.toJSON)return JSON.encode(t)}catch(r){return i(t)}return i(t)},a="Second parameter must be either non-empty string or false. More info at https://www.smartlook.com/docs/gdpr.",c="consent",u="manager.eu.smartlook.cloud",d=function(t,e){var o,n=t[0];if("properties"===n&&(e._recorderRunning?e._addProperties(t[1]):e._apiSubscribers.push((function(){return e._addProperties(t[1])}))),"identify"===n&&(e._recorderRunning?e._addIdentity(t[1],t[2]):e._apiSubscribers.push((function(){return e._addIdentity(t[1],t[2])}))),"track"===n&&(e._recorderRunning?e._addTrack(t[1],t[2],t[3]):e._apiSubscribers.push((function(){return e._addTrack(t[1],t[2])}))),"disable"===n&&e._disable(),0===n.indexOf(c)){var r=n.substr(c.length).toLowerCase();if("api"!==r&&"ip"!==r&&"forms"!==r)return;("boolean"!==typeof(o=t[1])&&"string"!==typeof o||"boolean"===typeof o&&o?(console.error(a),0):"string"!==typeof o||o||(console.error(a),0))&&(e._recorderRunning?e._giveConsent(r,t[1]):e._apiSubscribers.push((function(){return e._giveConsent(r,t[1])})))}if("expertForms"===n||"masterForms"===n){var i=function(){e._recordForms=!0,e.startRecordingForms&&e.startRecordingForms()};e._recorderRunning?i():e._apiSubscribers.push(i)}if("expertAPI"===n||"masterAPI"===n){i=function(){e.consent.api=!0,e.options&&(e.options.identifyApi=!0)};e._recorderRunning?i():e._apiSubscribers.push(i)}if("ban"===n&&e._ban(t[1]),"anonymize"===n&&e._anonymize(),"restart"===n&&e._restart&&e._restart(),"pause"===n&&(e._recorderRunning?e._pause&&e._pause():e._recorderPaused=!0),"resume"===n&&e._resume&&e._resume(),"error"===n&&(e._recorderRunning?e._error(t[1]):e._apiSubscribers.push((function(){return e._error(t[1])}))),"navigation"===n&&(e._recorderRunning?e._url(t[1]):e._apiSubscribers.push((function(){return e._url(t[1])}))),"url:beforeSend"===n&&e._url_setBeforeSendHook(t[1]),"record"===n){if(1===e._consentVersion)return t[1]&&"boolean"===typeof t[1].forms&&t[1].forms&&e.__giveConsent("forms","Consent to FORMS given using the Record API"),t[1]&&"boolean"===typeof t[1].forms&&!t[1].forms&&e.__giveConsent("forms",!1),t[1]&&"boolean"===typeof t[1].ips&&t[1].ips&&e.__giveConsent("ip","Consent to IP given using the Record API"),t[1]&&"boolean"===typeof t[1].api&&t[1].api&&e.__giveConsent("api","Consent to API given using the Record API"),void(t[1]&&"boolean"===typeof t[1].api&&!t[1].api&&e.__giveConsent("api",!1));t[1]&&"boolean"===typeof t[1].forms&&t[1].forms&&(e._recordForms=!0,e.startRecordingForms&&e.startRecordingForms()),t[1]&&"boolean"===typeof t[1].forms&&!t[1].forms&&(e._recordForms=!1,e.stopRecordingForms&&e.stopRecordingForms()),t[1]&&"boolean"===typeof t[1].emails&&t[1].emails&&(e._recordEmails=!0),t[1]&&"boolean"===typeof t[1].emails&&!t[1].emails&&(e._recordEmails=!1),t[1]&&"boolean"===typeof t[1].numbers&&t[1].numbers&&(e._recordNumbers=!0),t[1]&&"boolean"===typeof t[1].numbers&&!t[1].numbers&&(e._recordNumbers=!1),t[1]&&"boolean"===typeof t[1].ips&&t[1].ips&&(e._recordIPs=!0)}},l=function(){function t(){}return t.load=function(t){t.consent={ip:null,forms:null,api:null},t._apiSubscribers=[];for(var e=function(e){var o=t.api[e];if("init"===o[0]){if(t.key=o[1],t.projectKey=o[1],o[2]&&o[2].debug&&(t.debug=!0),o[2]&&o[2].host&&(t.host=o[2].host),o[2]&&o[2].region&&(t.region=o[2].region),o[2]&&"cookies"in o[2]&&(t.cookies=o[2].cookies),o[2]&&o[2].recording){var n=o[2].recording;t.recording={},n.host&&(t.recording.host=n.host),n.assetsHost&&(t.recording.assetsHost=n.assetsHost)}if(o[2]&&o[2].analytics){var r=o[2].analytics;t.analytics={},r.host&&(t.analytics.host=r.host)}if(o[2]&&o[2].options){var i=o[2].options;t.options={};["recordConsole","recordNetwork","disableForms","identifyApi","maskEmails","maskNumbers","signedDpa"].forEach((function(e){t.options&&e in i&&(t.options[e]=i[e])}))}}"string"===typeof o[0]&&d(o,t),"function"===typeof o[0]&&t._apiSubscribers.push(o[0])},o=0;o<t.api.length;o+=1)e(o);if(!t.host)if(t.region)if("eu"===t.region)t.host=u;else{if("us"!==t.region)throw new Error("Provided region '".concat(t.region,"' is not suppported"));t.host="manager.us.smartlook.cloud"}else t.host=u;if("cookies"in t||(t.cookies=!0),!t.key)throw new Error("Smartlook key is not provided");t.api.push=function(e){if("string"===typeof e[0]&&d(e,t),"function"===typeof e[0])if(t._recorderRunning)try{e[0]()}catch(o){console.error(o)}else t._apiSubscribers.push(e[0])}},t}(),p="SL_L_23361dd035530_VID",f="SL_L_23361dd035530_SID",h="SL_L_23361dd035530_KEY",m="smartlook_picker",g="SL_C_23361dd035530_KEY",y="SL_C_23361dd035530_SID",v="SL_C_23361dd035530_VID";var w=function(){function e(){}return e.getDate=function(){var t=new Date;return t.setMonth(t.getMonth()+13),t.toString()},e.getDomain=function(){return t||(t=function(t){for(var e=t.document,o=e.domain,n=o.split("."),r="f0189a22486d".concat(Date.now()),i=0;i<n.length-1&&-1===e.cookie.indexOf("".concat(r,"=").concat(r));)i+=1,o=n.slice(-1-i).join("."),e.cookie="".concat(r,"=").concat(r,";domain=").concat(o,";path=/;sameSite=strict;secure");return e.cookie="".concat(r,"=;expires=Thu, 01 Jan 1970 00:00:01 GMT;domain=").concat(o,";path=/;sameSite=strict;secure"),o}(window))},e.persistSessionId=function(t){if(t.sessionId?localStorage.setItem(f,t.sessionId):localStorage.removeItem(f),t.cookies)try{e.setCookie(y,t.sessionId)}catch(o){}},e.persistVisitorId=function(t){if(t.visitorId?localStorage.setItem(p,t.visitorId):localStorage.removeItem(p),t.cookies)try{e.setCookie(v,t.visitorId)}catch(o){}},e.persistProjectKey=function(t){if(t.projectKey?localStorage.setItem(h,t.projectKey):localStorage.removeItem(h),t.cookies)try{e.setCookie(g,t.projectKey)}catch(o){}},e.setCookie=function(t,e){window.document.cookie=e?"".concat(t,"=").concat(e,";expires=").concat(this.getDate(),";domain=").concat(this.getDomain(),";path=/;sameSite=strict;secure"):"".concat(t,"=;expires=Thu, 01 Jan 1970 00:00:01 GMT;domain=").concat(this.getDomain(),";path=/")},e}(),b=function(){function t(t){this.w=t}return t.prototype.getKeys=function(){var t=this.w.document.cookie.split(";"),e=null,o=null,n=null;try{for(var r=0;r<t.length;r+=1){var i=t[r].trim().split("=");switch(i[0]){case g:e=i[1];break;case y:o=i[1];break;case v:n=i[1]}}}catch(s){}return{key:e,sid:o,vid:n}},t}(),_=function(){function t(t){this.smartlook=t}return t.prototype.setSessionId=function(t){this.smartlook.sessionId=t,this.smartlook.sid=t,w.persistSessionId({sessionId:t,cookies:this.smartlook.cookies})},t.prototype.setVisitorId=function(t){this.smartlook.visitorId=t,this.smartlook.vid=t,w.persistVisitorId({visitorId:t,cookies:this.smartlook.cookies})},t.prototype.setProjectKey=function(t){this.smartlook.projectKey=t,this.smartlook.key=t,w.persistProjectKey({projectKey:t,cookies:this.smartlook.cookies})},t.prototype.setRecordId=function(t){this.smartlook.recordId=t,this.smartlook.rid=t},t.prototype.setPlayUrl=function(t){this.smartlook.playUrl=t},t.getSessionId=function(){return localStorage.getItem(f)},t.getVisitorId=function(){return localStorage.getItem(p)},t.getProjectKey=function(){return localStorage.getItem(h)},t.prototype.getStoredSidVid=function(e){var o=new b(window).getKeys(),n=o.sid,r=o.vid;o.key!==e&&(n=null,r=null);var i=t.getSessionId();!n&&i&&(n=i);var s=t.getVisitorId();!r&&s&&(r=s);var a=t.getProjectKey();if(a&&e!==a||n&&n.length>15){var c=new t(window.smartlook);c.setSessionId(void 0),c.setVisitorId(void 0),c.setProjectKey(void 0),n=null,r=null}return{sid:n,vid:r}},t.prototype.loadDebugMode=function(){localStorage.getItem("smartlook_debug")&&(this.smartlook.debug=!0)},t.prototype.setOptions=function(t){this.smartlook.options||(this.smartlook.options={});var e=this.smartlook.options;"undefined"===typeof e.recordConsole&&(e.recordConsole=t.recordConsole),"undefined"===typeof e.recordNetwork&&(e.recordNetwork=t.recordNetwork),"undefined"===typeof e.disableForms&&(e.disableForms=t.disableForms),"undefined"===typeof e.maskEmails&&(e.maskEmails=t.maskEmails),"undefined"===typeof e.maskNumbers&&(e.maskNumbers=t.maskNumbers),"undefined"===typeof e.signedDpa&&(e.signedDpa=t.signedDpa),"undefined"===typeof e.storeGroup&&(e.storeGroup=t.storeGroup),"undefined"===typeof e.identifyApi&&(e.identifyApi=t.identifyApi)},t.prototype.setConsentSettings=function(t){this.smartlook.consent.forms=t.forms,this.smartlook.consent.api=t.api,this.smartlook.consent.ip=t.ip},t.prototype.setAnalyticsSettings=function(t){this.smartlook.analytics||(this.smartlook.analytics={}),t.host&&!this.smartlook.analytics.host&&(this.smartlook.analytics.host=t.host),t.host&&!t.error&&t.ok||(this.smartlook.analytics=void 0)},t.prototype.setRecordingSettings=function(t){this.smartlook.recording||(this.smartlook.recording={});var e=this.smartlook.recording;e.hostDefault=t.hostDefault,e.host||(e.host=t.hostDefault),t.assetsHost&&!e.assetsHost&&(e.assetsHost=t.assetsHost),e.host&&!t.error||(this.smartlook.recording=void 0)},t.prototype.setIntegrationSettings=function(t){this.smartlook.integrations=t},t}(),k=function(){return k=Object.assign||function(t){for(var e,o=1,n=arguments.length;o<n;o++)for(var r in e=arguments[o])Object.prototype.hasOwnProperty.call(e,r)&&(t[r]=e[r]);return t},k.apply(this,arguments)},S=function(t,e){var o=e.numberOfRetries,n=void 0===o?1:o,r=e.nTry,i=void 0===r?1:r,s=e.onError,a=e.errorLogger;a&&a(i,t),n>1&&i<n?setTimeout((function(){I(k(k({},e),{nTry:i+1}))}),333*Math.pow(i+1,2)):s&&s(t)},I=function(t){var e=t.method,o=void 0===e?"GET":e,n=t.url,r=t.headers,i=t.body,s=t.timeout,a=t.onSuccess,c=t.isError,u=void 0===c?function(t){return t<200||t>=300}:c,d=t.withCredentials,l=void 0!==d&&d,p=new XMLHttpRequest;if("number"===typeof s&&(p.timeout=s),p.open(o,n,!0),r&&Object.keys(r).forEach((function(t){p.setRequestHeader(t,r[t])})),l)try{p.withCredentials=!0}catch(f){}p.onload=function(){u(p.status)?S(p,t):a&&a(p)},p.onabort=function(){S(p,t)},p.onerror=function(){S(p,t)},p.ontimeout=function(){S(p,t)},i?p.send(i):p.send()},O=function(){function t(){this.uid=null,this.props=null,this.host=null,this.timeout=null,this.logger=null,this.initialized=!1}return t.prototype.initialize=function(t,e){this.initialized||(this.host=t,this.logger=e,this.initialized=!0)},t.prototype.addIdentity=function(t,e){void 0===e&&(e={}),this.uid=t,this.props=e,this.sendData()},t.prototype.sendData=function(){var t=this,e=_.getVisitorId()||"";if(!this.initialized||!e)return clearTimeout(this.timeout),void(this.timeout=window.setTimeout(this.sendData.bind(this),500));if(this.uid){var o={vid:e,uid:this.uid,props:this.props||{}};I({method:"POST",url:"https://".concat(this.host,"/rec/identify"),body:s(o),headers:{"Content-Type":"text/plain;charset=UTF-8"},numberOfRetries:3,timeout:5e3,onSuccess:function(){t.logger&&t.logger.log("Sent identity",o)}}),this.uid=null,this.props=null}},t}(),P=function(){function t(){}return t.getCurrentUrl=function(){var t=window,e=t.smartlook,o=t.location&&t.location.href||"";if(e&&e._url_beforeSendHook)try{o=e._url_beforeSendHook(o)}catch(n){console.warn("Could not modify url with url:beforeSend method",n)}return"string"===typeof o?o.substring(0,1e3):""},t}(),j="Look at 'https://smartlook.github.io/docs/web/custom-events/' for more info.",E="Calling 'track' API with missing or invalid value in 'eventName' parameter. Non-empty string expected. ".concat(j),C="Calling 'track' API with invalid value in 'properties' parameter. Object with key value pairs expected. ".concat(j),A=function(){function t(){this.host=null,this.timeout=null,this.logger=null,this.initialized=!1,this.queue=[],this.w=window}return t.prototype.initialize=function(t,e){this.initialized||(this.host=t,this.logger=e,this.initialized=!0)},t.prototype.getUrl=function(){var t=this.w.smartlook,e=t.key,o=t.vid,n=t.rid,r=t.sid,i=this.w.smartlook.options&&this.w.smartlook.options.storeGroup||"";return e&&o&&n&&r&&i?"https://".concat(this.host,"/rec/events?rid=").concat(n,"&sid=").concat(r,"&key=").concat(e,"&vid=").concat(o,"&group=").concat(i,"&source=website&s=1"):null},t.prototype.addEvent=function(t){if(t.name&&"string"===typeof t.name)if(t.props&&"object"!==typeof t.props)console.warn(C);else{var e=0;this.w.smartlook.recording&&this.w.smartlook.recording.startTime&&(e=Math.max(0,t.createdAt-this.w.smartlook.recording.startTime));var o={type:"custom",time:e,name:t.name,id:t.id,createdAt:t.createdAt,props:t.props,pageUrl:P.getCurrentUrl(),internalProps:{}};t.elements&&Object.assign(o,{elements:t.elements}),t.className&&Object.assign(o.internalProps,{className:t.className}),t.elementId&&Object.assign(o.internalProps,{elementId:t.elementId}),this.w.smartlook._identityUid&&Object.assign(o.internalProps,{uid:this.w.smartlook._identityUid}),this.w.smartlook._globalProps&&Object.assign(o.props,this.w.smartlook._globalProps),this.w.smartlook._identityProps&&Object.assign(o.props,this.w.smartlook._identityProps),o.internalProps&&0===Object.keys(o.internalProps).length&&delete o.internalProps,o&&(this.queue.push({event:o,url:this.getUrl()}),this.sendEvents())}else console.warn(E)},t.prototype.sendEvents=function(){var t=this;if(!this.initialized)return clearTimeout(this.timeout),void(this.timeout=window.setTimeout(this.sendEvents.bind(this),333));var e=!1,o=this.queue.slice();this.queue=[],o.forEach((function(o){var n=o.url;if(n||(n=t.getUrl()),!n)return t.queue.push(o),void(e=!0);var r=s([o.event]);r?navigator.sendBeacon&&navigator.sendBeacon(n,r)?t.logger&&t.logger.log("Sent custom event using beacon",o.event):I({method:"POST",url:n,headers:{"Content-Type":"text/plain;charset=UTF-8"},body:r,timeout:5e3,numberOfRetries:2,onSuccess:function(){t.logger&&t.logger.log("Sent custom event using XHR",o.event)}}):t.logger&&t.logger.error("Could not create a stringify body of a custom event",o.event)})),e&&(clearTimeout(this.timeout),this.timeout=window.setTimeout(this.sendEvents.bind(this),333))},t}(),T=window.performance&&window.performance.timing&&window.performance.timing.navigationStart&&window.performance.now,N=function(){function t(){}return t.getElapsedTime=function(){return T?Math.round(window.performance.now()):Date.now()},t.now=function(){return T?Math.round(window.performance.timing.navigationStart+window.performance.now()):Date.now()},t}(),R=function(t,e){void 0===e&&(e=!0);var o=this;this.subscribe=function(t){o.listeners.push(t),o.useQueueEvents&&o.eventsQueue.length>0&&(o.eventsQueue=o.eventsQueue.filter((function(t){return t.ttl>=N.getElapsedTime()})),o.eventsQueue.forEach((function(e){return t(e.event)})))},this.unsubscribe=function(t){o.listeners=o.listeners.filter((function(e){return e!==t}))},this.publish=function(t){o.listeners.forEach((function(e){return e(t)}))},this.startTimeElapsed=N.getElapsedTime(),this.listeners=[],this.eventsQueue=[],this.w=t,this.useQueueEvents=e},x=function(){var t=function(e,o){return t=Object.setPrototypeOf||{__proto__:[]}instanceof Array&&function(t,e){t.__proto__=e}||function(t,e){for(var o in e)Object.prototype.hasOwnProperty.call(e,o)&&(t[o]=e[o])},t(e,o)};return function(e,o){if("function"!==typeof o&&null!==o)throw new TypeError("Class extends value "+String(o)+" is not a constructor or null");function n(){this.constructor=e}t(e,o),e.prototype=null===o?Object.create(o):(n.prototype=o.prototype,new n)}}(),F=function(t){function e(){return null!==t&&t.apply(this,arguments)||this}return x(e,t),e}(R),M=F,L=function(){var t=function(e,o){return t=Object.setPrototypeOf||{__proto__:[]}instanceof Array&&function(t,e){t.__proto__=e}||function(t,e){for(var o in e)Object.prototype.hasOwnProperty.call(e,o)&&(t[o]=e[o])},t(e,o)};return function(e,o){if("function"!==typeof o&&null!==o)throw new TypeError("Class extends value "+String(o)+" is not a constructor or null");function n(){this.constructor=e}t(e,o),e.prototype=null===o?Object.create(o):(n.prototype=o.prototype,new n)}}(),D=function(t){function e(){return null!==t&&t.apply(this,arguments)||this}return L(e,t),e}(R),H=D,V=function(){var t=function(e,o){return t=Object.setPrototypeOf||{__proto__:[]}instanceof Array&&function(t,e){t.__proto__=e}||function(t,e){for(var o in e)Object.prototype.hasOwnProperty.call(e,o)&&(t[o]=e[o])},t(e,o)};return function(e,o){if("function"!==typeof o&&null!==o)throw new TypeError("Class extends value "+String(o)+" is not a constructor or null");function n(){this.constructor=e}t(e,o),e.prototype=null===o?Object.create(o):(n.prototype=o.prototype,new n)}}(),U=function(t){function e(){return null!==t&&t.apply(this,arguments)||this}return V(e,t),e}(R),z=U,K=function(){function t(){}return t.generate=function(){return function(){for(var t=arguments.length>0&&void 0!==arguments[0]?arguments[0]:21,e="",o=crypto.getRandomValues(new Uint8Array(t));t--;){var n=63&o[t];e+=n<36?n.toString(36):n<62?(n-26).toString(36).toUpperCase():n<63?"_":"-"}return e}(10)},t}(),J=function(){function t(){this.host=null,this.timeout=null,this.logger=null,this.initialized=!1,this.consents={},this.w=window}return t.prototype.initialize=function(t,e){this.initialized||(this.host=t,this.logger=e,this.initialized=!0)},t.prototype.addConsent=function(t,e){this.consents[t]=e,clearTimeout(this.timeout),this.timeout=window.setTimeout(this.sendConsent.bind(this),500)},t.prototype.getUrl=function(){return"https://".concat(this.host,"/rec/consent")},t.prototype.sendConsent=function(){var t=this,e=this.w.smartlook,o=e.key,n=e.vid,r=e.sid;if(!this.initialized||!o||!n)return clearTimeout(this.timeout),void(this.timeout=window.setTimeout(this.sendConsent.bind(this),500));var i={source:"website",key:o,vid:n,consent:this.consents,sid:r};I({method:"POST",url:this.getUrl(),headers:{"Content-Type":"text/plain;charset=UTF-8"},body:s(i),numberOfRetries:3,onSuccess:function(){t.logger&&t.logger.log("Sent consent",i)},onError:function(){t.logger&&t.logger.log("Could not sent consent",i)}}),this.consents={}},t}(),W="smartlook_ban_reason",q="smartlook_ban_expire";function B(t,e){void 0===e&&(e=3e5);var o=Date.now()+e;localStorage.setItem(q,o.toString()),localStorage.setItem(W,t)}var G,Q,X,Y=function(t,e,o){if(o||2===arguments.length)for(var n,r=0,i=e.length;r<i;r++)!n&&r in e||(n||(n=Array.prototype.slice.call(e,0,r)),n[r]=e[r]);return t.concat(n||Array.prototype.slice.call(e))},$=function(t){return console.warn("%c Smartlook ","background: #a94442; color: #fff",t),!1},Z=function(){function t(t,e,o){this.debug=t,this.prefix=e||"Smartlook",this.prefixStyle=o||"background: #4d4d4d; color: #fff"}return t.prototype.log=function(){for(var t=[],e=0;e<arguments.length;e++)t[e]=arguments[e];if(this.debug)try{console.log.apply(console,Y(["%c ".concat(this.prefix," "),this.prefixStyle],t,!1))}catch(o){}},t.prototype.error=function(){for(var t=[],e=0;e<arguments.length;e++)t[e]=arguments[e];if(this.debug)try{console.error.apply(console,Y(["%c ".concat(this.prefix," error "),"background: #a94442; color: #fff"],t,!1))}catch(o){}},t.prototype.isDebug=function(){return this.debug},t}(),tt=function(){function t(){}return t.getMergedValidProps=function(t,e){if(!t||"object"!==typeof t)return{};e&&"object"!==typeof e&&(e=void 0);var o=Object.assign(e||{},t);return Object.keys(o).forEach((function(t){var e=o[t],n=typeof e;void 0!==e&&null!==e&&"function"!==n&&"object"!==n&&"symbol"!==n&&"undefined"!==n||delete o[t],"number"!==n&&"boolean"!==n&&"bigint"!==n||(o[t]=e.toString())})),o},t}(),et=function(){function t(){}return t.prototype.computedNthIndex=function(t){if(t.parentNode){for(var e=t.parentNode.childNodes,o=t.tagName,n=0,r=0,i=0,s=e.length;i<s;i+=1)if(1===e[i].nodeType){if(e[i]===t){n+=1,r+=1;break}e[i].tagName===o&&(n+=1),r+=1}return{nthOfType:n,nthChild:r}}return null},t.prototype.generate=function(t){for(var e=t,o=[];e;){var n={classes:[],tagName:"",id:""},r=this.computedNthIndex(e);n.classes=Array.from(e.classList||[]),n.tagName=e.tagName,n.id="string"===typeof e.id?e.id:"",r&&(n.nthOfType=r.nthOfType,n.nthChild=r.nthChild),o.push(n),e=e.parentElement}return o},t}(),ot=function(){function t(){}return t.register=function(t){G=new O,t._addIdentity=function(e,o){if(!t.options||t.options.identifyApi)if(t.consent.api||1!==t._consentVersion)if(e){var n=tt.getMergedValidProps(o);G.addIdentity(e,n),t._identityUid=e,t._identityProps=n}else console.warn("UserId must be provided");else console.warn("User has not given consent to use API");else console.warn("Identify API is not enabled in project settings")},Q=new A;var e=new M(window);t.onCustomEvent=function(t){return e.subscribe(t),function(){return e.unsubscribe(t)}},t._addProperties=function(e){e&&"object"===typeof e?t._globalProps=tt.getMergedValidProps(e,t._globalProps):console.warn("Properties object must be provided")},t._addTrack=function(o,n,r){if(!t.options||t.options.identifyApi){var i={type:"custom",name:o,props:tt.getMergedValidProps(n),id:K.generate(),createdAt:N.now()};if(r){var s=r,a=(new et).generate(r);Object.assign(i,{elements:a});var c=s.className;c&&Object.assign(i,{className:c});var u=s.id;u&&Object.assign(i,{elementId:u});var d=s.href;d&&Object.assign(i,{href:d})}Q.addEvent(i),e.publish(i)}else console.warn("Identify API is not enabled in project settings")},t._disable=function(){window.smartlook_stopped=!0,window.smartlook=function(){return $("Recording was disabled using API.")}},t._ban=function(t){window.smartlook_stopped=!0,t?B("Banned from API",t):B("Banned from API"),window.smartlook=function(){return $("Visitor was excluded from recording using API.")}},t._anonymize=function(){var e=new _(t);e.setSessionId(void 0),e.setVisitorId(void 0),e.setRecordId(void 0),e.setPlayUrl(void 0),t._recorderRunning&&t._restart&&t._restart()},X=new J,t.__giveConsent=function(e,o){t.options&&t.options.signedDpa?(t.consent[e]=!!o,X.addConsent(e,o),"forms"===e&&(o&&!t.options.disableForms&&(t._recordForms=!0,t.startRecordingForms&&t.startRecordingForms()),o||(t._recordForms=!1,t.stopRecordingForms&&t.stopRecordingForms()))):console.warn("Project owner did not sign 'Personal Data Processing Agreement' (https://www.smartlook.com/documents/dpa.pdf) in project settings")},t._giveConsent=function(e,o){2!==t._consentVersion?t.__giveConsent(e,o):console.warn("This API is deprecated. Please follow the https://docs.smartlook.com/docs/web/consent-sensitive-data guide")};var o=new H(window);t.onCustomError=function(t){return o.subscribe(t),function(){return o.unsubscribe(t)}},t._error=function(t){o.publish({type:"error",filename:"string"===typeof t?"":t.filename||"",colno:"string"===typeof t?0:t.colno||0,lineno:"string"===typeof t?0:t.lineno||0,value:"string"===typeof t?t:t.message,stack:"string"===typeof t?"":t.error&&t.error.stack||"",id:K.generate(),createdAt:N.now()})};var n=new z(window);t.onCustomUrl=function(t){return n.subscribe(t),function(){return n.unsubscribe(t)}},t._url=function(e){if(e){var o=e;if(e.startsWith("//")?o=location.protocol+o:e.startsWith("https://")||e.startsWith("http://")||e.startsWith("file://")||(o=location.origin+o),t._url_beforeSendHook)try{o=t._url_beforeSendHook(o)}catch(r){console.warn("Could not modify custom navigation event with url:beforeSend method",r)}n.publish({type:"url",value:o,id:K.generate(),createdAt:N.now()})}else console.warn("Missing path or location.")},t._url_setBeforeSendHook=function(e){t._url_beforeSendHook=e}},t.initialize=function(t){var e=t.host,o=t.analyticsHost,n=t.logger;G.initialize(e,n),X.initialize(e,n),o&&Q.initialize(o,n)},t}(),nt=function(){function t(){}return t.getResolution=function(){var t=Math.abs(window.orientation)-90===0?"landscape":"portrait",e="landscape"===t?window.screen.availHeight:window.screen.availWidth,o="landscape"===t?window.screen.availWidth:window.screen.availHeight;return window.innerWidth&&(e=window.innerWidth),window.innerHeight&&(o=window.innerHeight),isNaN(parseInt(e,10))||isNaN(parseInt(o,10))?null:{width:e,height:o,orientation:t}},t}();var rt=function(){function t(){}return t.appendScript=function(t){t.indexOf("MAIN_PATH")>-1&&(t="main.js"),t.indexOf("PICKER_PATH")>-1&&(t="picker.js");var e=document.getElementsByTagName("head")[0],o=document.createElement("script");o.async=!0,o.crossOrigin="anonymous",o.type="text/javascript",o.src="".concat('https://rec.smartlook.com',"/").concat(t),e.appendChild(o)},t}(),it=function(){function t(){}return t.tryLoad=function(t){window.smartlook_key=t,window.sessionStorage.getItem(m)||window.localStorage.getItem(m)?rt.appendScript("picker-20220331074633.js"):document.referrer.indexOf("picker/4f249306-efd5-4127-b768-79a6750a7c5d-ca97caf7-335a-4e1f-b047-be42cb6098f9")>=0&&(window.sessionStorage.setItem(m,"1"),rt.appendScript("picker-20220331074633.js"))},t}(),st=function(){return st=Object.assign||function(t){for(var e,o=1,n=arguments.length;o<n;o++)for(var r in e=arguments[o])Object.prototype.hasOwnProperty.call(e,r)&&(t[r]=e[r]);return t},st.apply(this,arguments)};!function(t){var e=function(){return function(t){var e=!1,o=window.document,n=function(r){e||(e=!0,o.removeEventListener("mousemove",n,{capture:!0}),o.removeEventListener("click",n,{capture:!0}),o.removeEventListener("keypress",n,{capture:!0}),o.removeEventListener("touchmove",n,{capture:!0}),o.removeEventListener("drag",n,{capture:!0}),o.removeEventListener("wheel",n,{capture:!0}),"visibility"===t()&&setTimeout(t,666))};o.addEventListener("mousemove",n,{passive:!0,capture:!0}),o.addEventListener("click",n,{passive:!0,capture:!0}),o.addEventListener("keypress",n,{passive:!0,capture:!0}),o.addEventListener("touchmove",n,{passive:!0,capture:!0}),o.addEventListener("drag",n,{passive:!0,capture:!0}),o.addEventListener("wheel",n,{passive:!0,capture:!0})}(t)};"complete"!==window.document.readyState&&"interactive"!==window.document.readyState?window.document.addEventListener("DOMContentLoaded",e,!1):e()}((function(){var t=window,e=t.smartlook;if(r.check(window.console)&&e&&Array.isArray(e.api)&&e.api&&!(e.api.length<=0)&&!e.recorderJSLoaded){e.version="v".concat("5.4.6 (2e5344762acf0b64bd3a1607da623ef0f2a4d38c - chore(release): 5.4.6 - 2022-03-31 09:44:49 +0200)"),e.recorderJSLoaded=!0,ot.register(e),l.load(e);var o=e.key;if(o){try{it.tryLoad(o)}catch(p){}if(function(){var t=parseInt(localStorage.getItem(q),10);return!!(t&&t>Date.now())||(localStorage.removeItem(q),localStorage.removeItem(W),!1)}())window.smartlook=function(){return $("This visitor is temporarily excluded from recording.")};else{var n=nt.getResolution();if(n)if(window===self){e.orientation=n.orientation,e.width=n.width||t.screen.width,e.height=n.height||t.screen.height;var i=new _(e),a=i.getStoredSidVid(o),c=a.sid,u=a.vid;i.loadDebugMode();var d={key:o,sid:c,vid:u,domain:t.document.location&&t.document.location.host,pageUrl:P.getCurrentUrl(),referer:t.document.referrer,screenWidth:e.width,screenHeight:e.height,internalProps:{version:"2e5344762acf0b64bd3a1607da623ef0f2a4d38c".substring(0,10)}};e._identityUid&&Object.assign(d,{uid:e._identityUid}),e._identityProps&&Object.assign(d,{props:e._identityProps}),I({method:"POST",url:"https://".concat(e.host,"/rec/check"),headers:{"Content-Type":"text/plain;charset=UTF-8"},body:s(d),withCredentials:!0,onSuccess:function(n){var r,s,a,c,u=JSON.parse(n.response);i.setSessionId(u.sid),i.setVisitorId(u.vid),i.setProjectKey(o),e._checkResponse=u,u.options&&(e._consentVersion=null!==(r=u.options.consentVersion)&&void 0!==r?r:1,i.setOptions(st(st({},u.options),{identifyApi:2===e._consentVersion?u.options.identifyApi:!u.options.disableApi}))),u.consent&&i.setConsentSettings(u.consent),u.analytics&&i.setAnalyticsSettings(u.analytics),u.recording&&i.setRecordingSettings(u.recording),u.integrations&&i.setIntegrationSettings(u.integrations),1===e._consentVersion?(e._recordEmails=!(null===(s=e.options)||void 0===s?void 0:s.maskEmails),e._recordNumbers=!(null===(a=e.options)||void 0===a?void 0:a.maskNumbers),e._recordForms=!(null===(c=e.options)||void 0===c?void 0:c.disableForms)&&!!e.consent.forms):2===e._consentVersion&&(e._recordEmails="boolean"===typeof e._recordEmails&&e._recordEmails,e._recordNumbers="boolean"===typeof e._recordNumbers&&e._recordNumbers,e._recordIPs="boolean"===typeof e._recordIPs&&e._recordIPs,e._recordForms="boolean"===typeof e._recordForms&&e._recordForms);var d=new Z(!!e.debug);t.smartlook_stopped||(ot.initialize({host:e.host,analyticsHost:e.analytics?e.analytics.host:void 0,logger:d}),e.recording&&rt.appendScript("main-20220331074633.js"))},onError:function(t){B("Check error - ".concat(t.response," - ").concat(t.status));try{var e=JSON.parse(t.response);console.warn("Smartlook not recording, reason:",e.message)}catch(p){}}})}else window.smartlook=function(){return $("Cannot record this user because self or window object is replaced with custom value.")};else window.smartlook=function(){return $("Cannot record this user because it is not possible to get visitor's display resolution.")}}}else window.smartlook=function(){return $("Missing Smartlook key.")}}}))}()}();