define(['module','Manadev_Core/js/functions/class','jquery','Manadev_Core/js/Data','Manadev_Core/js/vars/urlParser','Manadev_Core/js/vars/content','Manadev_LayeredNavigationAjax/js/State','Manadev_Core/js/vars/overlay'],function(module,class_,$,Data,urlParser,content,State,overlay){return class_(module.id,Data,{start:function(options){if(content.isPrevented('layered-navigation-ajax')){return;}
this.set(options);this.state=new State({url:location.hash?location.href.substr(0,location.href.length-location.hash.length):location.href,enabled:this.integrate_with_history,use_history:true});this.state.addChangeListener(this.onStateChange.bind(this));$(document).on('click','a',this.onClick.bind(this));this.started=true;},onClick:function(e){var el=this.findParentLinkElement(e.target)
var categ=(el.childElements()[0].className=="count")?true:false;if(el.hasClassName('page')||el.hasClassName('next')||el.hasClassName('previous')||el.hasClassName('filter-clear')||el.hasClassName('remove')||el.hasClassName('swatch-option-link-layered')||categ){this.showIndicators();}},findParentLinkElement:function(el){for(;el!=null;el=el.parentNode){if(el.tagName.toLowerCase()=='a'){return el;}}
return null;},intercept:function(url,el,action){var result;if($(el).hasClass('mana-apply-filters')){this.state.apply();return true;}
if((result=this.checkInterceptedParameters(url,el))!==undefined){return result;}
this.saveLastInterceptedUrl(url);if((action=this.parseAction(url,el,action))===undefined){return false;}
if(this.log_to_console){console.log({url:url,el:el,action:action});}
var shouldActionBeAppliedLater=this.shouldActionBeAppliedLater(action);this.state.addAction(action,shouldActionBeAppliedLater);if(shouldActionBeAppliedLater){var actionCount=this.state.state.pending_actions.length;$('.mana-apply-filters span').text(this.apply_filter_text);}
return true;},onStateChange:function(){var self=this;if(this.state.operation=='reset'){return;}
this.showIndicators();var currentCategory=this.getCurrentCategory();var request=new XMLHttpRequest();request.open('GET',this.getUrl(),true);request.onload=function(){if(request.status!=200){if(self.log_to_console){console.log('HTTP error occured while refreshing layered navigation and product list content');console.log(request);}
self.hideIndicators();return;}
if(!request.responseText.trim()){if(self.log_to_console){console.log('Empty layered navigation and product list content received');console.log(request);}
self.hideIndicators();return;}
var sections=request.responseText.split(self.getSectionSeparator());var json=JSON.parse(sections.shift());if(self.log_to_console){console.log({json:json,sections:sections});}
if(self.getQuery()!=json.query){if(self.log_to_console){console.log('While response was generated new AJAX request was sent. Skipping rendering.');}
return;}
try{var replacements={};for(var key in json.blocks){if(!json.blocks.hasOwnProperty(key))continue;var selector=self.selector_translations[key]||key;var $target=$(selector);if(!$target.length){if(self.log_to_console){console.log("Target element '"+selector+"' not found");}
continue;}
replacements[selector]=sections[json.blocks[key]];}
content.replace(replacements);if(self.shouldScrollToTop()){scroll(0,0);}
if(json.title){document.title=json.title;}
self.current_category=currentCategory;self.state.reset(json.url);self.reportToAnalytics(json.url);}
finally{self.hideIndicators();}};request.onerror=function(){if(self.log_to_console){console.log('General connectivity error occured while refreshing layered navigation and product list content');console.log(request);}
self.hideIndicators();};request.send();},shouldActionBeAppliedLater:function(action){return this.use_button_to_apply_filters&&!action.match(/^(p|product_list_order|product_list_dir|product_list_mode|product_list_limit)=/);},checkInterceptedParameters:function(url,el){if(url===this.lastInterceptedUrl){return true;}
if(url==location.href+'#'){return false;}
if(!this.selector||!el||!$(this.selector).has(el).length){return false;}},saveLastInterceptedUrl:function(url){var self=this;this.lastInterceptedUrl=url;setTimeout(function(){delete self.lastInterceptedUrl;},0);},parseAction:function(url,el,action){if(action){return action;}
if(action=this.parseLinkElementAction(el)){return action;}},parseLinkElementAction:function(el){return $(el).data('action');},getSectionSeparator:function(){return"91b5970cd70e2353d866806f8003c1cd56646961";},showIndicators:function(){if(this.show_overlay||this.use_button_to_apply_filters){overlay.show();}
if(this.show_indicator){$('#mana-please-wait').show();}},hideIndicators:function(){if(this.show_overlay||this.use_button_to_apply_filters){overlay.hide();}
if(this.show_indicator){$('#mana-please-wait').hide();}},shouldScrollToTop:function(){if(this.scroll_to_top_mode=='after_any_ajax_action'){return true;}
if(this.scroll_to_top_mode!='after_pager_clicks'){return false;}
for(var i=0;i<this.state.state.pending_actions.length;i++){if(this.state.state.pending_actions[i].match(/^p=\d+$/)){return true;}}
return false;},getCurrentPage:function(){for(var i=this.state.state.confirmed_actions.length-1;i>=0;i--){var query=urlParser.parseQuery(this.state.state.confirmed_actions[i]);if(query.p!==undefined){return parseInt(query.p||'1')||1;}}
return parseInt(urlParser.parseQuery(this.current_params).p||'1')||1;},getUrl:function(){var url=this.url;if(this.current_category!==this.getCurrentCategory()){url+='&_category_changed=1';}
var query=this.getQuery();if(query){url+='&'+query;}
return url;},getQuery:function(){var result='';this.sortParameters(this.getParameters()).forEach(function(parameter){if(result){result+='&';}
result+=parameter.key+'='+parameter.value;}.bind(this));return result;},sortParameters:function(parameters){var result=[];for(var key in parameters){if(!parameters.hasOwnProperty(key))continue;result.push({key:key,value:parameters[key]});}
result.sort(function(a,b){if(a.key<b.key)return-1;if(a.key>b.key)return 1;return 0;}.bind(this));return result;},getParameters:function(){var result=urlParser.parseQuery(this.current_params);this.addActionsToParameters(result,this.state.state.confirmed_actions);this.addActionsToParameters(result,this.state.state.pending_actions);return result;},addActionsToParameters:function(parameters,actions){this.forEachActionIn(actions,function(action){var match=action.match(/([+-]?)(.*)=(.*)/);if(!match){return;}
var operation=match[1],param=match[2],value=match[3],values,pos;switch(operation){case'+':values=parameters[param]!==undefined?parameters[param].split('_'):[];values.push(value);values.sort(function(a,b){if(isNaN(a-parseFloat(a))){if(a<b)return-1;if(a>b)return 1;}
else{if(parseInt(a)<parseInt(b))return-1;if(parseInt(a)>parseInt(b))return 1;}
return 0;}.bind(this));parameters[param]=values.join('_');break;case'-':values=parameters[param]!==undefined?parameters[param].split('_'):[];if((pos=values.indexOf(value))!==-1){values.splice(pos,1);}
if(values.length){parameters[param]=values.join('_');}
else if(parameters[param]!==undefined){delete parameters[param];}
break;default:if(value!==''){parameters[param]=value;}
else if(parameters[param]!==undefined){delete parameters[param];}}}.bind(this));},forEachActionIn:function(actions,callback){actions.forEach(function(query){query.split('&').forEach(function(action){callback(action);}.bind(this));}.bind(this));},reportToAnalytics:function(url){if(!this.ga_account){return;}
var parser=document.createElement('a');parser.href=url;if(window._gaq!==undefined){window._gaq.push(['_setAccount',this.ga_account]);window._gaq.push(['_trackPageview',url.substring(parser.protocol.length+parser.hostname.length+2)]);}
if(window.ga!==undefined){window.ga('send','pageview',{'page':url.substring(parser.protocol.length+parser.hostname.length+2)});}},getCurrentCategory:function(){var parameters=this.getParameters();return parameters.cat;}});});