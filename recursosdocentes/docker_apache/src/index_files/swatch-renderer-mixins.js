define(['jquery','underscore','Mageplaza_Core/js/jquery.magnific-popup.min'],function($,_){'use strict';window.Variables={initSizeChartLink:function(selector){if($('.mp-sizechart-popup-link').length===0){$(selector).append
('<div class="mp-sizechart-popup-link">'+'<a href="#open-popup"">'+sizeChartData.label+'<img src="'+sizeChartData.iconUrl+'" alt="chart-icon" /></a>'+'</div>'+'<div class="clearfix"></div> '+'<div id="open-popup" class="white-popup mfp-hide"> '+'<header>Size Chart</header>'+'<div id="mp-size-chart-wrapper">'+sizeChartData.ruleContentHtml+''+'</div>'+'</div>');$(selector).css({"position":"relative"});}
$('.mp-sizechart-popup-link a').magnificPopup({type:'inline',midClick:true});}};return function(widget){$.widget('mage.SwatchRenderer',widget,{_RenderControls:function(){this._super();if($('.product-info-main').length&&typeof sizeChartData!=="undefined"){var swatchContainer=$('.product-info-main .swatch-opt').find('[attribute-code="'+sizeChartData.attributeCode+'"]');if(swatchContainer.length&&sizeChartData.displayType.indexOf('popup')>=0){Variables.initSizeChartLink(swatchContainer);}}}});return $.mage.SwatchRenderer;};});