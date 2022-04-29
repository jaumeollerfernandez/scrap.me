var productStickerSummary=function(e){function t(r){if(n[r])return n[r].exports;var s=n[r]={exports:{},id:r,loaded:!1};return e[r].call(s.exports,s,s.exports,t),s.loaded=!0,s.exports}var n={};return t.m=e,t.c=n,t.p="",t(0)}([function(e,t,n){"use strict";var r=n(1),s=(n(2),n(3)),o=function(e){var t=r.getBaseConfig(e,"14px");return t.element=document.querySelector(e.element),t.element?(t.showRating=r.property.getBoolean(e,"showRating",!0),t.themePath=r.property.getString(e,"themePath","//widgets.trustedshops.com/reviews/tsSticker/css/"),t.scrollToReviews=r.property.getBoolean(e,"scrollToReviews",!1),t.enablePlaceholder=r.property.getBoolean(e,"enablePlaceholder",!1),t):(console.log("Trusted Shop Product Review Summary - Element not found"),!1)},i=i||function(){return{showSummary:function(e){if(!r.isConfigValid(e,"Trusted Shop Product Review Summary"))return!1;if(!e.element)return console.log("Trusted Shop Product Review Summary - Invalid element"),!1;var t=o(e),n=new s(t).loadReviewSticker;r.loadAndAddListeners(n)}}};e.exports=i},function(e,t,n){"use strict";var r=n(2),s=function(e){var t="de_DE";if(e)switch(e){case"de_DE":case"de_AT":case"de_CH":t="de_DE";break;case"en_GB":case"en_US":case"en_EU":t="en_GB";break;case"fr_FR":case"fr_CH":case"fr_BE":t="fr_FR";break;case"pt_PT":t="pt_PT";break;case"pl_PL":t="pl_PL";break;case"es_ES":t="es_ES";break;case"it_IT":t="it_IT";break;case"nl_NL":case"nl_BE":t="nl_NL";break;default:console.log("Unsupported locale: '"+e+"'. Setting default: 'de_DE'"),t="de_DE"}return t},o=function(e){var t=new RegExp("^[Xx][a-zA-Z0-9]{32}$");return t.test(e)},i={uniq:function(e){var t={"boolean":{},number:{},string:{}},n=[];return e.filter(function(e){var r=typeof e;return r in t?!t[r].hasOwnProperty(e)&&(t[r][e]=!0):!(n.indexOf(e)>=0)&&n.push(e)})}},a={isConfigValid:function(e,t){var n=!0;return r.isIE()&&r.isIE()<9&&(n=!1),e.tsId=e.tsId?e.tsId:e.tsid,e.tsId&&o(e.tsId)||(console.log(t+" - Invalid TSID"),n=!1),e.sku||(console.log(t+" - Invalid SKU"),n=!1),n},property:{getInteger:function(e,t,n){return t in e?parseInt(e[t]):parseInt(n)},getString:function(e,t,n){return t in e?e[t]:n},getBoolean:function(e,t,n){var r=n;if(t in e){var s=e[t];"boolean"==typeof s?r=s:"string"==typeof s&&(r="true"===s.trim().toLowerCase())}return r}},getBaseConfig:function(e,t){var n={};return n.tsId=a.property.getString(e,"tsId",null).toUpperCase(),n.sku=e.sku instanceof Array?i.uniq(e.sku):[e.sku],n.apiServer=a.property.getString(e,"apiServer","//cdn1.api.trustedshops.com/"),n.introtext=a.property.getString(e,"introtext","&nbsp;"),n.locale=s(a.property.getString(e,"locale","de_DE")),n.starColor=a.property.getString(e,"starColor",null),n.starSize=a.property.getString(e,"starSize",t),n.fontSize=a.property.getString(e,"fontSize","12px"),n.theme=a.property.getString(e,"theme","light"),n},isDom:function(e){try{return e instanceof HTMLElement}catch(t){return"object"==typeof e&&1===e.nodeType&&"object"==typeof e.style&&"object"==typeof e.ownerDocument}},loadAndAddListeners:function(e){"complete"===document.readyState?e():window.addEventListener?window.addEventListener("load",e,!1):window.attachEvent?window.attachEvent("onload",e):window.onload=e}};e.exports=a},function(e,t){"use strict";e.exports={isIE:function(){var e=navigator.userAgent.toLowerCase();return e.indexOf("msie")!==-1&&parseInt(e.split("msie")[1])},getTparameter:function(e,t,n){var r=n instanceof Array?n[0].trim():n.trim();return"?tsId="+t+"&sku="+r+"&page="+e},basepath:function(e,t){var n;return-1!==(n=e.lastIndexOf("/"))?e.substr(0,n)+t:e+"/"+t}}},function(e,t,n){"use strict";var r=n(4),s=n(5),o=n(7),i=n(6),a=i.Product,u=function(e){var t=function(e,t){e instanceof Array&&0===e.length&&(e=[new a]);var n=new o(t),r=n.render(e);t.element.innerHTML="",t.element.appendChild(r)},n=[],i=100,u=function(e){return 0===s.apiCdnProductReviewSummaries.runningRequestsCount()||0===i?(t(n,e),!0):(i--,void setTimeout(u,10,e))};return{loadReviewSticker:function(){r.loadTheme(e.themePath+e.theme+".theme.css",function(){for(var t=0;t<e.sku.length;t++)s.apiCdnProductReviewSummaries.incrementRunningRequestsCount(),s.apiCdnProductReviewSummaries.rest(e.apiServer,e.tsId,e.sku[t].trim(),function(e){"undefined"!=typeof e&&n.push(e),s.apiCdnProductReviewSummaries.decrementRunningRequestsCount()});u(e)})}}};e.exports=u},function(e,t){"use strict";e.exports={loadTheme:function(e,t){for(var n=document.getElementsByTagName("HEAD")[0],r=n.childNodes,s=0;s<r.length;s++)if("LINK"===r[s].nodeName.toUpperCase()&&r[s].href&&r[s].href===e)return void(t&&t());var o=document.createElement("LINK");o.rel="stylesheet",o.type="text/css",o.charset="utf-8",o.href=e,t&&(o.onload=t),n.appendChild(o)}}},function(e,t,n){"use strict";var r=n(6),s=r.Product,o=r.ProductReview,i=r.ShopStatement,a=r.ProductSummary,u=r.Buyer,c=n(2),d=function(e){for(var t="",n=unescape(encodeURIComponent(e)),r=0;r<n.length;r++)t+=n.charCodeAt(r).toString(16)+"";return t},p=function(e,t,n,r){var s;r=r||null;try{s=new XMLHttpRequest}catch(o){}if(s&&"withCredentials"in s)s.open("GET",e,!0);else{if("undefined"==typeof XDomainRequest)return;s=new XDomainRequest,s.open("GET",e)}if(null!==r&&"[object Array]"===Object.prototype.toString.call(r)&&r.length>0&&"function"==typeof s.setRequestHeader)for(var i=0;i<r.length;i++)s.setRequestHeader(r[i].name,r[i].value);var a=function(e){return function(r){c.isIE()?r=s:null,"load"===e&&(c.isIE()||4===r.readyState)&&t?t(r):n&&n(r)}};s.onload=function(e){a("load")(c.isIE()?e:e.target)},s.onerror=function(e){a("error")(c.isIE()?e:e.target)},s.send()},l={apiProductReviews:{rest:function(e,t,n,r,a){var c;switch(e){case"//api-integr.trustedshops.com/":c=e+"rest/protected/v2/shops/"+t+"/products/skus/"+d(n)+"/reviews.json";break;default:c=e+"shops/"+t+"/products/skus/"+d(n)+"/productreviewstickers/v1/reviews.json"}var l=[];p(c,function(e){var t=[],n=new s;if("{"===e.responseText.substring(0,1)){var a=JSON.parse(e.responseText);if("response"in a&&"code"in a.response&&200===parseInt(a.response.code,10)){if(!a.response.data.hasOwnProperty("product")||!a.response.data.product.hasOwnProperty("reviews"))return r(n);if(n.setName(a.response.data.product.name),a.response.data.product.hasOwnProperty("shop")){var c=a.response.data.product.shop.name;n.setShopName(c)}for(var d=0;d<a.response.data.product.reviews.length;d++){var p=new o(a.response.data.product.reviews[d].comment,a.response.data.product.reviews[d].mark,a.response.data.product.reviews[d].creationDate);p.setProductName(n.getName());var l=null;if(a.response.data.product.reviews[d].statement&&(l=new i(a.response.data.product.reviews[d].statement.creationDate,a.response.data.product.reviews[d].statement.comment)),p.setStatement(l),a.response.data.product.reviews[d].hasOwnProperty("reviewer")){var f=a.response.data.product.reviews[d].reviewer.profile.firstname,m=a.response.data.product.reviews[d].reviewer.profile.lastname,v=a.response.data.product.reviews[d].reviewer.profile.city,h=a.response.data.product.reviews[d].reviewer.profile.avatar60URL,g=a.response.data.product.reviews[d].reviewer.uuid,w=new u(f,m,g,v,h);p.setBuyer(w)}t.push(p)}n.setReviewCount(a.response.data.product.reviews.length),n.setReviews(t)}}r&&r(n)},a,l)},runningRequestsCount:function(){return l.apiProductReviews.runningRequests},incrementRunningRequestsCount:function(){l.apiProductReviews.runningRequests+=1},decrementRunningRequestsCount:function(){l.apiProductReviews.runningRequests>0&&(l.apiProductReviews.runningRequests-=1)},runningRequests:0},apiCdnProductReviewSummaries:{rest:function(e,t,n,r,o){var i;switch(e){case"//api-integr.trustedshops.com/":i=e+"rest/protected/v2/shops/"+t+"/products/skus/"+d(n)+"/quality/reviews.json";break;default:i=e+"shops/"+t+"/products/skus/"+d(n)+"/productstickersummaries/v1/quality/reviews.json"}var u=[];p(i,function(e){if("{"===e.responseText.substring(0,1)){var t=JSON.parse(e.responseText),n=new s;if("response"in t&&"code"in t.response&&200===parseInt(t.response.code,10)){if(void 0===t.response.data.product||void 0===t.response.data.product.qualityIndicators)return r(n);var i=new a(t.response.data.product.qualityIndicators.reviewIndicator.totalReviewCount,t.response.data.product.qualityIndicators.reviewIndicator.overallMark);n.setName(t.response.data.product.name),n.setProductSummary(i)}r&&r(n)}else o&&o()},o,u)},runningRequestsCount:function(){return l.apiCdnProductReviewSummaries.runningRequests},incrementRunningRequestsCount:function(){l.apiCdnProductReviewSummaries.runningRequests+=1},decrementRunningRequestsCount:function(){l.apiCdnProductReviewSummaries.runningRequests>0&&(l.apiCdnProductReviewSummaries.runningRequests-=1)},runningRequests:0}};e.exports=l},function(e,t){"use strict";var n=function(e){var t,n=[],r=0,s=e||"",o="Shopname";this.reviews=[],this.getReviews=function(){return n},this.setReviews=function(e){n=e},this.getName=function(){return s},this.setName=function(e){s=e},this.getReviewCount=function(){return r},this.setReviewCount=function(e){r=e},this.getShopName=function(){return o},this.setShopName=function(e){o=e},this.getProductSummary=function(){return t},this.setProductSummary=function(e){t=e}},r=function(e,t,n){var r,s,o;return{getComment:function(){return e||""},getRating:function(){return t||""},getStars:function(){return parseInt(t)},getPubDate:function(){return n||0},getBuyer:function(){return r},setBuyer:function(e){r=e},getProductName:function(){return s},setProductName:function(e){s=e},getStatement:function(){return o},setStatement:function(e){o=e}}},s=function(e,t){return{getCreationDate:function(){return e},getStatement:function(){return t||""}}},o=function(e,t){this.totalReviewCount=parseInt(e)||0,this.overallMark=parseFloat(t)||0},i=function(e,t,n,r,s){this.avatar=s,this.firstName=e,this.lastName=t,this.city=r,this.uuid=n};e.exports.Product=n,e.exports.ProductReview=r,e.exports.ShopStatement=s,e.exports.ProductSummary=o,e.exports.Buyer=i},function(e,t,n){"use strict";var r=n(8),s=n(9),o=function(e){var t;return t=e.scrollToReviews?r.dom("a",function(){this.className="ts-rating-"+e.theme+" ts-rating "+e.locale,this.setAttribute("href","#trustedshops-productreviews-sticker-wrapper")}):r.dom("div",function(){this.className="ts-rating-"+e.theme+" ts-rating "+e.locale})},i=function(e){return{render:function(t){for(var n=0,i=0,a="",u=o(e),c=0,d=0,p=0;p<t.length;p++)a=t[p].getProductSummary(),a&&a.totalReviewCount>0&&(c+=parseFloat(a.overallMark),i+=a.totalReviewCount,d++);d>0&&(n=(Math.round(c/d*100)/100).toFixed(2)),u.className=u.className+" productreviewsSummary",e.className&&(u.className=u.className+" "+e.className),e.borderColor&&(u.style.borderColor=e.borderColor);var l=!(n<=0||isNaN(n));if(e.enablePlaceholder||l){var f=e.enablePlaceholder&&0===i;u.appendChild(new s(n,"div",e.starSize,e.starColor)),f||(u.appendChild(r.dom("span",function(){this.className="ts-stars-reviewCount",this.innerHTML="("+i+")",this.style.fontSize=e.fontSize})),e.showRating&&u.appendChild(r.dom("div",function(){return this.className="ts-reviewSummary-averageRating",[r.dom("span",function(){this.className="ts-reviewSummary-ratingValue",this.innerHTML=n,this.style.fontSize=e.fontSize}),r.dom("span",function(){this.className="ts-reviewSummary-bestRating",this.innerHTML="/5.00",this.style.fontSize=e.fontSize})]})))}return u}}};e.exports=i},function(e,t,n){"use strict";n(2);e.exports={hasClass:function(e,t){return e.className&&(" "+e.className+" ").indexOf(" "+t+" ")>-1},dom:function(e,t){var n=document.createElement(e.toUpperCase());if(t){var r=t.apply(n);if(r){r instanceof Array||(r=[r]);for(var s=0;s<r.length;s++)n.appendChild(r[s])}}return n}}},function(e,t,n){"use strict";var r=n(8),s=function(e,t,n,s){return r.dom(t,function(){return this.className="ts-stars-wrapper",this.setAttribute("style","width: "+5*parseInt(n)+"px"),this.style.height=parseInt(n)+1+"px",[r.dom("div",function(){this.className="ts-stars-fullBar";var t=e*parseInt(n,10);return this.style.width=t+"px",this.style.height=parseInt(n)+1+"px",[r.dom("i",function(){this.className="icon-star-full",s&&(this.style.color=s),n&&(this.style.fontSize=n)}),r.dom("i",function(){this.className="icon-star-full",s&&(this.style.color=s),n&&(this.style.fontSize=n)}),r.dom("i",function(){this.className="icon-star-full",s&&(this.style.color=s),n&&(this.style.fontSize=n)}),r.dom("i",function(){this.className="icon-star-full",s&&(this.style.color=s),n&&(this.style.fontSize=n)}),r.dom("i",function(){this.className="icon-star-full",s&&(this.style.color=s),n&&(this.style.fontSize=n)})]}),r.dom("div",function(){return this.className="ts-stars-emptyBar",[r.dom("i",function(){this.className="icon-star-empty",n&&(this.style.fontSize=n)}),r.dom("i",function(){this.className="icon-star-empty",n&&(this.style.fontSize=n)}),r.dom("i",function(){this.className="icon-star-empty",n&&(this.style.fontSize=n)}),r.dom("i",function(){this.className="icon-star-empty",n&&(this.style.fontSize=n)}),r.dom("i",function(){this.className="icon-star-empty",n&&(this.style.fontSize=n)})]})]})};e.exports=s}]);