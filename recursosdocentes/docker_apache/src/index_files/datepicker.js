define(['ko','underscore','jquery','mage/translate','mage/calendar','moment','mageUtils'],function(ko,_,$,$t,calendar,moment,utils){'use strict';var defaults={dateFormat:'mm\/dd\/yyyy',showsTime:false,timeFormat:null,buttonImage:null,buttonImageOnly:null,buttonText:$t('Select Date')};ko.bindingHandlers.datepicker={init:function(el,valueAccessor){var config=valueAccessor(),observable,options={};_.extend(options,defaults);if(typeof config==='object'){observable=config.storage;_.extend(options,config.options);}else{observable=config;}
$(el).calendar(options);observable()&&$(el).datepicker('setDate',moment(observable(),utils.convertToMomentFormat(options.dateFormat+(options.showsTime?' '+options.timeFormat:''))).toDate());$(el).blur();ko.utils.registerEventHandler(el,'change',function(){observable(this.value);});}};});