define(['jquery','jquery/ui','mage/translate'],function($){'use strict';$.widget('mage.relatedProducts',{options:{relatedCheckbox:'.related-checkbox',relatedProductsCheckFlag:false,relatedProductsField:'#related-products-field',selectAllMessage:$.mage.__('select all'),unselectAllMessage:$.mage.__('unselect all'),selectAllLink:'[role="select-all"]',elementsSelector:'.item.product'},_create:function(){$(this.options.selectAllLink).on('click',$.proxy(this._selectAllRelated,this));$(this.options.relatedCheckbox).on('click',$.proxy(this._addRelatedToProduct,this));this._showRelatedProducts(this.element.find(this.options.elementsSelector),this.element.data('limit'),this.element.data('shuffle'));},_selectAllRelated:function(e){var innerHTML=this.options.relatedProductsCheckFlag?this.options.selectAllMessage:this.options.unselectAllMessage;$(e.target).html(innerHTML);$(this.options.relatedCheckbox).attr('checked',this.options.relatedProductsCheckFlag=!this.options.relatedProductsCheckFlag);this._addRelatedToProduct();return false;},_addRelatedToProduct:function(){$(this.options.relatedProductsField).val($(this.options.relatedCheckbox+':checked').map(function(){return this.value;}).get().join(','));},_showRelatedProducts:function(elements,limit,shuffle){var index;if(shuffle){this._shuffle(elements);}
if(limit===0){limit=elements.length;}
for(index=0;index<limit;index++){$(elements[index]).show();}},_shuffle:function shuffle(o){for(var j,x,i=o.length;i;j=Math.floor(Math.random()*i),x=o[--i],o[i]=o[j],o[j]=x);return o;}});return $.mage.relatedProducts;});