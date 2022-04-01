'use strict';define(['uiComponent','jquery','ko','MSP_ReCaptcha/js/registry'],function(Component,$,ko,registry,undefined){return Component.extend({defaults:{template:'MSP_ReCaptcha/reCaptcha',reCaptchaId:'msp-recaptcha'},_isApiRegistered:undefined,initialize:function(){this._super();this._loadApi();},_loadApi:function(){var element,scriptTag;if(this._isApiRegistered!==undefined){if(this._isApiRegistered===true){$(window).trigger('recaptchaapiready');}
return;}
this._isApiRegistered=false;window.globalOnRecaptchaOnLoadCallback=function(){this._isApiRegistered=true;$(window).trigger('recaptchaapiready');}.bind(this);element=document.createElement('script');scriptTag=document.getElementsByTagName('script')[0];element.async=true;element.src='https://www.google.com/recaptcha/api.js'
+'?onload=globalOnRecaptchaOnLoadCallback&render=explicit'
+(this.settings.lang?'&hl='+this.settings.lang:'');scriptTag.parentNode.insertBefore(element,scriptTag);},getIsVisible:function(){return this.settings.enabled[this.zone];},getIsInvisibleRecaptcha:function(){return this.settings.size==='invisible';},reCaptchaCallback:function(token){if(this.settings.size==='invisible'){this.tokenField.value=token;this.$parentForm.submit();}},initCaptcha:function(){var me=this,$parentForm,$wrapper,$reCaptcha,widgetId,listeners;if(this.captchaInitialized){return;}
this.captchaInitialized=true;$wrapper=$('#'+this.getReCaptchaId()+'-wrapper');$reCaptcha=$wrapper.find('.g-recaptcha');$reCaptcha.attr('id',this.getReCaptchaId());$parentForm=$wrapper.parents('form');me=this;widgetId=grecaptcha.render(this.getReCaptchaId(),{'sitekey':this.settings.siteKey,'theme':this.settings.theme,'size':this.settings.size,'badge':this.badge?this.badge:this.settings.badge,'callback':function(token){me.reCaptchaCallback(token);me.validateReCaptcha(true);},'expired-callback':function(){me.validateReCaptcha(false);}});if(this.settings.size==='invisible'&&$parentForm.length>0){$parentForm.submit(function(event){if(!me.tokenField.value){grecaptcha.execute(widgetId);event.preventDefault(event);event.stopImmediatePropagation();}});listeners=$._data($parentForm[0],'events').submit;listeners.unshift(listeners.pop());this.tokenField=$('<input type="text" name="token" style="display: none" />')[0];this.$parentForm=$parentForm;$parentForm.append(this.tokenField);}else{this.tokenField=null;}
registry.ids.push(this.getReCaptchaId());registry.captchaList.push(widgetId);registry.tokenFields.push(this.tokenField);},validateReCaptcha:function(state){if(this.settings.size!=='invisible'){return $(document).find('input[type=checkbox].required-captcha').prop("checked",state);}},renderReCaptcha:function(){var me=this;if(this.getIsVisible()){if(window.grecaptcha&&window.grecaptcha.render){me.initCaptcha();}else{$(window).on('recaptchaapiready',function(){me.initCaptcha();});}}},getReCaptchaId:function(){return this.reCaptchaId;}});});