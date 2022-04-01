/*!
  Knockout Fast Foreach v0.4.1 (2015-07-17T14:06:15.974Z)
  By: Brian M Hunt (C) 2015
  License: MIT

  Adds `fastForEach` to `ko.bindingHandlers`.
*/
(function(root,factory){if(typeof define==='function'&&define.amd){define(['knockout'],factory);}else if(typeof exports==='object'){module.exports=factory(require('knockout'));}else{root.KnockoutFastForeach=factory(root.ko);}}(this,function(ko){"use strict";function isPlainObject(o){return!!o&&typeof o==='object'&&o.constructor===Object;}
var commentNodesHaveTextProperty=document&&document.createComment("test").text==="<!--test-->";var startCommentRegex=commentNodesHaveTextProperty?/^<!--\s*ko(?:\s+([\s\S]+))?\s*-->$/:/^\s*ko(?:\s+([\s\S]+))?\s*$/;var supportsDocumentFragment=document&&typeof document.createDocumentFragment==="function";function isVirtualNode(node){return(node.nodeType===8)&&startCommentRegex.test(commentNodesHaveTextProperty?node.text:node.nodeValue);}
function makeTemplateNode(sourceNode){var container=document.createElement("div");var parentNode;if(sourceNode.content){parentNode=sourceNode.content;}else if(sourceNode.tagName==='SCRIPT'){parentNode=document.createElement("div");parentNode.innerHTML=sourceNode.text;}else{parentNode=sourceNode;}
ko.utils.arrayForEach(ko.virtualElements.childNodes(parentNode),function(child){if(child){container.insertBefore(child.cloneNode(true),null);}});return container;}
function insertAllAfter(containerNode,nodeOrNodeArrayToInsert,insertAfterNode){var frag,len,i;if(typeof nodeOrNodeArrayToInsert.nodeType!=="undefined"&&typeof nodeOrNodeArrayToInsert.length==="undefined"){throw new Error("Expected a single node or a node array");}
if(typeof nodeOrNodeArrayToInsert.nodeType!=="undefined"){ko.virtualElements.insertAfter(containerNode,nodeOrNodeArrayToInsert,insertAfterNode);return;}
if(nodeOrNodeArrayToInsert.length===1){ko.virtualElements.insertAfter(containerNode,nodeOrNodeArrayToInsert[0],insertAfterNode);return;}
if(supportsDocumentFragment){frag=document.createDocumentFragment();for(i=0,len=nodeOrNodeArrayToInsert.length;i!==len;++i){frag.appendChild(nodeOrNodeArrayToInsert[i]);}
ko.virtualElements.insertAfter(containerNode,frag,insertAfterNode);}else{for(i=nodeOrNodeArrayToInsert.length-1;i>=0;--i){var child=nodeOrNodeArrayToInsert[i];if(!child){return;}
ko.virtualElements.insertAfter(containerNode,child,insertAfterNode);}}}
function valueToChangeAddItem(value,index){return{status:'added',value:value,index:index};}
function isAdditionAdjacentToLast(changeIndex,arrayChanges){return changeIndex>0&&changeIndex<arrayChanges.length&&arrayChanges[changeIndex].status==="added"&&arrayChanges[changeIndex-1].status==="added"&&arrayChanges[changeIndex-1].index===arrayChanges[changeIndex].index-1;}
function FastForEach(spec){this.element=spec.element;this.container=isVirtualNode(this.element)?this.element.parentNode:this.element;this.$context=spec.$context;this.data=spec.data;this.as=spec.as;this.noContext=spec.noContext;this.templateNode=makeTemplateNode(spec.name?document.getElementById(spec.name).cloneNode(true):spec.element);this.afterQueueFlush=spec.afterQueueFlush;this.beforeQueueFlush=spec.beforeQueueFlush;this.changeQueue=[];this.lastNodesList=[];this.indexesToDelete=[];this.rendering_queued=false;ko.virtualElements.emptyNode(this.element);var primeData=ko.unwrap(this.data);if(primeData.map){this.onArrayChange(primeData.map(valueToChangeAddItem));}
if(ko.isObservable(this.data)){if(!this.data.indexOf){this.data=this.data.extend({trackArrayChanges:true});}
this.changeSubs=this.data.subscribe(this.onArrayChange,this,'arrayChange');}}
FastForEach.animateFrame=window.requestAnimationFrame||window.webkitRequestAnimationFrame||window.mozRequestAnimationFrame||window.msRequestAnimationFrame||function(cb){return window.setTimeout(cb,1000 / 60);};FastForEach.prototype.dispose=function(){if(this.changeSubs){this.changeSubs.dispose();}};FastForEach.prototype.onArrayChange=function(changeSet){var self=this;var changeMap={added:[],deleted:[]};for(var i=0,len=changeSet.length;i<len;i++){if(isAdditionAdjacentToLast(i,changeSet)){var batchValues=changeMap.added[changeMap.added.length-1].values;if(!batchValues){var lastAddition=changeMap.added.pop();var batchAddition={isBatch:true,status:'added',index:lastAddition.index,values:[lastAddition.value]};batchValues=batchAddition.values;changeMap.added.push(batchAddition);}
batchValues.push(changeSet[i].value);}else{changeMap[changeSet[i].status].push(changeSet[i]);}}
if(changeMap.deleted.length>0){this.changeQueue.push.apply(this.changeQueue,changeMap.deleted);this.changeQueue.push({status:'clearDeletedIndexes'});}
this.changeQueue.push.apply(this.changeQueue,changeMap.added);if(this.changeQueue.length>0&&!this.rendering_queued){this.rendering_queued=true;FastForEach.animateFrame.call(window,function(){self.processQueue();});}};FastForEach.prototype.processQueue=function(){var self=this;if(typeof this.beforeQueueFlush==='function'){this.beforeQueueFlush(this.changeQueue);}
ko.utils.arrayForEach(this.changeQueue,function(changeItem){self[changeItem.status](changeItem);});this.rendering_queued=false;if(typeof this.afterQueueFlush==='function'){this.afterQueueFlush(this.changeQueue);}
this.changeQueue=[];};FastForEach.prototype.added=function(changeItem){var index=changeItem.index;var valuesToAdd=changeItem.isBatch?changeItem.values:[changeItem.value];var referenceElement=this.lastNodesList[index-1]||null;var allChildNodes=[];for(var i=0,len=valuesToAdd.length;i<len;++i){var templateClone=this.templateNode.cloneNode(true);var childContext;if(this.noContext){childContext=this.$context.extend({'$item':valuesToAdd[i]});}else{childContext=this.$context.createChildContext(valuesToAdd[i],this.as||null);}
ko.applyBindingsToDescendants(childContext,templateClone);var childNodes=ko.virtualElements.childNodes(templateClone);allChildNodes.push.apply(allChildNodes,Array.prototype.slice.call(childNodes));this.lastNodesList.splice(index+i,0,childNodes[childNodes.length-1]);}
insertAllAfter(this.element,allChildNodes,referenceElement);};FastForEach.prototype.deleted=function(changeItem){var index=changeItem.index;var ptr=this.lastNodesList[index],lastNode=this.lastNodesList[index-1]||this.element;do{ptr=ptr.previousSibling;ko.removeNode((ptr&&ptr.nextSibling)||ko.virtualElements.firstChild(this.element));}while(ptr&&ptr!==lastNode);this.lastNodesList[index]=this.lastNodesList[index-1];this.indexesToDelete.push(index);};FastForEach.prototype.clearDeletedIndexes=function(){for(var i=this.indexesToDelete.length-1;i>=0;--i){this.lastNodesList.splice(this.indexesToDelete[i],1);}
this.indexesToDelete=[];};ko.bindingHandlers.fastForEach={init:function init(element,valueAccessor,bindings,vm,context){var value=valueAccessor(),ffe;if(isPlainObject(value)){value.element=value.element||element;value.$context=context;ffe=new FastForEach(value);}else{ffe=new FastForEach({element:element,data:ko.unwrap(context.$rawData)===value?context.$rawData:value,$context:context});}
ko.utils.domNodeDisposal.addDisposeCallback(element,function(){ffe.dispose();});return{controlsDescendantBindings:true};},FastForEach:FastForEach};ko.virtualElements.allowedBindings.fastForEach=true;}));