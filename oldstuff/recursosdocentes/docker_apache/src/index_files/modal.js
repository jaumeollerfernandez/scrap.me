define(['jquery','underscore','mage/template','text!ui/template/modal/modal-popup.html','text!ui/template/modal/modal-slide.html','text!ui/template/modal/modal-custom.html','Magento_Ui/js/lib/key-codes','jquery/ui','mage/translate'],function($,_,template,popupTpl,slideTpl,customTpl,keyCodes){'use strict';var transitionEvent=(function(){var transition,elementStyle=document.createElement('div').style,transitions={'transition':'transitionend','OTransition':'oTransitionEnd','MozTransition':'transitionend','WebkitTransition':'webkitTransitionEnd'};for(transition in transitions){if(elementStyle[transition]!==undefined&&transitions.hasOwnProperty(transition)){return transitions[transition];}}})();$.widget('mage.modal',{options:{id:null,type:'popup',title:'',subTitle:'',modalClass:'',focus:'[data-role="closeBtn"]',autoOpen:false,clickableOverlay:true,popupTpl:popupTpl,slideTpl:slideTpl,customTpl:customTpl,modalVisibleClass:'_show',parentModalClass:'_has-modal',innerScrollClass:'_inner-scroll',responsive:false,innerScroll:false,modalTitle:'[data-role="title"]',modalSubTitle:'[data-role="subTitle"]',modalBlock:'[data-role="modal"]',modalCloseBtn:'[data-role="closeBtn"]',modalContent:'[data-role="content"]',modalAction:'[data-role="action"]',focusableScope:'[data-role="focusable-scope"]',focusableStart:'[data-role="focusable-start"]',focusableEnd:'[data-role="focusable-end"]',appendTo:'body',wrapperClass:'modals-wrapper',overlayClass:'modals-overlay',responsiveClass:'modal-slide',trigger:'',modalLeftMargin:45,closeText:$.mage.__('Close'),buttons:[{text:$.mage.__('Ok'),class:'',attr:{},click:function(event){this.closeModal(event);}}],keyEventHandlers:{tabKey:function(){if(document.activeElement===this.modal[0]){this._setFocus('start');}},escapeKey:function(event){if(this.options.isOpen&&this.modal.find(document.activeElement).length||this.options.isOpen&&this.modal[0]===document.activeElement){this.closeModal(event);}}}},_create:function(){_.bindAll(this,'keyEventSwitcher','_tabSwitcher','closeModal');this.options.id=this.uuid;this.options.transitionEvent=transitionEvent;this._createWrapper();this._renderModal();this._createButtons();$(this.options.trigger).on('click',_.bind(this.toggleModal,this));this._on(this.modal.find(this.options.modalCloseBtn),{'click':this.options.modalCloseBtnHandler?this.options.modalCloseBtnHandler:this.closeModal});this._on(this.element,{'openModal':this.openModal,'closeModal':this.closeModal});this.options.autoOpen?this.openModal():false;},_getElem:function(elem){return this.modal.find(elem);},_getVisibleCount:function(){var modals=this.modalWrapper.find(this.options.modalBlock);return modals.filter('.'+this.options.modalVisibleClass).length;},_getVisibleSlideCount:function(){var elems=this.modalWrapper.find('[data-type="slide"]');return elems.filter('.'+this.options.modalVisibleClass).length;},keyEventSwitcher:function(event){var key=keyCodes[event.keyCode];if(this.options.keyEventHandlers.hasOwnProperty(key)){this.options.keyEventHandlers[key].apply(this,arguments);}},setTitle:function(title){var $title=$(this.options.modalTitle),$subTitle=this.modal.find(this.options.modalSubTitle);$title.text(title);$title.append($subTitle);},setSubTitle:function(subTitle){this.options.subTitle=subTitle;this.modal.find(this.options.modalSubTitle).html(subTitle);},toggleModal:function(){if(this.options.isOpen===true){this.closeModal();}else{this.openModal();}},openModal:function(){this.options.isOpen=true;this.focussedElement=document.activeElement;this._createOverlay();this._setActive();this._setKeyListener();this.modal.one(this.options.transitionEvent,_.bind(this._setFocus,this,'end','opened'));this.modal.one(this.options.transitionEvent,_.bind(this._trigger,this,'opened'));this.modal.addClass(this.options.modalVisibleClass);if(!this.options.transitionEvent){this._trigger('opened');}
return this.element;},_setFocus:function(position,type){var focusableElements,infelicity;if(type==='opened'&&this.options.focus){this.modal.find($(this.options.focus)).focus();}else if(type==='opened'&&!this.options.focus){this.modal.find(this.options.focusableScope).focus();}else if(position==='end'){this.modal.find(this.options.modalCloseBtn).focus();}else if(position==='start'){infelicity=2;focusableElements=this.modal.find(':focusable');focusableElements.eq(focusableElements.length-infelicity).focus();}},_setKeyListener:function(){this.modal.find(this.options.focusableStart).bind('focusin',this._tabSwitcher);this.modal.find(this.options.focusableEnd).bind('focusin',this._tabSwitcher);this.modal.bind('keydown',this.keyEventSwitcher);},_removeKeyListener:function(){this.modal.find(this.options.focusableStart).unbind('focusin',this._tabSwitcher);this.modal.find(this.options.focusableEnd).unbind('focusin',this._tabSwitcher);this.modal.unbind('keydown',this.keyEventSwitcher);},_tabSwitcher:function(e){var target=$(e.target);if(target.is(this.options.focusableStart)){this._setFocus('start');}else if(target.is(this.options.focusableEnd)){this._setFocus('end');}},closeModal:function(){var that=this;this._removeKeyListener();this.options.isOpen=false;this.modal.one(this.options.transitionEvent,function(){that._close();});this.modal.removeClass(this.options.modalVisibleClass);if(!this.options.transitionEvent){that._close();}
return this.element;},_close:function(){var trigger=_.bind(this._trigger,this,'closed',this.modal);$(this.focussedElement).focus();this._destroyOverlay();this._unsetActive();_.defer(trigger,this);},_setActive:function(){var zIndex=this.modal.zIndex(),baseIndex=zIndex+this._getVisibleCount();if(this.modal.data('active')){return;}
this.modal.data('active',true);this.overlay.zIndex(++baseIndex);this.prevOverlayIndex=this.overlay.zIndex();this.modal.zIndex(this.overlay.zIndex()+1);if(this._getVisibleSlideCount()){this.modal.css('marginLeft',this.options.modalLeftMargin*this._getVisibleSlideCount());}},_unsetActive:function(){this.modal.removeAttr('style');this.modal.data('active',false);if(this.overlay){this.overlay.zIndex(this.prevOverlayIndex-1);}},_createWrapper:function(){this.modalWrapper=$(this.options.appendTo).find('.'+this.options.wrapperClass);if(!this.modalWrapper.length){this.modalWrapper=$('<div></div>').addClass(this.options.wrapperClass).appendTo(this.options.appendTo);}},_renderModal:function(){$(template(this.options[this.options.type+'Tpl'],{data:this.options})).appendTo(this.modalWrapper);this.modal=this.modalWrapper.find(this.options.modalBlock).last();this.element.appendTo(this._getElem(this.options.modalContent));if(this.element.is(':hidden')){this.element.show();}},_createButtons:function(){this.buttons=this._getElem(this.options.modalAction);_.each(this.options.buttons,function(btn,key){var button=this.buttons[key];if(btn.attr){$(button).attr(btn.attr);}
if(btn.class){$(button).addClass(btn.class);}
if(!btn.click){btn.click=this.closeModal;}
$(button).on('click',_.bind(btn.click,this));},this);},_createOverlay:function(){var events,outerClickHandler=this.options.outerClickHandler||this.closeModal;this.overlay=$('.'+this.options.overlayClass);if(!this.overlay.length){$(this.options.appendTo).addClass(this.options.parentModalClass);this.overlay=$('<div></div>').addClass(this.options.overlayClass).appendTo(this.modalWrapper);}
events=$._data(this.overlay.get(0),'events');events?this.prevOverlayHandler=events.click[0].handler:false;this.options.clickableOverlay?this.overlay.unbind().on('click',outerClickHandler):false;},_destroyOverlay:function(){if(this._getVisibleCount()){this.overlay.unbind().on('click',this.prevOverlayHandler);}else{$(this.options.appendTo).removeClass(this.options.parentModalClass);this.overlay.remove();this.overlay=null;}}});return $.mage.modal;});