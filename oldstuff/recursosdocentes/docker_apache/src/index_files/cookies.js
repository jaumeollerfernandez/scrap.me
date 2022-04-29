define(['jquery','mage/cookies'],function($){if(!window.mage)var mage={};$.mage.cookies={};$.mage.cookies.expires=null;$.mage.cookies.path='/';$.mage.cookies.domain=null;$.mage.cookies.secure=false;$.mage.cookies.set=function(name,value){var argv=arguments;var argc=arguments.length;var expires=(argc>2)?argv[2]:$.mage.cookies.expires;var path=(argc>3)?argv[3]:$.mage.cookies.path;var domain=(argc>4)?argv[4]:$.mage.cookies.domain;var secure=(argc>5)?argv[5]:$.mage.cookies.secure;document.cookie=name+"="+value+
((expires==null)?"":("; expires="+expires.toGMTString()))+
((path==null)?"":("; path="+path))+
((domain==null)?"":("; domain="+domain))+
((secure==true)?"; secure":"");};$.mage.cookies.get=function(name){var arg=name+"=";var alen=arg.length;var clen=document.cookie.length;var i=0;var j=0;while(i<clen){j=i+alen;if(document.cookie.substring(i,j)==arg)
return $.mage.cookies.getCookieVal(j);i=document.cookie.indexOf(" ",i)+1;if(i==0)
break;}
return null;};$.mage.cookies.clear=function(name){if($.mage.cookies.get(name)){document.cookie=name+"="+"; expires=Thu, 01-Jan-70 00:00:01 GMT";}};$.mage.cookies.getCookieVal=function(offset){var endstr=document.cookie.indexOf(";",offset);if(endstr==-1){endstr=document.cookie.length;}
return unescape(document.cookie.substring(offset,endstr));};});