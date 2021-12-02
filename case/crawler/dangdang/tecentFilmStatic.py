# -*- coding: UTF-8 -*-

import requests
from bs4 import BeautifulSoup

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64;x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
# headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}

headers = {

    'user-agent': user_agent                      #浏览器头文件信息

}


url= 'https://v.qq.com/'


resopnseStr='''
D:\ProgramData\Anaconda3\python.exe D:/program/PycharmProjects/case/crawler/dangdang/tecentFilm.py
<!DOCTYPE html>
<!--[if lte IE 6 ]> <html class="ie ie6 lte_ie7 lte_ie8 lte_ie9 " lang="zh-CN"> <![endif]-->
<!--[if IE 7 ]> <html class="ie ie7 lte_ie7 lte_ie8 lte_ie9 " lang="zh-CN"> <![endif]-->
<!--[if IE 8 ]> <html class="ie ie8 lte_ie8 lte_ie9 " lang="zh-CN"> <![endif]-->
<!--[if IE 9 ]> <html class="ie ie9 lte_ie9 " lang="zh-CN"> <![endif]-->
<!--[if (gt IE 9)|!(IE)]><!-->
<html class="choice" lang="zh-CN">
 <!--<![endif]-->
 <head>
  <meta content="IE=Edge" http-equiv="X-UA-Compatible"/>
  <meta content="webkit" name="renderer"/>
  <meta charset="utf-8"/>
  <meta content="max-age=60" http-equiv="Cache-Control"/>
  <title>
   腾讯视频 - 中国领先的在线视频媒体平台,海量高清视频在线观看
  </title>
  <script type="text/javascript">
   (function(){function c(h,g){g=g||document.location.toString();var e=new RegExp("[?&#]"+h+"=([^&#]+)","i");var i=e.exec(g);if(i&&i.length>1){return i[1]}return""}function f(){var e=c("ptag")||c("PTAG"),g="v.index.adaptor";if(e){e+="#{defaulTag}#1"}else{if(/https?:\/\/(.+?)(\/|$)/.test(document.referrer)){e=RegExp.$1+"#{defaulTag}#2"}else{e="v_qq_com#{defaulTag}#3"}}return encodeURIComponent(e.replace("{defaulTag}",g))}try{if(window!=top&&document.referrer&&document.referrer.indexOf("v.baidu.com")!=-1){top.location.href=self.location.href}}catch(d){}var ua=navigator.userAgent;var istablet=/android/i.test(ua)&&!/mobile/i.test(ua);if(!istablet&&/(android)|(iphone)|(ipod)/i.test(ua)&&(!/mi pad/i.test(ua))&&(typeof document.referrer!="string"||document.referrer.indexOf("m.v.qq.com")==-1)){try{var a="http://m.v.qq.com/index.html?ptag=",b=f();a=a+b+"&";if(document.referrer){a+="mreferrer="+encodeURIComponent(document.referrer)+"&"}location.replace(a)}catch(d){}}})();
  </script>
  <link as="style" href="//vm.gtimg.cn/c/=/tencentvideo/vstyle/web/v6/style/css/base.css,head_channel.css,channel/channel_base.css?v=2021102215" rel="preload"/>
  <link as="style" href="//vm.gtimg.cn/c/=/tencentvideo/vstyle/web/v6/style/css/channel/channel.css?v=2021102215" rel="preload"/>
  <link href="//vm.gtimg.cn/c/=/tencentvideo/vstyle/web/v6/style/css/base.css,head_channel.css,channel/channel_base.css?v=2021102215" rel="stylesheet"/>
  <!--[if lte IE 9 ]>
    <link rel="stylesheet" href="//vm.gtimg.cn/c/=/tencentvideo/vstyle/web/v6/style/css/base.ie.css,head_channel.ie.css,channel/channel_base.ie.css?v=2021102215" />
    <![endif]-->
  <!--[if lte IE 8]><script type="text/javascript">document.createElement('svg');document.createElement('path');document.createElement('use');document.createElement('symbol');document.createElement('circle');document.createElement('defs');document.createElement('polygon');document.createElement('linearGradient')</script><![endif]-->
  <meta content="腾讯视频 - 中国领先的在线视频媒体平台,海量高清视频在线观看" itemprop="name"/>
  <meta content="腾讯视频,电影,电视剧,综艺,新闻,财经,音乐,MV,高清,视频,在线观看,全网搜,搜全网" name="keywords"/>
  <meta content="腾讯视频致力于打造中国领先的在线视频媒体平台，以丰富的内容、极致的观看体验、便捷的登录方式、24小时多平台无缝应用体验以及快捷分享的产品特性，主要满足用户在线观看视频的需求。" itemprop="description" name="description"/>
  <meta content="https://puui.qpic.cn/vupload/0/common_logo_square.png/0" itemprop="image"/>
  <meta content="app-id=407925512" name="apple-itunes-app"/>
  <link href="//v.qq.com/favicon.ico" rel="shortcut icon"/>
  <link href="//v.qq.com/opensearch.xml" rel="search" title="腾讯视频" type="application/opensearchdescription+xml"/>
  <script>
   window.channelName = '精选'
        window.channelInfos= {"channelId":"choice","channelName":"精选","parentName":"","parentEnName":"","darkmode":0,"pageQuery":{},"channelType":""}
        try {
            document.domain = "qq.com";
        } catch (e) {}
        function picerr(obj, num) {
            obj.onerror = null;
            var p = "blank";
            if (num == "h" || num == "v" || num == "s" || num == "f") {
                p = "pic_" + num;
            } else if (num == "a") {
                p = "avatar";
            } else {
                p = 'blank'
            }
            var img = "//puui.qpic.cn/vupload/0/common_" + p + ".png/0";
            obj.src = img;
            obj.srcset && (obj.srcset = img + ' 2x');
        }
        // 检测白屏跳转且防止死循环跳转
        window.emptyPageTimer = setTimeout(function () {
             var loc = window.location
             if(!~loc.pathname.indexOf('/bk/channel/choice.html')) {
                 loc.href = 'https://v.qq.com/bk/channel/choice.html'
             }
        }, 8000)
        try {
            !function(){var e=["lite"],t=["tesla"];function n(e){var t=document.createElement("style"),n=document.head||document.getElementsByTagName("head")[0];t.type="text/css",t.styleSheet?t.styleSheet.cssText=e:t.appendChild(document.createTextNode(e)),n.appendChild(t)}function o(e,t,n){var o="";if(n>0){var i=new Date;i.setTime(i.getTime()+24*n*60*60*1e3),o="; expires="+i.toUTCString()}else o=";expires=Thu, 01 Jan 1970 00:00:01 GMT";document.cookie=e+"="+(t||"")+o+"; path=/"}function i(e){for(var t=e+"=",n=document.cookie.split(";"),o=0;o<n.length;o++){for(var i=n[o];" "==i.charAt(0);)i=i.substring(1,i.length);if(0==i.indexOf(t))return i.substring(t.length,i.length)}return null}function a(e){for(var t={},n=("?"===e[0]?e.substr(1):e).split("&"),o=0;o<n.length;o++){var i=n[o].split("=");t[decodeURIComponent(i[0])]=decodeURIComponent(i[1]||"")}return t}!function(){var r=a(location&&location.search||""),c=navigator.userAgent.toLocaleLowerCase(),d=r.mode,l=i("__mode");try{t.some(function(e){return c.match(e)})}catch(e){}(d&&~e.indexOf(d)||l&&~e.indexOf(l))&&(n(".__client_download__,.__lite_hide__{display:none !important}"),function(){var e=a(location&&location.search||""),t=e&&e.scale||"";t?o("__scale",t,30):t=i("__scale");var r=(document.body&&document.body||document.getElementsByTagName("body")).clientWidth||1e3;if((t=+t)&&"number"==typeof t&&!isNaN(t)){var c="html,body{overflow-x: hidden;}body{transform: scale("+t+");transform-origin: center top;}";r<1280&&(c+="body{min-width: 990px;}",c+=".site_head .head_inner{position: relative;}"),n(c)}}()),window.channelInfos&&"choice"===window.channelInfos.channelId&&(d&&~e.indexOf(d)?o("__mode",d,30):o("__mode","",-1))}()}();
        } catch (e) {}

        function getQueryVariable(variable)
        {
            var query = window.location.search.substring(1);
            var vars = query.split("&");
            for (var i=0;i<vars.length;i++) {
                    var pair = vars[i].split("=");
                    if(pair[0] == variable){return pair[1];}
            }
            return(false);
        }
        
        if(getQueryVariable('open_type') === 'client'){
            document.documentElement.classList.add('lol_no_header')
        }

        if(getQueryVariable('desk_type') === 'mac'){
            document.documentElement.classList.add('lol_mac_desk')
        }
        
        if((location.pathname === '/channel/nba' || location.pathname === '/channel/lols11')  && getQueryVariable('plat') === 'mac'){
            document.documentElement.classList.add('__darkmode__')
            document.documentElement.classList.add('mac')
        }

        if((location.pathname === '/channel/nba' || location.pathname === '/channel/lols11')  && getQueryVariable('plat') === 'win'){
            document.documentElement.classList.add('__darkmode__')
            document.documentElement.classList.add('win')
        }
  </script>
  <link as="script" href="//vm.gtimg.cn/tencentvideo_v1/script/txv.core.js?v=20211119" rel="preload"/>
  <link as="script" href="//ra.gtimg.com/sc/vqq/crystal-min.js" rel="preload"/>
  <link as="script" href="//vm.gtimg.cn/c/=/tencentvideo/script/index2017/public_comps/shortcut.min.js,/tencentvideo/script/module/floatpanel.js" rel="preload"/>
 </head>
 <body _wind="scene=频道页&amp;pagename=精选频道" class="page_channel page_channel_choice">
  <svg class="svg_sprite" height="1" version="1.1" width="1" xmlns="http://www.w3.org/2000/svg">
   <lineargradient gradienttransform="matrix(10 0 0 -10 1275 285)" gradientunits="userSpaceOnUse" id="__lg_collect" x1="-126.4" x2="-126.4" y1="27.9" y2="26.9">
    <stop offset="0" stop-color="#fc5131">
    </stop>
    <stop offset="1" stop-color="#ff147c">
    </stop>
   </lineargradient>
   <symbol id="svg_icon_collect" viewbox="0 0 16 16">
    <path d="M3.7 10C2.3 8.7 1 7 1 5.1 1 .3 6.3-.1 8 3c1.6-3 7-2.7 7 2.1" fill="none" stroke="#ff5c38" stroke-linecap="round" stroke-linejoin="round" stroke-width="2">
    </path>
    <circle cx="11" cy="11" fill="url(#__lg_collect)" r="5">
    </circle>
    <path class="st2" d="M10 8h2v6h-2V8z" fill="#fff">
    </path>
    <path class="st2" d="M14 10v2H8v-2h6z" fill="#fff">
    </path>
   </symbol>
   <symbol id="svg_icon_collected" viewbox="0 0 16 16">
    <path d="M14.9 5.2c-3.2-2.1-7.6-1.2-9.7 2-.6.8-.9 1.7-1.1 2.6l-.4.2C2.3 8.7 1 7 1 5.1 1 .3 6.3-.1 8 3c1.6-3 7-2.7 7 2.1l-.1.1z" fill="#ff1b40" stroke="#ff1b40" stroke-linecap="round" stroke-linejoin="round" stroke-width="2">
    </path>
    <circle cx="11" cy="11" fill="url(#__lg_collect)" r="5">
    </circle>
    <path d="M9 11l1.5 1.5 3-2.5" fill="none" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="2">
    </path>
   </symbol>
   <symbol id="svg_icon_collect_pure" viewbox="0 0 16 16">
    <path d="M3.739 10C2.276 8.685 1 7 1 5.121 1 .29 6.277-.115 7.995 2.975 9.583-.045 15 .246 15 5.095" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2">
    </path>
    <path d="M11 16a5 5 0 1 1 0-10 5 5 0 0 1 0 10zm1-6V8h-2v2H8v2h2v2h2v-2h2v-2h-2z" fill="currentColor" fill-rule="nonzero">
    </path>
   </symbol>
   <symbol id="svg_icon_collected_pure" viewbox="0 0 16 16">
    <path d="M3.739 10C2.276 8.685 1 7 1 5.121 1 .29 6.277-.115 7.995 2.975 9.583-.045 15 .246 15 5.095" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2">
    </path>
    <path d="M11 16a5 5 0 1 1 0-10 5 5 0 0 1 0 10zm1.414-5l1.414-1.414-1.414-1.414L11 9.586 9.586 8.172 8.172 9.586 9.586 11l-1.414 1.414 1.414 1.414L11 12.414l1.414 1.414 1.414-1.414L12.414 11z" fill="currentColor" fill-rule="nonzero">
    </path>
   </symbol>
   <symbol id="svg_icon_collected_cancel_pure" viewbox="0 0 16 16">
    <path d="M3.739 10C2.276 8.685 1 7 1 5.121 1 .29 6.277-.115 7.995 2.975 9.583-.045 15 .246 15 5.095" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2">
    </path>
    <path d="M11 16a5 5 0 1 1 0-10 5 5 0 0 1 0 10zm1.414-5l1.414-1.414-1.414-1.414L11 9.586 9.586 8.172 8.172 9.586 9.586 11l-1.414 1.414 1.414 1.414L11 12.414l1.414 1.414 1.414-1.414L12.414 11z" fill="currentColor" fill-rule="nonzero">
    </path>
   </symbol>
   <symbol id="svg_icon_follow" viewbox="0 0 20 20">
    <path d="M19.2 7l-5.6-1.1L11 1.1c-.2-.3-.5-.6-.9-.6s-.7.2-.9.6L6.4 5.9.7 7c-.4.2-.7.6-.7 1 0 .3.1.6.4.8l3.7 4-.6 5.5v.1c0 .6.5 1 1 1 .2 0 .3 0 .5-.1l5.1-2.2 5.1 2.3c.1.1.3.1.4.1.6 0 1-.5 1-1v-.2l-.5-4c0-.6-.5-1.1-1.1-1.1s-1 .4-1 1l.2 2.5-4.2-1.9-4.3 1.9.6-4.7-3.1-3.3 4.6-.9L10 3.7l2.2 4.1 4.6.9-1.5 1.6-.1.1c-.2.2-.3.5-.3.8 0 .6.5 1.1 1.1 1.1.3 0 .5-.1.7-.3l2.9-3.2c.3-.2.4-.5.4-.8 0-.5-.4-.9-.8-1z">
    </path>
   </symbol>
   <symbol id="svg_icon_followed" viewbox="0 0 20 20">
    <path d="M15 8.5c1.4 0 2.7.5 3.7 1.3l.9-1c.2-.1.3-.4.3-.6.1-.5-.2-1.1-.8-1.2l-5.5-1.1L11 1.1c-.1-.2-.3-.3-.4-.4-.6-.3-1.3-.1-1.5.4L6.4 5.9.8 7c-.3.1-.4.2-.6.4-.4.4-.3 1.1.1 1.4l3.7 4-.6 5.5v.1c0 .2 0 .3.1.5.3.5.9.7 1.4.4l4.7-2.1c-.3-.7-.6-1.7-.6-2.7 0-3.3 2.7-6 6-6zm-.1.8c-2.8 0-5 2.2-5 5s2.2 5 5 5 5-2.2 5-5-2.3-5-5-5zM18 14l-3.2 3.2c-.2.2-.4.3-.7.3-.2 0-.5-.1-.6-.3L12.1 16c-.3-.3-.3-.9 0-1.2.3-.3.9-.3 1.2 0l.7.7 2.7-2.7c.3-.3.9-.3 1.2 0 .4.3.4.8.1 1.2z">
    </path>
   </symbol>
  </svg>
  <div class="site_head_placeholder">
  </div>
  <div class="site_head dd site_head_absolute" id="new_vs_header">
   <div class="head_inner">
    <h1 class="site_logo">
     <a _stat="顶部导航区:主导航_LOGO" class="link_logo" href="https://v.qq.com/">
      腾讯视频
     </a>
    </h1>
    <div class="site_channel">
     <a _stat="顶部导航区:主导航:精选" class="channel_nav channel_nav_0 _channel_nav_精选 current" data-icon="" data-key="精选" href="//v.qq.com/channel/choice">
      精选
     </a>
     <a _stat="顶部导航区:主导航:电视剧" class="channel_nav channel_nav_1 _channel_nav_电视剧" data-icon="//puui.qpic.cn/vupload/0/20181206_1544081196478_lrgd9cazlhs.png/0" data-key="电视剧" href="//v.qq.com/channel/tv">
      电视剧
     </a>
     <a _stat="顶部导航区:主导航:电影" class="channel_nav channel_nav_2 _channel_nav_电影" data-icon="//puui.qpic.cn/vupload/0/20181206_1544081196504_itmr2xdlmpb.png/0" data-key="电影" href="//v.qq.com/channel/movie">
      电影
     </a>
     <a _stat="顶部导航区:主导航:综艺" class="channel_nav channel_nav_3 _channel_nav_综艺" data-icon="//puui.qpic.cn/vupload/0/20181206_1544081196514_yzvp912kh1p.png/0" data-key="综艺" href="//v.qq.com/channel/variety">
      综艺
     </a>
     <a _stat="顶部导航区:主导航:动漫" class="channel_nav channel_nav_4 _channel_nav_动漫" data-icon="//puui.qpic.cn/vupload/0/20181206_1544081196508_jhfbyyujr58.png/0" data-key="动漫" href="//v.qq.com/channel/cartoon">
      动漫
     </a>
     <a _stat="顶部导航区:主导航:少儿" class="channel_nav channel_nav_5 _channel_nav_少儿" data-icon="//puui.qpic.cn/vupload/0/20181206_1544081196514_po0qlecenmr.png/0" data-key="少儿" href="//v.qq.com/channel/child">
      少儿
     </a>
     <a _stat="顶部导航区:主导航:纪录片" class="channel_nav channel_nav_6 _channel_nav_纪录片" data-icon="//puui.qpic.cn/vupload/0/20181206_1544081196512_zj8b2z4ql2m.png/0" data-key="纪录片" href="//v.qq.com/channel/doco">
      纪录片
     </a>
     <a _stat="顶部导航区:主导航:VIP会员" class="channel_nav channel_nav_7 _channel_nav_VIP会员" data-icon="//img1.gtimg.com/v/pics/hv1/161/167/2257/146804171.png" data-key="VIP会员" href="https://film.qq.com/" target="_blank">
      VIP会员
     </a>
     <a _stat="顶部导航区:主导航:音乐" class="channel_nav channel_nav_8 _channel_nav_音乐" data-icon="" data-key="音乐" href="//v.qq.com/channel/music">
      音乐
     </a>
     <a _stat="顶部导航区:主导航:NBA" class="channel_nav channel_nav_9 _channel_nav_NBA" data-icon="" data-key="NBA" href="https://v.qq.com/channel/nba" target="_blank">
      NBA
     </a>
     <a _stat="顶部导航区:主导航:全部频道" class="channel_more _site_channel_more" href="javascript:void(0);" title="展开更多频道">
      <span class="icon_text">
       全部
      </span>
      <svg class="svg_icon_menu_sm" height="18" viewbox="0 0 18 18" width="18">
       <g class="svg_before">
        <circle cx="5" cy="5" fill="none" r="2.4" stroke="#ffb821" stroke-width="1.2">
        </circle>
        <circle cx="5" cy="13" fill="none" r="2.4" stroke="#fc5131" stroke-width="1.2">
        </circle>
        <circle cx="13" cy="5" fill="none" r="2.4" stroke="#ff1919" stroke-width="1.2">
        </circle>
        <circle cx="13" cy="13" fill="none" r="2.4" stroke="#ff147c" stroke-width="1.2">
        </circle>
       </g>
       <g class="svg_after">
        <path d="M6.6 4.1c-.3-.5-.9-.9-1.5-.9-1.1 0-1.9.8-1.9 1.9 0 .7.3 1.2.9 1.6v.5c0 .3 0 .6.1.9C2.9 7.6 2 6.4 2 5.1 2 3.4 3.4 2 5.1 2c1.3 0 2.5.9 2.9 2.2-.3-.1-.6-.2-.9-.2-.2 0-.3.1-.5.1z" fill="#ffb821">
        </path>
        <path d="M6.6 13.9h.5c.3 0 .6 0 .9-.1-.4 1.3-1.6 2.2-2.9 2.2C3.4 16 2 14.6 2 12.9c0-1.4.9-2.6 2.2-2.9-.1.3-.2.6-.2.9v.5c-.5.3-.9.9-.9 1.6 0 1 .8 1.8 1.8 1.8.8 0 1.4-.4 1.7-.9z" fill="#fc5131">
        </path>
        <path d="M13.9 6.6c.5-.3.9-.9.9-1.6 0-1-.8-1.8-1.8-1.8-.7 0-1.2.3-1.6.9h-.5c-.3 0-.6 0-.9.1.4-1.3 1.6-2.2 2.9-2.2C14.6 2 16 3.4 16 5.1c0 1.4-.9 2.6-2.2 2.9.1-.3.2-.6.2-.9 0-.2-.1-.3-.1-.5z" fill="#ff1919">
        </path>
        <path d="M13.9 11.4v-.5c0-.3 0-.6-.1-.9 1.3.4 2.2 1.6 2.2 2.9 0 1.7-1.4 3.1-3.1 3.1-1.4 0-2.6-.9-2.9-2.2.3.1.6.1.9.1h.5c.3.5.9.9 1.6.9 1 0 1.8-.8 1.8-1.8 0-.7-.4-1.3-.9-1.6z" fill="#ff147c">
        </path>
       </g>
      </svg>
     </a>
    </div>
    <img alt="" class="unusual_pic none" data-cartoon="" data-child="" data-choice="" data-doco="" data-hlw="" data-movie="" data-music="" data-nba="" data-tv="" data-variety="" src="//puui.qpic.cn/vupload/0/common_blank.png/0"/>
    <div class="mod_search">
     <form action="//v.qq.com/x/search/" class="search_form cf" false="" id="searchForm" method="get">
      <label class="search_label" for="keywords">
       搜索关键词
      </label>
      <div class="search_keywords">
       <input _stat="顶部导航区_搜索框" autocomplete="off" class="search_input" id="keywords" name="q" placeholder="" type="text"/>
      </div>
      <input name="stag" type="hidden"/>
      <input name="smartbox_ab" type="hidden"/>
      <button _stat="顶部导航区_搜索按钮" class="search_btn" type="submit">
       <svg class="svg_icon svg_icon_search" height="18" viewbox="0 0 18 18" width="18">
        <path d="M4.5 4.5c-1.9 1.9-1.9 5.1 0 7.1s5.1 1.9 7.1 0 1.9-5.1 0-7.1-5.2-2-7.1 0zm10.8 12.2l-3.1-3.1c-2.7 2-6.6 1.9-9.1-.6C.3 10.2.3 5.8 3 3 5.7.3 10.2.3 12.9 3c2.5 2.5 2.7 6.4.6 9.1l3.1 3.1c.4.4.4 1 0 1.4-.3.5-.9.5-1.3.1z" fill="currentColor">
        </path>
       </svg>
       <span class="btn_inner">
        全网搜
       </span>
      </button>
      <a class="btn_search_hot" href="https://v.qq.com/biu/ranks/?t=hotsearch" target="_blank" title="热搜榜">
       <svg class="svg_icon_fire" height="15" viewbox="0 0 12 15" width="12">
        <lineargradient id="__gradient_fire" x1="41.309%" x2="71.734%" y1="32.314%" y2="100%">
         <stop offset="0%" stop-color="#FF9630">
         </stop>
         <stop offset="0%" stop-color="#FF9630">
         </stop>
         <stop offset="100%" stop-color="#FF1E1E">
         </stop>
        </lineargradient>
        <path d="M6.634 17C2.539 14.21 1.905 10.843 4.73 6.898 6.307 4.845 7.253 4.053 7.253 2c.353.183 5.134 2.569 4.024 7.5 1.01-.505 1.684-1.659 2.025-3.463 2.28 3.767 2.264 6.9-.051 9.4-.489.528-1.211 1.05-1.873 1.563-1.33-.625-2.932-1.875-3.573-5.625C6.524 12.833 6.133 14.708 6.634 17z" fill="url(#__gradient_fire)" transform="translate(-3 -2)">
        </path>
       </svg>
       热搜榜
      </a>
     </form>
     <div class="mod_smartbox none" id="smartbox">
     </div>
    </div>
    <!-- 快捷入口 开始 -->
    <div class="mod_quick cf">
     <div class="quick_item quick_vip">
      <a _stat="顶部导航区:VIP" class="quick_link" href="https://film.qq.com/" target="_blank" title="VIP频道">
       <svg class="svg_quick_icon svg_icon_vip" height="26" viewbox="0 0 26 26" width="26">
        <filter filterunits="objectBoundingBox" height="132%" id="__gradient_vip1" width="134.8%" x="-17.4%" y="-16%">
         <feoffset in="SourceAlpha" result="shadowOffsetOuter1">
         </feoffset>
         <fegaussianblur in="shadowOffsetOuter1" result="shadowBlurOuter1" stddeviation="1">
         </fegaussianblur>
         <fecolormatrix in="shadowBlurOuter1" result="shadowMatrixOuter1" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.08 0">
         </fecolormatrix>
         <femerge>
          <femergenode in="shadowMatrixOuter1">
          </femergenode>
          <femergenode in="SourceGraphic">
          </femergenode>
         </femerge>
        </filter>
        <lineargradient id="__gradient_vip2" x1="-4.4%" x2="58.5%" y1="3.5%" y2="104.9%">
         <stop offset="0%" stop-color="#FFF1CC">
         </stop>
         <stop offset="36.9%" stop-color="#FFCD45">
         </stop>
         <stop offset="100%" stop-color="#FF7000">
         </stop>
        </lineargradient>
        <lineargradient id="__gradient_vip3" x1="20.3%" x2="86.2%" y1="11.1%" y2="88.9%">
         <stop offset="0%" stop-color="#FFF8E6">
         </stop>
         <stop offset="44.5%" stop-color="#FFCD45">
         </stop>
         <stop offset="100%" stop-color="#FF7000">
         </stop>
        </lineargradient>
        <lineargradient id="__gradient_vip4" x1="0%" x2="50%" y1="35.6%" y2="94.2%">
         <stop offset="0%" stop-color="#FFF1CC">
         </stop>
         <stop offset="40.9%" stop-color="#FFCD45">
         </stop>
         <stop offset="100%" stop-color="#FF7000">
         </stop>
        </lineargradient>
        <g fill="none" fill-rule="evenodd" filter="url(#__gradient_vip1)" transform="translate(2 1)">
         <path d="M18.2.1l-6.8 12h-.1L4.5 0h-4C.3.1 0 .5.3.8l10.7 19c.2.4.7.4.9 0L22.6.8c.1-.3 0-.7-.5-.7h-3.9z" fill="url(#__gradient_vip2)" stroke="#FFF" stroke-opacity=".8" stroke-width=".2" transform="translate(0 3.4)">
         </path>
         <path d="M0 0l5.9 10.4L11.8 0z" fill="url(#__gradient_vip3)" opacity=".3" transform="translate(5.5 3.4)">
         </path>
         <path d="M1.7 6.2L6 4.3l4.2 1.9 1.6-2.8v-.6-1.3-1c0-.2-.2-.4-.5-.4H11L6 2.4h-.2L.8.1H.6C.3.1 0 .3 0 .6v2.8l1.6 2.8z" fill="url(#__gradient_vip4)" stroke="#FFF" stroke-opacity=".8" stroke-width=".2" transform="translate(5.5)">
         </path>
        </g>
       </svg>
       <span class="quick_text">
        VIP
       </span>
      </a>
     </div>
     <!-- 历史浮层 -->
     <div class="quick_item quick_history" id="modHistory">
      <a _stat="顶部导航区:观看历史" class="quick_link" href="https://v.qq.com/biu/u/history/" target="_blank">
       <svg class="svg_quick_icon svg_icon_time" height="26" viewbox="0 0 26 26" width="26">
        <circle cx="13" cy="13" fill="none" r="11" stroke="currentColor" stroke-width="2">
        </circle>
        <path d="M14 13h3c.6 0 1 .4 1 1s-.4 1-1 1h-4c-.6 0-1-.4-1-1V8c0-.6.4-1 1-1s1 .4 1 1v5z" fill="currentColor">
        </path>
       </svg>
       <span class="quick_text">
        看过
       </span>
      </a>
      <!-- 历史播放浮层 开始 -->
      <div class="mod_quick_pop mod_pop_history" id="history_pop">
       <div class="quick_pop_tabs" id="quickPopTabs">
        <button class="pop_tab current" data-type="History" id="btnQuickHistory">
         看过
        </button>
        <button class="pop_tab" data-type="Favs" id="btnQuickFavs">
         收藏
        </button>
        <button class="pop_tab" data-type="Subs" id="btnQuickSubs">
         订阅
        </button>
       </div>
       <div _wind="columnname=顶部导航区&amp;controlname=看过浮层" class="mod_quick_videolist mod_quick_videolist_history" id="modQuickHistory">
       </div>
       <div _wind="columnname=顶部导航区&amp;controlname=收藏浮层" class="mod_quick_videolist mod_quick_videolist_favs none" id="modQuickFavs">
       </div>
       <div _wind="columnname=顶部导航区&amp;controlname=关注浮层" class="mod_quick_videolist mod_quick_videolist_subs none" id="modQuickSubs">
       </div>
       <a class="quick_pop_footer quick_pop_footer_disabled" href="#" id="quickHistoryFooterLink">
       </a>
      </div>
      <!-- 历史播放浮层 结束 -->
     </div>
     <!-- 创作中心 -->
     <div class="quick_item quick_upload __lite_hide__">
      <a _stat="顶部导航区:创作中心" class="quick_link" href="https://cc.v.qq.com" target="_blank" title="创作中心">
       <svg class="svg_quick_icon svg_icon_upload" height="26" viewbox="0 0 26 26" width="26">
        <path d="M16.6 4c1.988 0 3.6 1.727 3.6 3.857v.513l2.983-1.916c.568-.365 1.305-.168 1.646.441.112.2.171.429.171.662v10.886c0 .71-.537 1.286-1.2 1.286a1.14 1.14 0 01-.617-.183L20.2 17.629v.514c0 2.13-1.612 3.857-3.6 3.857h-12C2.612 22 1 20.273 1 18.143V7.857C1 5.727 2.612 4 4.6 4h12z" fill="none" stroke="currentColor" stroke-linejoin="round" stroke-width="2">
        </path>
        <path d="M14.036 11.943a1 1 0 01.117 1.993l-.117.007h-5a1 1 0 01-.117-1.994l.117-.006h5z" fill="currentColor" stroke-linejoin="square">
        </path>
        <path d="M11.536 9.443a1 1 0 01.993.883l.007.117v5a1 1 0 01-1.993.116l-.007-.116v-5a1 1 0 011-1z" fill="currentColor" stroke-linejoin="square">
        </path>
       </svg>
       <span class="quick_text">
        创作中心
       </span>
      </a>
     </div>
     <!-- pc客户端 -->
     <div class="quick_item quick_client __lite_hide__" id="pc_client">
      <a _hot="顶部导航区:客户端" _stat="顶部导航区:客户端" class="quick_link" href="https://node.video.qq.com/x/api/download_pc">
       <svg class="svg_quick_icon svg_icon_client" height="26" viewbox="0 0 26 26" width="26">
        <path d="M15 18v2H7c-2.2 0-4-1.8-4-4V7c0-2.2 1.8-4 4-4h12c2.2 0 4 1.8 4 4v6h-2V7c0-1.1-.9-2-2-2H7c-1.1 0-2 .9-2 2v9c0 1.1.9 2 2 2h8zm0 5v2H9v-2h6zM21 23h2v-6c0-.6-.4-1-1-1s-1 .4-1 1v6z" fill="currentColor">
        </path>
        <path d="M19 21l3 2M25 21l-3 2" fill="none" stroke="currentColor" stroke-linecap="square" stroke-width="2">
        </path>
       </svg>
       <span class="quick_text">
        下载客户端
       </span>
       <i class="triangle_up">
        <i class="triangle_inner">
        </i>
       </i>
       <!-- <span class="mark_events" style="display: none;">抢福利</span> -->
      </a>
      <div class="mod_quick_pop mod_pop_client">
       <div class="pop_info_content pop_client_wrap _win">
        <div class="pop_privilege_line">
         <span class="icon_text">
          1080P蓝光画质
         </span>
        </div>
        <div class="pop_privilege_line">
         <span class="icon_text">
          三倍流畅播放
         </span>
        </div>
        <div class="pop_privilege_line">
         <span class="icon_text">
          4K超清体验
         </span>
        </div>
        <div class="pop_privilege_btns">
         <a class="btn_em" href="javascript:;">
          立即体验
         </a>
        </div>
       </div>
       <div class="pop_info_content pop_client_wrap _mac">
        <div class="pop_privilege_line hl">
         <span class="icon_text">
          1080P蓝光画质
         </span>
        </div>
        <div class="pop_privilege_line">
         <span class="icon_text">
          三倍流畅播放
         </span>
        </div>
        <div class="pop_privilege_line">
         <span class="icon_text">
          4K超清体验
         </span>
        </div>
        <div class="pop_privilege_btns">
         <a class="btn_em" href="javascript:;">
          立即体验
         </a>
        </div>
       </div>
      </div>
      <div class="mod_quick_tips none mod_client_bubble">
       <i class="quick_tips_triangle">
       </i>
       <div class="quick_tips_inner">
        <div class="quick_tips_content">
         <!-- <a class="tips_txt tips_txt_vip none tips_txt_0" href="//node.video.qq.com/x/api/download_pc" _hot="nav.download.bubble1" _stat="顶部导航区:pc_client_bubble1">
                        
                        <span class="txt">PC客户端连续签到</span>
                        <span class="txt_bold">7天抢福利</span>
                        <span class="btn_close" _stat="顶部导航区:pc_client_close_bubble1">
                             
                        </span>
                    </a> -->
         <a _hot="nav.download.bubble2" _stat="顶部导航区:pc_client_bubble2" class="tips_txt none tips_txt_1 tips_txt_mac_0" href="//node.video.qq.com/x/api/download_pc">
          <span class="txt">
           PC客户端
          </span>
          <span class="txt_bold">
           免费蓝光播放
          </span>
          <span _stat="顶部导航区:pc_client_close_bubble2" class="btn_close">
          </span>
         </a>
         <a _hot="nav.download.bubble3" _stat="顶部导航区:pc_client_bubble3" class="tips_txt none tips_txt_2 tips_txt_mac_1" href="//node.video.qq.com/x/api/download_pc">
          <span class="txt">
           PC客户端
          </span>
          <span class="txt_bold">
           3倍流畅播放
          </span>
          <span _stat="顶部导航区:pc_client_close_bubble3" class="btn_close">
          </span>
         </a>
         <a _hot="nav.download.bubble4" _stat="顶部导航区:pc_client_bubble4" class="tips_txt none tips_txt_3" href="//node.video.qq.com/x/api/download_pc">
          <span class="txt">
           PC客户端
          </span>
          <span class="txt_bold">
           提前一小时追剧
          </span>
          <span _stat="顶部导航区:pc_client_close_bubble4" class="btn_close">
          </span>
         </a>
         <a _hot="nav.download.bubble5" _stat="顶部导航区:pc_client_bubble5" class="tips_txt none tips_txt_4" href="//node.video.qq.com/x/api/download_pc">
          <span class="txt">
           PC客户端
          </span>
          <span class="txt_bold">
           自动更新下载剧集
          </span>
          <span _stat="顶部导航区:pc_client_close_bubble5" class="btn_close">
          </span>
         </a>
        </div>
       </div>
      </div>
     </div>
     <div class="quick_item quick_user" id="mod_head_user">
      <a _stat="顶部导航区:头像" class="quick_link _checklogin" href="https://v.qq.com/biu/u/history/" id="mod_head_notice_trigger" target="_blank">
       <img class="quick_user_avatar" data-avatarsize="40" data-type="avatar" src="//puui.qpic.cn/vupload/0/common_avatar.png/0"/>
       <span class="account_type" data-type="account_type_logo">
        <i class="icon icon_qq __account_type_qq none">
         <svg class="svg_icon svg_icon_qq" height="8" viewbox="0 0 20 20" width="8">
          <path d="M16.3 13.7c-.3.7-.7 1.3-1.2 1.8 1.1.3.8.9.8.9.5.3.5 2-2.3 2-1.8 0-2.6-.5-2.9-.9H10c-.3 0-.6 0-.9-.1-.3.3-1.1.9-2.9.9-2.7 0-2.7-1.7-2.2-2 0 0-.3-.6 1-.9-.5-.6-.9-1.2-1.2-2-1.1 2-1.7.7-1.6-.9.1-1.4 1.3-2.9 1.6-3.3V9c0-.3.1-.6.4-.9v-.2c0-.3.2-.6.4-.8V7c0-3 2.5-5.5 5.6-5.5S15.7 4 15.7 7v.3c.2.2.3.4.3.6v.2c.2.2.4.5.4.8 0 .2 0 .3-.1.5.3.4 1.5 1.9 1.6 3.3-.1 1.5-.6 2.8-1.6 1z">
          </path>
         </svg>
        </i>
        <i class="icon icon_wechat __account_type_wx none">
         <svg class="svg_icon svg_icon_wechat" height="8" viewbox="0 0 20 20" width="8">
          <path d="M13.4 7.6h.7c-.6-2.7-3.6-4.8-7.1-4.8-3.9 0-7 2.6-7 6 0 1.9 1.1 3.5 2.8 4.7l-.7 2.1 2.5-1.2c.9.2 1.6.4 2.5.4h.7c-.1-.5-.2-1-.2-1.5-.1-3.2 2.5-5.7 5.8-5.7zM9.7 5.7c.5 0 .9.3.9.9 0 .5-.3.9-.9.9-.5 0-1.1-.4-1.1-.9s.5-.9 1.1-.9zm-5 1.8c-.5 0-1.1-.4-1.1-.9s.5-.9 1.1-.9.9.3.9.9c0 .5-.3.9-.9.9zM19.8 13.1c0-2.8-2.8-5.1-6-5.1-3.3 0-6 2.3-6 5.1s2.6 5.1 6 5.1c.7 0 1.4-.2 2.1-.4l1.9 1.1-.5-1.8c1.5-1 2.5-2.4 2.5-4zm-7.9-.9c-.3 0-.7-.3-.7-.7 0-.3.4-.7.7-.7.5 0 .9.4.9.7 0 .4-.3.7-.9.7zm3.9 0c-.3 0-.7-.3-.7-.7 0-.3.4-.7.7-.7.5 0 .9.4.9.7 0 .4-.4.7-.9.7z">
          </path>
         </svg>
        </i>
       </span>
       <img alt="" class="icon_vip_pic none" data-type="viplogo" src="//puui.qpic.cn/vupload/0/common_blank.png/0" width="15"/>
       <i class="triangle_up">
        <i class="triangle_inner">
        </i>
       </i>
      </a>
      <!-- 用户信息浮层 开始 -->
      <div _stat="顶部导航区:头像浮层" class="mod_quick_pop mod_pop_user" id="mod_head_notice_pop">
       <div class="pop_info_content quick_pop_user">
        <div class="quick_pop_user_hd">
         <span class="account_type __accout_type_name">
         </span>
         <a _stat="顶部导航区:头像浮层:昵称" class="user_name _nickname" href="https://v.qq.com/biu/u/history/">
         </a>
         <a _stat="顶部导航区:头像浮层:vipicon" class="link_vip_icon" href="https://film.qq.com/vip/my/">
          <img alt="" class="icon_vip_pic none" data-type="viplogo" src="//puui.qpic.cn/vupload/0/common_blank.png/0" width="24"/>
         </a>
         <a _stat="顶部导航区:头像浮层:切换账号" class="link_change" data-type="switchlogin" href="javascript:;" title="切换账号">
          切换
         </a>
         <a _stat="顶部导航区:头像浮层:退出" class="link_quit" data-type="logout" href="javascript:;" title="退出">
          退出
         </a>
         <div class="quick_vip_meta" data-version="3" id="quick_user_vip">
         </div>
        </div>
        <div class="quick_pop_user_bd">
         <div class="quick_features cf">
          <a _hot="顶部导航区:头像浮层:user_message" _stat="顶部导航区:头像浮层:user_message" class="feature_item" href="//v.qq.com/u/comment/" target="_blank">
           <img class="icon_feature" src="https://vfiles.gtimg.cn/vupload/20200619/2d581a1592554803839.png" srcset="https://vfiles.gtimg.cn/vupload/20200619/03b8481592559225259.png"/>
           <span class="icon_text">
            评论消息
           </span>
          </a>
          <a _hot="顶部导航区:头像浮层:user_history" _stat="顶部导航区:头像浮层:user_history" class="feature_item" href="//v.qq.com/u/history/" target="_blank">
           <img class="icon_feature" src="https://vfiles.gtimg.cn/vupload/20200619/92045c1592554803837.png" srcset="https://vfiles.gtimg.cn/vupload/20200619/36d2ce1592559225258.png"/>
           <span class="icon_text">
            云同步观看记录
           </span>
          </a>
          <a _hot="顶部导航区:头像浮层:user_lottery" _stat="顶部导航区:头像浮层:user_lottery" class="feature_item" href="//cc.v.qq.com/" target="_blank">
           <img class="icon_feature" src="https://vfiles.gtimg.cn/wupload/vqqcom.quick_features/20200730_qwzmcjia368icon.png" srcset="https://vfiles.gtimg.cn/wupload/vqqcom.quick_features/20200730_g6sb4bwm72icon.png"/>
           <span class="icon_text">
            创作中心
           </span>
          </a>
          <a _hot="顶部导航区:头像浮层:download" _stat="顶部导航区:头像浮层:download" class="feature_item" href="//node.video.qq.com/x/api/download_pc" target="_blank">
           <img class="icon_feature" src="https://vfiles.gtimg.cn/vupload/20200619/59554b1592554803837.png" srcset="https://vfiles.gtimg.cn/vupload/20200619/3ac3ad1592559225258.png"/>
           <span class="icon_text">
            用客户端看抢VIP
           </span>
          </a>
         </div>
        </div>
       </div>
      </div>
      <!--未登录会员账号 开始-->
      <div class="mod_quick_pop mod_pop_user none" id="mod_notlogin_pop">
       <div class="pop_info_content quick_pop_user">
        <div class="quick_pop_user_hd">
         <span class="account_type">
          登录之后可以
         </span>
         <div class="quick_vip_meta">
          <span class="vip_now">
           开通VIP/超级影视VIP 看大片
          </span>
          <span class="vip_next">
           <a _stat="顶部导航区:头像浮层:开通vip" class="btn_vip_em __open_vip_notLogin" href="javascript:;">
            开通
           </a>
          </span>
         </div>
        </div>
        <div class="quick_pop_user_bd">
         <div class="quick_features cf">
          <a _hot="顶部导航区:头像浮层:user_message" _stat="顶部导航区:头像浮层:user_message" class="feature_item" href="//v.qq.com/u/comment/" target="_blank">
           <img class="icon_feature" src="https://vfiles.gtimg.cn/vupload/20200619/2d581a1592554803839.png" srcset="https://vfiles.gtimg.cn/vupload/20200619/03b8481592559225259.png"/>
           <span class="icon_text">
            评论消息
           </span>
          </a>
          <a _hot="顶部导航区:头像浮层:user_history" _stat="顶部导航区:头像浮层:user_history" class="feature_item" href="//v.qq.com/u/history/" target="_blank">
           <img class="icon_feature" src="https://vfiles.gtimg.cn/vupload/20200619/92045c1592554803837.png" srcset="https://vfiles.gtimg.cn/vupload/20200619/36d2ce1592559225258.png"/>
           <span class="icon_text">
            云同步观看记录
           </span>
          </a>
          <a _hot="顶部导航区:头像浮层:user_lottery" _stat="顶部导航区:头像浮层:user_lottery" class="feature_item" href="//cc.v.qq.com/" target="_blank">
           <img class="icon_feature" src="https://vfiles.gtimg.cn/wupload/vqqcom.quick_features/20200730_qwzmcjia368icon.png" srcset="https://vfiles.gtimg.cn/wupload/vqqcom.quick_features/20200730_g6sb4bwm72icon.png"/>
           <span class="icon_text">
            创作中心
           </span>
          </a>
          <a _hot="顶部导航区:头像浮层:download" _stat="顶部导航区:头像浮层:download" class="feature_item" href="//node.video.qq.com/x/api/download_pc" target="_blank">
           <img class="icon_feature" src="https://vfiles.gtimg.cn/vupload/20200619/59554b1592554803837.png" srcset="https://vfiles.gtimg.cn/vupload/20200619/3ac3ad1592559225258.png"/>
           <span class="icon_text">
            用客户端看抢VIP
           </span>
          </a>
         </div>
         <div class="quick_pop_btn">
          <a _stat="顶部导航区:头像浮层:立即登录" class="btn_pop_link" data-boss="5" data-type="login" href="javascript:;">
           立即登录
          </a>
         </div>
        </div>
       </div>
      </div>
      <!--未登录会员账号 结束-->
      <!-- 用户信息浮层 结束 -->
     </div>
    </div>
    <!-- 快捷入口 结束 -->
   </div>
   <div class="site_head_nav">
    <div class="site_head_nav_inner">
     <div class="nav_area">
      <img alt="影视推荐" class="nav_label" data-src="//puui.qpic.cn/vupload/0/20181206_mfjob5lc2f/0" src="//puui.qpic.cn/vupload/0/common_blank.png/0"/>
      <div class="nav_content">
       <div class="nav_cell">
        <a _stat="顶部导航区_全部频道浮层_精选" class="nav_link_main" href="//v.qq.com/channel/choice">
         精选
        </a>
       </div>
       <div class="nav_cell">
        <a _stat="顶部导航区_全部频道浮层_电视剧" class="nav_link_main" href="//v.qq.com/channel/tv">
         电视剧
        </a>
       </div>
       <div class="nav_cell">
        <a _stat="顶部导航区_全部频道浮层_电影" class="nav_link_main" href="//v.qq.com/channel/movie">
         电影
        </a>
       </div>
       <div class="nav_cell">
        <a _stat="顶部导航区_全部频道浮层_综艺" class="nav_link_main" href="//v.qq.com/channel/variety">
         综艺
        </a>
       </div>
       <div class="nav_cell">
        <a _stat="顶部导航区_全部频道浮层_动漫" class="nav_link_main" href="//v.qq.com/channel/cartoon">
         动漫
        </a>
       </div>
       <div class="nav_cell">
        <a _stat="顶部导航区_全部频道浮层_少儿" class="nav_link_main" href="//v.qq.com/channel/child">
         少儿
        </a>
       </div>
       <div class="nav_cell">
        <a _stat="顶部导航区_全部频道浮层_纪录片" class="nav_link_main" href="//v.qq.com/channel/doco">
         纪录片
        </a>
       </div>
       <div class="nav_cell">
        <a _stat="顶部导航区_全部频道浮层_VIP会员" class="nav_link_main" href="https://film.qq.com/" target="_blank">
         VIP会员
        </a>
       </div>
      </div>
     </div>
     <div class="nav_area">
      <img alt="乐享生活" class="nav_label" data-src="//puui.qpic.cn/vupload/0/20181206_5deqrhrqvnm/0" src="//puui.qpic.cn/vupload/0/common_blank.png/0"/>
      <div class="nav_content">
       <div class="nav_cell">
        <a _stat="顶部导航区_全部频道浮层_音乐" class="nav_link_main" href="//v.qq.com/channel/music">
         音乐
        </a>
       </div>
       <div class="nav_cell">
        <a _stat="顶部导航区_全部频道浮层_生活" class="nav_link_main" href="//v.qq.com/channel/life">
         生活
        </a>
       </div>
       <div class="nav_cell">
        <a _stat="顶部导航区_全部频道浮层_艺术" class="nav_link_main" href="//v.qq.com/channel/art">
         艺术
        </a>
       </div>
       <div class="nav_cell">
        <a _stat="顶部导航区_全部频道浮层_活动" class="nav_link_main" href="https://cc.v.qq.com/activity" target="_blank">
         活动
        </a>
       </div>
       <div class="nav_cell">
        <a _stat="顶部导航区_全部频道浮层_育儿" class="nav_link_main" href="//v.qq.com/channel/baby">
         育儿
        </a>
       </div>
       <div class="nav_cell">
        <a _stat="顶部导航区_全部频道浮层_旅游" class="nav_link_main" href="//v.qq.com/channel/travel">
         旅游
        </a>
       </div>
       <div class="nav_cell">
        <a _stat="顶部导航区_全部频道浮层_演唱会" class="nav_link_main" href="https://v.qq.com/livemusic/">
         演唱会
        </a>
       </div>
       <div class="nav_cell">
        <a _stat="顶部导航区_全部频道浮层_搞笑" class="nav_link_main" href="//v.qq.com/channel/fun">
         搞笑
        </a>
       </div>
      </div>
     </div>
     <div class="nav_area">
      <img alt="游戏体育" class="nav_label" data-src="//puui.qpic.cn/vupload/0/20181226_1545830743429_ynggg8rc7hd.png/0" src="//puui.qpic.cn/vupload/0/common_blank.png/0"/>
      <div class="nav_content">
       <div class="nav_cell">
        <a _stat="顶部导航区_全部频道浮层_NBA" class="nav_link_main" href="https://v.qq.com/channel/nba" target="_blank">
         NBA
        </a>
       </div>
       <div class="nav_cell">
        <a _stat="顶部导航区_全部频道浮层_体育" class="nav_link_main" href="//v.qq.com/channel/sports_new">
         体育
        </a>
       </div>
       <div class="nav_cell">
        <a _stat="顶部导航区_全部频道浮层_游戏" class="nav_link_main" href="//v.qq.com/channel/games">
         游戏
        </a>
       </div>
       <div class="nav_cell">
        <a _stat="顶部导航区_全部频道浮层_S11" class="nav_link_main" href="https://v.qq.com/channel/lols11" target="_blank">
         S11
        </a>
       </div>
       <div class="nav_cell">
        <a _stat="顶部导航区_全部频道浮层_WWE" class="nav_link_main" href="//v.qq.com/channel/wwe">
         WWE
        </a>
       </div>
       <div class="nav_cell">
        <a _stat="顶部导航区_全部频道浮层_网页游戏" class="nav_link_main" href="https://iwan.qq.com/pcwebsite/game?ADTAG=vzdh" target="_blank">
         网页游戏
        </a>
       </div>
      </div>
     </div>
     <div class="nav_area">
      <img alt="资讯前沿" class="nav_label" data-src="//puui.qpic.cn/vupload/0/20181206_nnf2w1onto/0" src="//puui.qpic.cn/vupload/0/common_blank.png/0"/>
      <div class="nav_content">
       <div class="nav_cell">
        <a _stat="顶部导航区_全部频道浮层_娱乐" class="nav_link_main" href="//v.qq.com/channel/ent">
         娱乐
        </a>
       </div>
       <div class="nav_cell">
        <a _stat="顶部导航区_全部频道浮层_新闻" class="nav_link_main" href="//v.qq.com/channel/news">
         新闻
        </a>
       </div>
       <div class="nav_cell">
        <a _stat="顶部导航区_全部频道浮层_时尚" class="nav_link_main" href="//v.qq.com/channel/fashion">
         时尚
        </a>
       </div>
       <div class="nav_cell">
        <a _stat="顶部导航区_全部频道浮层_科技" class="nav_link_main" href="//v.qq.com/channel/tech">
         科技
        </a>
       </div>
       <div class="nav_cell">
        <a _stat="顶部导航区_全部频道浮层_汽车" class="nav_link_main" href="//v.qq.com/channel/auto">
         汽车
        </a>
       </div>
       <div class="nav_cell">
        <a _stat="顶部导航区_全部频道浮层_房产" class="nav_link_main" href="//v.qq.com/channel/house">
         房产
        </a>
       </div>
       <div class="nav_cell">
        <a _stat="顶部导航区_全部频道浮层_财经" class="nav_link_main" href="//v.qq.com/channel/finance">
         财经
        </a>
       </div>
      </div>
     </div>
     <div class="nav_area">
      <img alt="就好这口" class="nav_label" data-src="//puui.qpic.cn/vupload/0/20181206_wm4s3djxw0i/0" src="//puui.qpic.cn/vupload/0/common_blank.png/0"/>
      <div class="nav_content">
       <div class="nav_cell">
        <a _stat="顶部导航区_全部频道浮层_知识" class="nav_link_main" href="//v.qq.com/channel/knowledge">
         知识
        </a>
       </div>
       <div class="nav_cell">
        <a _stat="顶部导航区_全部频道浮层_教育课堂" class="nav_link_main" href="//v.qq.com/channel/education">
         教育课堂
        </a>
       </div>
       <div class="nav_cell">
        <a _stat="顶部导航区_全部频道浮层_热播榜" class="nav_link_main" href="https://v.qq.com/biu/ranks/?t=hotplay&amp;channel=all&amp;ptag=vheader" target="_blank">
         热播榜
        </a>
       </div>
       <div class="nav_cell">
        <a _stat="顶部导航区_全部频道浮层_热搜榜" class="nav_link_main" href="https://v.qq.com/biu/ranks/?t=hotsearch&amp;ptag=vheader" target="_blank">
         热搜榜
        </a>
       </div>
       <div class="nav_cell">
        <a _stat="顶部导航区_全部频道浮层_直播" class="nav_link_main" href="http://v.qq.com/x/live/">
         直播
        </a>
       </div>
       <div class="nav_cell">
        <a _stat="顶部导航区_全部频道浮层_爱看" class="nav_link_main" href="//v.qq.com/channel/feeds_hotspot">
         爱看
        </a>
       </div>
       <div class="nav_cell">
        <a _stat="顶部导航区_全部频道浮层_星座" class="nav_link_main" href="//v.qq.com/channel/astro">
         星座
        </a>
       </div>
      </div>
     </div>
    </div>
   </div>
  </div>
  <script>
   /*var abTestResult = window.sessionStorage.getItem("abTestResult");

    setTimeout(function() {
        if ($) {
            if (!abTestResult) {
                $.ajax({
                    url: 'https://pbaccess.video.qq.com/trpc.videosearch.search_cgi.http/web_search_abtest',
                    CSRF: true,
                    type: 'GET',
                    xhrFields: {
                        withCredentials: true
                    },
                    success: function (data) {
                        if (data && data.data && data.data.new_service) {
                            abTestResult = '1';
                            window.sessionStorage.setItem('abTestResult', '1');
                        }
                    },
                    error: function (xhr, msg) {
                        abTestResult = -1;
                        window.sessionStorage.setItem('abTestResult', -1);
                    }
                });
            }

            $('#searchForm .search_btn').click(function() {
                var currentUrl = window.location;
                if (currentUrl && currentUrl.href && (currentUrl.href.indexOf('/x/search') >= 0 || currentUrl.href.indexOf('/x/newsearch') >= 0)) {
                    $('#searchForm').attr('target', '_self');
                } else {
                    $('#searchForm').attr('target', '_blank');
                }
                if (abTestResult === '1') {
                    $('#searchForm').attr('action', '//v.qq.com/x/newsearch/');
                } else {
                    $('#searchForm').attr('action', '//v.qq.com/x/search/');
                }
                $('#searchForm').submit();
            });
        }
    }, 1000);*/
  </script>
  <div class="site_board_ads _dkb">
   <div class="site_board_ads_inner dkb_2017">
    <!--QQlive_SP_HP_DKB_div AD begin...."l=QQlive_SP_HP_DKB&log=off"-->
    <div class="l_qq_com" id="QQlive_SP_HP_DKB" style="width:1px;height:1px;">
    </div>
    <!--QQlive_SP_HP_DKB AD end -->
    <!--[if !IE]>|xGv00|78cffffc5fd2076581282be70c2cbffe<![endif]-->
   </div>
  </div>
  <!--QQlive_SP_RM_div AD begin...."l=QQlive_SP_RM&log=off"-->
  <div class="l_qq_com" id="QQlive_SP_RM" style="width:1px;height:1px;display:none;margin:0 auto;">
  </div>
  <!--QQlive_SP_RM AD end -->
  <!--[if !IE]>|xGv00|435ca0f3215d5a24182b945fde421dfc<![endif]-->
  <div _expose="new_vs_focus" class="site_slider site_slider_intrude" data-context="0" data-istyle="35" id="new_vs_focus">
   <div class="slider_inner">
    <a _stat="焦点图:大图" class="slider_item in" href="https://v.qq.com/x/cover/mzc00200mcm0lzz.html" style="background-color: #324b74;background-image: url(//puui.qpic.cn/media_img/lena/PIC8qmq9a_580_1680/0)" target="_blank">
    </a>
    <a _stat="焦点图:大图" class="slider_item out" href="https://v.qq.com/x/cover/mzc00200mcm0lzz.html" style="background-color: #324b74;background-image: url(//puui.qpic.cn/media_img/lena/PIC8qmq9a_580_1680/0)" target="_blank">
    </a>
    <div _wind="columnname=精选_焦点图_追剧&amp;controlname=choice_focus_right" class="slider_item_mine" data-page="1">
     <div class="bg">
     </div>
     <canvas class="bg_slider_canvas" id="bg_slider_canvas_1">
     </canvas>
     <canvas class="bg_slider_canvas" id="bg_slider_canvas_2">
     </canvas>
     <div class="slider_figure_wrap _quicklink">
      <div class="slider_figure_inner">
       <a __wind="" class="slider_figure" href="https://v.qq.com/x/cover/mzc00200lxzhhqz.html" target="_blank">
        <img _stat="焦点图:大家在追:视频封面" alt="" class="figure_pic" onerror="picerr(this,'v')" src="//puui.qpic.cn/vcover_vt_pic/0/mzc00200lxzhhqz1628216915340/350"/>
        <div class="slider_figure_video" data-cid="mzc00200lxzhhqz" id="smallvideo_mzc00200lxzhhqz">
        </div>
        <div class="slider_figure_catpion">
         <div _stat="焦点图:大家在追:视频标题" class="slider_figure_title" title="扫黑风暴">
          扫黑风暴
         </div>
         <div class="slider_figure_desc slider_figure_desc_mzc00200lxzhhqz" data-update="全28集">
          孙红雷张艺兴惩黑除恶
         </div>
         <div class="slider_figure_desc2" title="孙红雷张艺兴惩黑除恶">
          孙红雷张艺兴惩黑除恶
         </div>
         <div _stat="焦点图:大家在追:播放按钮" class="slider_figure_btn slider_figure_btn_mzc00200lxzhhqz">
          立即观看
         </div>
        </div>
       </a>
       <a __wind="" class="slider_figure" href="https://v.qq.com/x/cover/m441e3rjq9kwpsc.html" target="_blank">
        <img _stat="焦点图:大家在追:视频封面" alt="" class="figure_pic" onerror="picerr(this,'v')" src="//puui.qpic.cn/vcover_vt_pic/0/m441e3rjq9kwpsc1635739384893/350"/>
        <div class="slider_figure_video" data-cid="m441e3rjq9kwpsc" id="smallvideo_m441e3rjq9kwpsc">
        </div>
        <div class="slider_figure_catpion">
         <div _stat="焦点图:大家在追:视频标题" class="slider_figure_title" title="斗罗大陆">
          斗罗大陆
         </div>
         <div class="slider_figure_desc slider_figure_desc_m441e3rjq9kwpsc" data-update="更新至184集">
          此生不悔入唐门
         </div>
         <div class="slider_figure_desc2" title="此生不悔入唐门">
          此生不悔入唐门
         </div>
         <div _stat="焦点图:大家在追:播放按钮" class="slider_figure_btn slider_figure_btn_m441e3rjq9kwpsc">
          立即观看
         </div>
        </div>
       </a>
       <a __wind="" class="slider_figure" href="https://v.qq.com/x/cover/mzc00200xh9313v.html" target="_blank">
        <img _stat="焦点图:大家在追:视频封面" alt="" class="figure_pic" onerror="picerr(this,'v')" src="//puui.qpic.cn/vcover_vt_pic/0/mzc00200xh9313v1625146391713/350"/>
        <div class="slider_figure_video" data-cid="mzc00200xh9313v" id="smallvideo_mzc00200xh9313v">
        </div>
        <div class="slider_figure_catpion">
         <div _stat="焦点图:大家在追:视频标题" class="slider_figure_title" title="你是我的荣耀">
          你是我的荣耀
         </div>
         <div class="slider_figure_desc slider_figure_desc_mzc00200xh9313v" data-update="全32集">
          杨洋迪丽热巴共谱浪漫爱情
         </div>
         <div class="slider_figure_desc2" title="杨洋迪丽热巴共谱浪漫爱情">
          杨洋迪丽热巴共谱浪漫爱情
         </div>
         <div _stat="焦点图:大家在追:播放按钮" class="slider_figure_btn slider_figure_btn_mzc00200xh9313v">
          立即观看
         </div>
        </div>
       </a>
       <a __wind="" class="slider_figure" href="https://v.qq.com/x/cover/mzc00200dwnknik.html" target="_blank">
        <img _stat="焦点图:大家在追:视频封面" alt="" class="figure_pic" onerror="picerr(this,'v')" src="//puui.qpic.cn/vcover_vt_pic/0/mzc00200dwnknik1625711204754/350"/>
        <div class="slider_figure_video" data-cid="mzc00200dwnknik" id="smallvideo_mzc00200dwnknik">
        </div>
        <div class="slider_figure_catpion">
         <div _stat="焦点图:大家在追:视频标题" class="slider_figure_title" title="开心锤锤">
          开心锤锤
         </div>
         <div class="slider_figure_desc slider_figure_desc_mzc00200dwnknik">
          普通锤锤的爆笑日常
         </div>
         <div class="slider_figure_desc2" title="普通锤锤的爆笑日常">
          普通锤锤的爆笑日常
         </div>
         <div _stat="焦点图:大家在追:播放按钮" class="slider_figure_btn slider_figure_btn_mzc00200dwnknik">
          立即观看
         </div>
        </div>
       </a>
       <a __wind="" class="slider_figure" href="https://v.qq.com/x/cover/p9txi710x7yl924.html" target="_blank">
        <img _stat="焦点图:大家在追:视频封面" alt="" class="figure_pic" onerror="picerr(this,'v')" src="//puui.qpic.cn/vcover_vt_pic/0/p9txi710x7yl9241505126773/350"/>
        <div class="slider_figure_video" data-cid="p9txi710x7yl924" id="smallvideo_p9txi710x7yl924">
        </div>
        <div class="slider_figure_catpion">
         <div _stat="焦点图:大家在追:视频标题" class="slider_figure_title" title="天使之路">
          天使之路
         </div>
         <div class="slider_figure_desc slider_figure_desc_p9txi710x7yl924">
          天使之路
         </div>
         <div class="slider_figure_desc2" title="天使之路">
          天使之路
         </div>
         <div _stat="焦点图:大家在追:播放按钮" class="slider_figure_btn slider_figure_btn_p9txi710x7yl924">
          立即观看
         </div>
        </div>
       </a>
       <a __wind="" class="slider_figure" href="https://v.qq.com/x/cover/zetvrs2mhhx5njt.html" target="_blank">
        <img _stat="焦点图:大家在追:视频封面" alt="" class="figure_pic" onerror="picerr(this,'v')" src="//puui.qpic.cn/vcover_vt_pic/0/zetvrs2mhhx5njt1536576016/350"/>
        <div class="slider_figure_video" data-cid="zetvrs2mhhx5njt" id="smallvideo_zetvrs2mhhx5njt">
        </div>
        <div class="slider_figure_catpion">
         <div _stat="焦点图:大家在追:视频标题" class="slider_figure_title" title="潮音战纪">
          潮音战纪
         </div>
         <div class="slider_figure_desc slider_figure_desc_zetvrs2mhhx5njt">
          燃炸舞台！不嗨算我输
         </div>
         <div class="slider_figure_desc2" title="燃炸舞台！不嗨算我输">
          燃炸舞台！不嗨算我输
         </div>
         <div _stat="焦点图:大家在追:播放按钮" class="slider_figure_btn slider_figure_btn_zetvrs2mhhx5njt">
          立即观看
         </div>
        </div>
       </a>
       <a __wind="" class="slider_figure" href="https://v.qq.com/x/cover/oe6b9noeu4p7713.html" target="_blank">
        <img _stat="焦点图:大家在追:视频封面" alt="" class="figure_pic" onerror="picerr(this,'v')" src="//puui.qpic.cn/vcover_vt_pic/0/oe6b9noeu4p7713t1444941652.jpg/350"/>
        <div class="slider_figure_video" data-cid="oe6b9noeu4p7713" id="smallvideo_oe6b9noeu4p7713">
        </div>
        <div class="slider_figure_catpion">
         <div _stat="焦点图:大家在追:视频标题" class="slider_figure_title" title="大牌驾到">
          大牌驾到
         </div>
         <div class="slider_figure_desc slider_figure_desc_oe6b9noeu4p7713">
          现场特别版：陈晓苦追赵丽颖 于正力挺陈晓演杨过
         </div>
         <div class="slider_figure_desc2" title="现场特别版：陈晓苦追赵丽颖 于正力挺陈晓演杨过">
          现场特别版：陈晓苦追赵丽颖 于正力挺陈晓演杨过
         </div>
         <div _stat="焦点图:大家在追:播放按钮" class="slider_figure_btn slider_figure_btn_oe6b9noeu4p7713">
          立即观看
         </div>
        </div>
       </a>
       <a __wind="" class="slider_figure" href="https://v.qq.com/x/cover/mzc00200bvdf163.html" target="_blank">
        <img _stat="焦点图:大家在追:视频封面" alt="" class="figure_pic" onerror="picerr(this,'v')" src="//puui.qpic.cn/vcover_vt_pic/0/mzc00200bvdf1631569330214/350"/>
        <div class="slider_figure_video" data-cid="mzc00200bvdf163" id="smallvideo_mzc00200bvdf163">
        </div>
        <div class="slider_figure_catpion">
         <div _stat="焦点图:大家在追:视频标题" class="slider_figure_title" title="亲爱的客栈 第3季">
          亲爱的客栈 第3季
         </div>
         <div class="slider_figure_desc slider_figure_desc_mzc00200bvdf163">
          林心如张翰马天宇加盟
         </div>
         <div class="slider_figure_desc2" title="林心如张翰马天宇加盟">
          林心如张翰马天宇加盟
         </div>
         <div _stat="焦点图:大家在追:播放按钮" class="slider_figure_btn slider_figure_btn_mzc00200bvdf163">
          立即观看
         </div>
        </div>
       </a>
       <a __wind="" class="slider_figure" href="https://v.qq.com/x/cover/v4rhq09kpjuv7ks.html" target="_blank">
        <img _stat="焦点图:大家在追:视频封面" alt="" class="figure_pic" lz_next="//puui.qpic.cn/vcover_vt_pic/0/v4rhq09kpjuv7ks1554344628/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
        <div class="slider_figure_video" data-cid="v4rhq09kpjuv7ks" id="smallvideo_v4rhq09kpjuv7ks">
        </div>
        <div class="slider_figure_catpion">
         <div _stat="焦点图:大家在追:视频标题" class="slider_figure_title" title="床垫里的百万欧元">
          床垫里的百万欧元
         </div>
         <div class="slider_figure_desc slider_figure_desc_v4rhq09kpjuv7ks">
          一家人找床垫
         </div>
         <div class="slider_figure_desc2" title="一家人找床垫">
          一家人找床垫
         </div>
         <div _stat="焦点图:大家在追:播放按钮" class="slider_figure_btn slider_figure_btn_v4rhq09kpjuv7ks">
          立即观看
         </div>
        </div>
       </a>
       <a __wind="" class="slider_figure" href="https://v.qq.com/x/cover/tj93ryfojz2rcm4.html" target="_blank">
        <img _stat="焦点图:大家在追:视频封面" alt="" class="figure_pic" lz_next="//puui.qpic.cn/vcover_vt_pic/0/tj93ryfojz2rcm4t1458550857.jpg/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
        <div class="slider_figure_video" data-cid="tj93ryfojz2rcm4" id="smallvideo_tj93ryfojz2rcm4">
        </div>
        <div class="slider_figure_catpion">
         <div _stat="焦点图:大家在追:视频标题" class="slider_figure_title" title="综艺最爆点">
          综艺最爆点
         </div>
         <div class="slider_figure_desc slider_figure_desc_tj93ryfojz2rcm4">
          小萝莉激情献唱《万物生
         </div>
         <div class="slider_figure_desc2" title="小萝莉激情献唱《万物生">
          小萝莉激情献唱《万物生
         </div>
         <div _stat="焦点图:大家在追:播放按钮" class="slider_figure_btn slider_figure_btn_tj93ryfojz2rcm4">
          立即观看
         </div>
        </div>
       </a>
       <a __wind="" class="slider_figure" href="https://v.qq.com/x/cover/qunlf5aipuwzqq1.html" target="_blank">
        <img _stat="焦点图:大家在追:视频封面" alt="" class="figure_pic" lz_next="//puui.qpic.cn/vcover_vt_pic/0/qunlf5aipuwzqq11522825870/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
        <div class="slider_figure_video" data-cid="qunlf5aipuwzqq1" id="smallvideo_qunlf5aipuwzqq1">
        </div>
        <div class="slider_figure_catpion">
         <div _stat="焦点图:大家在追:视频标题" class="slider_figure_title" title="创造101陈芳语个人专辑">
          创造101陈芳语个人专辑
         </div>
         <div class="slider_figure_desc slider_figure_desc_qunlf5aipuwzqq1">
          陈芳语邀请创始人多关照
         </div>
         <div class="slider_figure_desc2" title="陈芳语邀请创始人多关照">
          陈芳语邀请创始人多关照
         </div>
         <div _stat="焦点图:大家在追:播放按钮" class="slider_figure_btn slider_figure_btn_qunlf5aipuwzqq1">
          立即观看
         </div>
        </div>
       </a>
       <a __wind="" class="slider_figure" href="https://v.qq.com/x/cover/y25epedasv3z6lq.html" target="_blank">
        <img _stat="焦点图:大家在追:视频封面" alt="" class="figure_pic" lz_next="//puui.qpic.cn/vcover_vt_pic/0/y25epedasv3z6lqt1448719228.jpg/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
        <div class="slider_figure_video" data-cid="y25epedasv3z6lq" id="smallvideo_y25epedasv3z6lq">
        </div>
        <div class="slider_figure_catpion">
         <div _stat="焦点图:大家在追:视频标题" class="slider_figure_title" title="燃烧吧少年伍嘉成">
          燃烧吧少年伍嘉成
         </div>
         <div class="slider_figure_desc slider_figure_desc_y25epedasv3z6lq">
          他就是阳光男孩！
         </div>
         <div class="slider_figure_desc2" title="他就是阳光男孩！">
          他就是阳光男孩！
         </div>
         <div _stat="焦点图:大家在追:播放按钮" class="slider_figure_btn slider_figure_btn_y25epedasv3z6lq">
          立即观看
         </div>
        </div>
       </a>
       <a __wind="" class="slider_figure" href="https://v.qq.com/x/cover/1terhu9ncm1v4nu.html" target="_blank">
        <img _stat="焦点图:大家在追:视频封面" alt="" class="figure_pic" lz_next="//puui.qpic.cn/vcover_vt_pic/0/1terhu9ncm1v4nu1520323933/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
        <div class="slider_figure_video" data-cid="1terhu9ncm1v4nu" id="smallvideo_1terhu9ncm1v4nu">
        </div>
        <div class="slider_figure_catpion">
         <div _stat="焦点图:大家在追:视频标题" class="slider_figure_title" title="最强大脑粉丝悠享版">
          最强大脑粉丝悠享版
         </div>
         <div class="slider_figure_desc slider_figure_desc_1terhu9ncm1v4nu">
          水哥点赞95后学霸美女
         </div>
         <div class="slider_figure_desc2" title="水哥点赞95后学霸美女">
          水哥点赞95后学霸美女
         </div>
         <div _stat="焦点图:大家在追:播放按钮" class="slider_figure_btn slider_figure_btn_1terhu9ncm1v4nu">
          立即观看
         </div>
        </div>
       </a>
       <a __wind="" class="slider_figure" href="https://v.qq.com/x/cover/bzfkv5se8qaqel2.html" target="_blank">
        <img _stat="焦点图:大家在追:视频封面" alt="" class="figure_pic" lz_next="//puui.qpic.cn/vcover_vt_pic/0/bzfkv5se8qaqel2t1466571646.jpg/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
        <div class="slider_figure_video" data-cid="bzfkv5se8qaqel2" id="smallvideo_bzfkv5se8qaqel2">
        </div>
        <div class="slider_figure_catpion">
         <div _stat="焦点图:大家在追:视频标题" class="slider_figure_title" title="小猪佩奇全集">
          小猪佩奇全集
         </div>
         <div class="slider_figure_desc slider_figure_desc_bzfkv5se8qaqel2" data-update="全305集">
          萌萌小猪佩奇
         </div>
         <div class="slider_figure_desc2" title="萌萌小猪佩奇">
          萌萌小猪佩奇
         </div>
         <div _stat="焦点图:大家在追:播放按钮" class="slider_figure_btn slider_figure_btn_bzfkv5se8qaqel2">
          立即观看
         </div>
        </div>
       </a>
       <a __wind="" class="slider_figure" href="https://v.qq.com/x/cover/ikltnnoqvnot7qc.html" target="_blank">
        <img _stat="焦点图:大家在追:视频封面" alt="" class="figure_pic" lz_next="//puui.qpic.cn/vcover_vt_pic/0/ikltnnoqvnot7qct1453442446.jpg/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
        <div class="slider_figure_video" data-cid="ikltnnoqvnot7qc" id="smallvideo_ikltnnoqvnot7qc">
        </div>
        <div class="slider_figure_catpion">
         <div _stat="焦点图:大家在追:视频标题" class="slider_figure_title" title="综艺大爆炸">
          综艺大爆炸
         </div>
         <div class="slider_figure_desc slider_figure_desc_ikltnnoqvnot7qc">
          高亮！CP粉快来吃糖
         </div>
         <div class="slider_figure_desc2" title="高亮！CP粉快来吃糖">
          高亮！CP粉快来吃糖
         </div>
         <div _stat="焦点图:大家在追:播放按钮" class="slider_figure_btn slider_figure_btn_ikltnnoqvnot7qc">
          立即观看
         </div>
        </div>
       </a>
       <a __wind="" class="slider_figure" href="https://v.qq.com/x/cover/xjskgdpy4lr7o5z.html" target="_blank">
        <img _stat="焦点图:大家在追:视频封面" alt="" class="figure_pic" lz_next="//puui.qpic.cn/vcover_vt_pic/0/xjskgdpy4lr7o5z1560688178/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
        <div class="slider_figure_video" data-cid="xjskgdpy4lr7o5z" id="smallvideo_xjskgdpy4lr7o5z">
        </div>
        <div class="slider_figure_catpion">
         <div _stat="焦点图:大家在追:视频标题" class="slider_figure_title" title="马天宇个人特辑">
          马天宇个人特辑
         </div>
         <div class="slider_figure_desc slider_figure_desc_xjskgdpy4lr7o5z">
          马天宇个人特辑
         </div>
         <div class="slider_figure_desc2" title="马天宇个人特辑">
          马天宇个人特辑
         </div>
         <div _stat="焦点图:大家在追:播放按钮" class="slider_figure_btn slider_figure_btn_xjskgdpy4lr7o5z">
          立即观看
         </div>
        </div>
       </a>
       <a __wind="" class="slider_figure" href="https://v.qq.com/x/cover/mzc00200xrvb4dk.html" target="_blank">
        <img _stat="焦点图:大家在追:视频封面" alt="" class="figure_pic" lz_next="//puui.qpic.cn/vcover_vt_pic/0/mzc00200xrvb4dk1583736334730/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
        <div class="slider_figure_video" data-cid="mzc00200xrvb4dk" id="smallvideo_mzc00200xrvb4dk">
        </div>
        <div class="slider_figure_catpion">
         <div _stat="焦点图:大家在追:视频标题" class="slider_figure_title" title="每日综艺必看">
          每日综艺必看
         </div>
         <div class="slider_figure_desc slider_figure_desc_mzc00200xrvb4dk">
          沈腾现场笑到合不拢嘴
         </div>
         <div class="slider_figure_desc2" title="沈腾现场笑到合不拢嘴">
          沈腾现场笑到合不拢嘴
         </div>
         <div _stat="焦点图:大家在追:播放按钮" class="slider_figure_btn slider_figure_btn_mzc00200xrvb4dk">
          立即观看
         </div>
        </div>
       </a>
       <a __wind="" class="slider_figure" href="https://v.qq.com/x/cover/drr9tfx2g6x4qzp.html" target="_blank">
        <img _stat="焦点图:大家在追:视频封面" alt="" class="figure_pic" lz_next="//puui.qpic.cn/vcover_vt_pic/0/drr9tfx2g6x4qzp1550215529/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
        <div class="slider_figure_video" data-cid="drr9tfx2g6x4qzp" id="smallvideo_drr9tfx2g6x4qzp">
        </div>
        <div class="slider_figure_catpion">
         <div _stat="焦点图:大家在追:视频标题" class="slider_figure_title" title="中国新相亲 第2季">
          中国新相亲 第2季
         </div>
         <div class="slider_figure_desc slider_figure_desc_drr9tfx2g6x4qzp">
          房哥炫富被张国立呛
         </div>
         <div class="slider_figure_desc2" title="房哥炫富被张国立呛">
          房哥炫富被张国立呛
         </div>
         <div _stat="焦点图:大家在追:播放按钮" class="slider_figure_btn slider_figure_btn_drr9tfx2g6x4qzp">
          立即观看
         </div>
        </div>
       </a>
       <a __wind="" class="slider_figure" href="https://v.qq.com/x/cover/quev1kiynwznrbp.html" target="_blank">
        <img _stat="焦点图:大家在追:视频封面" alt="" class="figure_pic" lz_next="//puui.qpic.cn/vcover_vt_pic/0/quev1kiynwznrbpt1456138826.jpg/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
        <div class="slider_figure_video" data-cid="quev1kiynwznrbp" id="smallvideo_quev1kiynwznrbp">
        </div>
        <div class="slider_figure_catpion">
         <div _stat="焦点图:大家在追:视频标题" class="slider_figure_title" title="江苏卫视元宵晚会">
          江苏卫视元宵晚会
         </div>
         <div class="slider_figure_desc slider_figure_desc_quev1kiynwznrbp">
          王宁柳岩上演《新上海滩》“之恋”
         </div>
         <div class="slider_figure_desc2" title="王宁柳岩上演《新上海滩》“之恋”">
          王宁柳岩上演《新上海滩》“之恋”
         </div>
         <div _stat="焦点图:大家在追:播放按钮" class="slider_figure_btn slider_figure_btn_quev1kiynwznrbp">
          立即观看
         </div>
        </div>
       </a>
       <a __wind="" class="slider_figure" href="https://v.qq.com/x/cover/xtzq09wxoyfp7rm.html" target="_blank">
        <img _stat="焦点图:大家在追:视频封面" alt="" class="figure_pic" lz_next="//puui.qpic.cn/vcover_vt_pic/0/xtzq09wxoyfp7rmt1456164011.jpg/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
        <div class="slider_figure_video" data-cid="xtzq09wxoyfp7rm" id="smallvideo_xtzq09wxoyfp7rm">
        </div>
        <div class="slider_figure_catpion">
         <div _stat="焦点图:大家在追:视频标题" class="slider_figure_title" title="2016辽宁卫视元宵晚会">
          2016辽宁卫视元宵晚会
         </div>
         <div class="slider_figure_desc slider_figure_desc_xtzq09wxoyfp7rm">
          宋小宝“苏格兰调情”偶遇小沈阳
         </div>
         <div class="slider_figure_desc2" title="宋小宝“苏格兰调情”偶遇小沈阳">
          宋小宝“苏格兰调情”偶遇小沈阳
         </div>
         <div _stat="焦点图:大家在追:播放按钮" class="slider_figure_btn slider_figure_btn_xtzq09wxoyfp7rm">
          立即观看
         </div>
        </div>
       </a>
       <button _stat="焦点图:追剧:上一页" class="btn_figure_prev disabled" wind-click="100">
        <svg class="svg_icon svg_icon_prev" height="18" viewbox="0 0 10 18" width="10">
         <path d="M9 1L1 9.07 9 17" fill-rule="nonzero" stroke="currentColor" stroke-linecap="round" stroke-width="1.4" style="fill:none">
         </path>
        </svg>
       </button>
      </div>
     </div>
     <button _stat="焦点图:追剧:下一页" class="btn_figure_next" wind-click="100">
      <svg class="svg_icon svg_icon_next" height="18" viewbox="0 0 10 18" width="10">
       <path d="M1 1l8 8.07L1 17" fill-rule="evenodd" stroke="currentColor" stroke-linecap="round" stroke-width="1.4" style="fill:none">
       </path>
      </svg>
     </button>
    </div>
    <!--[if lte IE 8 ]><div class="slider_top_mask"></div><![endif]-->
   </div>
   <div _wind="columnname=精选_焦点图&amp;controlname=new_vs_focus" class="slider_nav _quicklink slider_nav_watched">
    <a _stat="焦点图:追剧:大标题入口" class="nav_link nav_link_mine current" data-bgcolor="#3b7580" data-bgimage="//puui.qpic.cn/vupload/0/common_blank.png/0" href="http://v.qq.com/u/history/" target="_blank">
     <svg class="svg_slider_icon svg_icon_zj" height="11" width="16">
      <path class="path_1" d="M15 8A7 7 0 0 0 1 8" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2">
      </path>
      <path class="path_2" d="M8.9 5.1a1.5 1.5 0 1 0 2 2 3 3 0 1 1-2-2z" fill="currentColor">
      </path>
     </svg>
     <span class="text">
      大家在看
     </span>
    </a>
    <span class="nav_label">
     <svg class="svg_slider_icon svg_icon_zb" height="15" width="12">
      <defs>
       <lineargradient id="__gradient_zb_light" x1="41.309%" x2="71.734%" y1="32.314%" y2="100%">
        <stop offset="0%" stop-color="#FF9630">
        </stop>
        <stop offset="0%" stop-color="#FF9630">
        </stop>
        <stop offset="100%" stop-color="#FF1E1E">
        </stop>
       </lineargradient>
      </defs>
      <path class="path_1" d="M3.6 15C-.5 12.2-1.1 8.8 1.7 4.9 3.3 2.8 4.3 2.1 4.3 0c.4.2 5.1 2.6 4 7.5 1-.5 1.7-1.7 2-3.5 2.3 3.8 2.3 6.9-.1 9.4-.4.6-1.2 1.1-1.8 1.6-1.4-.6-3-1.9-3.6-5.6-1.3 1.4-1.7 3.3-1.2 5.6z">
      </path>
      <path class="path_2" d="M.3 7.7c.3-.9.7-1.8 1.4-2.8C3.3 2.8 4.3 2.1 4.3 0 4.5.1 5.8.8 7 2.1c.5 2.7-1.3 5.3-4 5.8-1 .2-1.9.1-2.7-.2z" fill="#ffb821">
      </path>
     </svg>
     <span class="text">
      重磅推荐
     </span>
    </span>
    <a __wind="" _stat="焦点图:标题:1:末日救援" class="nav_link" data-bgcolor="#324b74" data-bgimage="//puui.qpic.cn/media_img/lena/PIC8qmq9a_580_1680/0" data-navcolor="undefined" href="https://v.qq.com/x/cover/mzc00200mcm0lzz.html" target="_blank">
     <span class="text text2" title="末日救援: 姜超凌潇肃血战异星虫潮">
      <span class="title_text">
       末日救援
      </span>
      姜超凌潇肃血战异星虫潮
     </span>
    </a>
    <a __wind="" _stat="焦点图:标题:2:良言写意" class="nav_link" data-bgcolor="#0a0605" data-bgimage="//puui.qpic.cn/media_img/lena/PICez1zq6_580_1680/0" data-navcolor="undefined" href="https://v.qq.com/x/cover/mzc00200ev05cth.html" target="_blank">
     <span class="text text2" title="良言写意: 罗云熙程潇8倍速之恋">
      <span class="title_text">
       良言写意
      </span>
      罗云熙程潇8倍速之恋
     </span>
    </a>
    <a __wind="" _stat="焦点图:标题:3:斛珠夫人" class="nav_link" data-bgcolor="#275460" data-bgimage="//puui.qpic.cn/media_img/lena/PICi7iriq_580_1680/0" data-navcolor="undefined" href="https://v.qq.com/x/cover/mzc00200prv7r23.html" target="_blank">
     <span class="text text2" title="斛珠夫人: 海市方诸爱意相通">
      <span class="title_text">
       斛珠夫人
      </span>
      海市方诸爱意相通
     </span>
    </a>
    <a __wind="" _stat="焦点图:标题:4:正直播KPL季后赛" class="nav_link" data-bgcolor="#06123c" data-bgimage="//vc.qpic.cn/tpic/mtviuCbF5BR6S/pvos8442yp4ik909/1680" data-navcolor="undefined" href="https://v.qq.com/live/p/topic/130987/index.html#player" target="_blank">
     <span class="text text2" title="正直播KPL季后赛: AG vs RW侠">
      <span class="title_text">
       正直播KPL季后赛
      </span>
      AG vs RW侠
     </span>
    </a>
    <a __wind="" _stat="焦点图:标题:5:乌海·会员免费" class="nav_link" data-bgcolor="#412a1c" data-bgimage="//puui.qpic.cn/media_img/lena/PICxyr9vt_580_1680/0" data-navcolor="undefined" href="https://v.qq.com/x/cover/mzc002004hmja57.html" target="_blank">
     <span class="text text2" title="乌海·会员免费: 虐！黄轩杨子姗夫妻">
      <span class="title_text">
       乌海·会员免费
      </span>
      虐！黄轩杨子姗夫妻"陌路"
     </span>
    </a>
    <a __wind="" _stat="焦点图:标题:6:哈哈哈哈哈" class="nav_link" data-bgcolor="#2d3920" data-bgimage="//puui.qpic.cn/media_img/lena/PIChdkczb_580_1680/0" data-navcolor="undefined" href="https://v.qq.com/x/cover/mzc00200h593q8k.html" target="_blank">
     <span class="text text2" title="哈哈哈哈哈: 浮夸！陈赫演蚕蛹">
      <span class="title_text">
       哈哈哈哈哈
      </span>
      浮夸！陈赫演蚕蛹
     </span>
    </a>
    <a __wind="" _stat="焦点图:标题:7:来自三峡的“梦想之橙”" class="nav_link" data-bgcolor="#c9561d" data-bgimage="//vfiles.gtimg.cn/vupload/20211201/9eafe71638327515682.jpg" data-navcolor="undefined" href="https://v.qq.com/x/cover/mzc00200v5lhxat.html" target="_blank">
     <span class="text text2" title="来自三峡的“梦想之橙”: 丰收了好村光">
      <span class="title_text">
       来自三峡的“梦想之橙”
      </span>
      丰收了好村光
     </span>
    </a>
    <a __wind="" _stat="焦点图:标题:8:爱很美味" class="nav_link" data-bgcolor="#e3d3b1" data-bgimage="//vc.qpic.cn/tpic/mtviuzLMiANbm/8jrr7911eiydo676/1680" data-navcolor="undefined" href="https://v.qq.com/x/cover/mzc00200kqq8aps.html" target="_blank">
     <span class="text text2" title="爱很美味: 闺蜜团追爱作战爆笑解压">
      <span class="title_text">
       爱很美味
      </span>
      闺蜜团追爱作战爆笑解压
     </span>
    </a>
    <a __wind="" _stat="焦点图:标题:9:中国这么美·更新" class="nav_link" data-bgcolor="#2f4a53" data-bgimage="//vc.qpic.cn/tpic/mtviuCi1yVTMJ.jpg" data-navcolor="undefined" href="https://v.qq.com/x/cover/mzc00200cl0prlg/z00415wvf6z.html" target="_blank">
     <span class="text text2" title="中国这么美·更新: 张尕怂黄河边开嗓">
      <span class="title_text">
       中国这么美·更新
      </span>
      张尕怂黄河边开嗓
     </span>
    </a>
   </div>
  </div>
  <link href="//vm.gtimg.cn/c/=/tencentvideo/vstyle/web/v6/style/css/channel/channel.css?v=2021102215" rel="stylesheet"/>
  <!--[if lte IE 9 ]>
<link rel="stylesheet" href="//vm.gtimg.cn/c/=/tencentvideo/vstyle/web/v6/style/css/channel/channel.ie.css?v=2021102215" />
<![endif]-->
  <script src="//vm.gtimg.cn/tencentvideo_v1/script/txv.core.js?v=20211119" type="text/javascript">
  </script>
  <div _expose="v_index_nav" class="mod_main_nav" data-context="1" data-istyle="103" data-wind="columnname=精选_频道推荐区&amp;controlname=v_index_nav" id="mod_main_nav">
   <meta charset="utf-8"/>
   <div class="main_nav main_nav_0">
    <div class="main_nav_block main_nav_block_1">
     <a _stat="频道推荐区:主频道:电视剧" class="nav_link bold t3" data-channel="tv" href="/channel/tv">
      <img alt="" class="nav_icon" src="//puui.qpic.cn/vupload/0/20181206_1544081196478_lrgd9cazlhs.png/0"/>
      电视剧
     </a>
     <a _stat="频道推荐区:子频道:海外剧" class="nav_link grey t4" data-key="海外剧" href="/channel/usuk">
      海外剧
     </a>
     <a _stat="频道推荐区:子频道:网络剧" class="nav_link grey t4" data-key="网络剧" href="/channel/net_tv">
      网络剧
     </a>
    </div>
    <div class="main_nav_block main_nav_block_2">
     <a _stat="频道推荐区:主频道:电影" class="nav_link bold t3" data-channel="movie" href="/channel/movie">
      <img alt="" class="nav_icon" src="//puui.qpic.cn/vupload/0/20181206_1544081196504_itmr2xdlmpb.png/0"/>
      电影
     </a>
     <a _stat="频道推荐区:子频道:院线大片" class="nav_link grey t4" data-key="院线大片" href="/channel/movie?listpage=1&amp;channel=movie&amp;itype=100062">
      院线大片
     </a>
     <a _stat="频道推荐区:子频道:自制电影" class="nav_link grey t4" data-key="自制电影" href="/channel/dv">
      自制电影
     </a>
    </div>
   </div>
   <div class="main_nav main_nav_1">
    <div class="main_nav_block main_nav_block_1">
     <a _stat="频道推荐区:主频道:综艺" class="nav_link bold t2" data-channel="variety" href="/channel/variety">
      <img alt="" class="nav_icon" src="//puui.qpic.cn/vupload/0/20181206_1544081196514_yzvp912kh1p.png/0"/>
      综艺
     </a>
     <a _stat="频道推荐区:子频道:腾讯自制" class="nav_link grey t4" data-key="腾讯自制" href="/channel/variety?listpage=1&amp;channel=variety&amp;source=1&amp;exclusive=1">
      腾讯自制
     </a>
     <a _stat="频道推荐区:子频道:独播" class="nav_link grey t2" data-key="独播" href="/channel/variety?listpage=1&amp;channel=variety&amp;source=1&amp;exclusive=2">
      独播
     </a>
    </div>
    <div class="main_nav_block main_nav_block_2">
     <a _stat="频道推荐区:主频道:动漫" class="nav_link bold t2" data-channel="cartoon" href="/channel/cartoon">
      <img alt="" class="nav_icon" src="//puui.qpic.cn/vupload/0/20181206_1544081196508_jhfbyyujr58.png/0"/>
      动漫
     </a>
     <a _stat="频道推荐区:子频道:国漫" class="nav_link grey t4" data-key="国漫" href="/channel/cartoon?listpage=1&amp;channel=cartoon&amp;iarea=1">
      国漫
     </a>
     <a _stat="频道推荐区:子频道:日漫" class="nav_link grey t2" data-key="日漫" href="/channel/cartoon?listpage=1&amp;channel=cartoon&amp;iarea=2">
      日漫
     </a>
    </div>
   </div>
   <div class="main_nav main_nav_2">
    <div class="main_nav_block main_nav_block_1">
     <a _stat="频道推荐区:主频道:少儿" class="nav_link bold t3" data-channel="child" href="/channel/child">
      <img alt="" class="nav_icon" src="//puui.qpic.cn/vupload/0/20181206_1544081196514_po0qlecenmr.png/0"/>
      少儿
     </a>
     <a _stat="频道推荐区:子频道:益智" class="nav_link grey t2" data-key="益智" href="/channel/child?listpage=1&amp;channel=children&amp;itype=2">
      益智
     </a>
     <a _stat="频道推荐区:子频道:儿歌" class="nav_link grey t2" data-key="儿歌" href="/channel/child?listpage=1&amp;channel=children&amp;itype=1">
      儿歌
     </a>
    </div>
    <div class="main_nav_block main_nav_block_2">
     <a _stat="频道推荐区:主频道:纪录片" class="nav_link bold t3" data-channel="doco" href="/channel/doco">
      <img alt="" class="nav_icon" src="//puui.qpic.cn/vupload/0/20181206_1544081196512_zj8b2z4ql2m.png/0"/>
      纪录片
     </a>
     <a _stat="频道推荐区:子频道:美食" class="nav_link grey t2" data-key="美食" href="/channel/doco?listpage=1&amp;channel=doco&amp;itype=9">
      美食
     </a>
     <a _stat="频道推荐区:子频道:自然" class="nav_link grey t2" data-key="自然" href="/channel/doco?listpage=1&amp;channel=doco&amp;itype=4">
      自然
     </a>
    </div>
   </div>
   <div class="main_nav main_nav_3">
    <div class="main_nav_cell main_nav_cell_0">
     <a _stat="频道推荐区:主频道:VIP会员" class="nav_link nav_link_1" href="https://film.qq.com/" target="_blank">
      VIP会员
     </a>
     <a _stat="频道推荐区:主频道:音乐" class="nav_link nav_link_2" data-channel="music" href="/channel/music">
      音乐
     </a>
    </div>
    <div class="main_nav_cell main_nav_cell_1">
     <a _stat="频道推荐区:主频道:NBA" class="nav_link nav_link_1" href="https://v.qq.com/channel/nba" target="_blank">
      NBA
     </a>
     <a _stat="频道推荐区:主频道:体育" class="nav_link nav_link_2" data-channel="sports_new" href="/channel/sports_new">
      体育
     </a>
    </div>
    <div class="main_nav_cell main_nav_cell_2">
     <a _stat="频道推荐区:主频道:娱乐" class="nav_link nav_link_1" data-channel="ent" href="/channel/ent">
      娱乐
     </a>
     <a _stat="频道推荐区:主频道:生活" class="nav_link nav_link_2" data-channel="life" href="/channel/life">
      生活
     </a>
    </div>
    <div class="main_nav_cell main_nav_cell_3">
     <a _stat="频道推荐区:主频道:新闻" class="nav_link nav_link_1" data-channel="news" href="/channel/news">
      新闻
     </a>
     <a _stat="频道推荐区:主频道:游戏" class="nav_link nav_link_2" data-channel="games" href="/channel/games">
      游戏
     </a>
    </div>
    <div class="main_nav_cell main_nav_cell_4">
     <a _stat="频道推荐区:主频道:艺术" class="nav_link nav_link_1" data-channel="art" href="/channel/art">
      艺术
     </a>
     <a _stat="频道推荐区:主频道:知识" class="nav_link nav_link_2" data-channel="knowledge" href="/channel/knowledge">
      知识
     </a>
    </div>
    <div class="main_nav_cell main_nav_cell_5">
     <a _stat="频道推荐区:主频道:S11" class="nav_link nav_link_1" href="https://v.qq.com/channel/lols11" target="_blank">
      S11
     </a>
     <a _stat="频道推荐区:主频道:教育课堂" class="nav_link nav_link_2" data-channel="education" href="/channel/education">
      教育课堂
     </a>
    </div>
    <div class="main_nav_cell main_nav_cell_6">
     <a _stat="频道推荐区:主频道:时尚" class="nav_link nav_link_1" data-channel="fashion" href="/channel/fashion">
      时尚
     </a>
     <a _stat="频道推荐区:主频道:科技" class="nav_link nav_link_2" data-channel="tech" href="/channel/tech">
      科技
     </a>
    </div>
    <div class="main_nav_cell main_nav_cell_7">
     <a _stat="频道推荐区:主频道:活动" class="nav_link nav_link_1" href="https://cc.v.qq.com/activity" target="_blank">
      活动
     </a>
     <a _stat="频道推荐区:更多" class="nav_link nav_link_more" data-pop="nav_popup_area_more" href="javascript:;">
      更多
     </a>
     <div class="nav_popup_area nav_popup_area_more nav_popup_area_更多">
      <div class="nav_popup_area_title">
       <span class="nav_pop_label">
        更多频道
       </span>
      </div>
      <div class="nav_popup_inner">
       <a _stat="频道推荐区:更多浮层:新闻" class="nav_pop_link nav_pop_link_0 nav_pop_link_xs" href="/channel/news">
        新闻
       </a>
       <a _stat="频道推荐区:更多浮层:游戏" class="nav_pop_link nav_pop_link_1 nav_pop_link_xs" href="/channel/games">
        游戏
       </a>
       <a _stat="频道推荐区:更多浮层:艺术" class="nav_pop_link nav_pop_link_2 nav_pop_link_ms" href="/channel/art">
        艺术
       </a>
       <a _stat="频道推荐区:更多浮层:知识" class="nav_pop_link nav_pop_link_3 nav_pop_link_ms" href="/channel/knowledge">
        知识
       </a>
       <a _stat="频道推荐区:更多浮层:S11" class="nav_pop_link nav_pop_link_4 nav_pop_link_ls" href="https://v.qq.com/channel/lols11" target="_blank">
        S11
       </a>
       <a _stat="频道推荐区:更多浮层:教育课堂" class="nav_pop_link nav_pop_link_5 nav_pop_link_ls" href="/channel/education">
        教育课堂
       </a>
       <a _stat="频道推荐区:更多浮层:时尚" class="nav_pop_link nav_pop_link_6 nav_pop_link_ls" href="/channel/fashion">
        时尚
       </a>
       <a _stat="频道推荐区:更多浮层:科技" class="nav_pop_link nav_pop_link_7 nav_pop_link_ls" href="/channel/tech">
        科技
       </a>
       <a _stat="频道推荐区:更多浮层:活动" class="nav_pop_link nav_pop_link_8" href="https://cc.v.qq.com/activity" target="_blank">
        活动
       </a>
       <a _stat="频道推荐区:更多浮层:汽车" class="nav_pop_link nav_pop_link_9" href="/channel/auto">
        汽车
       </a>
       <a _stat="频道推荐区:更多浮层:WWE" class="nav_pop_link nav_pop_link_10" href="/channel/wwe">
        WWE
       </a>
       <a _stat="频道推荐区:更多浮层:育儿" class="nav_pop_link nav_pop_link_11" href="/channel/baby">
        育儿
       </a>
       <a _stat="频道推荐区:更多浮层:旅游" class="nav_pop_link nav_pop_link_12" href="/channel/travel">
        旅游
       </a>
       <a _stat="频道推荐区:更多浮层:房产" class="nav_pop_link nav_pop_link_13" href="/channel/house">
        房产
       </a>
       <a _stat="频道推荐区:更多浮层:财经" class="nav_pop_link nav_pop_link_14" href="/channel/finance">
        财经
       </a>
       <a _stat="频道推荐区:更多浮层:热播榜" class="nav_pop_link nav_pop_link_15" href="https://v.qq.com/biu/ranks/?t=hotplay&amp;channel=all&amp;ptag=vheader" target="_blank">
        热播榜
       </a>
       <a _stat="频道推荐区:更多浮层:热搜榜" class="nav_pop_link nav_pop_link_16" href="https://v.qq.com/biu/ranks/?t=hotsearch&amp;ptag=vheader" target="_blank">
        热搜榜
       </a>
       <a _stat="频道推荐区:更多浮层:直播" class="nav_pop_link nav_pop_link_17" href="http://v.qq.com/x/live/">
        直播
       </a>
       <a _stat="频道推荐区:更多浮层:网页游戏" class="nav_pop_link nav_pop_link_18" href="https://iwan.qq.com/pcwebsite/game?ADTAG=vzdh" target="_blank">
        网页游戏
       </a>
       <a _stat="频道推荐区:更多浮层:演唱会" class="nav_pop_link nav_pop_link_19" href="https://v.qq.com/livemusic/">
        演唱会
       </a>
       <a _stat="频道推荐区:更多浮层:爱看" class="nav_pop_link nav_pop_link_20" href="/channel/feeds_hotspot">
        爱看
       </a>
       <a _stat="频道推荐区:更多浮层:搞笑" class="nav_pop_link nav_pop_link_21" href="/channel/fun">
        搞笑
       </a>
       <a _stat="频道推荐区:更多浮层:星座" class="nav_pop_link nav_pop_link_22" href="/channel/astro">
        星座
       </a>
      </div>
     </div>
    </div>
   </div>
   <div class="main_feature">
    <a _stat="频道推荐区:应用中心" class="mf_item mf_item_0 __lite_hide__" href="https://v.qq.com/biu/download#Windows">
     <span class="item_pic">
      <img alt="应用中心" class="pic1" src="//puui.qpic.cn/vupload/0/20190708_h2gvgd4og8/0"/>
      <img alt="应用中心" class="pic2" src="//puui.qpic.cn/vupload/0/20190708_9h1ffex3prf/0"/>
     </span>
     <span class="icon_text">
      应用中心
     </span>
    </a>
    <a _stat="频道推荐区:VIP影院" class="mf_item mf_item_1" href="https://film.qq.com/">
     <span class="item_pic">
      <img alt="VIP影院" class="pic1" src="//puui.qpic.cn/vupload/0/20190708_put2hy5e2g/0"/>
      <img alt="VIP影院" class="pic2" src="//puui.qpic.cn/vupload/0/20190708_hvl7275ycy7/0"/>
     </span>
     <span class="icon_text">
      VIP影院
     </span>
    </a>
   </div>
  </div>
  <div _expose="new_vs_hot_today" _wind="columnname=精选_今日热门&amp;controlname=new_vs_hot_today" class="mod_row_box" cur-page-num="0" data-context="1" data-istyle="4" has-next-page="false" id="new_vs_hot_today">
   <div class="mod_hd">
    <h2 class="mod_title">
     今日热门
    </h2>
    <a _stat="new_vs_hot_today:通栏功能区:广播" class="subtitle" href="https://film.qq.com/film/p/topic/hqfyt01/index.html?ptag=hot" target="_blank">
     集电影勋章 赢小黄人投影仪
    </a>
    <div class="mod_page_small">
     <button _stat="new_vs_hot_today:通栏功能区:上一页" class="btn_prev disabled" title="上一页" wind-click="100">
      <svg class="svg_icon svg_icon_prev" height="10" viewbox="0 0 6 10" width="6">
       <path d="M1.4 4.7L5 1M1.3 5.3L5 9" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="1.4">
       </path>
      </svg>
     </button>
     <span class="page_num" data-count="6" data-info="8 42" data-page="1">
      1/6
     </span>
     <button _stat="new_vs_hot_today:通栏功能区:下一页" class="btn_next" title="下一页" wind-click="100">
      <svg class="svg_icon svg_icon_next" height="10" viewbox="0 0 6 10" width="6">
       <path d="M4.6 4.7L1 1M4.7 5.3L1 9" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="1.4">
       </path>
      </svg>
     </button>
    </div>
   </div>
   <div class="mod_bd cf _quickopen _quickopen_duration">
    <div class="mod_figure mod_figure_h_default mod_figure_h_default_1row mod_figure_h_default mod_figure_scroll" data-rowcount="8" data-rowlen="1">
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_today:img:【大伙之家】徐志胜pk奥运冠军吹画片" class="figure" data-float="v0041nyonq8" data-quickopen="true" href="https://v.qq.com/x/cover/mzc00200mquy6aa/v0041nyonq8.html" tabindex="-1" target="_blank">
       <img alt="【大伙之家】徐志胜pk奥运冠军吹画片" class="figure_pic" loading="lazy" onerror="picerr(this,'h')" src="//puui.qpic.cn/media_img/lena/PIC74esyd_304_540/0"/>
       <div class="figure_caption">
        01:32
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_today:title:【大伙之家】徐志胜pk奥运冠军吹画片" class="figure_title figure_title_two_row" href="https://v.qq.com/x/cover/mzc00200mquy6aa/v0041nyonq8.html" target="_blank" title="【大伙之家】徐志胜pk奥运冠军吹画片">
        【大伙之家】徐志胜pk奥运冠军吹画片
       </a>
       <div class="figure_desc" title="谁的DNA动了？女排冠军讲述郎平励志故事">
        谁的DNA动了？女排冠军讲述郎平励志故事
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_today:img:我国科学家在月球背面发现“天外来客”" class="figure" data-float="j3311lw227c" data-quickopen="true" href="https://v.qq.com/x/page/j3311lw227c.html" tabindex="-1" target="_blank">
       <img alt="我国科学家在月球背面发现“天外来客”" class="figure_pic" loading="lazy" onerror="picerr(this,'h')" src="//puui.qpic.cn/qqvideo_ori/0/j3311lw227c_360_204/0"/>
       <div class="figure_caption">
        00:38
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_today:title:我国科学家在月球背面发现“天外来客”" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/j3311lw227c.html" target="_blank" title="我国科学家在月球背面发现“天外来客”">
        我国科学家在月球背面发现“天外来客”
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_today:img:汪文斌痛斥安倍涉台狂言：胡言乱语！" class="figure" data-float="s3311fqxcdz" data-quickopen="true" href="https://v.qq.com/x/page/s3311fqxcdz.html" tabindex="-1" target="_blank">
       <img alt="汪文斌痛斥安倍涉台狂言：胡言乱语！" class="figure_pic" loading="lazy" onerror="picerr(this,'h')" src="//puui.qpic.cn/qqvideo_ori/0/s3311fqxcdz_360_204/0"/>
       <div class="figure_caption">
        01:12
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_today:title:汪文斌痛斥安倍涉台狂言：胡言乱语！" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/s3311fqxcdz.html" target="_blank" title="汪文斌痛斥安倍涉台狂言：胡言乱语！">
        汪文斌痛斥安倍涉台狂言：胡言乱语！
       </a>
      </div>
     </div>
     <!--QQlive_FB_CAP_ss_rm_div AD begin...."l=QQlive_FB_CAP_ss_rm&log=off"-->
     <div class="l_qq_com" id="QQlive_FB_CAP_ss_rm" style="width:1px;height:1px;display:none;">
     </div>
     <!--QQlive_FB_CAP_ss_rm AD end -->
     <!--[if !IE]>|xGv00|c12474066497e6c706d23e9842e0d3ba<![endif]-->
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_today:img:冰雪起源·邹市明介绍冬奥项目钢架雪车" class="figure" data-float="p0041ae7hsd" data-quickopen="true" href="https://v.qq.com/x/page/p0041ae7hsd.html" tabindex="-1" target="_blank">
       <img alt="冰雪起源·邹市明介绍冬奥项目钢架雪车" class="figure_pic" loading="lazy" onerror="picerr(this,'h')" src="//puui.qpic.cn/qqvideo_ori/0/p0041ae7hsd_360_204/0"/>
       <div class="figure_caption">
        01:34
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_today:title:冰雪起源·邹市明介绍冬奥项目钢架雪车" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/p0041ae7hsd.html" target="_blank" title="冰雪起源·邹市明介绍冬奥项目钢架雪车">
        冰雪起源·邹市明介绍冬奥项目钢架雪车
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_today:img:奥运冠军石智勇办婚礼，樊振东隔空“证婚”" class="figure" data-float="s3311mjlgnu" data-quickopen="true" href="https://v.qq.com/x/page/s3311mjlgnu.html" tabindex="-1" target="_blank">
       <img alt="奥运冠军石智勇办婚礼，樊振东隔空“证婚”" class="figure_pic" loading="lazy" onerror="picerr(this,'h')" src="//puui.qpic.cn/qqvideo_ori/0/s3311mjlgnu_360_204/0"/>
       <div class="figure_caption">
        00:32
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_today:title:奥运冠军石智勇办婚礼，樊振东隔空“证婚”" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/s3311mjlgnu.html" target="_blank" title="奥运冠军石智勇办婚礼，樊振东隔空“证婚”">
        奥运冠军石智勇办婚礼，樊振东隔空“证婚”
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_today:img:宋祖儿：王安宇和邵北笙一样自恋，我也挺直女的" class="figure" data-float="k3311paosz2" data-quickopen="true" href="https://v.qq.com/x/page/k3311paosz2.html" tabindex="-1" target="_blank">
       <img alt="宋祖儿：王安宇和邵北笙一样自恋，我也挺直女的" class="figure_pic" loading="lazy" onerror="picerr(this,'h')" src="//puui.qpic.cn/media_img/lena/PICp9iy3e_304_540/0"/>
       <div class="figure_caption">
        06:44
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_today:title:宋祖儿：王安宇和邵北笙一样自恋，我也挺直女的" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/k3311paosz2.html" target="_blank" title="宋祖儿：王安宇和邵北笙一样自恋，我也挺直女的">
        宋祖儿：王安宇和邵北笙一样自恋，我也挺直女的
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_today:img:村民袭警被击倒身亡：民警多次警告无效后开枪" class="figure" data-float="a3311fohbwi" data-quickopen="true" href="https://v.qq.com/x/page/a3311fohbwi.html" tabindex="-1" target="_blank">
       <img alt="村民袭警被击倒身亡：民警多次警告无效后开枪" class="figure_pic" loading="lazy" onerror="picerr(this,'h')" src="//puui.qpic.cn/qqvideo_ori/0/a3311fohbwi_360_204/0"/>
       <div class="figure_caption">
        03:22
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_today:title:村民袭警被击倒身亡：民警多次警告无效后开枪" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/a3311fohbwi.html" target="_blank" title="村民袭警被击倒身亡：民警多次警告无效后开枪">
        村民袭警被击倒身亡：民警多次警告无效后开枪
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_today:img:【鹿先森·后毕业时代】理性和感性哪个更重要" class="figure" data-float="g33118u2osm" href="https://v.qq.com/x/cover/mzc003qigg4aigg/g33118u2osm.html" tabindex="-1" target="_blank">
       <img alt="【鹿先森·后毕业时代】理性和感性哪个更重要" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/media_img/lena/PIC8pu3w4_360_640/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        19:18
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_today:title:【鹿先森·后毕业时代】理性和感性哪个更重要" class="figure_title figure_title_two_row" href="https://v.qq.com/x/cover/mzc003qigg4aigg/g33118u2osm.html" target="_blank" title="【鹿先森·后毕业时代】理性和感性哪个更重要">
        【鹿先森·后毕业时代】理性和感性哪个更重要
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_today:img:年轻演员不认识老演员？刘佩琦呼吁年轻演员重传承" class="figure" data-float="k33118okewt" data-quickopen="true" href="https://v.qq.com/x/page/k33118okewt.html" tabindex="-1" target="_blank">
       <img alt="年轻演员不认识老演员？刘佩琦呼吁年轻演员重传承" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/media_img/lena/PICcbpgro_360_640/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        00:28
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_today:title:年轻演员不认识老演员？刘佩琦呼吁年轻演员重传承" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/k33118okewt.html" target="_blank" title="年轻演员不认识老演员？刘佩琦呼吁年轻演员重传承">
        年轻演员不认识老演员？刘佩琦呼吁年轻演员重传承
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_today:img:【云首发Livehouse黄旭专场】美女歌迷与黄旭合唱" class="figure" data-float="mzc00200gis6rz5" href="https://v.qq.com/x/cover/mzc00200gis6rz5.html" tabindex="-1" target="_blank">
       <img alt="【云首发Livehouse黄旭专场】美女歌迷与黄旭合唱" class="figure_pic" loading="lazy" lz_next="//vc.qpic.cn/tpic/mtviuBUcd96wQ/41y5835945a7p726/285" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
       <img alt="云首发" class="mark_v mark_v_云首发" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20210121/tag_nor_vip_released_x1_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20210121/tag_nor_vip_released_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_today:title:【云首发Livehouse黄旭专场】美女歌迷与黄旭合唱" class="figure_title figure_title_two_row" href="https://v.qq.com/x/cover/mzc00200gis6rz5.html" target="_blank" title="【云首发Livehouse黄旭专场】美女歌迷与黄旭合唱">
        【云首发Livehouse黄旭专场】美女歌迷与黄旭合唱
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_today:img:感动、震撼、怀念…3分钟回顾2021年“破防”瞬间" class="figure" data-float="f3311okhl9f" data-quickopen="true" href="https://v.qq.com/x/page/f3311okhl9f.html" tabindex="-1" target="_blank">
       <img alt="感动、震撼、怀念…3分钟回顾2021年“破防”瞬间" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo_ori/0/f3311okhl9f_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        03:35
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_today:title:感动、震撼、怀念…3分钟回顾2021年“破防”瞬间" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/f3311okhl9f.html" target="_blank" title="感动、震撼、怀念…3分钟回顾2021年“破防”瞬间">
        感动、震撼、怀念…3分钟回顾2021年“破防”瞬间
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_today:img:被周深唱火的《起风了》，买辣椒也用券巡演再现经典" class="figure" data-float="o0041m3ievt" data-quickopen="true" href="https://v.qq.com/x/cover/mzc00200hizmi75/o0041m3ievt.html" tabindex="-1" target="_blank">
       <img alt="被周深唱火的《起风了》，买辣椒也用券巡演再现经典" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/media_img/lena/PICfgnske_304_540/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        05:16
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_today:title:被周深唱火的《起风了》，买辣椒也用券巡演再现经典" class="figure_title figure_title_two_row" href="https://v.qq.com/x/cover/mzc00200hizmi75/o0041m3ievt.html" target="_blank" title="被周深唱火的《起风了》，买辣椒也用券巡演再现经典">
        被周深唱火的《起风了》，买辣椒也用券巡演再现经典
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_today:img:佳木斯通报“女公务员殴打母亲”：已立案审查" class="figure" data-float="l3311ax3s8f" data-quickopen="true" href="https://v.qq.com/x/page/l3311ax3s8f.html" tabindex="-1" target="_blank">
       <img alt="佳木斯通报“女公务员殴打母亲”：已立案审查" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo_ori/0/l3311ax3s8f_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        00:37
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_today:title:佳木斯通报“女公务员殴打母亲”：已立案审查" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/l3311ax3s8f.html" target="_blank" title="佳木斯通报“女公务员殴打母亲”：已立案审查">
        佳木斯通报“女公务员殴打母亲”：已立案审查
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_today:img:四川宜宾长宁县发生4.2级地震 家中宠物突然跑开" class="figure" data-float="q3311o0pa8q" data-quickopen="true" href="https://v.qq.com/x/page/q3311o0pa8q.html" tabindex="-1" target="_blank">
       <img alt="四川宜宾长宁县发生4.2级地震 家中宠物突然跑开" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo_ori/0/q3311o0pa8q_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        00:25
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_today:title:四川宜宾长宁县发生4.2级地震 家中宠物突然跑开" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/q3311o0pa8q.html" target="_blank" title="四川宜宾长宁县发生4.2级地震 家中宠物突然跑开">
        四川宜宾长宁县发生4.2级地震 家中宠物突然跑开
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_today:img:冰雪起源·王安宇为你讲述花样滑雪的历史故事" class="figure" data-float="c0041qsame5" data-quickopen="true" href="https://v.qq.com/x/page/c0041qsame5.html" tabindex="-1" target="_blank">
       <img alt="冰雪起源·王安宇为你讲述花样滑雪的历史故事" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo_ori/0/c0041qsame5_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        01:45
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_today:title:冰雪起源·王安宇为你讲述花样滑雪的历史故事" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/c0041qsame5.html" target="_blank" title="冰雪起源·王安宇为你讲述花样滑雪的历史故事">
        冰雪起源·王安宇为你讲述花样滑雪的历史故事
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_today:img:现场!世界上又多了一个国家，蕾哈娜成“英雄”" class="figure" data-float="m33111rqnpi" data-quickopen="true" href="https://v.qq.com/x/page/m33111rqnpi.html" tabindex="-1" target="_blank">
       <img alt="现场!世界上又多了一个国家，蕾哈娜成“英雄”" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo_ori/0/m33111rqnpi_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        00:50
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_today:title:现场!世界上又多了一个国家，蕾哈娜成“英雄”" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/m33111rqnpi.html" target="_blank" title="现场!世界上又多了一个国家，蕾哈娜成“英雄”">
        现场!世界上又多了一个国家，蕾哈娜成“英雄”
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_today:img:速度滑冰，非同一般的极限体验" class="figure" data-float="d0034e3zhjt" data-quickopen="true" href="https://v.qq.com/x/page/d0034e3zhjt.html" tabindex="-1" target="_blank">
       <img alt="速度滑冰，非同一般的极限体验" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo_ori/0/d0034e3zhjt_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        02:00
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_today:title:速度滑冰，非同一般的极限体验" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/d0034e3zhjt.html" target="_blank" title="速度滑冰，非同一般的极限体验">
        速度滑冰，非同一般的极限体验
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_today:img:前辈的肯定！“大魔王”张怡宁夸奖“小魔王”孙颖莎" class="figure" data-float="z3311rqv1g6" data-quickopen="true" href="https://v.qq.com/x/page/z3311rqv1g6.html" tabindex="-1" target="_blank">
       <img alt="前辈的肯定！“大魔王”张怡宁夸奖“小魔王”孙颖莎" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo_ori/0/z3311rqv1g6_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        00:37
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_today:title:前辈的肯定！“大魔王”张怡宁夸奖“小魔王”孙颖莎" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/z3311rqv1g6.html" target="_blank" title="前辈的肯定！“大魔王”张怡宁夸奖“小魔王”孙颖莎">
        前辈的肯定！“大魔王”张怡宁夸奖“小魔王”孙颖莎
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_today:img:实至名归！梅西第七次获金球奖 现场点亮埃菲尔铁塔" class="figure" data-float="g3311cc6ojf" data-quickopen="true" href="https://v.qq.com/x/page/g3311cc6ojf.html" tabindex="-1" target="_blank">
       <img alt="实至名归！梅西第七次获金球奖 现场点亮埃菲尔铁塔" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo_ori/0/g3311cc6ojf_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        01:03
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_today:title:实至名归！梅西第七次获金球奖 现场点亮埃菲尔铁塔" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/g3311cc6ojf.html" target="_blank" title="实至名归！梅西第七次获金球奖 现场点亮埃菲尔铁塔">
        实至名归！梅西第七次获金球奖 现场点亮埃菲尔铁塔
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_today:img:刘国梁：在美最大挑战不是对手 是新冠" class="figure" data-float="h3311176bl8" data-quickopen="true" href="https://v.qq.com/x/page/h3311176bl8.html" tabindex="-1" target="_blank">
       <img alt="刘国梁：在美最大挑战不是对手 是新冠" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo_ori/0/h3311176bl8_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        01:16
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_today:title:刘国梁：在美最大挑战不是对手 是新冠" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/h3311176bl8.html" target="_blank" title="刘国梁：在美最大挑战不是对手 是新冠">
        刘国梁：在美最大挑战不是对手 是新冠
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_today:img:王艺迪世乒赛战胜伊藤美诚！伊藤赛后落泪" class="figure" data-float="y3311um38yl" data-quickopen="true" href="https://v.qq.com/x/page/y3311um38yl.html" tabindex="-1" target="_blank">
       <img alt="王艺迪世乒赛战胜伊藤美诚！伊藤赛后落泪" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo_ori/0/y3311um38yl_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        00:55
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_today:title:王艺迪世乒赛战胜伊藤美诚！伊藤赛后落泪" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/y3311um38yl.html" target="_blank" title="王艺迪世乒赛战胜伊藤美诚！伊藤赛后落泪">
        王艺迪世乒赛战胜伊藤美诚！伊藤赛后落泪
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_today:img:错过的收藏！90秒回放今年浪漫天象" class="figure" data-float="g3311k6h844" data-quickopen="true" href="https://v.qq.com/x/page/g3311k6h844.html" tabindex="-1" target="_blank">
       <img alt="错过的收藏！90秒回放今年浪漫天象" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo_ori/0/g3311k6h844_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        01:25
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_today:title:错过的收藏！90秒回放今年浪漫天象" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/g3311k6h844.html" target="_blank" title="错过的收藏！90秒回放今年浪漫天象">
        错过的收藏！90秒回放今年浪漫天象
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_today:img:“奥密克戎”有多大危害？钟南山最新研判" class="figure" data-float="q3311zodt37" data-quickopen="true" href="https://v.qq.com/x/page/q3311zodt37.html" tabindex="-1" target="_blank">
       <img alt="“奥密克戎”有多大危害？钟南山最新研判" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo_ori/0/q3311zodt37_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        00:53
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_today:title:“奥密克戎”有多大危害？钟南山最新研判" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/q3311zodt37.html" target="_blank" title="“奥密克戎”有多大危害？钟南山最新研判">
        “奥密克戎”有多大危害？钟南山最新研判
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_today:img:年度最佳动画！？深度解析双城之战的Balance" class="figure" data-float="k0041ag5gqw" href="https://v.qq.com/x/page/k0041ag5gqw.html" tabindex="-1" target="_blank">
       <img alt="年度最佳动画！？深度解析双城之战的Balance" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo_ori/0/k0041ag5gqw_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        15:04
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_today:title:年度最佳动画！？深度解析双城之战的Balance" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/k0041ag5gqw.html" target="_blank" title="年度最佳动画！？深度解析双城之战的Balance">
        年度最佳动画！？深度解析双城之战的Balance
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_today:img:《大伙之家》故事开启，徐志胜连线鹿晗句句笑喷" class="figure" data-float="mzc002009az6yh5" href="https://v.qq.com/x/cover/mzc002009az6yh5.html" tabindex="-1" target="_blank">
       <img alt="《大伙之家》故事开启，徐志胜连线鹿晗句句笑喷" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/media_img/lena/PICj2738w_152_270/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        2021-11-25 期
       </div>
       <img alt="腾讯出品" class="mark_v mark_v_腾讯出品" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_self_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_self_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_today:title:《大伙之家》故事开启，徐志胜连线鹿晗句句笑喷" class="figure_title figure_title_two_row" href="https://v.qq.com/x/cover/mzc002009az6yh5.html" target="_blank" title="《大伙之家》故事开启，徐志胜连线鹿晗句句笑喷">
        《大伙之家》故事开启，徐志胜连线鹿晗句句笑喷
       </a>
       <div class="figure_desc" title="徐志胜何广智对跳广场舞">
        徐志胜何广智对跳广场舞
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_today:img:警方侦破不法经营赌博案  “洗米华”被移送检察院" class="figure" data-float="l3311pw2esb" data-quickopen="true" href="https://v.qq.com/x/page/l3311pw2esb.html" tabindex="-1" target="_blank">
       <img alt="警方侦破不法经营赌博案  “洗米华”被移送检察院" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo_ori/0/l3311pw2esb_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        01:17
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_today:title:警方侦破不法经营赌博案  “洗米华”被移送检察院" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/l3311pw2esb.html" target="_blank" title="警方侦破不法经营赌博案  “洗米华”被移送检察院">
        警方侦破不法经营赌博案  “洗米华”被移送检察院
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_today:img:瞿秋白之女瞿独伊逝世，曾用俄语向世界播报开国大典" class="figure" data-float="y3311ube5om" data-quickopen="true" href="https://v.qq.com/x/page/y3311ube5om.html" tabindex="-1" target="_blank">
       <img alt="瞿秋白之女瞿独伊逝世，曾用俄语向世界播报开国大典" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo_ori/0/y3311ube5om_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        01:18
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_today:title:瞿秋白之女瞿独伊逝世，曾用俄语向世界播报开国大典" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/y3311ube5om.html" target="_blank" title="瞿秋白之女瞿独伊逝世，曾用俄语向世界播报开国大典">
        瞿秋白之女瞿独伊逝世，曾用俄语向世界播报开国大典
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_today:img:新乡一学校学生集体呕吐，校长痛哭：换不动送餐公司" class="figure" data-float="v33103zkk0z" data-quickopen="true" href="https://v.qq.com/x/page/v33103zkk0z.html" tabindex="-1" target="_blank">
       <img alt="新乡一学校学生集体呕吐，校长痛哭：换不动送餐公司" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo_ori/0/v33103zkk0z_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        01:22
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_today:title:新乡一学校学生集体呕吐，校长痛哭：换不动送餐公司" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/v33103zkk0z.html" target="_blank" title="新乡一学校学生集体呕吐，校长痛哭：换不动送餐公司">
        新乡一学校学生集体呕吐，校长痛哭：换不动送餐公司
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_today:img:3D还原哀牢山4名地质员失联始末 天气突变酿悲剧" class="figure" data-float="u33109uyyuz" data-quickopen="true" href="https://v.qq.com/x/page/u33109uyyuz.html" tabindex="-1" target="_blank">
       <img alt="3D还原哀牢山4名地质员失联始末 天气突变酿悲剧" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo_ori/0/u33109uyyuz_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        06:33
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_today:title:3D还原哀牢山4名地质员失联始末 天气突变酿悲剧" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/u33109uyyuz.html" target="_blank" title="3D还原哀牢山4名地质员失联始末 天气突变酿悲剧">
        3D还原哀牢山4名地质员失联始末 天气突变酿悲剧
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_today:img:【后毕业时代】工作后还能成为学习小能手吗？" class="figure" data-float="e3310sar3y6" href="https://v.qq.com/x/page/e3310sar3y6.html" tabindex="-1" target="_blank">
       <img alt="【后毕业时代】工作后还能成为学习小能手吗？" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo_ori/0/e3310sar3y6_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        16:16
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_today:title:【后毕业时代】工作后还能成为学习小能手吗？" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/e3310sar3y6.html" target="_blank" title="【后毕业时代】工作后还能成为学习小能手吗？">
        【后毕业时代】工作后还能成为学习小能手吗？
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_today:img:非遗鼓乐版《孤勇者》，见证低谷与荣耀，为LPL加油！" class="figure" data-float="i0041jwcvfw" data-quickopen="true" href="https://v.qq.com/x/page/i0041jwcvfw.html" tabindex="-1" target="_blank">
       <img alt="非遗鼓乐版《孤勇者》，见证低谷与荣耀，为LPL加油！" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo_ori/0/i0041jwcvfw_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        03:26
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_today:title:非遗鼓乐版《孤勇者》，见证低谷与荣耀，为LPL加油！" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/i0041jwcvfw.html" target="_blank" title="非遗鼓乐版《孤勇者》，见证低谷与荣耀，为LPL加油！">
        非遗鼓乐版《孤勇者》，见证低谷与荣耀，为LPL加油！
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_today:img:李冰冰谈爱情与现实：生活的琐碎可以把爱情击得粉碎" class="figure" data-float="m0041s8x2oj" data-quickopen="true" href="https://v.qq.com/x/page/m0041s8x2oj.html" tabindex="-1" target="_blank">
       <img alt="李冰冰谈爱情与现实：生活的琐碎可以把爱情击得粉碎" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo_ori/0/m0041s8x2oj_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        01:22
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_today:title:李冰冰谈爱情与现实：生活的琐碎可以把爱情击得粉碎" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/m0041s8x2oj.html" target="_blank" title="李冰冰谈爱情与现实：生活的琐碎可以把爱情击得粉碎">
        李冰冰谈爱情与现实：生活的琐碎可以把爱情击得粉碎
       </a>
       <div class="figure_desc" title="李冰冰谈爱情轻易被现实打败？">
        李冰冰谈爱情轻易被现实打败？
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_today:img:航天员叶光富花式健身集锦：满头大汗 脚步不停" class="figure" data-float="v3310iehq6b" data-quickopen="true" href="https://v.qq.com/x/page/v3310iehq6b.html" tabindex="-1" target="_blank">
       <img alt="航天员叶光富花式健身集锦：满头大汗 脚步不停" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo_ori/0/v3310iehq6b_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        02:18
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_today:title:航天员叶光富花式健身集锦：满头大汗 脚步不停" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/v3310iehq6b.html" target="_blank" title="航天员叶光富花式健身集锦：满头大汗 脚步不停">
        航天员叶光富花式健身集锦：满头大汗 脚步不停
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_today:img:感动！飞行员逼退外机后合唱我和我的祖国" class="figure" data-float="q33107uqdc1" data-quickopen="true" href="https://v.qq.com/x/page/q33107uqdc1.html" tabindex="-1" target="_blank">
       <img alt="感动！飞行员逼退外机后合唱我和我的祖国" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo_ori/0/q33107uqdc1_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        02:52
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_today:title:感动！飞行员逼退外机后合唱我和我的祖国" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/q33107uqdc1.html" target="_blank" title="感动！飞行员逼退外机后合唱我和我的祖国">
        感动！飞行员逼退外机后合唱我和我的祖国
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_today:img:中国空间站长镜头拍地球 神舟飞船在一旁陪伴旋转" class="figure" data-float="c33105ontfq" data-quickopen="true" href="https://v.qq.com/x/page/c33105ontfq.html" tabindex="-1" target="_blank">
       <img alt="中国空间站长镜头拍地球 神舟飞船在一旁陪伴旋转" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo_ori/0/c33105ontfq_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        01:15
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_today:title:中国空间站长镜头拍地球 神舟飞船在一旁陪伴旋转" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/c33105ontfq.html" target="_blank" title="中国空间站长镜头拍地球 神舟飞船在一旁陪伴旋转">
        中国空间站长镜头拍地球 神舟飞船在一旁陪伴旋转
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_today:img:女子辞职前骗同事200万，同事：看她特别老实" class="figure" data-float="a3310e56e4p" data-quickopen="true" href="https://v.qq.com/x/page/a3310e56e4p.html" tabindex="-1" target="_blank">
       <img alt="女子辞职前骗同事200万，同事：看她特别老实" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo_ori/0/a3310e56e4p_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        01:01
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_today:title:女子辞职前骗同事200万，同事：看她特别老实" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/a3310e56e4p.html" target="_blank" title="女子辞职前骗同事200万，同事：看她特别老实">
        女子辞职前骗同事200万，同事：看她特别老实
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_today:img:外交部：普京愉快地接受了北京冬奥会开幕式邀请" class="figure" data-float="c33101bj7kp" data-quickopen="true" href="https://v.qq.com/x/page/c33101bj7kp.html" tabindex="-1" target="_blank">
       <img alt="外交部：普京愉快地接受了北京冬奥会开幕式邀请" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo_ori/0/c33101bj7kp_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        01:02
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_today:title:外交部：普京愉快地接受了北京冬奥会开幕式邀请" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/c33101bj7kp.html" target="_blank" title="外交部：普京愉快地接受了北京冬奥会开幕式邀请">
        外交部：普京愉快地接受了北京冬奥会开幕式邀请
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_today:img:又美又飒！北影女孩考上公务员又当上火箭军" class="figure" data-float="v3310my7hp1" data-quickopen="true" href="https://v.qq.com/x/page/v3310my7hp1.html" tabindex="-1" target="_blank">
       <img alt="又美又飒！北影女孩考上公务员又当上火箭军" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo_ori/0/v3310my7hp1_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        02:03
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_today:title:又美又飒！北影女孩考上公务员又当上火箭军" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/v3310my7hp1.html" target="_blank" title="又美又飒！北影女孩考上公务员又当上火箭军">
        又美又飒！北影女孩考上公务员又当上火箭军
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_today:img:杨幂专访：和方诸恋爱太辛苦，陈伟霆是剧组开心果" class="figure" data-float="h3310kokoo7" data-quickopen="true" href="https://v.qq.com/x/page/h3310kokoo7.html" tabindex="-1" target="_blank">
       <img alt="杨幂专访：和方诸恋爱太辛苦，陈伟霆是剧组开心果" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/media_img/lena/PICqir7ds_720_1280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        08:00
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_today:title:杨幂专访：和方诸恋爱太辛苦，陈伟霆是剧组开心果" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/h3310kokoo7.html" target="_blank" title="杨幂专访：和方诸恋爱太辛苦，陈伟霆是剧组开心果">
        杨幂专访：和方诸恋爱太辛苦，陈伟霆是剧组开心果
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_today:img:月牙泉雪落“变装” 呈现一幅唯美的东方诗意画卷" class="figure" data-float="v3310sawk9m" data-quickopen="true" href="https://v.qq.com/x/page/v3310sawk9m.html" tabindex="-1" target="_blank">
       <img alt="月牙泉雪落“变装” 呈现一幅唯美的东方诗意画卷" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo_ori/0/v3310sawk9m_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        01:09
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_today:title:月牙泉雪落“变装” 呈现一幅唯美的东方诗意画卷" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/v3310sawk9m.html" target="_blank" title="月牙泉雪落“变装” 呈现一幅唯美的东方诗意画卷">
        月牙泉雪落“变装” 呈现一幅唯美的东方诗意画卷
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_today:img:上戏00后女生京剧戏腔唱古风走红  回应：会坚持" class="figure" data-float="q331048o0q6" data-quickopen="true" href="https://v.qq.com/x/page/q331048o0q6.html" tabindex="-1" target="_blank">
       <img alt="上戏00后女生京剧戏腔唱古风走红  回应：会坚持" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo_ori/0/q331048o0q6_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        02:03
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_today:title:上戏00后女生京剧戏腔唱古风走红  回应：会坚持" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/q331048o0q6.html" target="_blank" title="上戏00后女生京剧戏腔唱古风走红  回应：会坚持">
        上戏00后女生京剧戏腔唱古风走红  回应：会坚持
       </a>
      </div>
     </div>
    </div>
   </div>
  </div>
  <div _expose="new_vs_originals" _wind="columnname=精选_原创精选&amp;controlname=new_vs_originals" class="mod_row_box" cur-page-num="0" data-context="1" data-istyle="109" has-next-page="false" id="new_vs_originals">
   <div class="mod_hd">
    <h2 class="mod_title">
     原创精选
    </h2>
    <div class="mod_author_tablist">
     <a class="author_item vcuid" href="//v.qq.com/biu/creator/home?vcuid=9000129926" target="_blank">
      <img alt="苏炳添" class="author_pic" loading="lazy" lz_src="//inews.gtimg.com/newsapp_ls/0/1853976421_200200/0" onerror="picerr(this,'a')" src="//puui.qpic.cn/vupload/0/common_blank.png/0"/>
      <span class="author_name">
       苏炳添
      </span>
     </a>
     <a class="author_item vcuid" href="//v.qq.com/biu/creator/home?vcuid=9000001492" target="_blank">
      <img alt="papi酱" class="author_pic" loading="lazy" lz_src="//inews.gtimg.com/newsapp_ls/0/107730335_100100/0" onerror="picerr(this,'a')" src="//puui.qpic.cn/vupload/0/common_blank.png/0"/>
      <span class="author_name">
       papi酱
      </span>
     </a>
     <a class="author_item vcuid" href="//v.qq.com/biu/creator/home?vcuid=9000007096" target="_blank">
      <img alt="李子柒" class="author_pic" loading="lazy" lz_src="//inews.gtimg.com/newsapp_ls/0/2726210789_200200/0" onerror="picerr(this,'a')" src="//puui.qpic.cn/vupload/0/common_blank.png/0"/>
      <span class="author_name">
       李子柒
      </span>
     </a>
     <a class="author_item vcuid" href="//v.qq.com/biu/creator/home?vcuid=9000021134" target="_blank">
      <img alt="维维啊" class="author_pic" loading="lazy" lz_src="//vpic.cms.qq.com/nj_vpic/507955747/1617791664736318185" onerror="picerr(this,'a')" src="//puui.qpic.cn/vupload/0/common_blank.png/0"/>
      <span class="author_name">
       维维啊
      </span>
     </a>
     <a class="author_item vcuid" href="//v.qq.com/biu/creator/home?vcuid=9000002516" target="_blank">
      <img alt="V小妞" class="author_pic" loading="lazy" lz_src="//vpic.cms.qq.com/nj_vpic/107251461/1618997016708063112" onerror="picerr(this,'a')" src="//puui.qpic.cn/vupload/0/common_blank.png/0"/>
      <span class="author_name">
       V小妞
      </span>
     </a>
     <a class="author_item vcuid" href="//v.qq.com/biu/creator/home?vcuid=9000125699" target="_blank">
      <img alt="相信音乐" class="author_pic" loading="lazy" lz_src="//vpic.cms.qq.com/nj_vpic/2761276255/1624601813322842778" onerror="picerr(this,'a')" src="//puui.qpic.cn/vupload/0/common_blank.png/0"/>
      <span class="author_name">
       相信音乐
      </span>
     </a>
    </div>
    <div class="mod_page_small">
     <button _stat="new_vs_originals:通栏功能区:上一页" class="btn_prev disabled" title="上一页" wind-click="100">
      <svg class="svg_icon svg_icon_prev" height="10" viewbox="0 0 6 10" width="6">
       <path d="M1.4 4.7L5 1M1.3 5.3L5 9" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="1.4">
       </path>
      </svg>
     </button>
     <span class="page_num" data-count="4" data-info="8 30" data-page="1">
      1/4
     </span>
     <button _stat="new_vs_originals:通栏功能区:下一页" class="btn_next" title="下一页" wind-click="100">
      <svg class="svg_icon svg_icon_next" height="10" viewbox="0 0 6 10" width="6">
       <path d="M4.6 4.7L1 1M4.7 5.3L1 9" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="1.4">
       </path>
      </svg>
     </button>
    </div>
   </div>
   <div class="mod_bd cf _quickopen _quickopen_duration">
    <div class="mod_figure mod_figure_h_default mod_figure_h_default_1row mod_figure_h_default mod_figure_scroll mod_figure_author" data-rowcount="8" data-rowlen="1">
     <div __wind="" class="list_item">
      <a _stat="new_vs_originals:img:KPL联赛S战队佛山GK欢乐探营：谁是队霸？" class="figure" data-float="w0041cl7900" href="https://v.qq.com/x/page/w0041cl7900.html" tabindex="-1" target="_blank">
       <img alt="KPL联赛S战队佛山GK欢乐探营：谁是队霸？" class="figure_pic" loading="lazy" onerror="picerr(this,'h')" src="//puui.qpic.cn/qqvideo_ori/0/w0041cl7900_360_204/0"/>
       <div class="figure_caption">
        19:55
       </div>
      </a>
      <a _stat="new_vs_originals:avatar:腾讯爱玩游戏" class="figure_author vcuid" href="//v.qq.com/biu/creator/home?vcuid=9000008839">
       <img alt="腾讯爱玩游戏" class="author_pic" loading="lazy" lz_src="//inews.gtimg.com/newsapp_ls/0/11577262435_200200/0"/>
       <span class="author_name">
        腾讯爱玩游戏
       </span>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_originals:title:KPL联赛S战队佛山GK欢乐探营：谁是队霸？" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/w0041cl7900.html" target="_blank" title="KPL联赛S战队佛山GK欢乐探营：谁是队霸？">
        KPL联赛S战队佛山GK欢乐探营：谁是队霸？
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_originals:img:迷妹专访×甘望星：参加盛典最期待晚上干饭" class="figure" data-float="g0041zeecjz" data-quickopen="true" href="https://v.qq.com/x/page/g0041zeecjz.html" tabindex="-1" target="_blank">
       <img alt="迷妹专访×甘望星：参加盛典最期待晚上干饭" class="figure_pic" loading="lazy" onerror="picerr(this,'h')" src="//puui.qpic.cn/media_img/lena/PICoxeicq_720_1280/0"/>
       <div class="figure_caption">
        02:35
       </div>
      </a>
      <a _stat="new_vs_originals:avatar:V小妞" class="figure_author vcuid" href="//v.qq.com/biu/creator/home?vcuid=9000002516">
       <img alt="V小妞" class="author_pic" loading="lazy" lz_src="//vpic.cms.qq.com/nj_vpic/107251461/1618997016708063112"/>
       <span class="author_name">
        V小妞
       </span>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_originals:title:迷妹专访×甘望星：参加盛典最期待晚上干饭" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/g0041zeecjz.html" target="_blank" title="迷妹专访×甘望星：参加盛典最期待晚上干饭">
        迷妹专访×甘望星：参加盛典最期待晚上干饭
       </a>
      </div>
     </div>
     <!--QQlive_FB_CAP_ss_yc_div AD begin...."l=QQlive_FB_CAP_ss_yc&log=off"-->
     <div class="l_qq_com" id="QQlive_FB_CAP_ss_yc" style="width:1px;height:1px;display:none;">
     </div>
     <!--QQlive_FB_CAP_ss_yc AD end -->
     <!--[if !IE]>|xGv00|f6a2fe4473afa0303ea6730116422cbf<![endif]-->
     <div __wind="" class="list_item">
      <a _stat="new_vs_originals:img:张若昀专访：安利冬日抗寒穿搭，分享旅游计划" class="figure" data-float="j33105fnth9" data-quickopen="true" href="https://v.qq.com/x/page/j33105fnth9.html" tabindex="-1" target="_blank">
       <img alt="张若昀专访：安利冬日抗寒穿搭，分享旅游计划" class="figure_pic" loading="lazy" onerror="picerr(this,'h')" src="//puui.qpic.cn/qqvideo_ori/0/j33105fnth9_360_204/0"/>
       <div class="figure_caption">
        02:13
       </div>
      </a>
      <a _stat="new_vs_originals:avatar:A咖时尚" class="figure_author vcuid" href="//v.qq.com/biu/creator/home?vcuid=9000003121">
       <img alt="A咖时尚" class="author_pic" loading="lazy" lz_src="//vpic.cms.qq.com/nj_vpic/227609002/1621333190990807698"/>
       <span class="author_name">
        A咖时尚
       </span>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_originals:title:张若昀专访：安利冬日抗寒穿搭，分享旅游计划" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/j33105fnth9.html" target="_blank" title="张若昀专访：安利冬日抗寒穿搭，分享旅游计划">
        张若昀专访：安利冬日抗寒穿搭，分享旅游计划
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_originals:img:鹿先森乐队 《一起跳支舞》不插电live" class="figure" data-float="l3311f3041e" data-quickopen="true" href="https://v.qq.com/x/page/l3311f3041e.html" tabindex="-1" target="_blank">
       <img alt="鹿先森乐队 《一起跳支舞》不插电live" class="figure_pic" loading="lazy" onerror="picerr(this,'h')" src="//puui.qpic.cn/media_img/lena/PICw86058_720_1280/0"/>
       <div class="figure_caption">
        02:55
       </div>
      </a>
      <a _stat="new_vs_originals:avatar:鹿先森" class="figure_author vcuid" href="//v.qq.com/biu/creator/home?vcuid=9000143929">
       <img alt="鹿先森" class="author_pic" loading="lazy" lz_src="//vpic.cms.qq.com/nj_vpic/484974243/1630376422892673180"/>
       <span class="author_name">
        鹿先森
       </span>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_originals:title:鹿先森乐队 《一起跳支舞》不插电live" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/l3311f3041e.html" target="_blank" title="鹿先森乐队 《一起跳支舞》不插电live">
        鹿先森乐队 《一起跳支舞》不插电live
       </a>
      </div>
     </div>
     <!--QQlive_SP_HP_R_rm_2017_div AD begin...."l=QQlive_SP_HP_R_rm_2017&log=off"-->
     <div class="l_qq_com" id="QQlive_SP_HP_R_rm_2017" style="display:none;">
     </div>
     <!--QQlive_SP_HP_R_rm_2017 AD end -->
     <!--[if !IE]>|xGv00|737ad7c990a69804c0aeacb5aec44c6c<![endif]-->
     <!--QQlive_SP_ZZSP_2017_div AD begin...."l=QQlive_SP_ZZSP_2017&log=off"-->
     <div class="l_qq_com" id="QQlive_SP_ZZSP_2017" style="width:240px;height:135px;display:none;">
     </div>
     <!--QQlive_SP_ZZSP_2017 AD end -->
     <!--[if !IE]>|xGv00|84ce96efa7d2c40294cbe2ccee97674e<![endif]-->
     <div __wind="" class="list_item">
      <a _stat="new_vs_originals:img:四象法则解析2022十二星座整体运势" class="figure" data-float="mzc002002c209d7" href="https://v.qq.com/x/cover/mzc002002c209d7.html" tabindex="-1" target="_blank">
       <img alt="四象法则解析2022十二星座整体运势" class="figure_pic" loading="lazy" onerror="picerr(this,'h')" src="//puui.qpic.cn/vcover_hz_pic/0/gu4b63v2hvzms6m/332"/>
       <div class="figure_caption">
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_originals:title:四象法则解析2022十二星座整体运势" class="figure_title figure_title_two_row" href="https://v.qq.com/x/cover/mzc002002c209d7.html" target="_blank" title="四象法则解析2022十二星座整体运势">
        四象法则解析2022十二星座整体运势
       </a>
       <div class="figure_desc" title="2022大师季·五福临门">
        2022大师季·五福临门
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_originals:img:国潮趣味之旅：三星堆奇幻礼物，在家也能考古" class="figure" data-float="b330622erk5" data-quickopen="true" href="https://v.qq.com/x/page/b330622erk5.html" tabindex="-1" target="_blank">
       <img alt="国潮趣味之旅：三星堆奇幻礼物，在家也能考古" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/media_img/lena/PIClww8sj_720_1280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        05:29
       </div>
      </a>
      <a _stat="new_vs_originals:avatar:网不红萌叔Joey" class="figure_author vcuid" href="//v.qq.com/biu/creator/home?vcuid=9000008405">
       <img alt="网不红萌叔Joey" class="author_pic" loading="lazy" lz_src="//inews.gtimg.com/newsapp_ls/0/8248239851_200200/0"/>
       <span class="author_name">
        网不红萌叔Joey
       </span>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_originals:title:国潮趣味之旅：三星堆奇幻礼物，在家也能考古" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/b330622erk5.html" target="_blank" title="国潮趣味之旅：三星堆奇幻礼物，在家也能考古">
        国潮趣味之旅：三星堆奇幻礼物，在家也能考古
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_originals:img:追忆童年！20部国内热播日本动画片主题曲来啦" class="figure" data-float="o3308lfa03l" href="https://v.qq.com/x/page/o3308lfa03l.html" tabindex="-1" target="_blank">
       <img alt="追忆童年！20部国内热播日本动画片主题曲来啦" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo_ori/0/o3308lfa03l_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        24:35
       </div>
      </a>
      <a _stat="new_vs_originals:avatar:音乐影视馆" class="figure_author vcuid" href="//v.qq.com/biu/creator/home?vcuid=9000156781">
       <img alt="音乐影视馆" class="author_pic" loading="lazy" lz_next="//image.video.qpic.cn/10010_2a552e-0_1831277258_1636018225076485"/>
       <span class="author_name">
        音乐影视馆
       </span>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_originals:title:追忆童年！20部国内热播日本动画片主题曲来啦" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/o3308lfa03l.html" target="_blank" title="追忆童年！20部国内热播日本动画片主题曲来啦">
        追忆童年！20部国内热播日本动画片主题曲来啦
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_originals:img:【2022大师季·五福临门】十二星座的最佳结婚时间" class="figure" data-float="mzc00200drvjuzi" href="https://v.qq.com/x/cover/mzc00200drvjuzi.html" tabindex="-1" target="_blank">
       <img alt="【2022大师季·五福临门】十二星座的最佳结婚时间" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_hz_pic/0/izc765j7x05qlgw/332" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_originals:title:【2022大师季·五福临门】十二星座的最佳结婚时间" class="figure_title figure_title_two_row" href="https://v.qq.com/x/cover/mzc00200drvjuzi.html" target="_blank" title="【2022大师季·五福临门】十二星座的最佳结婚时间">
        【2022大师季·五福临门】十二星座的最佳结婚时间
       </a>
       <div class="figure_desc" title="2022大师季·五福临门">
        2022大师季·五福临门
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_originals:img:【迷妹专访】×林子闳：第一次用浴霸被惊艳！" class="figure" data-float="p0041ziqbfe" href="https://v.qq.com/x/page/p0041ziqbfe.html" tabindex="-1" target="_blank">
       <img alt="【迷妹专访】×林子闳：第一次用浴霸被惊艳！" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/media_img/lena/PICpkdbex_720_1280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        16:01
       </div>
      </a>
      <a _stat="new_vs_originals:avatar:V小妞" class="figure_author vcuid" href="//v.qq.com/biu/creator/home?vcuid=9000002516">
       <img alt="V小妞" class="author_pic" loading="lazy" lz_next="//vpic.cms.qq.com/nj_vpic/107251461/1618997016708063112"/>
       <span class="author_name">
        V小妞
       </span>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_originals:title:【迷妹专访】×林子闳：第一次用浴霸被惊艳！" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/p0041ziqbfe.html" target="_blank" title="【迷妹专访】×林子闳：第一次用浴霸被惊艳！">
        【迷妹专访】×林子闳：第一次用浴霸被惊艳！
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_originals:img:听音乐会有哪些规矩？" class="figure" data-float="u3309iy88gm" href="https://v.qq.com/x/page/u3309iy88gm.html" tabindex="-1" target="_blank">
       <img alt="听音乐会有哪些规矩？" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo_ori/0/u3309iy88gm_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        15:49
       </div>
      </a>
      <a _stat="new_vs_originals:avatar:乐咖与乐渣" class="figure_author vcuid" href="//v.qq.com/biu/creator/home?vcuid=9000158974">
       <img alt="乐咖与乐渣" class="author_pic" loading="lazy" lz_next="//image.video.qpic.cn/10010_88b7d-37_1297652093_1636372536092600"/>
       <span class="author_name">
        乐咖与乐渣
       </span>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_originals:title:听音乐会有哪些规矩？" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/u3309iy88gm.html" target="_blank" title="听音乐会有哪些规矩？">
        听音乐会有哪些规矩？
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_originals:img:破防！谷蓝帝深情演唱《电露泡影》共情能力一级棒" class="figure" data-float="b0041pvdpna" data-quickopen="true" href="https://v.qq.com/x/page/b0041pvdpna.html" tabindex="-1" target="_blank">
       <img alt="破防！谷蓝帝深情演唱《电露泡影》共情能力一级棒" class="figure_pic" loading="lazy" lz_next="//vc.qpic.cn/tpic/mtvius5EwZK6j/tvius5Exbuv7.jpeg/250" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        04:37
       </div>
      </a>
      <a _stat="new_vs_originals:avatar:1平米演唱会" class="figure_author vcuid" href="//v.qq.com/biu/creator/home?vcuid=9000141556">
       <img alt="1平米演唱会" class="author_pic" loading="lazy" lz_next="//vpic.cms.qq.com/nj_vpic/2344102840/1630472910115580136/7008141807898707761"/>
       <span class="author_name">
        1平米演唱会
       </span>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_originals:title:破防！谷蓝帝深情演唱《电露泡影》共情能力一级棒" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/b0041pvdpna.html" target="_blank" title="破防！谷蓝帝深情演唱《电露泡影》共情能力一级棒">
        破防！谷蓝帝深情演唱《电露泡影》共情能力一级棒
       </a>
       <div class="figure_desc" title="谷蓝帝唱《电露泡影》，共情又好哭">
        谷蓝帝唱《电露泡影》，共情又好哭
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_originals:img:鹅选优品母婴节优质作品展播" class="figure" data-float="mzc002008da7704" href="https://v.qq.com/x/cover/mzc002008da7704.html" tabindex="-1" target="_blank">
       <img alt="鹅选优品母婴节优质作品展播" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_hz_pic/0/mzc002008da77041636946858746/332" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_originals:title:鹅选优品母婴节优质作品展播" class="figure_title figure_title_two_row" href="https://v.qq.com/x/cover/mzc002008da7704.html" target="_blank" title="鹅选优品母婴节优质作品展播">
        鹅选优品母婴节优质作品展播
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_originals:img:超新星现场直击9:奥斯卡姚琛互放狠话" class="figure" data-float="p3307pi80am" data-quickopen="true" href="https://v.qq.com/x/page/p3307pi80am.html" tabindex="-1" target="_blank">
       <img alt="超新星现场直击9:奥斯卡姚琛互放狠话" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/media_img/lena/PIC1837u5_720_1280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        00:52
       </div>
      </a>
      <a _stat="new_vs_originals:avatar:一只打工鹅" class="figure_author vcuid" href="//v.qq.com/biu/creator/home?vcuid=9000152269">
       <img alt="一只打工鹅" class="author_pic" loading="lazy" lz_next="//image.video.qpic.cn/10010_88b7d-32_1406515174_1634539599405040"/>
       <span class="author_name">
        一只打工鹅
       </span>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_originals:title:超新星现场直击9:奥斯卡姚琛互放狠话" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/p3307pi80am.html" target="_blank" title="超新星现场直击9:奥斯卡姚琛互放狠话">
        超新星现场直击9:奥斯卡姚琛互放狠话
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_originals:img:白色音浪 | 户冢优斗：教练，我想滑雪！" class="figure" data-float="s0041tgvygm" data-quickopen="true" href="https://v.qq.com/x/page/s0041tgvygm.html" tabindex="-1" target="_blank">
       <img alt="白色音浪 | 户冢优斗：教练，我想滑雪！" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo_ori/0/s0041tgvygm_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        04:25
       </div>
      </a>
      <a _stat="new_vs_originals:avatar:腾讯冰雪" class="figure_author vcuid" href="//v.qq.com/biu/creator/home?vcuid=9000118809">
       <img alt="腾讯冰雪" class="author_pic" loading="lazy" lz_next="//image.video.qpic.cn/10010_88b7d-10_629700710_1623107561766833"/>
       <span class="author_name">
        腾讯冰雪
       </span>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_originals:title:白色音浪 | 户冢优斗：教练，我想滑雪！" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/s0041tgvygm.html" target="_blank" title="白色音浪 | 户冢优斗：教练，我想滑雪！">
        白色音浪 | 户冢优斗：教练，我想滑雪！
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_originals:img:靳东：为了《突围》放弃了很多自己的坚持" class="figure" data-float="v3306t76kj7" data-quickopen="true" href="https://v.qq.com/x/page/v3306t76kj7.html" tabindex="-1" target="_blank">
       <img alt="靳东：为了《突围》放弃了很多自己的坚持" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo_ori/0/v3306t76kj7_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        07:35
       </div>
      </a>
      <a _stat="new_vs_originals:avatar:入戏" class="figure_author vcuid" href="//v.qq.com/biu/creator/home?vcuid=9000007180">
       <img alt="入戏" class="author_pic" loading="lazy" lz_next="//vpic.cms.qq.com/nj_vpic/708031180/1621499230413091963"/>
       <span class="author_name">
        入戏
       </span>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_originals:title:靳东：为了《突围》放弃了很多自己的坚持" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/v3306t76kj7.html" target="_blank" title="靳东：为了《突围》放弃了很多自己的坚持">
        靳东：为了《突围》放弃了很多自己的坚持
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_originals:img:水果星球逛水果园挑战一触即发，用魔法打败魔法" class="figure" data-float="k0040tazml1" data-quickopen="true" href="https://v.qq.com/x/page/k0040tazml1.html" tabindex="-1" target="_blank">
       <img alt="水果星球逛水果园挑战一触即发，用魔法打败魔法" class="figure_pic" loading="lazy" lz_next="//vc.qpic.cn/tpic/mtviupSqYBJFj/tviupSqYNu67.jpeg/250" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        08:06
       </div>
      </a>
      <a _stat="new_vs_originals:avatar:腾讯视频doki" class="figure_author vcuid" href="//v.qq.com/biu/creator/home?vcuid=9000008166">
       <img alt="腾讯视频doki" class="author_pic" loading="lazy" lz_next="//image.video.qpic.cn/10010_88b7d-11_1654235270_1622794362995400"/>
       <span class="author_name">
        腾讯视频doki
       </span>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_originals:title:水果星球逛水果园挑战一触即发，用魔法打败魔法" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/k0040tazml1.html" target="_blank" title="水果星球逛水果园挑战一触即发，用魔法打败魔法">
        水果星球逛水果园挑战一触即发，用魔法打败魔法
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_originals:img:当HR问：你目前有几个Offer？该怎么回答" class="figure" data-float="v3303ffkce2" data-quickopen="true" href="https://v.qq.com/x/page/v3303ffkce2.html" tabindex="-1" target="_blank">
       <img alt="当HR问：你目前有几个Offer？该怎么回答" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo_ori/0/v3303ffkce2_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        02:32
       </div>
      </a>
      <a _stat="new_vs_originals:avatar:智联招聘" class="figure_author vcuid" href="//v.qq.com/biu/creator/home?vcuid=9000140203">
       <img alt="智联招聘" class="author_pic" loading="lazy" lz_next="//vpic.cms.qq.com/nj_vpic/360169105/1629276438279152616"/>
       <span class="author_name">
        智联招聘
       </span>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_originals:title:当HR问：你目前有几个Offer？该怎么回答" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/v3303ffkce2.html" target="_blank" title="当HR问：你目前有几个Offer？该怎么回答">
        当HR问：你目前有几个Offer？该怎么回答
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_originals:img:麦玲玲：2022年娱乐圈运势大揭秘" class="figure" data-float="v0040zlyg2f" href="https://v.qq.com/x/page/v0040zlyg2f.html" tabindex="-1" target="_blank">
       <img alt="麦玲玲：2022年娱乐圈运势大揭秘" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo_ori/0/v0040zlyg2f_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        42:51
       </div>
      </a>
      <a _stat="new_vs_originals:avatar:呦呦星座运势" class="figure_author" href="https://v.qq.com/s/videoplus/2205943810">
       <img alt="呦呦星座运势" class="author_pic" loading="lazy" lz_next="//inews.gtimg.com/newsapp_ls/0/12144057197_200200/0"/>
       <span class="author_name">
        呦呦星座运势
       </span>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_originals:title:麦玲玲：2022年娱乐圈运势大揭秘" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/v0040zlyg2f.html" target="_blank" title="麦玲玲：2022年娱乐圈运势大揭秘">
        麦玲玲：2022年娱乐圈运势大揭秘
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_originals:img:《迷妹专访》×任豪：在线改写卓文远结局" class="figure" data-float="p00401tli3d" href="https://v.qq.com/x/page/p00401tli3d.html" tabindex="-1" target="_blank">
       <img alt="《迷妹专访》×任豪：在线改写卓文远结局" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/media_img/lena/PICfg2cq6_720_1280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        15:34
       </div>
      </a>
      <a _stat="new_vs_originals:avatar:V小妞" class="figure_author vcuid" href="//v.qq.com/biu/creator/home?vcuid=9000002516">
       <img alt="V小妞" class="author_pic" loading="lazy" lz_next="//vpic.cms.qq.com/nj_vpic/107251461/1618997016708063112"/>
       <span class="author_name">
        V小妞
       </span>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_originals:title:《迷妹专访》×任豪：在线改写卓文远结局" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/p00401tli3d.html" target="_blank" title="《迷妹专访》×任豪：在线改写卓文远结局">
        《迷妹专访》×任豪：在线改写卓文远结局
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_originals:img:专访北京致知学校创校校长张晔：时光不语，静待花开" class="figure" data-float="k0040bm8tf7" href="https://v.qq.com/x/page/k0040bm8tf7.html" tabindex="-1" target="_blank">
       <img alt="专访北京致知学校创校校长张晔：时光不语，静待花开" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo_ori/0/k0040bm8tf7_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        19:32
       </div>
      </a>
      <a _stat="new_vs_originals:avatar:鹅老师课堂" class="figure_author vcuid" href="//v.qq.com/biu/creator/home?vcuid=9000011446">
       <img alt="鹅老师课堂" class="author_pic" loading="lazy" lz_next="//inews.gtimg.com/newsapp_ls/0/11467634255_200200/0"/>
       <span class="author_name">
        鹅老师课堂
       </span>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_originals:title:专访北京致知学校创校校长张晔：时光不语，静待花开" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/k0040bm8tf7.html" target="_blank" title="专访北京致知学校创校校长张晔：时光不语，静待花开">
        专访北京致知学校创校校长张晔：时光不语，静待花开
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_originals:img:为什么国外叫宇航员，我们叫航天员呢" class="figure" data-float="y3302ogb9e7" data-quickopen="true" href="https://v.qq.com/x/page/y3302ogb9e7.html" tabindex="-1" target="_blank">
       <img alt="为什么国外叫宇航员，我们叫航天员呢" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo_ori/0/y3302ogb9e7_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        01:11
       </div>
      </a>
      <a _stat="new_vs_originals:avatar:米粒计划" class="figure_author vcuid" href="//v.qq.com/biu/creator/home?vcuid=9000005059">
       <img alt="米粒计划" class="author_pic" loading="lazy" lz_next="//vpic.cms.qq.com/nj_vpic/383948866/1617668991680168786"/>
       <span class="author_name">
        米粒计划
       </span>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_originals:title:为什么国外叫宇航员，我们叫航天员呢" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/y3302ogb9e7.html" target="_blank" title="为什么国外叫宇航员，我们叫航天员呢">
        为什么国外叫宇航员，我们叫航天员呢
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_originals:img:烧鹅·学霸组合 有被牛骏峰阅片量惊讶到！" class="figure" data-float="d0041oz85mx" data-quickopen="true" href="https://v.qq.com/x/page/d0041oz85mx.html" tabindex="-1" target="_blank">
       <img alt="烧鹅·学霸组合 有被牛骏峰阅片量惊讶到！" class="figure_pic" loading="lazy" lz_next="//vfiles.gtimg.cn/vupload/20211109/c1fd321636432378096.png" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        00:25
       </div>
      </a>
      <a _stat="new_vs_originals:avatar:深井烧鹅" class="figure_author vcuid" href="//v.qq.com/biu/creator/home?vcuid=9000008832">
       <img alt="深井烧鹅" class="author_pic" loading="lazy" lz_next="//vpic.cms.qq.com/nj_vpic/1226982338/1617860066496939108"/>
       <span class="author_name">
        深井烧鹅
       </span>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_originals:title:烧鹅·学霸组合 有被牛骏峰阅片量惊讶到！" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/d0041oz85mx.html" target="_blank" title="烧鹅·学霸组合 有被牛骏峰阅片量惊讶到！">
        烧鹅·学霸组合 有被牛骏峰阅片量惊讶到！
       </a>
       <div class="figure_desc" title="学霸发言！有被牛骏峰的阅片量惊讶到~">
        学霸发言！有被牛骏峰的阅片量惊讶到~
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_originals:img:最近大火的4首歌，随便一首播放量都轻松过亿" class="figure" data-float="b3302020iwy" data-quickopen="true" href="https://v.qq.com/x/page/b3302020iwy.html" tabindex="-1" target="_blank">
       <img alt="最近大火的4首歌，随便一首播放量都轻松过亿" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo_ori/0/b3302020iwy_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        04:07
       </div>
      </a>
      <a _stat="new_vs_originals:avatar:Music郑在看" class="figure_author vcuid" href="//v.qq.com/biu/creator/home?vcuid=9000009313">
       <img alt="Music郑在看" class="author_pic" loading="lazy" lz_next="//vpic.cms.qq.com/nj_vpic/1271111325/1617936442761067782"/>
       <span class="author_name">
        Music郑在看
       </span>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_originals:title:最近大火的4首歌，随便一首播放量都轻松过亿" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/b3302020iwy.html" target="_blank" title="最近大火的4首歌，随便一首播放量都轻松过亿">
        最近大火的4首歌，随便一首播放量都轻松过亿
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_originals:img:【半佛】酒店的卫生问题，是一种必然。" class="figure" data-float="a3301dn3gf9" data-quickopen="true" href="https://v.qq.com/x/page/a3301dn3gf9.html" tabindex="-1" target="_blank">
       <img alt="【半佛】酒店的卫生问题，是一种必然。" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo_ori/0/a3301dn3gf9_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        10:03
       </div>
      </a>
      <a _stat="new_vs_originals:avatar:半佛仙人" class="figure_author vcuid" href="//v.qq.com/biu/creator/home?vcuid=9000003897">
       <img alt="半佛仙人" class="author_pic" loading="lazy" lz_next="//vpic.cms.qq.com/nj_vpic/334414751/1618408573671818870"/>
       <span class="author_name">
        半佛仙人
       </span>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_originals:title:【半佛】酒店的卫生问题，是一种必然。" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/a3301dn3gf9.html" target="_blank" title="【半佛】酒店的卫生问题，是一种必然。">
        【半佛】酒店的卫生问题，是一种必然。
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_originals:img:宋词还能这样唱？纯人声演绎欧阳修《蝶恋花》" class="figure" data-float="r3275ex9c30" data-quickopen="true" href="https://v.qq.com/x/page/r3275ex9c30.html" tabindex="-1" target="_blank">
       <img alt="宋词还能这样唱？纯人声演绎欧阳修《蝶恋花》" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo_ori/0/r3275ex9c30_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        02:39
       </div>
      </a>
      <a _stat="new_vs_originals:avatar:寻声人声乐团" class="figure_author vcuid" href="//v.qq.com/biu/creator/home?vcuid=9000002755">
       <img alt="寻声人声乐团" class="author_pic" loading="lazy" lz_next="//vpic.cms.qq.com/nj_vpic/152482306/1619237085322446473"/>
       <span class="author_name">
        寻声人声乐团
       </span>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_originals:title:宋词还能这样唱？纯人声演绎欧阳修《蝶恋花》" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/r3275ex9c30.html" target="_blank" title="宋词还能这样唱？纯人声演绎欧阳修《蝶恋花》">
        宋词还能这样唱？纯人声演绎欧阳修《蝶恋花》
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_originals:img:小魔侦探苦苦寻找，终于发现八戒踪迹" class="figure" data-float="r3276dtj1wv" data-quickopen="true" href="https://v.qq.com/x/page/r3276dtj1wv.html" tabindex="-1" target="_blank">
       <img alt="小魔侦探苦苦寻找，终于发现八戒踪迹" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/media_img/lena/PICkzbamh_304_540/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        01:16
       </div>
      </a>
      <a _stat="new_vs_originals:avatar:小魔姐" class="figure_author vcuid" href="//v.qq.com/biu/creator/home?vcuid=9000014976">
       <img alt="小魔姐" class="author_pic" loading="lazy" lz_next="//image.video.qpic.cn/10010_2a552e-1_390751283_1618018328320904"/>
       <span class="author_name">
        小魔姐
       </span>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_originals:title:小魔侦探苦苦寻找，终于发现八戒踪迹" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/r3276dtj1wv.html" target="_blank" title="小魔侦探苦苦寻找，终于发现八戒踪迹">
        小魔侦探苦苦寻找，终于发现八戒踪迹
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_originals:img:露大腿逛寺庙，这些“佛媛”网红脸都不要了？" class="figure" data-float="n3275swfsh2" data-quickopen="true" href="https://v.qq.com/x/page/n3275swfsh2.html" tabindex="-1" target="_blank">
       <img alt="露大腿逛寺庙，这些“佛媛”网红脸都不要了？" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo_ori/0/n3275swfsh2_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        02:27
       </div>
      </a>
      <a _stat="new_vs_originals:avatar:韩笑半步癫" class="figure_author vcuid" href="//v.qq.com/biu/creator/home?vcuid=9000109245">
       <img alt="韩笑半步癫" class="author_pic" loading="lazy" lz_next="//tvpic.gtimg.cn/head/531540604c12c4fbaa89a9820e5d788a12047b7311f5ef71e5cc1b1a9a0cd10265ad2b03/271"/>
       <span class="author_name">
        韩笑半步癫
       </span>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_originals:title:露大腿逛寺庙，这些“佛媛”网红脸都不要了？" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/n3275swfsh2.html" target="_blank" title="露大腿逛寺庙，这些“佛媛”网红脸都不要了？">
        露大腿逛寺庙，这些“佛媛”网红脸都不要了？
       </a>
      </div>
     </div>
    </div>
   </div>
  </div>
  <script>
   clearTimeout(window.emptyPageTimer)
  </script>
  <div _expose="multi_feed_V" _wind="columnname=精选_热点短视频&amp;controlname=multi_feed_V" class="mod_row_box" cur-page-num="0" data-context="2" data-istyle="48" has-next-page="false" id="multi_feed_V">
   <div class="mod_hd">
    <h2 class="mod_title">
     <a _stat="multi_feed_V:通栏功能区:通栏标题" class="title_link" data-target="_blank" href=" https://v.qq.com/channel/feeds_hotspot">
      热点短视频
     </a>
    </h2>
    <div class="mod_title_tabs">
     <button _stat="multi_feed_V:通栏功能区:通栏标题tab:为你推荐" class="tab_item tab_item_0 current" data-content="10" data-seq="0" data-type="为你推荐" wind-click="500">
      为你推荐
     </button>
     <button _stat="multi_feed_V:通栏功能区:通栏标题tab:军事" class="tab_item tab_item_1" data-content="10" data-seq="1" data-type="军事" wind-click="500">
      军事
     </button>
     <button _stat="multi_feed_V:通栏功能区:通栏标题tab:搞笑" class="tab_item tab_item_2" data-content="10" data-seq="2" data-type="搞笑" wind-click="500">
      搞笑
     </button>
     <button _stat="multi_feed_V:通栏功能区:通栏标题tab:艺术" class="tab_item tab_item_3" data-content="10" data-seq="3" data-type="艺术" wind-click="500">
      艺术
     </button>
    </div>
    <div class="mod_page_small none">
     <button _stat="multi_feed_V:通栏功能区:上一页" class="btn_prev disabled" title="上一页" wind-click="100">
      <svg class="svg_icon svg_icon_prev" height="10" viewbox="0 0 6 10" width="6">
       <path d="M1.4 4.7L5 1M1.3 5.3L5 9" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="1.4">
       </path>
      </svg>
     </button>
     <span class="page_num" data-count="1" data-info="10 9" data-page="1">
      1/1
     </span>
     <button _stat="multi_feed_V:通栏功能区:下一页" class="btn_next" title="下一页" wind-click="100">
      <svg class="svg_icon svg_icon_next" height="10" viewbox="0 0 6 10" width="6">
       <path d="M4.6 4.7L1 1M4.7 5.3L1 9" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="1.4">
       </path>
      </svg>
     </button>
    </div>
   </div>
   <div class="mod_bd cf">
    <div class="mod_figure_1fp2r">
     <div class="mod_focus_player" data-multi="_multi_feed_V_data">
      <div class="mod_player" data-autopause="1" data-id="a3150exlzrz" data-need-tab-ctrl="1" data-title="怀孕三个月去医院做产检需要注意什么？ 记得这项检查最重要" data-triggerplay="1" data-url="https://v.qq.com/x/page/a3150exlzrz.html" id="mod_player_multi_feed_V">
      </div>
      <div class="fp_player_title">
       <a class="title_link" data-target="_blank" href="javascript:;">
       </a>
      </div>
      <div class="fp_playlist __playlist" id="mod_player_multi_feed_V_tab">
       <div class="fp_playlist_inner">
        <a _stat="multi_feed_V:播放列表:怀孕三个月去医院做产检需要注意什么？ 记得这项检查最重要" class="item item_0 item_a3150exlzrz current" data-url="https://v.qq.com/x/page/a3150exlzrz.html" data-vid="a3150exlzrz" href="https://v.qq.com/x/page/a3150exlzrz.html">
         <span class="title" title="怀孕三个月去医院做产检需要注意什么？ 记得这项检查最重要">
          怀孕三个月去医院做产检需要注意什么？ 记得这项检查最重要
         </span>
         <span class="desc">
         </span>
        </a>
        <a _stat="multi_feed_V:播放列表:《仲夏满天心》人间自恋靳泽一！自信满满的画风也太欠了" class="item item_1 item_o3145vnfjyy" data-url="https://v.qq.com/x/page/o3145vnfjyy.html" data-vid="o3145vnfjyy" href="https://v.qq.com/x/page/o3145vnfjyy.html">
         <span class="title" title="《仲夏满天心》人间自恋靳泽一！自信满满的画风也太欠了">
          《仲夏满天心》人间自恋靳泽一！自信满满的画风也太欠了
         </span>
         <span class="desc">
         </span>
        </a>
        <a _stat="multi_feed_V:播放列表:走错片场？当《乡村爱情》谢广坤来到大明，略带喜感却气场全开" class="item item_2 item_v3052r25qi6" data-url="https://v.qq.com/x/page/v3052r25qi6.html" data-vid="v3052r25qi6" href="https://v.qq.com/x/page/v3052r25qi6.html">
         <span class="title" title="走错片场？当《乡村爱情》谢广坤来到大明，略带喜感却气场全开">
          走错片场？当《乡村爱情》谢广坤来到大明，略带喜感却气场全开
         </span>
         <span class="desc">
         </span>
        </a>
        <a _stat="multi_feed_V:播放列表:【鹿晗X吴磊】穿越火线 sold out 这么帅的第一次见吧" class="item item_3 item_h313448akr0" data-url="https://v.qq.com/x/page/h313448akr0.html" data-vid="h313448akr0" href="https://v.qq.com/x/page/h313448akr0.html">
         <span class="title" title="【鹿晗X吴磊】穿越火线 sold out 这么帅的第一次见吧">
          【鹿晗X吴磊】穿越火线 sold out 这么帅的第一次见吧
         </span>
         <span class="desc">
         </span>
        </a>
        <a _stat="multi_feed_V:播放列表:唐老鸭拆汪汪队立大功奇趣蛋 开心宝贝出奇蛋" class="item item_4 item_j0502qo91fm" data-url="https://v.qq.com/x/page/j0502qo91fm.html" data-vid="j0502qo91fm" href="https://v.qq.com/x/page/j0502qo91fm.html">
         <span class="title" title="唐老鸭拆汪汪队立大功奇趣蛋 开心宝贝出奇蛋">
          唐老鸭拆汪汪队立大功奇趣蛋 开心宝贝出奇蛋
         </span>
         <span class="desc">
         </span>
        </a>
        <a _stat="multi_feed_V:播放列表:Roblox杀手模拟器：学会新技能！可毫无用武之地！小飞象解说" class="item item_5 item_k0967pcznzt" data-url="https://v.qq.com/x/page/k0967pcznzt.html" data-vid="k0967pcznzt" href="https://v.qq.com/x/page/k0967pcznzt.html">
         <span class="title" title="Roblox杀手模拟器：学会新技能！可毫无用武之地！小飞象解说">
          Roblox杀手模拟器：学会新技能！可毫无用武之地！小飞象解说
         </span>
         <span class="desc">
         </span>
        </a>
        <a _stat="multi_feed_V:播放列表:董力厨房手忙脚乱，什么都找不到大喊“救命”" class="item item_6 item_c0033m9y8r9" data-url="https://v.qq.com/x/page/c0033m9y8r9.html" data-vid="c0033m9y8r9" href="https://v.qq.com/x/page/c0033m9y8r9.html">
         <span class="title" title="董力厨房手忙脚乱，什么都找不到大喊“救命”">
          董力厨房手忙脚乱，什么都找不到大喊“救命”
         </span>
         <span class="desc">
         </span>
        </a>
        <a _stat="multi_feed_V:播放列表:老板：“想去摩旅？这个火龙果先给我雕刻出98块的样子！”" class="item item_7 item_r093509hghi" data-url="https://v.qq.com/x/page/r093509hghi.html" data-vid="r093509hghi" href="https://v.qq.com/x/page/r093509hghi.html">
         <span class="title" title="老板：“想去摩旅？这个火龙果先给我雕刻出98块的样子！”">
          老板：“想去摩旅？这个火龙果先给我雕刻出98块的样子！”
         </span>
         <span class="desc">
         </span>
        </a>
        <a _stat="multi_feed_V:播放列表:为啥一到凌晨3、4点就“自然醒”？或是这几种疾病在作祟" class="item item_8 item_d3224crs1zu" data-url="https://v.qq.com/x/page/d3224crs1zu.html" data-vid="d3224crs1zu" href="https://v.qq.com/x/page/d3224crs1zu.html">
         <span class="title" title="为啥一到凌晨3、4点就“自然醒”？或是这几种疾病在作祟">
          为啥一到凌晨3、4点就“自然醒”？或是这几种疾病在作祟
         </span>
         <span class="desc">
         </span>
        </a>
        <a _stat="multi_feed_V:播放列表:用星座的方式打开《花不弃》这俩货相似程度99+" class="item item_9 item_j0840bazfu1" data-url="https://v.qq.com/x/page/j0840bazfu1.html" data-vid="j0840bazfu1" href="https://v.qq.com/x/page/j0840bazfu1.html">
         <span class="title" title="用星座的方式打开《花不弃》这俩货相似程度99+">
          用星座的方式打开《花不弃》这俩货相似程度99+
         </span>
         <span class="desc">
         </span>
        </a>
       </div>
       <div class="fp_switch">
        <svg class="svg_icon svg_icon_switch" height="13" viewbox="0 0 8 13" width="8">
         <path class="svg_path_prev" d="M1.5 6.5L7 12M1.5 6.5L7 1" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="2">
         </path>
         <path class="svg_path_next" d="M6.5 6.5L1 1M6.5 6.5L1 12" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="2">
         </path>
        </svg>
       </div>
      </div>
      <script id="_multi_feed_V_data" type="text">
       [
 [
  {
   "vid": "a3150exlzrz",
   "title": "怀孕三个月去医院做产检需要注意什么？ 记得这项检查最重要",
   "second_title": "",
   "url": "https://v.qq.com/x/page/a3150exlzrz.html",
   "pic": "//puui.qpic.cn/qqvideo/0/a3150exlzrz/332"
  },
  {
   "vid": "o3145vnfjyy",
   "title": "《仲夏满天心》人间自恋靳泽一！自信满满的画风也太欠了",
   "second_title": "",
   "url": "https://v.qq.com/x/page/o3145vnfjyy.html",
   "pic": "//puui.qpic.cn/qqvideo/0/o3145vnfjyy/332"
  },
  {
   "vid": "v3052r25qi6",
   "title": "走错片场？当《乡村爱情》谢广坤来到大明，略带喜感却气场全开",
   "second_title": "",
   "url": "https://v.qq.com/x/page/v3052r25qi6.html",
   "pic": "//puui.qpic.cn/qqvideo/0/v3052r25qi6/332"
  },
  {
   "vid": "h313448akr0",
   "title": "【鹿晗X吴磊】穿越火线 sold out 这么帅的第一次见吧",
   "second_title": "",
   "url": "https://v.qq.com/x/page/h313448akr0.html",
   "pic": "//puui.qpic.cn/qqvideo/0/h313448akr0/332"
  },
  {
   "vid": "j0502qo91fm",
   "title": "唐老鸭拆汪汪队立大功奇趣蛋 开心宝贝出奇蛋",
   "second_title": "",
   "url": "https://v.qq.com/x/page/j0502qo91fm.html",
   "pic": "//puui.qpic.cn/qqvideo/0/j0502qo91fm/332"
  },
  {
   "vid": "k0967pcznzt",
   "title": "Roblox杀手模拟器：学会新技能！可毫无用武之地！小飞象解说",
   "second_title": "",
   "url": "https://v.qq.com/x/page/k0967pcznzt.html",
   "pic": "//puui.qpic.cn/qqvideo/0/k0967pcznzt/332"
  },
  {
   "vid": "c0033m9y8r9",
   "title": "董力厨房手忙脚乱，什么都找不到大喊“救命”",
   "second_title": "",
   "url": "https://v.qq.com/x/page/c0033m9y8r9.html",
   "pic": "//puui.qpic.cn/qqvideo/0/c0033m9y8r9/332"
  },
  {
   "vid": "r093509hghi",
   "title": "老板：“想去摩旅？这个火龙果先给我雕刻出98块的样子！”",
   "second_title": "",
   "url": "https://v.qq.com/x/page/r093509hghi.html",
   "pic": "//puui.qpic.cn/qqvideo/0/r093509hghi/332"
  },
  {
   "vid": "d3224crs1zu",
   "title": "为啥一到凌晨3、4点就“自然醒”？或是这几种疾病在作祟",
   "second_title": "",
   "url": "https://v.qq.com/x/page/d3224crs1zu.html",
   "pic": "//puui.qpic.cn/qqvideo/0/d3224crs1zu/332"
  },
  {
   "vid": "j0840bazfu1",
   "title": "用星座的方式打开《花不弃》这俩货相似程度99+",
   "second_title": "",
   "url": "https://v.qq.com/x/page/j0840bazfu1.html",
   "pic": "//puui.qpic.cn/qqvideo/0/j0840bazfu1/332"
  }
 ],
 [
  {
   "vid": "y0034pjasob",
   "title": "赵粤变了！这次狠话超霸气，彻底撕掉“不敢”的标签",
   "second_title": "赵粤承载队友的梦想霸气发言，超敢！",
   "url": "https://v.qq.com/x/page/y0034pjasob.html",
   "pic": "//puui.qpic.cn/qqvideo/0/y0034pjasob/332"
  },
  {
   "vid": "y3227gq80fo",
   "title": "5种疾病，腹部症状像胃痛，需要仔细辨别",
   "second_title": "",
   "url": "https://v.qq.com/x/page/y3227gq80fo.html",
   "pic": "//puui.qpic.cn/qqvideo/0/y3227gq80fo/332"
  },
  {
   "vid": "q3209w7nojw",
   "title": "贾玲爆笑空降《相遇别离》，霸总严谨又被俘获了！",
   "second_title": "",
   "url": "https://v.qq.com/x/page/q3209w7nojw.html",
   "pic": "//puui.qpic.cn/qqvideo/0/q3209w7nojw/332"
  },
  {
   "vid": "j09516x2kgh",
   "title": "中风来临前，通常会有3个“前兆信号”，越早发现越好",
   "second_title": "",
   "url": "https://v.qq.com/x/page/j09516x2kgh.html",
   "pic": "//puui.qpic.cn/qqvideo/0/j09516x2kgh/332"
  },
  {
   "vid": "o3159jd4esl",
   "title": "迷你世界奥特曼：抵御野人袭击，但是野人去哪里了？",
   "second_title": "",
   "url": "https://v.qq.com/x/page/o3159jd4esl.html",
   "pic": "//puui.qpic.cn/qqvideo/0/o3159jd4esl/332"
  },
  {
   "vid": "v0954uasxlz",
   "title": "女仆罢工哄不回来，那就再召唤一个吧！",
   "second_title": "",
   "url": "https://v.qq.com/x/page/v0954uasxlz.html",
   "pic": "//puui.qpic.cn/qqvideo/0/v0954uasxlz/332"
  },
  {
   "vid": "a3070br60y0",
   "title": "第1次玩里里家铁盒史莱姆，手感果然名不虚传！就味道有点上头？",
   "second_title": "【HowTo】教你玩转铁盒史莱姆，手感名不虚传，来看看吧",
   "url": "https://v.qq.com/x/page/a3070br60y0.html",
   "pic": "//puui.qpic.cn/qqvideo/0/a3070br60y0/332"
  },
  {
   "vid": "d0854lzmk7q",
   "title": "《Tinrry+》Tinrry教你做青团",
   "second_title": "",
   "url": "https://v.qq.com/x/page/d0854lzmk7q.html",
   "pic": "//puui.qpic.cn/qqvideo/0/d0854lzmk7q/332"
  },
  {
   "vid": "u0895j7eomo",
   "title": "我的世界：滑稽世界模组！有变成墨鱼的萌妹，还有蹦迪的BOSS",
   "second_title": "",
   "url": "https://v.qq.com/x/page/u0895j7eomo.html",
   "pic": "//puui.qpic.cn/qqvideo/0/u0895j7eomo/332"
  },
  {
   "vid": "r07239gid8n",
   "title": "王者荣耀更新：六神装赵云vs典韦！新的版本之帝诞生了",
   "second_title": "",
   "url": "https://v.qq.com/x/page/r07239gid8n.html",
   "pic": "//puui.qpic.cn/qqvideo/0/r07239gid8n/332"
  }
 ],
 [
  {
   "vid": "b3256l5ttup",
   "title": "喜剧小品《多大点事》：妻子怀孕老公却检查出不能生，笑料不断",
   "second_title": "",
   "url": "https://v.qq.com/x/page/b3256l5ttup.html",
   "pic": "//puui.qpic.cn/qqvideo/0/b3256l5ttup/332"
  },
  {
   "vid": "x3266as5qkz",
   "title": "搞笑歌曲改编，有钱就是好，家里红旗不倒外面彩旗飘",
   "second_title": "",
   "url": "https://v.qq.com/x/page/x3266as5qkz.html",
   "pic": "//puui.qpic.cn/qqvideo/0/x3266as5qkz/332"
  },
  {
   "vid": "i32600q07fi",
   "title": "你们在宿舍中遇到过什么奇葩室友？简直要奔溃！",
   "second_title": "",
   "url": "https://v.qq.com/x/page/i32600q07fi.html",
   "pic": "//puui.qpic.cn/qqvideo/0/i32600q07fi/332"
  },
  {
   "vid": "p3249shyvfx",
   "title": "赵本山罕见笑场名场面，宋小宝一个字让赵本山忍不住，直接笑场停不下！ #鹅创剪辑大赏 第二阶段#",
   "second_title": "",
   "url": "https://v.qq.com/x/page/p3249shyvfx.html",
   "pic": "//puui.qpic.cn/qqvideo/0/p3249shyvfx/332"
  },
  {
   "vid": "c0616e81a57",
   "title": "雷军：小米十个季度将回归国内第一！我看没那么容易",
   "second_title": "",
   "url": "https://v.qq.com/x/page/c0616e81a57.html",
   "pic": "//puui.qpic.cn/qqvideo/0/c0616e81a57/332"
  },
  {
   "vid": "d0910divqys",
   "title": "你最想对前男友说什么？妹子回答句句扎心，很真实",
   "second_title": "",
   "url": "https://v.qq.com/x/page/d0910divqys.html",
   "pic": "//puui.qpic.cn/qqvideo/0/d0910divqys/332"
  },
  {
   "vid": "c32102oo7xp",
   "title": "南方小伙娶北方媳妇，地域语言差异一目了然，太难了",
   "second_title": "",
   "url": "https://v.qq.com/x/page/c32102oo7xp.html",
   "pic": "//puui.qpic.cn/qqvideo/0/c32102oo7xp/332"
  },
  {
   "vid": "d3255c1t2hv",
   "title": "戏精马不想被人骑，一骑就倒地装死，演技逼真浑身是戏！",
   "second_title": "",
   "url": "https://v.qq.com/x/page/d3255c1t2hv.html",
   "pic": "//puui.qpic.cn/qqvideo/0/d3255c1t2hv/332"
  },
  {
   "vid": "b3027dwvfcr",
   "title": "主人不舒服，泰迪妞妞还逼着主人上班，哪有这样的狗狗",
   "second_title": "",
   "url": "https://v.qq.com/x/page/b3027dwvfcr.html",
   "pic": "//puui.qpic.cn/qqvideo/0/b3027dwvfcr/332"
  },
  {
   "vid": "d32567jynzu",
   "title": "搞笑改编歌曲《老婆就是女王》，以前男人都是三妻四妾，现在娶一个都够呛还特惨",
   "second_title": "",
   "url": "https://v.qq.com/x/page/d32567jynzu.html",
   "pic": "//puui.qpic.cn/qqvideo/0/d32567jynzu/332"
  }
 ],
 [
  {
   "vid": "m00412dohd6",
   "title": "德里克・库克绝佳续写，马勒满载死亡与人生感悟的未完之作《第十交响曲》",
   "second_title": "",
   "url": "https://v.qq.com/x/page/m00412dohd6.html",
   "pic": "//puui.qpic.cn/qqvideo/0/m00412dohd6/332"
  },
  {
   "vid": "x0041puihag",
   "title": "FOAM摄影博物馆 - 《乌博特拉乌》- 吉勒姆•特拉彭伯格",
   "second_title": "",
   "url": "https://v.qq.com/x/page/x0041puihag.html",
   "pic": "//puui.qpic.cn/qqvideo/0/x0041puihag/332"
  },
  {
   "vid": "v0039dw0e1c",
   "title": "林肯中心室内乐协会：来自西藏圣土佛教经幡的启迪",
   "second_title": "",
   "url": "https://v.qq.com/x/page/v0039dw0e1c.html",
   "pic": "//puui.qpic.cn/qqvideo/0/v0039dw0e1c/332"
  },
  {
   "vid": "g00391kba60",
   "title": "巴洛克时代双子星之一“亨德尔”为女高音而作的宣叙调",
   "second_title": "",
   "url": "https://v.qq.com/x/page/g00391kba60.html",
   "pic": "//puui.qpic.cn/qqvideo/0/g00391kba60/332"
  },
  {
   "vid": "z0036ptt80l",
   "title": "典雅而平衡，室内乐的精髓之作：巴赫 勃兰登堡G大调第四协奏曲BWV 1049",
   "second_title": "",
   "url": "https://v.qq.com/x/page/z0036ptt80l.html",
   "pic": "//puui.qpic.cn/qqvideo/0/z0036ptt80l/332"
  },
  {
   "vid": "f0041vfd6zu",
   "title": "余隆携手小提琴独奏家李伟纲实力演绎巴伯《小提琴协奏曲》",
   "second_title": "",
   "url": "https://v.qq.com/x/page/f0041vfd6zu.html",
   "pic": "//puui.qpic.cn/qqvideo/0/f0041vfd6zu/332"
  },
  {
   "vid": "l3238ecg7gs",
   "title": "轻纱如云，梦中仙子翩翩起舞——马林斯基《胡桃夹子》",
   "second_title": "",
   "url": "https://v.qq.com/x/page/l3238ecg7gs.html",
   "pic": "//puui.qpic.cn/qqvideo/0/l3238ecg7gs/332"
  },
  {
   "vid": "s32491d0342",
   "title": "强强合作，安德烈·波切利 & HAUSER -《Melodramma》",
   "second_title": "",
   "url": "https://v.qq.com/x/page/s32491d0342.html",
   "pic": "//puui.qpic.cn/qqvideo/0/s32491d0342/332"
  },
  {
   "vid": "m3259ulb7sj",
   "title": "湖畔落日，晚霞似火 |简单绘画教程",
   "second_title": "",
   "url": "https://v.qq.com/x/page/m3259ulb7sj.html",
   "pic": "//puui.qpic.cn/qqvideo/0/m3259ulb7sj/332"
  },
  {
   "vid": "y32665eagj1",
   "title": "TeamLab-世界遗产东寺的数字光影秀",
   "second_title": "",
   "url": "https://v.qq.com/x/page/y32665eagj1.html",
   "pic": "//puui.qpic.cn/qqvideo/0/y32665eagj1/332"
  }
 ]
]
      </script>
      <svg class="svg_sprite" height="1" width="1">
       <symbol id="svg_icon_preview" viewbox="0 0 17 15">
        <path d="M4 10v2H2c-1.1 0-2-.9-2-2V2C0 .9.9 0 2 0h9c1.1 0 2 .9 2 2v4h-2V2H2v8h2zM11 15c-1.6 0-3.3-.8-5.1-2.5-.8-.8-.8-2-.1-2.8l.1-.1C7.7 7.8 9.4 7 11 7c1.6 0 3.3.9 4.9 2.6.7.8.7 1.9 0 2.7-1.6 1.8-3.3 2.7-4.9 2.7zm0-2c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2z" fill="currentcolor">
        </path>
        <circle cx="11" cy="11" fill="currentcolor" r="1">
        </circle>
       </symbol>
      </svg>
     </div>
     <div class="figure_2row">
      <div class="mod_figure mod_figure_h_default mod_figure_h_default_2row mod_figure_h_default" data-rowcount="5" data-rowlen="2">
       <div __wind="" class="list_item">
        <a _stat="multi_feed_V:img:undefined" class="figure" data-float="a3150exlzrz" data-quickopen="true" href="https://v.qq.com/x/page/a3150exlzrz.html" tabindex="-1" target="_blank">
         <img alt="怀孕三个月去医院做产检需要注意什么？ 记得这项检查最重要" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/qqvideo/0/a3150exlzrz/332" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
         <div class="figure_caption">
          01:15
         </div>
        </a>
        <div class="figure_detail figure_detail_two_row figure_detail_preview">
         <a _stat="multi_feed_V:title:怀孕三个月去医院做产检需要注意什么？ 记得这项检查最重要" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/a3150exlzrz.html" target="_blank" title="怀孕三个月去医院做产检需要注意什么？ 记得这项检查最重要">
          怀孕三个月去医院做产检需要注意什么？ 记得这项检查最重要
         </a>
         <div class="figure_btn_preview figure_btn_preview_a3150exlzrz" data-vid="a3150exlzrz">
          <svg class="svg_icon svg_icon_preview" height="15" viewbox="0 0 17 15" width="17">
           <use xlink:href="#svg_icon_preview">
           </use>
          </svg>
          <span class="icon_text">
           预览
          </span>
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="multi_feed_V:img:undefined" class="figure" data-float="o3145vnfjyy" data-quickopen="true" href="https://v.qq.com/x/page/o3145vnfjyy.html" tabindex="-1" target="_blank">
         <img alt="《仲夏满天心》人间自恋靳泽一！自信满满的画风也太欠了" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/qqvideo/0/o3145vnfjyy/332" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
         <div class="figure_caption">
          01:23
         </div>
        </a>
        <div class="figure_detail figure_detail_two_row figure_detail_preview">
         <a _stat="multi_feed_V:title:《仲夏满天心》人间自恋靳泽一！自信满满的画风也太欠了" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/o3145vnfjyy.html" target="_blank" title="《仲夏满天心》人间自恋靳泽一！自信满满的画风也太欠了">
          《仲夏满天心》人间自恋靳泽一！自信满满的画风也太欠了
         </a>
         <div class="figure_btn_preview figure_btn_preview_o3145vnfjyy" data-vid="o3145vnfjyy">
          <svg class="svg_icon svg_icon_preview" height="15" viewbox="0 0 17 15" width="17">
           <use xlink:href="#svg_icon_preview">
           </use>
          </svg>
          <span class="icon_text">
           预览
          </span>
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="multi_feed_V:img:undefined" class="figure" data-float="v3052r25qi6" data-quickopen="true" href="https://v.qq.com/x/page/v3052r25qi6.html" tabindex="-1" target="_blank">
         <img alt="走错片场？当《乡村爱情》谢广坤来到大明，略带喜感却气场全开" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/qqvideo/0/v3052r25qi6/332" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
         <div class="figure_caption">
          00:55
         </div>
        </a>
        <div class="figure_detail figure_detail_two_row figure_detail_preview">
         <a _stat="multi_feed_V:title:走错片场？当《乡村爱情》谢广坤来到大明，略带喜感却气场全开" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/v3052r25qi6.html" target="_blank" title="走错片场？当《乡村爱情》谢广坤来到大明，略带喜感却气场全开">
          走错片场？当《乡村爱情》谢广坤来到大明，略带喜感却气场全开
         </a>
         <div class="figure_btn_preview figure_btn_preview_v3052r25qi6" data-vid="v3052r25qi6">
          <svg class="svg_icon svg_icon_preview" height="15" viewbox="0 0 17 15" width="17">
           <use xlink:href="#svg_icon_preview">
           </use>
          </svg>
          <span class="icon_text">
           预览
          </span>
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="multi_feed_V:img:undefined" class="figure" data-float="h313448akr0" data-quickopen="true" href="https://v.qq.com/x/page/h313448akr0.html" tabindex="-1" target="_blank">
         <img alt="【鹿晗X吴磊】穿越火线 sold out 这么帅的第一次见吧" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/qqvideo/0/h313448akr0/332" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
         <div class="figure_caption">
          00:33
         </div>
        </a>
        <div class="figure_detail figure_detail_two_row figure_detail_preview">
         <a _stat="multi_feed_V:title:【鹿晗X吴磊】穿越火线 sold out 这么帅的第一次见吧" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/h313448akr0.html" target="_blank" title="【鹿晗X吴磊】穿越火线 sold out 这么帅的第一次见吧">
          【鹿晗X吴磊】穿越火线 sold out 这么帅的第一次见吧
         </a>
         <div class="figure_btn_preview figure_btn_preview_h313448akr0" data-vid="h313448akr0">
          <svg class="svg_icon svg_icon_preview" height="15" viewbox="0 0 17 15" width="17">
           <use xlink:href="#svg_icon_preview">
           </use>
          </svg>
          <span class="icon_text">
           预览
          </span>
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="multi_feed_V:img:undefined" class="figure" data-float="j0502qo91fm" data-quickopen="true" href="https://v.qq.com/x/page/j0502qo91fm.html" tabindex="-1" target="_blank">
         <img alt="唐老鸭拆汪汪队立大功奇趣蛋 开心宝贝出奇蛋" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/qqvideo/0/j0502qo91fm/332" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
         <div class="figure_caption">
          04:46
         </div>
        </a>
        <div class="figure_detail figure_detail_two_row figure_detail_preview">
         <a _stat="multi_feed_V:title:唐老鸭拆汪汪队立大功奇趣蛋 开心宝贝出奇蛋" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/j0502qo91fm.html" target="_blank" title="唐老鸭拆汪汪队立大功奇趣蛋 开心宝贝出奇蛋">
          唐老鸭拆汪汪队立大功奇趣蛋 开心宝贝出奇蛋
         </a>
         <div class="figure_btn_preview figure_btn_preview_j0502qo91fm" data-vid="j0502qo91fm">
          <svg class="svg_icon svg_icon_preview" height="15" viewbox="0 0 17 15" width="17">
           <use xlink:href="#svg_icon_preview">
           </use>
          </svg>
          <span class="icon_text">
           预览
          </span>
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="multi_feed_V:img:undefined" class="figure" data-float="k0967pcznzt" href="https://v.qq.com/x/page/k0967pcznzt.html" tabindex="-1" target="_blank">
         <img alt="Roblox杀手模拟器：学会新技能！可毫无用武之地！小飞象解说" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/qqvideo/0/k0967pcznzt/332" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
         <div class="figure_caption">
          19:24
         </div>
        </a>
        <div class="figure_detail figure_detail_two_row figure_detail_preview">
         <a _stat="multi_feed_V:title:Roblox杀手模拟器：学会新技能！可毫无用武之地！小飞象解说" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/k0967pcznzt.html" target="_blank" title="Roblox杀手模拟器：学会新技能！可毫无用武之地！小飞象解说">
          Roblox杀手模拟器：学会新技能！可毫无用武之地！小飞象解说
         </a>
         <div class="figure_btn_preview figure_btn_preview_k0967pcznzt" data-vid="k0967pcznzt">
          <svg class="svg_icon svg_icon_preview" height="15" viewbox="0 0 17 15" width="17">
           <use xlink:href="#svg_icon_preview">
           </use>
          </svg>
          <span class="icon_text">
           预览
          </span>
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="multi_feed_V:img:undefined" class="figure" data-float="c0033m9y8r9" data-quickopen="true" href="https://v.qq.com/x/page/c0033m9y8r9.html" tabindex="-1" target="_blank">
         <img alt="董力厨房手忙脚乱，什么都找不到大喊“救命”" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/qqvideo/0/c0033m9y8r9/332" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
         <div class="figure_caption">
          01:54
         </div>
        </a>
        <div class="figure_detail figure_detail_two_row figure_detail_preview">
         <a _stat="multi_feed_V:title:董力厨房手忙脚乱，什么都找不到大喊“救命”" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/c0033m9y8r9.html" target="_blank" title="董力厨房手忙脚乱，什么都找不到大喊“救命”">
          董力厨房手忙脚乱，什么都找不到大喊“救命”
         </a>
         <div class="figure_btn_preview figure_btn_preview_c0033m9y8r9" data-vid="c0033m9y8r9">
          <svg class="svg_icon svg_icon_preview" height="15" viewbox="0 0 17 15" width="17">
           <use xlink:href="#svg_icon_preview">
           </use>
          </svg>
          <span class="icon_text">
           预览
          </span>
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="multi_feed_V:img:undefined" class="figure" data-float="r093509hghi" data-quickopen="true" href="https://v.qq.com/x/page/r093509hghi.html" tabindex="-1" target="_blank">
         <img alt="老板：“想去摩旅？这个火龙果先给我雕刻出98块的样子！”" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/qqvideo/0/r093509hghi/332" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
         <div class="figure_caption">
          02:12
         </div>
        </a>
        <div class="figure_detail figure_detail_two_row figure_detail_preview">
         <a _stat="multi_feed_V:title:老板：“想去摩旅？这个火龙果先给我雕刻出98块的样子！”" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/r093509hghi.html" target="_blank" title="老板：“想去摩旅？这个火龙果先给我雕刻出98块的样子！”">
          老板：“想去摩旅？这个火龙果先给我雕刻出98块的样子！”
         </a>
         <div class="figure_btn_preview figure_btn_preview_r093509hghi" data-vid="r093509hghi">
          <svg class="svg_icon svg_icon_preview" height="15" viewbox="0 0 17 15" width="17">
           <use xlink:href="#svg_icon_preview">
           </use>
          </svg>
          <span class="icon_text">
           预览
          </span>
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="multi_feed_V:img:undefined" class="figure" data-float="d3224crs1zu" data-quickopen="true" href="https://v.qq.com/x/page/d3224crs1zu.html" tabindex="-1" target="_blank">
         <img alt="为啥一到凌晨3、4点就“自然醒”？或是这几种疾病在作祟" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/qqvideo/0/d3224crs1zu/332" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
         <div class="figure_caption">
          02:19
         </div>
        </a>
        <div class="figure_detail figure_detail_two_row figure_detail_preview">
         <a _stat="multi_feed_V:title:为啥一到凌晨3、4点就“自然醒”？或是这几种疾病在作祟" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/d3224crs1zu.html" target="_blank" title="为啥一到凌晨3、4点就“自然醒”？或是这几种疾病在作祟">
          为啥一到凌晨3、4点就“自然醒”？或是这几种疾病在作祟
         </a>
         <div class="figure_btn_preview figure_btn_preview_d3224crs1zu" data-vid="d3224crs1zu">
          <svg class="svg_icon svg_icon_preview" height="15" viewbox="0 0 17 15" width="17">
           <use xlink:href="#svg_icon_preview">
           </use>
          </svg>
          <span class="icon_text">
           预览
          </span>
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="multi_feed_V:img:undefined" class="figure" data-float="j0840bazfu1" data-quickopen="true" href="https://v.qq.com/x/page/j0840bazfu1.html" tabindex="-1" target="_blank">
         <img alt="用星座的方式打开《花不弃》这俩货相似程度99+" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/qqvideo/0/j0840bazfu1/332" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
         <div class="figure_caption">
          02:15
         </div>
        </a>
        <div class="figure_detail figure_detail_two_row figure_detail_preview">
         <a _stat="multi_feed_V:title:用星座的方式打开《花不弃》这俩货相似程度99+" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/j0840bazfu1.html" target="_blank" title="用星座的方式打开《花不弃》这俩货相似程度99+">
          用星座的方式打开《花不弃》这俩货相似程度99+
         </a>
         <div class="figure_btn_preview figure_btn_preview_j0840bazfu1" data-vid="j0840bazfu1">
          <svg class="svg_icon svg_icon_preview" height="15" viewbox="0 0 17 15" width="17">
           <use xlink:href="#svg_icon_preview">
           </use>
          </svg>
          <span class="icon_text">
           预览
          </span>
         </div>
        </div>
       </div>
      </div>
      <div class="mod_figure mod_figure_h_default mod_figure_h_default_2row mod_figure_h_default none" data-rowcount="5" data-rowlen="2">
       <div __wind="" class="list_item">
        <a _stat="multi_feed_V:img:undefined" class="figure" data-float="y0034pjasob" data-quickopen="true" href="https://v.qq.com/x/page/y0034pjasob.html" tabindex="-1" target="_blank">
         <img alt="赵粤变了！这次狠话超霸气，彻底撕掉“不敢”的标签" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo/0/y0034pjasob/332" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
         <div class="figure_caption">
          01:39
         </div>
        </a>
        <div class="figure_detail figure_detail_two_row figure_detail_preview">
         <a _stat="multi_feed_V:title:赵粤变了！这次狠话超霸气，彻底撕掉“不敢”的标签" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/y0034pjasob.html" target="_blank" title="赵粤变了！这次狠话超霸气，彻底撕掉“不敢”的标签">
          赵粤变了！这次狠话超霸气，彻底撕掉“不敢”的标签
         </a>
         <div class="figure_desc" title="赵粤承载队友的梦想霸气发言，超敢！">
          赵粤承载队友的梦想霸气发言，超敢！
         </div>
         <div class="figure_btn_preview figure_btn_preview_y0034pjasob" data-vid="y0034pjasob">
          <svg class="svg_icon svg_icon_preview" height="15" viewbox="0 0 17 15" width="17">
           <use xlink:href="#svg_icon_preview">
           </use>
          </svg>
          <span class="icon_text">
           预览
          </span>
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="multi_feed_V:img:undefined" class="figure" data-float="y3227gq80fo" data-quickopen="true" href="https://v.qq.com/x/page/y3227gq80fo.html" tabindex="-1" target="_blank">
         <img alt="5种疾病，腹部症状像胃痛，需要仔细辨别" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo/0/y3227gq80fo/332" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
         <div class="figure_caption">
          01:57
         </div>
        </a>
        <div class="figure_detail figure_detail_two_row figure_detail_preview">
         <a _stat="multi_feed_V:title:5种疾病，腹部症状像胃痛，需要仔细辨别" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/y3227gq80fo.html" target="_blank" title="5种疾病，腹部症状像胃痛，需要仔细辨别">
          5种疾病，腹部症状像胃痛，需要仔细辨别
         </a>
         <div class="figure_btn_preview figure_btn_preview_y3227gq80fo" data-vid="y3227gq80fo">
          <svg class="svg_icon svg_icon_preview" height="15" viewbox="0 0 17 15" width="17">
           <use xlink:href="#svg_icon_preview">
           </use>
          </svg>
          <span class="icon_text">
           预览
          </span>
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="multi_feed_V:img:undefined" class="figure" data-float="q3209w7nojw" data-quickopen="true" href="https://v.qq.com/x/page/q3209w7nojw.html" tabindex="-1" target="_blank">
         <img alt="贾玲爆笑空降《相遇别离》，霸总严谨又被俘获了！" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo/0/q3209w7nojw/332" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
         <div class="figure_caption">
          01:18
         </div>
        </a>
        <div class="figure_detail figure_detail_two_row figure_detail_preview">
         <a _stat="multi_feed_V:title:贾玲爆笑空降《相遇别离》，霸总严谨又被俘获了！" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/q3209w7nojw.html" target="_blank" title="贾玲爆笑空降《相遇别离》，霸总严谨又被俘获了！">
          贾玲爆笑空降《相遇别离》，霸总严谨又被俘获了！
         </a>
         <div class="figure_btn_preview figure_btn_preview_q3209w7nojw" data-vid="q3209w7nojw">
          <svg class="svg_icon svg_icon_preview" height="15" viewbox="0 0 17 15" width="17">
           <use xlink:href="#svg_icon_preview">
           </use>
          </svg>
          <span class="icon_text">
           预览
          </span>
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="multi_feed_V:img:undefined" class="figure" data-float="j09516x2kgh" data-quickopen="true" href="https://v.qq.com/x/page/j09516x2kgh.html" tabindex="-1" target="_blank">
         <img alt="中风来临前，通常会有3个“前兆信号”，越早发现越好" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo/0/j09516x2kgh/332" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
         <div class="figure_caption">
          01:50
         </div>
        </a>
        <div class="figure_detail figure_detail_two_row figure_detail_preview">
         <a _stat="multi_feed_V:title:中风来临前，通常会有3个“前兆信号”，越早发现越好" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/j09516x2kgh.html" target="_blank" title="中风来临前，通常会有3个“前兆信号”，越早发现越好">
          中风来临前，通常会有3个“前兆信号”，越早发现越好
         </a>
         <div class="figure_btn_preview figure_btn_preview_j09516x2kgh" data-vid="j09516x2kgh">
          <svg class="svg_icon svg_icon_preview" height="15" viewbox="0 0 17 15" width="17">
           <use xlink:href="#svg_icon_preview">
           </use>
          </svg>
          <span class="icon_text">
           预览
          </span>
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="multi_feed_V:img:undefined" class="figure" data-float="o3159jd4esl" data-quickopen="true" href="https://v.qq.com/x/page/o3159jd4esl.html" tabindex="-1" target="_blank">
         <img alt="迷你世界奥特曼：抵御野人袭击，但是野人去哪里了？" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo/0/o3159jd4esl/332" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
         <div class="figure_caption">
          01:08
         </div>
        </a>
        <div class="figure_detail figure_detail_two_row figure_detail_preview">
         <a _stat="multi_feed_V:title:迷你世界奥特曼：抵御野人袭击，但是野人去哪里了？" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/o3159jd4esl.html" target="_blank" title="迷你世界奥特曼：抵御野人袭击，但是野人去哪里了？">
          迷你世界奥特曼：抵御野人袭击，但是野人去哪里了？
         </a>
         <div class="figure_btn_preview figure_btn_preview_o3159jd4esl" data-vid="o3159jd4esl">
          <svg class="svg_icon svg_icon_preview" height="15" viewbox="0 0 17 15" width="17">
           <use xlink:href="#svg_icon_preview">
           </use>
          </svg>
          <span class="icon_text">
           预览
          </span>
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="multi_feed_V:img:undefined" class="figure" data-float="v0954uasxlz" href="https://v.qq.com/x/page/v0954uasxlz.html" tabindex="-1" target="_blank">
         <img alt="女仆罢工哄不回来，那就再召唤一个吧！" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo/0/v0954uasxlz/332" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
         <div class="figure_caption">
          16:18
         </div>
        </a>
        <div class="figure_detail figure_detail_two_row figure_detail_preview">
         <a _stat="multi_feed_V:title:女仆罢工哄不回来，那就再召唤一个吧！" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/v0954uasxlz.html" target="_blank" title="女仆罢工哄不回来，那就再召唤一个吧！">
          女仆罢工哄不回来，那就再召唤一个吧！
         </a>
         <div class="figure_btn_preview figure_btn_preview_v0954uasxlz" data-vid="v0954uasxlz">
          <svg class="svg_icon svg_icon_preview" height="15" viewbox="0 0 17 15" width="17">
           <use xlink:href="#svg_icon_preview">
           </use>
          </svg>
          <span class="icon_text">
           预览
          </span>
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="multi_feed_V:img:undefined" class="figure" data-float="a3070br60y0" data-quickopen="true" href="https://v.qq.com/x/page/a3070br60y0.html" tabindex="-1" target="_blank">
         <img alt="第1次玩里里家铁盒史莱姆，手感果然名不虚传！就味道有点上头？" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo/0/a3070br60y0/332" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
         <div class="figure_caption">
          01:36
         </div>
        </a>
        <div class="figure_detail figure_detail_two_row figure_detail_preview">
         <a _stat="multi_feed_V:title:第1次玩里里家铁盒史莱姆，手感果然名不虚传！就味道有点上头？" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/a3070br60y0.html" target="_blank" title="第1次玩里里家铁盒史莱姆，手感果然名不虚传！就味道有点上头？">
          第1次玩里里家铁盒史莱姆，手感果然名不虚传！就味道有点上头？
         </a>
         <div class="figure_desc" title="【HowTo】教你玩转铁盒史莱姆，手感名不虚传，来看看吧">
          【HowTo】教你玩转铁盒史莱姆，手感名不虚传，来看看吧
         </div>
         <div class="figure_btn_preview figure_btn_preview_a3070br60y0" data-vid="a3070br60y0">
          <svg class="svg_icon svg_icon_preview" height="15" viewbox="0 0 17 15" width="17">
           <use xlink:href="#svg_icon_preview">
           </use>
          </svg>
          <span class="icon_text">
           预览
          </span>
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="multi_feed_V:img:undefined" class="figure" data-float="d0854lzmk7q" href="https://v.qq.com/x/page/d0854lzmk7q.html" tabindex="-1" target="_blank">
         <img alt="《Tinrry+》Tinrry教你做青团" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo/0/d0854lzmk7q/332" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
         <div class="figure_caption">
          18:21
         </div>
        </a>
        <div class="figure_detail figure_detail_two_row figure_detail_preview">
         <a _stat="multi_feed_V:title:《Tinrry+》Tinrry教你做青团" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/d0854lzmk7q.html" target="_blank" title="《Tinrry+》Tinrry教你做青团">
          《Tinrry+》Tinrry教你做青团
         </a>
         <div class="figure_btn_preview figure_btn_preview_d0854lzmk7q" data-vid="d0854lzmk7q">
          <svg class="svg_icon svg_icon_preview" height="15" viewbox="0 0 17 15" width="17">
           <use xlink:href="#svg_icon_preview">
           </use>
          </svg>
          <span class="icon_text">
           预览
          </span>
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="multi_feed_V:img:undefined" class="figure" data-float="u0895j7eomo" data-quickopen="true" href="https://v.qq.com/x/page/u0895j7eomo.html" tabindex="-1" target="_blank">
         <img alt="我的世界：滑稽世界模组！有变成墨鱼的萌妹，还有蹦迪的BOSS" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo/0/u0895j7eomo/332" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
         <div class="figure_caption">
          01:41
         </div>
        </a>
        <div class="figure_detail figure_detail_two_row figure_detail_preview">
         <a _stat="multi_feed_V:title:我的世界：滑稽世界模组！有变成墨鱼的萌妹，还有蹦迪的BOSS" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/u0895j7eomo.html" target="_blank" title="我的世界：滑稽世界模组！有变成墨鱼的萌妹，还有蹦迪的BOSS">
          我的世界：滑稽世界模组！有变成墨鱼的萌妹，还有蹦迪的BOSS
         </a>
         <div class="figure_btn_preview figure_btn_preview_u0895j7eomo" data-vid="u0895j7eomo">
          <svg class="svg_icon svg_icon_preview" height="15" viewbox="0 0 17 15" width="17">
           <use xlink:href="#svg_icon_preview">
           </use>
          </svg>
          <span class="icon_text">
           预览
          </span>
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="multi_feed_V:img:undefined" class="figure" data-float="r07239gid8n" data-quickopen="true" href="https://v.qq.com/x/page/r07239gid8n.html" tabindex="-1" target="_blank">
         <img alt="王者荣耀更新：六神装赵云vs典韦！新的版本之帝诞生了" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo/0/r07239gid8n/332" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
         <div class="figure_caption">
          00:59
         </div>
        </a>
        <div class="figure_detail figure_detail_two_row figure_detail_preview">
         <a _stat="multi_feed_V:title:王者荣耀更新：六神装赵云vs典韦！新的版本之帝诞生了" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/r07239gid8n.html" target="_blank" title="王者荣耀更新：六神装赵云vs典韦！新的版本之帝诞生了">
          王者荣耀更新：六神装赵云vs典韦！新的版本之帝诞生了
         </a>
         <div class="figure_btn_preview figure_btn_preview_r07239gid8n" data-vid="r07239gid8n">
          <svg class="svg_icon svg_icon_preview" height="15" viewbox="0 0 17 15" width="17">
           <use xlink:href="#svg_icon_preview">
           </use>
          </svg>
          <span class="icon_text">
           预览
          </span>
         </div>
        </div>
       </div>
      </div>
      <div class="mod_figure mod_figure_h_default mod_figure_h_default_2row mod_figure_h_default none" data-rowcount="5" data-rowlen="2">
       <div __wind="" class="list_item">
        <a _stat="multi_feed_V:img:undefined" class="figure" data-float="b3256l5ttup" data-quickopen="true" href="https://v.qq.com/x/page/b3256l5ttup.html" tabindex="-1" target="_blank">
         <img alt="喜剧小品《多大点事》：妻子怀孕老公却检查出不能生，笑料不断" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo/0/b3256l5ttup/332" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
         <div class="figure_caption">
          11:04
         </div>
        </a>
        <div class="figure_detail figure_detail_two_row figure_detail_preview">
         <a _stat="multi_feed_V:title:喜剧小品《多大点事》：妻子怀孕老公却检查出不能生，笑料不断" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/b3256l5ttup.html" target="_blank" title="喜剧小品《多大点事》：妻子怀孕老公却检查出不能生，笑料不断">
          喜剧小品《多大点事》：妻子怀孕老公却检查出不能生，笑料不断
         </a>
         <div class="figure_btn_preview figure_btn_preview_b3256l5ttup" data-vid="b3256l5ttup">
          <svg class="svg_icon svg_icon_preview" height="15" viewbox="0 0 17 15" width="17">
           <use xlink:href="#svg_icon_preview">
           </use>
          </svg>
          <span class="icon_text">
           预览
          </span>
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="multi_feed_V:img:undefined" class="figure" data-float="x3266as5qkz" data-quickopen="true" href="https://v.qq.com/x/page/x3266as5qkz.html" tabindex="-1" target="_blank">
         <img alt="搞笑歌曲改编，有钱就是好，家里红旗不倒外面彩旗飘" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo/0/x3266as5qkz/332" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
         <div class="figure_caption">
          01:02
         </div>
        </a>
        <div class="figure_detail figure_detail_two_row figure_detail_preview">
         <a _stat="multi_feed_V:title:搞笑歌曲改编，有钱就是好，家里红旗不倒外面彩旗飘" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/x3266as5qkz.html" target="_blank" title="搞笑歌曲改编，有钱就是好，家里红旗不倒外面彩旗飘">
          搞笑歌曲改编，有钱就是好，家里红旗不倒外面彩旗飘
         </a>
         <div class="figure_btn_preview figure_btn_preview_x3266as5qkz" data-vid="x3266as5qkz">
          <svg class="svg_icon svg_icon_preview" height="15" viewbox="0 0 17 15" width="17">
           <use xlink:href="#svg_icon_preview">
           </use>
          </svg>
          <span class="icon_text">
           预览
          </span>
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="multi_feed_V:img:undefined" class="figure" data-float="i32600q07fi" data-quickopen="true" href="https://v.qq.com/x/page/i32600q07fi.html" tabindex="-1" target="_blank">
         <img alt="你们在宿舍中遇到过什么奇葩室友？简直要奔溃！" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo/0/i32600q07fi/332" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
         <div class="figure_caption">
          01:45
         </div>
        </a>
        <div class="figure_detail figure_detail_two_row figure_detail_preview">
         <a _stat="multi_feed_V:title:你们在宿舍中遇到过什么奇葩室友？简直要奔溃！" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/i32600q07fi.html" target="_blank" title="你们在宿舍中遇到过什么奇葩室友？简直要奔溃！">
          你们在宿舍中遇到过什么奇葩室友？简直要奔溃！
         </a>
         <div class="figure_btn_preview figure_btn_preview_i32600q07fi" data-vid="i32600q07fi">
          <svg class="svg_icon svg_icon_preview" height="15" viewbox="0 0 17 15" width="17">
           <use xlink:href="#svg_icon_preview">
           </use>
          </svg>
          <span class="icon_text">
           预览
          </span>
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="multi_feed_V:img:undefined" class="figure" data-float="p3249shyvfx" data-quickopen="true" href="https://v.qq.com/x/page/p3249shyvfx.html" tabindex="-1" target="_blank">
         <img alt="赵本山罕见笑场名场面，宋小宝一个字让赵本山忍不住，直接笑场停不下！ #鹅创剪辑大赏 第二阶段#" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo/0/p3249shyvfx/332" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
         <div class="figure_caption">
          07:21
         </div>
        </a>
        <div class="figure_detail figure_detail_two_row figure_detail_preview">
         <a _stat="multi_feed_V:title:赵本山罕见笑场名场面，宋小宝一个字让赵本山忍不住，直接笑场停不下！ #鹅创剪辑大赏 第二阶段#" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/p3249shyvfx.html" target="_blank" title="赵本山罕见笑场名场面，宋小宝一个字让赵本山忍不住，直接笑场停不下！ #鹅创剪辑大赏 第二阶段#">
          赵本山罕见笑场名场面，宋小宝一个字让赵本山忍不住，直接笑场停不下！ #鹅创剪辑大赏 第二阶段#
         </a>
         <div class="figure_btn_preview figure_btn_preview_p3249shyvfx" data-vid="p3249shyvfx">
          <svg class="svg_icon svg_icon_preview" height="15" viewbox="0 0 17 15" width="17">
           <use xlink:href="#svg_icon_preview">
           </use>
          </svg>
          <span class="icon_text">
           预览
          </span>
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="multi_feed_V:img:undefined" class="figure" data-float="c0616e81a57" data-quickopen="true" href="https://v.qq.com/x/page/c0616e81a57.html" tabindex="-1" target="_blank">
         <img alt="雷军：小米十个季度将回归国内第一！我看没那么容易" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo/0/c0616e81a57/332" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
         <div class="figure_caption">
          07:06
         </div>
        </a>
        <div class="figure_detail figure_detail_two_row figure_detail_preview">
         <a _stat="multi_feed_V:title:雷军：小米十个季度将回归国内第一！我看没那么容易" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/c0616e81a57.html" target="_blank" title="雷军：小米十个季度将回归国内第一！我看没那么容易">
          雷军：小米十个季度将回归国内第一！我看没那么容易
         </a>
         <div class="figure_btn_preview figure_btn_preview_c0616e81a57" data-vid="c0616e81a57">
          <svg class="svg_icon svg_icon_preview" height="15" viewbox="0 0 17 15" width="17">
           <use xlink:href="#svg_icon_preview">
           </use>
          </svg>
          <span class="icon_text">
           预览
          </span>
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="multi_feed_V:img:undefined" class="figure" data-float="d0910divqys" data-quickopen="true" href="https://v.qq.com/x/page/d0910divqys.html" tabindex="-1" target="_blank">
         <img alt="你最想对前男友说什么？妹子回答句句扎心，很真实" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo/0/d0910divqys/332" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
         <div class="figure_caption">
          01:42
         </div>
        </a>
        <div class="figure_detail figure_detail_two_row figure_detail_preview">
         <a _stat="multi_feed_V:title:你最想对前男友说什么？妹子回答句句扎心，很真实" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/d0910divqys.html" target="_blank" title="你最想对前男友说什么？妹子回答句句扎心，很真实">
          你最想对前男友说什么？妹子回答句句扎心，很真实
         </a>
         <div class="figure_btn_preview figure_btn_preview_d0910divqys" data-vid="d0910divqys">
          <svg class="svg_icon svg_icon_preview" height="15" viewbox="0 0 17 15" width="17">
           <use xlink:href="#svg_icon_preview">
           </use>
          </svg>
          <span class="icon_text">
           预览
          </span>
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="multi_feed_V:img:undefined" class="figure" data-float="c32102oo7xp" data-quickopen="true" href="https://v.qq.com/x/page/c32102oo7xp.html" tabindex="-1" target="_blank">
         <img alt="南方小伙娶北方媳妇，地域语言差异一目了然，太难了" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo/0/c32102oo7xp/332" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
         <div class="figure_caption">
          01:01
         </div>
        </a>
        <div class="figure_detail figure_detail_two_row figure_detail_preview">
         <a _stat="multi_feed_V:title:南方小伙娶北方媳妇，地域语言差异一目了然，太难了" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/c32102oo7xp.html" target="_blank" title="南方小伙娶北方媳妇，地域语言差异一目了然，太难了">
          南方小伙娶北方媳妇，地域语言差异一目了然，太难了
         </a>
         <div class="figure_btn_preview figure_btn_preview_c32102oo7xp" data-vid="c32102oo7xp">
          <svg class="svg_icon svg_icon_preview" height="15" viewbox="0 0 17 15" width="17">
           <use xlink:href="#svg_icon_preview">
           </use>
          </svg>
          <span class="icon_text">
           预览
          </span>
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="multi_feed_V:img:undefined" class="figure" data-float="d3255c1t2hv" data-quickopen="true" href="https://v.qq.com/x/page/d3255c1t2hv.html" tabindex="-1" target="_blank">
         <img alt="戏精马不想被人骑，一骑就倒地装死，演技逼真浑身是戏！" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo/0/d3255c1t2hv/332" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
         <div class="figure_caption">
          00:57
         </div>
        </a>
        <div class="figure_detail figure_detail_two_row figure_detail_preview">
         <a _stat="multi_feed_V:title:戏精马不想被人骑，一骑就倒地装死，演技逼真浑身是戏！" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/d3255c1t2hv.html" target="_blank" title="戏精马不想被人骑，一骑就倒地装死，演技逼真浑身是戏！">
          戏精马不想被人骑，一骑就倒地装死，演技逼真浑身是戏！
         </a>
         <div class="figure_btn_preview figure_btn_preview_d3255c1t2hv" data-vid="d3255c1t2hv">
          <svg class="svg_icon svg_icon_preview" height="15" viewbox="0 0 17 15" width="17">
           <use xlink:href="#svg_icon_preview">
           </use>
          </svg>
          <span class="icon_text">
           预览
          </span>
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="multi_feed_V:img:undefined" class="figure" data-float="b3027dwvfcr" data-quickopen="true" href="https://v.qq.com/x/page/b3027dwvfcr.html" tabindex="-1" target="_blank">
         <img alt="主人不舒服，泰迪妞妞还逼着主人上班，哪有这样的狗狗" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo/0/b3027dwvfcr/332" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
         <div class="figure_caption">
          00:42
         </div>
        </a>
        <div class="figure_detail figure_detail_two_row figure_detail_preview">
         <a _stat="multi_feed_V:title:主人不舒服，泰迪妞妞还逼着主人上班，哪有这样的狗狗" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/b3027dwvfcr.html" target="_blank" title="主人不舒服，泰迪妞妞还逼着主人上班，哪有这样的狗狗">
          主人不舒服，泰迪妞妞还逼着主人上班，哪有这样的狗狗
         </a>
         <div class="figure_btn_preview figure_btn_preview_b3027dwvfcr" data-vid="b3027dwvfcr">
          <svg class="svg_icon svg_icon_preview" height="15" viewbox="0 0 17 15" width="17">
           <use xlink:href="#svg_icon_preview">
           </use>
          </svg>
          <span class="icon_text">
           预览
          </span>
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="multi_feed_V:img:undefined" class="figure" data-float="d32567jynzu" data-quickopen="true" href="https://v.qq.com/x/page/d32567jynzu.html" tabindex="-1" target="_blank">
         <img alt="搞笑改编歌曲《老婆就是女王》，以前男人都是三妻四妾，现在娶一个都够呛还特惨" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo/0/d32567jynzu/332" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
         <div class="figure_caption">
          01:14
         </div>
        </a>
        <div class="figure_detail figure_detail_two_row figure_detail_preview">
         <a _stat="multi_feed_V:title:搞笑改编歌曲《老婆就是女王》，以前男人都是三妻四妾，现在娶一个都够呛还特惨" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/d32567jynzu.html" target="_blank" title="搞笑改编歌曲《老婆就是女王》，以前男人都是三妻四妾，现在娶一个都够呛还特惨">
          搞笑改编歌曲《老婆就是女王》，以前男人都是三妻四妾，现在娶一个都够呛还特惨
         </a>
         <div class="figure_btn_preview figure_btn_preview_d32567jynzu" data-vid="d32567jynzu">
          <svg class="svg_icon svg_icon_preview" height="15" viewbox="0 0 17 15" width="17">
           <use xlink:href="#svg_icon_preview">
           </use>
          </svg>
          <span class="icon_text">
           预览
          </span>
         </div>
        </div>
       </div>
      </div>
      <div class="mod_figure mod_figure_h_default mod_figure_h_default_2row mod_figure_h_default none" data-rowcount="5" data-rowlen="2">
       <div __wind="" class="list_item">
        <a _stat="multi_feed_V:img:德里克・库克绝佳续写，马勒满载死亡与人生感悟的未完之作《第十交响曲》" class="figure" data-float="m00412dohd6" data-quickopen="true" href="https://v.qq.com/x/page/m00412dohd6.html" tabindex="-1" target="_blank">
         <img alt="德里克・库克绝佳续写，马勒满载死亡与人生感悟的未完之作《第十交响曲》" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo_ori/0/m00412dohd6_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
         <div class="figure_caption">
          03:04
         </div>
        </a>
        <div class="figure_detail figure_detail_two_row figure_detail_preview">
         <a _stat="multi_feed_V:title:德里克・库克绝佳续写，马勒满载死亡与人生感悟的未完之作《第十交响曲》" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/m00412dohd6.html" target="_blank" title="德里克・库克绝佳续写，马勒满载死亡与人生感悟的未完之作《第十交响曲》">
          德里克・库克绝佳续写，马勒满载死亡与人生感悟的未完之作《第十交响曲》
         </a>
         <div class="figure_btn_preview figure_btn_preview_m00412dohd6" data-vid="m00412dohd6">
          <svg class="svg_icon svg_icon_preview" height="15" viewbox="0 0 17 15" width="17">
           <use xlink:href="#svg_icon_preview">
           </use>
          </svg>
          <span class="icon_text">
           预览
          </span>
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="multi_feed_V:img:FOAM摄影博物馆 - 《乌博特拉乌》- 吉勒姆•特拉彭伯格" class="figure" data-float="x0041puihag" data-quickopen="true" href="https://v.qq.com/x/page/x0041puihag.html" tabindex="-1" target="_blank">
         <img alt="FOAM摄影博物馆 - 《乌博特拉乌》- 吉勒姆•特拉彭伯格" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo_ori/0/x0041puihag_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
         <div class="figure_caption">
          05:33
         </div>
        </a>
        <div class="figure_detail figure_detail_two_row figure_detail_preview">
         <a _stat="multi_feed_V:title:FOAM摄影博物馆 - 《乌博特拉乌》- 吉勒姆•特拉彭伯格" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/x0041puihag.html" target="_blank" title="FOAM摄影博物馆 - 《乌博特拉乌》- 吉勒姆•特拉彭伯格">
          FOAM摄影博物馆 - 《乌博特拉乌》- 吉勒姆•特拉彭伯格
         </a>
         <div class="figure_btn_preview figure_btn_preview_x0041puihag" data-vid="x0041puihag">
          <svg class="svg_icon svg_icon_preview" height="15" viewbox="0 0 17 15" width="17">
           <use xlink:href="#svg_icon_preview">
           </use>
          </svg>
          <span class="icon_text">
           预览
          </span>
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="multi_feed_V:img:林肯中心室内乐协会：来自西藏圣土佛教经幡的启迪" class="figure" data-float="v0039dw0e1c" data-quickopen="true" href="https://v.qq.com/x/page/v0039dw0e1c.html" tabindex="-1" target="_blank">
         <img alt="林肯中心室内乐协会：来自西藏圣土佛教经幡的启迪" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo_ori/0/v0039dw0e1c_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
         <div class="figure_caption">
          10:29
         </div>
        </a>
        <div class="figure_detail figure_detail_two_row figure_detail_preview">
         <a _stat="multi_feed_V:title:林肯中心室内乐协会：来自西藏圣土佛教经幡的启迪" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/v0039dw0e1c.html" target="_blank" title="林肯中心室内乐协会：来自西藏圣土佛教经幡的启迪">
          林肯中心室内乐协会：来自西藏圣土佛教经幡的启迪
         </a>
         <div class="figure_btn_preview figure_btn_preview_v0039dw0e1c" data-vid="v0039dw0e1c">
          <svg class="svg_icon svg_icon_preview" height="15" viewbox="0 0 17 15" width="17">
           <use xlink:href="#svg_icon_preview">
           </use>
          </svg>
          <span class="icon_text">
           预览
          </span>
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="multi_feed_V:img:巴洛克时代双子星之一“亨德尔”为女高音而作的宣叙调" class="figure" data-float="g00391kba60" href="https://v.qq.com/x/page/g00391kba60.html" tabindex="-1" target="_blank">
         <img alt="巴洛克时代双子星之一“亨德尔”为女高音而作的宣叙调" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo_ori/0/g00391kba60_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
         <div class="figure_caption">
          16:51
         </div>
        </a>
        <div class="figure_detail figure_detail_two_row figure_detail_preview">
         <a _stat="multi_feed_V:title:巴洛克时代双子星之一“亨德尔”为女高音而作的宣叙调" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/g00391kba60.html" target="_blank" title="巴洛克时代双子星之一“亨德尔”为女高音而作的宣叙调">
          巴洛克时代双子星之一“亨德尔”为女高音而作的宣叙调
         </a>
         <div class="figure_btn_preview figure_btn_preview_g00391kba60" data-vid="g00391kba60">
          <svg class="svg_icon svg_icon_preview" height="15" viewbox="0 0 17 15" width="17">
           <use xlink:href="#svg_icon_preview">
           </use>
          </svg>
          <span class="icon_text">
           预览
          </span>
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="multi_feed_V:img:典雅而平衡，室内乐的精髓之作：巴赫 勃兰登堡G大调第四协奏曲BWV 1049" class="figure" data-float="z0036ptt80l" href="https://v.qq.com/x/page/z0036ptt80l.html" tabindex="-1" target="_blank">
         <img alt="典雅而平衡，室内乐的精髓之作：巴赫 勃兰登堡G大调第四协奏曲BWV 1049" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo_ori/0/z0036ptt80l_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
         <div class="figure_caption">
          15:33
         </div>
        </a>
        <div class="figure_detail figure_detail_two_row figure_detail_preview">
         <a _stat="multi_feed_V:title:典雅而平衡，室内乐的精髓之作：巴赫 勃兰登堡G大调第四协奏曲BWV 1049" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/z0036ptt80l.html" target="_blank" title="典雅而平衡，室内乐的精髓之作：巴赫 勃兰登堡G大调第四协奏曲BWV 1049">
          典雅而平衡，室内乐的精髓之作：巴赫 勃兰登堡G大调第四协奏曲BWV 1049
         </a>
         <div class="figure_btn_preview figure_btn_preview_z0036ptt80l" data-vid="z0036ptt80l">
          <svg class="svg_icon svg_icon_preview" height="15" viewbox="0 0 17 15" width="17">
           <use xlink:href="#svg_icon_preview">
           </use>
          </svg>
          <span class="icon_text">
           预览
          </span>
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="multi_feed_V:img:余隆携手小提琴独奏家李伟纲实力演绎巴伯《小提琴协奏曲》" class="figure" data-float="f0041vfd6zu" data-quickopen="true" href="https://v.qq.com/x/page/f0041vfd6zu.html" tabindex="-1" target="_blank">
         <img alt="余隆携手小提琴独奏家李伟纲实力演绎巴伯《小提琴协奏曲》" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo_ori/0/f0041vfd6zu_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
         <div class="figure_caption">
          03:09
         </div>
        </a>
        <div class="figure_detail figure_detail_two_row figure_detail_preview">
         <a _stat="multi_feed_V:title:余隆携手小提琴独奏家李伟纲实力演绎巴伯《小提琴协奏曲》" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/f0041vfd6zu.html" target="_blank" title="余隆携手小提琴独奏家李伟纲实力演绎巴伯《小提琴协奏曲》">
          余隆携手小提琴独奏家李伟纲实力演绎巴伯《小提琴协奏曲》
         </a>
         <div class="figure_btn_preview figure_btn_preview_f0041vfd6zu" data-vid="f0041vfd6zu">
          <svg class="svg_icon svg_icon_preview" height="15" viewbox="0 0 17 15" width="17">
           <use xlink:href="#svg_icon_preview">
           </use>
          </svg>
          <span class="icon_text">
           预览
          </span>
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="multi_feed_V:img:轻纱如云，梦中仙子翩翩起舞——马林斯基《胡桃夹子》" class="figure" data-float="l3238ecg7gs" data-quickopen="true" href="https://v.qq.com/x/page/l3238ecg7gs.html" tabindex="-1" target="_blank">
         <img alt="轻纱如云，梦中仙子翩翩起舞——马林斯基《胡桃夹子》" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo_ori/0/l3238ecg7gs_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
         <div class="figure_caption">
          02:58
         </div>
        </a>
        <div class="figure_detail figure_detail_two_row figure_detail_preview">
         <a _stat="multi_feed_V:title:轻纱如云，梦中仙子翩翩起舞——马林斯基《胡桃夹子》" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/l3238ecg7gs.html" target="_blank" title="轻纱如云，梦中仙子翩翩起舞——马林斯基《胡桃夹子》">
          轻纱如云，梦中仙子翩翩起舞——马林斯基《胡桃夹子》
         </a>
         <div class="figure_btn_preview figure_btn_preview_l3238ecg7gs" data-vid="l3238ecg7gs">
          <svg class="svg_icon svg_icon_preview" height="15" viewbox="0 0 17 15" width="17">
           <use xlink:href="#svg_icon_preview">
           </use>
          </svg>
          <span class="icon_text">
           预览
          </span>
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="multi_feed_V:img:强强合作，安德烈·波切利 &amp; HAUSER -《Melodramma》" class="figure" data-float="s32491d0342" data-quickopen="true" href="https://v.qq.com/x/page/s32491d0342.html" tabindex="-1" target="_blank">
         <img alt="强强合作，安德烈·波切利 &amp; HAUSER -《Melodramma》" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo_ori/0/s32491d0342_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
         <div class="figure_caption">
          04:13
         </div>
        </a>
        <div class="figure_detail figure_detail_two_row figure_detail_preview">
         <a _stat="multi_feed_V:title:强强合作，安德烈·波切利 &amp; HAUSER -《Melodramma》" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/s32491d0342.html" target="_blank" title="强强合作，安德烈·波切利 &amp; HAUSER -《Melodramma》">
          强强合作，安德烈·波切利 &amp; HAUSER -《Melodramma》
         </a>
         <div class="figure_btn_preview figure_btn_preview_s32491d0342" data-vid="s32491d0342">
          <svg class="svg_icon svg_icon_preview" height="15" viewbox="0 0 17 15" width="17">
           <use xlink:href="#svg_icon_preview">
           </use>
          </svg>
          <span class="icon_text">
           预览
          </span>
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="multi_feed_V:img:湖畔落日，晚霞似火 |简单绘画教程" class="figure" data-float="m3259ulb7sj" data-quickopen="true" href="https://v.qq.com/x/page/m3259ulb7sj.html" tabindex="-1" target="_blank">
         <img alt="湖畔落日，晚霞似火 |简单绘画教程" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo_ori/0/m3259ulb7sj_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
         <div class="figure_caption">
          05:07
         </div>
        </a>
        <div class="figure_detail figure_detail_two_row figure_detail_preview">
         <a _stat="multi_feed_V:title:湖畔落日，晚霞似火 |简单绘画教程" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/m3259ulb7sj.html" target="_blank" title="湖畔落日，晚霞似火 |简单绘画教程">
          湖畔落日，晚霞似火 |简单绘画教程
         </a>
         <div class="figure_btn_preview figure_btn_preview_m3259ulb7sj" data-vid="m3259ulb7sj">
          <svg class="svg_icon svg_icon_preview" height="15" viewbox="0 0 17 15" width="17">
           <use xlink:href="#svg_icon_preview">
           </use>
          </svg>
          <span class="icon_text">
           预览
          </span>
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="multi_feed_V:img:TeamLab-世界遗产东寺的数字光影秀" class="figure" data-float="y32665eagj1" data-quickopen="true" href="https://v.qq.com/x/page/y32665eagj1.html" tabindex="-1" target="_blank">
         <img alt="TeamLab-世界遗产东寺的数字光影秀" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo_ori/0/y32665eagj1_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
         <div class="figure_caption">
          03:18
         </div>
        </a>
        <div class="figure_detail figure_detail_two_row figure_detail_preview">
         <a _stat="multi_feed_V:title:TeamLab-世界遗产东寺的数字光影秀" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/y32665eagj1.html" target="_blank" title="TeamLab-世界遗产东寺的数字光影秀">
          TeamLab-世界遗产东寺的数字光影秀
         </a>
         <div class="figure_btn_preview figure_btn_preview_y32665eagj1" data-vid="y32665eagj1">
          <svg class="svg_icon svg_icon_preview" height="15" viewbox="0 0 17 15" width="17">
           <use xlink:href="#svg_icon_preview">
           </use>
          </svg>
          <span class="icon_text">
           预览
          </span>
         </div>
        </div>
       </div>
      </div>
     </div>
    </div>
   </div>
  </div>
  <div _expose="new_vs_hot_tv" _wind="columnname=精选_同步剧场&amp;controlname=new_vs_hot_tv" class="mod_row_box" cur-page-num="0" data-context="2" data-istyle="8" has-next-page="false" id="new_vs_hot_tv">
   <div class="mod_bd cf _quickopen _quickopen_duration">
    <div class="mod_column_main">
     <div class="mod_hd mod_column_hd">
      <h2 class="mod_title">
       <a _stat="new_vs_hot_tv:通栏功能区:通栏标题" class="title_link" data-target="_blank" href="https://v.qq.com/channel/tv">
        同步剧场
       </a>
      </h2>
      <div class="mod_page_small">
       <button _stat="new_vs_hot_tv:通栏功能区:上一页" class="btn_prev disabled" title="上一页" wind-click="100">
        <svg class="svg_icon svg_icon_prev" height="10" viewbox="0 0 6 10" width="6">
         <path d="M1.4 4.7L5 1M1.3 5.3L5 9" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="1.4">
         </path>
        </svg>
       </button>
       <span class="page_num" data-count="2" data-info="12 18" data-page="1">
        1/2
       </span>
       <button _stat="new_vs_hot_tv:通栏功能区:下一页" class="btn_next" title="下一页" wind-click="100">
        <svg class="svg_icon svg_icon_next" height="10" viewbox="0 0 6 10" width="6">
         <path d="M4.6 4.7L1 1M4.7 5.3L1 9" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="1.4">
         </path>
        </svg>
       </button>
      </div>
     </div>
     <div class="mod_column_bd">
      <div class="mod_figure mod_figure_v_default mod_figure_v_default_2row mod_figure_v_default" data-rowcount="6" data-rowlen="2">
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_tv:img:良言写意" class="figure" data-float="mzc00200ev05cth" href="https://v.qq.com/x/cover/mzc00200ev05cth.html" tabindex="-1" target="_blank">
         <img alt="良言写意" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/mzc00200ev05cth1638169421944/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
         <div class="figure_caption">
          更新至12集
         </div>
         <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_tv:title:良言写意" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200ev05cth.html" target="_blank" title="良言写意">
          良言写意
         </a>
         <div class="figure_desc" title="罗云熙程潇高颜值蜜恋">
          罗云熙程潇高颜值蜜恋
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_tv:img:爱很美味" class="figure" data-float="mzc00200kqq8aps" href="https://v.qq.com/x/cover/mzc00200kqq8aps.html" tabindex="-1" target="_blank">
         <img alt="爱很美味" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/mzc00200kqq8aps1637163733151/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
         <div class="figure_caption">
          更新至10集
         </div>
         <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_tv:title:爱很美味" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200kqq8aps.html" target="_blank" title="爱很美味">
          爱很美味
         </a>
         <div class="figure_desc" title="豆瓣高分！都市姐妹飒爽追爱">
          豆瓣高分！都市姐妹飒爽追爱
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_tv:img:陪你逐风飞翔" class="figure" data-float="mzc00200dd5r9fv" href="https://v.qq.com/x/cover/mzc00200dd5r9fv.html" tabindex="-1" target="_blank">
         <img alt="陪你逐风飞翔" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/mzc00200dd5r9fv1637294235803/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
         <div class="figure_caption">
          更新至19集
         </div>
         <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_tv:title:陪你逐风飞翔" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200dd5r9fv.html" target="_blank" title="陪你逐风飞翔">
          陪你逐风飞翔
         </a>
         <div class="figure_desc" title="宋祖儿王安宇冬日甜恋">
          宋祖儿王安宇冬日甜恋
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_tv:img:斛珠夫人" class="figure" data-float="mzc00200prv7r23" href="https://v.qq.com/x/cover/mzc00200prv7r23.html" tabindex="-1" target="_blank">
         <img alt="斛珠夫人" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/mzc00200prv7r231636526271896/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
         <div class="figure_caption">
          更新至42集
         </div>
         <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_tv:title:斛珠夫人" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200prv7r23.html" target="_blank" title="斛珠夫人">
          斛珠夫人
         </a>
         <div class="figure_desc" title="杨幂陈伟霆破命运相恋">
          杨幂陈伟霆破命运相恋
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_tv:img:不惑之旅" class="figure" data-float="mzc0020053nri1m" href="https://v.qq.com/x/cover/mzc0020053nri1m.html" tabindex="-1" target="_blank">
         <img alt="不惑之旅" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/mzc0020053nri1m1636945575021/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
         <div class="figure_caption">
          更新至28集
         </div>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_tv:title:不惑之旅" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc0020053nri1m.html" target="_blank" title="不惑之旅">
          不惑之旅
         </a>
         <div class="figure_desc" title="陈建斌梅婷中年爱情太好嗑">
          陈建斌梅婷中年爱情太好嗑
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_tv:img:池塘怪谈" class="figure" data-float="mzc00200df196we" href="https://v.qq.com/x/cover/mzc00200df196we.html" tabindex="-1" target="_blank">
         <img alt="池塘怪谈" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/mzc00200df196we1638236174071/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
         <div class="figure_caption">
          全10集
         </div>
         <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_tv:title:池塘怪谈" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200df196we.html" target="_blank" title="池塘怪谈">
          池塘怪谈
         </a>
         <div class="figure_desc" title="吴青峰携鱼团开启奇幻之旅">
          吴青峰携鱼团开启奇幻之旅
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_tv:img:当家主母" class="figure" data-float="mzc00200roxc0ff" href="https://v.qq.com/x/cover/mzc00200roxc0ff.html" tabindex="-1" target="_blank">
         <img alt="当家主母" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/mzc00200roxc0ff1635388771310/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
         <div class="figure_caption">
          全35集
         </div>
         <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_tv:title:当家主母" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200roxc0ff.html" target="_blank" title="当家主母">
          当家主母
         </a>
         <div class="figure_desc" title="蒋勤勤深宅大院爱恨纠缠">
          蒋勤勤深宅大院爱恨纠缠
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_tv:img:漫撕男[短剧上新]" class="figure" data-float="mzc002002wuoh5b" href="https://v.qq.com/x/cover/mzc002002wuoh5b.html" tabindex="-1" target="_blank">
         <img alt="漫撕男[短剧上新]" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/mzc002002wuoh5b1637563033340/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
         <div class="figure_caption">
          更新至12集
         </div>
         <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_tv:title:漫撕男[短剧上新]" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc002002wuoh5b.html" target="_blank" title="漫撕男[短剧上新]">
          漫撕男[短剧上新]
         </a>
         <div class="figure_desc" title="狼系漫撕男跨界之恋">
          狼系漫撕男跨界之恋
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_tv:img:北洋残案" class="figure" data-float="mzc00200bu5eopx" href="https://v.qq.com/x/cover/mzc00200bu5eopx.html" tabindex="-1" target="_blank">
         <img alt="北洋残案" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/mzc00200bu5eopx1636528493985/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
         <div class="figure_caption">
          全12集
         </div>
         <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_tv:title:北洋残案" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200bu5eopx.html" target="_blank" title="北洋残案">
          北洋残案
         </a>
         <div class="figure_desc" title="低能侦探破连环自杀奇案">
          低能侦探破连环自杀奇案
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_tv:img:撩动心弦·短剧" class="figure" data-float="mzc00200rzjtws6" href="https://v.qq.com/x/cover/mzc00200rzjtws6.html" tabindex="-1" target="_blank">
         <img alt="撩动心弦·短剧" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/mzc00200rzjtws61637057949697/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
         <div class="figure_caption">
          全30集
         </div>
         <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_tv:title:撩动心弦·短剧" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200rzjtws6.html" target="_blank" title="撩动心弦·短剧">
          撩动心弦·短剧
         </a>
         <div class="figure_desc" title="千金嫡女变丫鬟上演逆袭复仇">
          千金嫡女变丫鬟上演逆袭复仇
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_tv:img:和平之舟" class="figure" data-float="mzc00200ctufml7" href="https://v.qq.com/x/cover/mzc00200ctufml7.html" tabindex="-1" target="_blank">
         <img alt="和平之舟" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/mzc00200ctufml71635859675854/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
         <div class="figure_caption">
          全32集
         </div>
         <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_tv:title:和平之舟" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200ctufml7.html" target="_blank" title="和平之舟">
          和平之舟
         </a>
         <div class="figure_desc" title="陈坤张天爱演绎海上救援">
          陈坤张天爱演绎海上救援
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_tv:img:替身姐妹[短剧上新]" class="figure" data-float="mzc00200c9cpfxs" href="https://v.qq.com/x/cover/mzc00200c9cpfxs.html" tabindex="-1" target="_blank">
         <img alt="替身姐妹[短剧上新]" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/mzc00200c9cpfxs1636081841914/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
         <div class="figure_caption">
          全40集
         </div>
         <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_tv:title:替身姐妹[短剧上新]" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200c9cpfxs.html" target="_blank" title="替身姐妹[短剧上新]">
          替身姐妹[短剧上新]
         </a>
         <div class="figure_desc" title="双胞胎互换人生">
          双胞胎互换人生
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_tv:img:梦见狮子" class="figure" data-float="mzc00200sism3bx" href="https://v.qq.com/x/cover/mzc00200sism3bx.html" tabindex="-1" target="_blank">
         <img alt="梦见狮子" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/mzc00200sism3bx1635388700402/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
         <div class="figure_caption">
          全30集
         </div>
         <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_tv:title:梦见狮子" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200sism3bx.html" target="_blank" title="梦见狮子">
          梦见狮子
         </a>
         <div class="figure_desc" title="姚弛陈雨锶跨次元联动">
          姚弛陈雨锶跨次元联动
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_tv:img:浮尘下的枪声" class="figure" data-float="mzc00200psxum4j" href="https://v.qq.com/x/cover/mzc00200psxum4j.html" tabindex="-1" target="_blank">
         <img alt="浮尘下的枪声" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/mzc00200psxum4j1637030205536/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
         <div class="figure_caption">
          更新至20集
         </div>
         <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_tv:title:浮尘下的枪声" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200psxum4j.html" target="_blank" title="浮尘下的枪声">
          浮尘下的枪声
         </a>
         <div class="figure_desc" title="一场正义与邪恶的较量">
          一场正义与邪恶的较量
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_tv:img:永不者1（上）" class="figure" data-float="mzc00200umgk074" href="https://v.qq.com/x/cover/mzc00200umgk074.html" tabindex="-1" target="_blank">
         <img alt="永不者1（上）" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/mzc00200umgk0741635910803608/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
         <div class="figure_caption">
          更新至04集
         </div>
         <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_tv:title:永不者1（上）" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200umgk074.html" target="_blank" title="永不者1（上）">
          永不者1（上）
         </a>
         <div class="figure_desc" title="20点独播 超能力美少女">
          20点独播 超能力美少女
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_tv:img:管你来自哪颗星" class="figure" data-float="mzc00200b5fbw8s" href="https://v.qq.com/x/cover/mzc00200b5fbw8s.html" tabindex="-1" target="_blank">
         <img alt="管你来自哪颗星" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/mzc00200b5fbw8s1635850225668/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
         <div class="figure_caption">
          全30集
         </div>
         <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_tv:title:管你来自哪颗星" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200b5fbw8s.html" target="_blank" title="管你来自哪颗星">
          管你来自哪颗星
         </a>
         <div class="figure_desc" title="短剧版“星你”">
          短剧版“星你”
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_tv:img:前行者" class="figure" data-float="mzc00200og22jqj" href="https://v.qq.com/x/cover/mzc00200og22jqj.html" tabindex="-1" target="_blank">
         <img alt="前行者" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_vt_pic/0/mzc00200og22jqj1634884397644/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
         <div class="figure_caption">
          全40集
         </div>
         <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_tv:title:前行者" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200og22jqj.html" target="_blank" title="前行者">
          前行者
         </a>
         <div class="figure_desc" title="潜伏原著作者最新力作">
          潜伏原著作者最新力作
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_tv:img:突围" class="figure" data-float="p4oc75vffwfh1lp" href="https://v.qq.com/x/cover/p4oc75vffwfh1lp.html" tabindex="-1" target="_blank">
         <img alt="突围" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_vt_pic/0/p4oc75vffwfh1lp1634263990929/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
         <div class="figure_caption">
          全45集
         </div>
         <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_tv:title:突围" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/p4oc75vffwfh1lp.html" target="_blank" title="突围">
          突围
         </a>
         <div class="figure_desc" title="靳东闫妮揭5亿巨款之谜">
          靳东闫妮揭5亿巨款之谜
         </div>
        </div>
       </div>
      </div>
     </div>
    </div>
    <div class="mod_column_side">
     <div class="mod_hd mod_column_hd">
      <h2 class="mod_title">
       电视剧热播排行榜
      </h2>
      <div class="bg_rank_ball">
      </div>
      <div class="mod_hd_action">
       <a _stat="new_vs_hot_tv:通栏功能区:更多" class="action_item" href="https://v.qq.com/biu/ranks/?t=hotplay">
        更多
        <svg class="svg_icon svg_icon_next" height="10" viewbox="0 0 6 10" width="6">
         <path d="M4.6 4.7L1 1M4.7 5.3L1 9" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="1.4">
         </path>
        </svg>
       </a>
      </div>
     </div>
     <div class="mod_rank_list mod_rank_list_1column">
      <a __wind="" class="rank_item rank_item_1 cf" href="https://v.qq.com/x/cover/mzc00200prv7r23.html" title="斛珠夫人">
       <span class="rank_num rank_num_1">
        1
       </span>
       <span class="rank_title">
        斛珠夫人
       </span>
       <span class="rank_desc">
        杨幂陈伟霆破命运相恋
       </span>
       <span class="rank_update">
        更新至42集
       </span>
      </a>
      <a __wind="" class="rank_item rank_item_2 cf" href="https://v.qq.com/x/cover/mzc00200dd5r9fv.html" title="陪你逐风飞翔">
       <span class="rank_num rank_num_2">
        2
       </span>
       <span class="rank_title">
        陪你逐风飞翔
       </span>
       <span class="rank_desc">
        宋祖儿王安宇冬日甜恋
       </span>
       <span class="rank_update">
        更新至19集
       </span>
      </a>
      <a __wind="" class="rank_item rank_item_3 cf" href="https://v.qq.com/x/cover/mzc00200roxc0ff.html" title="当家主母">
       <span class="rank_num rank_num_3">
        3
       </span>
       <span class="rank_title">
        当家主母
       </span>
       <span class="rank_desc">
        蒋勤勤深宅大院爱恨纠缠
       </span>
       <span class="rank_update">
        全35集
       </span>
      </a>
      <a __wind="" class="rank_item rank_item_4 cf" href="https://v.qq.com/x/cover/mzc0020053nri1m.html" title="不惑之旅">
       <span class="rank_num rank_num_4">
        4
       </span>
       <span class="rank_title">
        不惑之旅
       </span>
       <span class="rank_desc">
        陈建斌梅婷中年追爱
       </span>
       <span class="rank_update">
        更新至28集
       </span>
      </a>
      <a __wind="" class="rank_item rank_item_5 cf" href="https://v.qq.com/x/cover/mzc00200o94tdv2.html" title="嘉南传">
       <span class="rank_num rank_num_5">
        5
       </span>
       <span class="rank_title">
        嘉南传
       </span>
       <span class="rank_desc">
        鞠婧祎曾舜晞郡主爱上侍卫
       </span>
       <span class="rank_update">
        全40集
       </span>
      </a>
      <a __wind="" class="rank_item rank_item_6 cf" href="https://v.qq.com/x/cover/p4oc75vffwfh1lp.html" title="突围">
       <span class="rank_num rank_num_6">
        6
       </span>
       <span class="rank_title">
        突围
       </span>
       <span class="rank_desc">
        靳东闫妮揭5亿巨款之谜
       </span>
       <span class="rank_update">
        全45集
       </span>
      </a>
      <a __wind="" class="rank_item rank_item_7 cf" href="https://v.qq.com/x/cover/mzc00200kqq8aps.html" title="爱很美味">
       <span class="rank_num rank_num_7">
        7
       </span>
       <span class="rank_title">
        爱很美味
       </span>
       <span class="rank_desc">
        玩味姐妹追爱作战太过瘾
       </span>
       <span class="rank_update">
        更新至10集
       </span>
      </a>
      <a __wind="" class="rank_item rank_item_8 cf" href="https://v.qq.com/x/cover/mzc00200xh9313v.html" title="你是我的荣耀">
       <span class="rank_num rank_num_8">
        8
       </span>
       <span class="rank_title">
        你是我的荣耀
       </span>
       <span class="rank_desc">
        杨洋迪丽热巴共谱浪漫爱情
       </span>
       <span class="rank_update">
        全32集
       </span>
      </a>
      <a __wind="" class="rank_item rank_item_9 cf" href="https://v.qq.com/x/cover/0pj8vuntnocu797.html" title="三十而已">
       <span class="rank_num rank_num_9">
        9
       </span>
       <span class="rank_title">
        三十而已
       </span>
       <span class="rank_desc">
        江疏影童瑶毛晓彤直面女性困境
       </span>
       <span class="rank_update">
        全43集
       </span>
      </a>
      <a __wind="" class="rank_item rank_item_10 cf" href="https://v.qq.com/x/cover/mzc00200ev05cth.html" title="良言写意">
       <span class="rank_num rank_num_10">
        10
       </span>
       <span class="rank_title">
        良言写意
       </span>
       <span class="rank_desc">
        罗云熙程潇甜蜜满分
       </span>
       <span class="rank_update">
        更新至12集
       </span>
      </a>
     </div>
    </div>
   </div>
  </div>
  <div _expose="new_vs_hot_movie" _wind="columnname=精选_电影&amp;controlname=new_vs_hot_movie" class="mod_row_box" cur-page-num="0" data-context="2" data-istyle="8" has-next-page="false" id="new_vs_hot_movie">
   <div class="mod_bd cf _quickopen _quickopen_duration">
    <div class="mod_column_main">
     <div class="mod_hd mod_column_hd">
      <h2 class="mod_title">
       <a _stat="new_vs_hot_movie:通栏功能区:通栏标题" class="title_link" data-target="_blank" href="https://v.qq.com/channel/movie">
        电影
       </a>
      </h2>
      <div class="mod_page_small">
       <button _stat="new_vs_hot_movie:通栏功能区:上一页" class="btn_prev disabled" title="上一页" wind-click="100">
        <svg class="svg_icon svg_icon_prev" height="10" viewbox="0 0 6 10" width="6">
         <path d="M1.4 4.7L5 1M1.3 5.3L5 9" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="1.4">
         </path>
        </svg>
       </button>
       <span class="page_num" data-count="2" data-info="12 18" data-page="1">
        1/2
       </span>
       <button _stat="new_vs_hot_movie:通栏功能区:下一页" class="btn_next" title="下一页" wind-click="100">
        <svg class="svg_icon svg_icon_next" height="10" viewbox="0 0 6 10" width="6">
         <path d="M4.6 4.7L1 1M4.7 5.3L1 9" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="1.4">
         </path>
        </svg>
       </button>
      </div>
     </div>
     <div class="mod_column_bd">
      <div class="mod_figure mod_figure_v_default mod_figure_v_default_2row mod_figure_v_default" data-rowcount="6" data-rowlen="2">
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_movie:img:末日救援·灾难大片" class="figure" data-float="mzc00200mcm0lzz" href="https://v.qq.com/x/cover/mzc00200mcm0lzz.html" tabindex="-1" target="_blank">
         <img alt="末日救援·灾难大片" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/mzc00200mcm0lzz1638328943230/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
         <div class="figure_caption">
          01:31:09
         </div>
         <div class="figure_score">
          7.9
         </div>
         <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_movie:title:末日救援·灾难大片" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200mcm0lzz.html" target="_blank" title="末日救援·灾难大片">
          末日救援·灾难大片
         </a>
         <div class="figure_desc" title="中国战士对抗外星虫群！">
          中国战士对抗外星虫群！
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_movie:img:南希·德鲁与隐藏的楼梯" class="figure" data-float="mzc00200kp2bkpt" href="https://v.qq.com/x/cover/mzc00200kp2bkpt.html" tabindex="-1" target="_blank">
         <img alt="南希·德鲁与隐藏的楼梯" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/mzc00200kp2bkpt1638169732373/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
         <div class="figure_caption">
          01:25:26
         </div>
         <img alt="付费" class="mark_v mark_v_付费" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_pay_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_pay_x2.png 2x"/>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_movie:title:南希·德鲁与隐藏的楼梯" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200kp2bkpt.html" target="_blank" title="南希·德鲁与隐藏的楼梯">
          南希·德鲁与隐藏的楼梯
         </a>
         <div class="figure_desc" title="阁楼里的神秘事件">
          阁楼里的神秘事件
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_movie:img:二捕出山" class="figure" data-float="mzc00200tz3zq5m" href="https://v.qq.com/x/cover/mzc00200tz3zq5m.html" tabindex="-1" target="_blank">
         <img alt="二捕出山" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/mzc00200tz3zq5m1637551921833/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
         <div class="figure_caption">
          01:18:53
         </div>
         <div class="figure_score">
          7.7
         </div>
         <img alt="独播" class="mark_v mark_v_独播" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_only_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_only_x2.png 2x"/>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_movie:title:二捕出山" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200tz3zq5m.html" target="_blank" title="二捕出山">
          二捕出山
         </a>
         <div class="figure_desc" title="镖师救太子笑料百出">
          镖师救太子笑料百出
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_movie:img:名侦探柯南：绯色的子弹" class="figure" data-float="mzc002001m5wxlo" href="https://v.qq.com/x/cover/mzc002001m5wxlo.html" tabindex="-1" target="_blank">
         <img alt="名侦探柯南：绯色的子弹" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/mzc002001m5wxlo1617767537512/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
         <div class="figure_caption">
          01:49:48
         </div>
         <div class="figure_score">
          7.6
         </div>
         <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_movie:title:名侦探柯南：绯色的子弹" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc002001m5wxlo.html" target="_blank" title="名侦探柯南：绯色的子弹">
          名侦探柯南：绯色的子弹
         </a>
         <div class="figure_desc" title="最强组合为正义而战">
          最强组合为正义而战
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_movie:img:神龟岛" class="figure" data-float="mzc00200j13nsmc" href="https://v.qq.com/x/cover/mzc00200j13nsmc.html" tabindex="-1" target="_blank">
         <img alt="神龟岛" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/mzc00200j13nsmc1637890693861/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
         <div class="figure_caption">
          01:08:41
         </div>
         <div class="figure_score">
          7.7
         </div>
         <img alt="独播" class="mark_v mark_v_独播" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_only_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_only_x2.png 2x"/>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_movie:title:神龟岛" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200j13nsmc.html" target="_blank" title="神龟岛">
          神龟岛
         </a>
         <div class="figure_desc" title="仙侠CP携手斗巨龟">
          仙侠CP携手斗巨龟
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_movie:img:明日之战" class="figure" data-float="mzc00200qlqx97g" href="https://v.qq.com/x/cover/mzc00200qlqx97g.html" tabindex="-1" target="_blank">
         <img alt="明日之战" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/mzc00200qlqx97g1637656896964/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
         <div class="figure_caption">
          02:17:37
         </div>
         <div class="figure_score">
          7.7
         </div>
         <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_movie:title:明日之战" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200qlqx97g.html" target="_blank" title="明日之战">
          明日之战
         </a>
         <div class="figure_desc" title="星爵大战外星生物白长钉">
          星爵大战外星生物白长钉
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_movie:img:嫌疑人之长夜将尽" class="figure" data-float="mzc00200mbkh5o2" href="https://v.qq.com/x/cover/mzc00200mbkh5o2.html" tabindex="-1" target="_blank">
         <img alt="嫌疑人之长夜将尽" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/mzc00200mbkh5o21637828282646/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
         <div class="figure_caption">
          01:32:56
         </div>
         <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_movie:title:嫌疑人之长夜将尽" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200mbkh5o2.html" target="_blank" title="嫌疑人之长夜将尽">
          嫌疑人之长夜将尽
         </a>
         <div class="figure_desc" title="超强记忆警官破案中案">
          超强记忆警官破案中案
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_movie:img:寻龙之发丘天棺" class="figure" data-float="mzc002006fqrk2l" href="https://v.qq.com/x/cover/mzc002006fqrk2l.html" tabindex="-1" target="_blank">
         <img alt="寻龙之发丘天棺" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/mzc002006fqrk2l1636704829621/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
         <div class="figure_caption">
          01:19:44
         </div>
         <div class="figure_score">
          7.7
         </div>
         <img alt="独播" class="mark_v mark_v_独播" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_only_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_only_x2.png 2x"/>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_movie:title:寻龙之发丘天棺" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc002006fqrk2l.html" target="_blank" title="寻龙之发丘天棺">
          寻龙之发丘天棺
         </a>
         <div class="figure_desc" title="万年古墓惊现食人巨蛇">
          万年古墓惊现食人巨蛇
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_movie:img:生生" class="figure" data-float="mzc00200zhhd7m3" href="https://v.qq.com/x/cover/mzc00200zhhd7m3.html" tabindex="-1" target="_blank">
         <img alt="生生" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/mzc00200zhhd7m31637302973985/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
         <div class="figure_caption">
          01:36:42
         </div>
         <div class="figure_score">
          7.5
         </div>
         <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_movie:title:生生" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200zhhd7m3.html" target="_blank" title="生生">
          生生
         </a>
         <div class="figure_desc" title="与最爱的人说“我爱你”">
          与最爱的人说“我爱你”
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_movie:img:天堂电影院" class="figure" data-float="cj48e9olxbbjiq7" href="https://v.qq.com/x/cover/cj48e9olxbbjiq7.html" tabindex="-1" target="_blank">
         <img alt="天堂电影院" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/cj48e9olxbbjiq71637046842057/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
         <div class="figure_caption">
          02:03:24
         </div>
         <div class="figure_score">
          9.4
         </div>
         <img alt="独播" class="mark_v mark_v_独播" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_only_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_only_x2.png 2x"/>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_movie:title:天堂电影院" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/cj48e9olxbbjiq7.html" target="_blank" title="天堂电影院">
          天堂电影院
         </a>
         <div class="figure_desc" title="有梦想的地方就有天堂">
          有梦想的地方就有天堂
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_movie:img:不速来客" class="figure" data-float="mzc00200svcvjv2" href="https://v.qq.com/x/cover/mzc00200svcvjv2.html" tabindex="-1" target="_blank">
         <img alt="不速来客" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/mzc00200svcvjv21637458776951/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
         <div class="figure_caption">
          01:46:01
         </div>
         <div class="figure_score">
          7.8
         </div>
         <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_movie:title:不速来客" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200svcvjv2.html" target="_blank" title="不速来客">
          不速来客
         </a>
         <div class="figure_desc" title="范伟窦骁张颂文演绎悬疑喜剧">
          范伟窦骁张颂文演绎悬疑喜剧
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_movie:img:巨兽岛" class="figure" data-float="mzc002004rm13qi" href="https://v.qq.com/x/cover/mzc002004rm13qi.html" tabindex="-1" target="_blank">
         <img alt="巨兽岛" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/mzc002004rm13qi1636619774567/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
         <div class="figure_caption">
          01:11:53
         </div>
         <div class="figure_score">
          7.7
         </div>
         <img alt="独播" class="mark_v mark_v_独播" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_only_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_only_x2.png 2x"/>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_movie:title:巨兽岛" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc002004rm13qi.html" target="_blank" title="巨兽岛">
          巨兽岛
         </a>
         <div class="figure_desc" title="王者争霸！谁是怪兽一哥？">
          王者争霸！谁是怪兽一哥？
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_movie:img:混沌行走" class="figure" data-float="mzc00200hdpza6k" href="https://v.qq.com/x/cover/mzc00200hdpza6k.html" tabindex="-1" target="_blank">
         <img alt="混沌行走" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/mzc00200hdpza6k1637372921980/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
         <div class="figure_caption">
          01:48:58
         </div>
         <div class="figure_score">
          7.7
         </div>
         <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_movie:title:混沌行走" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200hdpza6k.html" target="_blank" title="混沌行走">
          混沌行走
         </a>
         <div class="figure_desc" title="荷兰弟感染“噪音”病毒">
          荷兰弟感染“噪音”病毒
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_movie:img:保安日记" class="figure" data-float="mzc00200rf3dccm" href="https://v.qq.com/x/cover/mzc00200rf3dccm.html" tabindex="-1" target="_blank">
         <img alt="保安日记" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/mzc00200rf3dccm1636689754088/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
         <div class="figure_caption">
          01:10:09
         </div>
         <div class="figure_score">
          7.8
         </div>
         <img alt="独播" class="mark_v mark_v_独播" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_only_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_only_x2.png 2x"/>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_movie:title:保安日记" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200rf3dccm.html" target="_blank" title="保安日记">
          保安日记
         </a>
         <div class="figure_desc" title="宋晓峰爆笑护宝擒贼王">
          宋晓峰爆笑护宝擒贼王
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_movie:img:冬去冬又来" class="figure" data-float="mzc00200d85e2ib" href="https://v.qq.com/x/cover/mzc00200d85e2ib.html" tabindex="-1" target="_blank">
         <img alt="冬去冬又来" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/mzc00200d85e2ib1636092178869/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
         <div class="figure_caption">
          01:49:14
         </div>
         <div class="figure_score">
          7.5
         </div>
         <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_movie:title:冬去冬又来" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200d85e2ib.html" target="_blank" title="冬去冬又来">
          冬去冬又来
         </a>
         <div class="figure_desc" title="战争时期命运几经沉浮">
          战争时期命运几经沉浮
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_movie:img:无所依靠" class="figure" data-float="mzc00200u4wad8r" href="https://v.qq.com/x/cover/mzc00200u4wad8r.html" tabindex="-1" target="_blank">
         <img alt="无所依靠" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/mzc00200u4wad8r1637252641800/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
         <div class="figure_caption">
          01:26:46
         </div>
         <div class="figure_score">
          7.6
         </div>
         <img alt="付费" class="mark_v mark_v_付费" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_pay_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_pay_x2.png 2x"/>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_movie:title:无所依靠" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200u4wad8r.html" target="_blank" title="无所依靠">
          无所依靠
         </a>
         <div class="figure_desc" title="老实人被欺开启杀神模式">
          老实人被欺开启杀神模式
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_movie:img:皮皮鲁与鲁西西之罐头小人" class="figure" data-float="mzc00200kf6p1kk" href="https://v.qq.com/x/cover/mzc00200kf6p1kk.html" tabindex="-1" target="_blank">
         <img alt="皮皮鲁与鲁西西之罐头小人" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_vt_pic/0/mzc00200kf6p1kk1635493930889/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
         <div class="figure_caption">
          01:33:58
         </div>
         <div class="figure_score">
          7.6
         </div>
         <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_movie:title:皮皮鲁与鲁西西之罐头小人" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200kf6p1kk.html" target="_blank" title="皮皮鲁与鲁西西之罐头小人">
          皮皮鲁与鲁西西之罐头小人
         </a>
         <div class="figure_desc" title="郑渊洁经典童话改编">
          郑渊洁经典童话改编
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_movie:img:南海鲛人" class="figure" data-float="mzc00200wryter9" href="https://v.qq.com/x/cover/mzc00200wryter9.html" tabindex="-1" target="_blank">
         <img alt="南海鲛人" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_vt_pic/0/mzc00200wryter91636718809500/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
         <div class="figure_caption">
          01:18:12
         </div>
         <div class="figure_score">
          7.7
         </div>
         <img alt="独播" class="mark_v mark_v_独播" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_only_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_only_x2.png 2x"/>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_movie:title:南海鲛人" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200wryter9.html" target="_blank" title="南海鲛人">
          南海鲛人
         </a>
         <div class="figure_desc" title="神秘水怪强掳新婚少女">
          神秘水怪强掳新婚少女
         </div>
        </div>
       </div>
      </div>
     </div>
    </div>
    <div class="mod_column_side">
     <div class="mod_hd mod_column_hd">
      <h2 class="mod_title">
       电影热播排行榜
      </h2>
      <div class="bg_rank_ball">
      </div>
      <div class="mod_hd_action">
       <a _stat="new_vs_hot_movie:通栏功能区:更多" class="action_item" href="https://v.qq.com/x/rank/#movie">
        更多
        <svg class="svg_icon svg_icon_next" height="10" viewbox="0 0 6 10" width="6">
         <path d="M4.6 4.7L1 1M4.7 5.3L1 9" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="1.4">
         </path>
        </svg>
       </a>
      </div>
     </div>
     <div class="mod_rank_list mod_rank_list_1column">
      <a __wind="" class="rank_item rank_item_1 cf" href="https://v.qq.com/x/cover/mzc00200qlqx97g.html" title="明日之战">
       <span class="rank_num rank_num_1">
        1
       </span>
       <span class="rank_title">
        明日之战
       </span>
       <span class="rank_desc">
        星爵大战外星生物白长钉
       </span>
       <span class="rank_update">
       </span>
      </a>
      <a __wind="" class="rank_item rank_item_2 cf" href="https://v.qq.com/x/cover/pb69zpzabgg1t7n.html" title="哈利·波特与魔法石">
       <span class="rank_num rank_num_2">
        2
       </span>
       <span class="rank_title">
        哈利·波特与魔法石
       </span>
       <span class="rank_desc">
        格兰芬多铁三角组合萌翻了
       </span>
       <span class="rank_update">
        159
       </span>
      </a>
      <a __wind="" class="rank_item rank_item_3 cf" href="https://v.qq.com/x/cover/mzc00200j13nsmc.html" title="神龟岛">
       <span class="rank_num rank_num_3">
        3
       </span>
       <span class="rank_title">
        神龟岛
       </span>
       <span class="rank_desc">
        仙侠CP携手斗巨龟
       </span>
       <span class="rank_update">
       </span>
      </a>
      <a __wind="" class="rank_item rank_item_4 cf" href="https://v.qq.com/x/cover/mzc002001m5wxlo.html" title="名侦探柯南：绯色的子弹">
       <span class="rank_num rank_num_4">
        4
       </span>
       <span class="rank_title">
        名侦探柯南：绯色的子弹
       </span>
       <span class="rank_desc">
        最强组合为正义而战
       </span>
       <span class="rank_update">
       </span>
      </a>
      <a __wind="" class="rank_item rank_item_5 cf" href="https://v.qq.com/x/cover/mzc00200oa8qvnd.html" title="图兰朵：魔咒缘起">
       <span class="rank_num rank_num_5">
        5
       </span>
       <span class="rank_title">
        图兰朵：魔咒缘起
       </span>
       <span class="rank_desc">
        关晓彤破爱情诅咒
       </span>
       <span class="rank_update">
       </span>
      </a>
      <a __wind="" class="rank_item rank_item_6 cf" href="https://v.qq.com/x/cover/96sxjj429lictza.html" title="蜘蛛侠：英雄远征">
       <span class="rank_num rank_num_6">
        6
       </span>
       <span class="rank_title">
        蜘蛛侠：英雄远征
       </span>
       <span class="rank_desc">
        小蜘蛛侠开启全新旅程
       </span>
       <span class="rank_update">
       </span>
      </a>
      <a __wind="" class="rank_item rank_item_7 cf" href="https://v.qq.com/x/cover/mcmdrpnv9n82jnc.html" title="日常幻想指南">
       <span class="rank_num rank_num_7">
        7
       </span>
       <span class="rank_title">
        日常幻想指南
       </span>
       <span class="rank_desc">
        王彦霖遭雷劈获得超能力
       </span>
       <span class="rank_update">
       </span>
      </a>
      <a __wind="" class="rank_item rank_item_8 cf" href="https://v.qq.com/x/cover/mzc002004rm13qi.html" title="巨兽岛">
       <span class="rank_num rank_num_8">
        8
       </span>
       <span class="rank_title">
        巨兽岛
       </span>
       <span class="rank_desc">
        王者争霸！谁是怪兽一哥？
       </span>
       <span class="rank_update">
       </span>
      </a>
      <a __wind="" class="rank_item rank_item_9 cf" href="https://v.qq.com/x/cover/mzc00200l2xw1x0.html" title="关于我妈的一切">
       <span class="rank_num rank_num_9">
        9
       </span>
       <span class="rank_title">
        关于我妈的一切
       </span>
       <span class="rank_desc">
        徐帆张婧仪诠释母女情
       </span>
       <span class="rank_update">
       </span>
      </a>
      <a __wind="" class="rank_item rank_item_10 cf" href="https://v.qq.com/x/cover/mzc00200svcvjv2.html" title="不速来客">
       <span class="rank_num rank_num_10">
        10
       </span>
       <span class="rank_title">
        不速来客
       </span>
       <span class="rank_desc">
        范伟窦骁张颂文演绎悬疑喜剧
       </span>
       <span class="rank_update">
       </span>
      </a>
     </div>
    </div>
   </div>
  </div>
  <div _expose="new_vs_hot_var" _wind="columnname=精选_综艺&amp;controlname=new_vs_hot_var" class="mod_row_box" cur-page-num="0" data-context="3" data-istyle="5" has-next-page="false" id="new_vs_hot_var">
   <div class="mod_bd cf _quickopen _quickopen_duration">
    <div class="mod_column_main">
     <div class="mod_hd mod_column_hd">
      <h2 class="mod_title">
       <a _stat="new_vs_hot_var:通栏功能区:通栏标题" class="title_link" data-target="_blank" href="https://v.qq.com/channel/variety">
        综艺
       </a>
      </h2>
      <div class="mod_page_small">
       <button _stat="new_vs_hot_var:通栏功能区:上一页" class="btn_prev disabled" title="上一页" wind-click="100">
        <svg class="svg_icon svg_icon_prev" height="10" viewbox="0 0 6 10" width="6">
         <path d="M1.4 4.7L5 1M1.3 5.3L5 9" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="1.4">
         </path>
        </svg>
       </button>
       <span class="page_num" data-count="2" data-info="12 18" data-page="1">
        1/2
       </span>
       <button _stat="new_vs_hot_var:通栏功能区:下一页" class="btn_next" title="下一页" wind-click="100">
        <svg class="svg_icon svg_icon_next" height="10" viewbox="0 0 6 10" width="6">
         <path d="M4.6 4.7L1 1M4.7 5.3L1 9" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="1.4">
         </path>
        </svg>
       </button>
      </div>
     </div>
     <div class="mod_column_bd">
      <div class="mod_figure mod_figure_h_default mod_figure_h_default_2row mod_figure_h_default" data-rowcount="6" data-rowlen="2">
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_var:img:大伙之家·更新" class="figure" data-float="mzc00200mquy6aa" href="http://v.qq.com/x/cover/mzc00200mquy6aa/d0041youvxb.html?videoMark=" tabindex="-1" target="_blank">
         <img alt="大伙之家·更新" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/media_img/lena/PIC54n78f_152_270/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
         <div class="figure_caption">
          2021-12-02 期
         </div>
         <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_var:title:大伙之家·更新" class="figure_title figure_title_two_row bold" href="http://v.qq.com/x/cover/mzc00200mquy6aa/d0041youvxb.html?videoMark=" target="_blank" title="大伙之家·更新">
          大伙之家·更新
         </a>
         <div class="figure_desc" title="徐志胜渣男语录：爱过">
          徐志胜渣男语录：爱过
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_var:img:令人心动的offer" class="figure" data-float="mzc0020027kt27b" href="https://v.qq.com/x/cover/mzc0020027kt27b.html?videoMark=" tabindex="-1" target="_blank">
         <img alt="令人心动的offer" class="figure_pic" loading="lazy" lz_src="//vc.qpic.cn/tpic/mtviuBUg6J9dY/gy3883591vtoc970/250" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
         <div class="figure_caption">
          2021-12-01 期
         </div>
         <img alt="腾讯出品" class="mark_v mark_v_腾讯出品" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_self_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_self_x2.png 2x"/>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_var:title:令人心动的offer" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc0020027kt27b.html?videoMark=" target="_blank" title="令人心动的offer">
          令人心动的offer
         </a>
         <div class="figure_desc" title="新人空降！各科室全员戒备">
          新人空降！各科室全员戒备
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_var:img:哈哈哈哈哈2" class="figure" data-float="mzc00200h593q8k" href="http://v.qq.com/x/cover/mzc00200h593q8k/f004134rqar.html?videoMark=" tabindex="-1" target="_blank">
         <img alt="哈哈哈哈哈2" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/media_img/lena/PICq3chk7_304_540/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
         <div class="figure_caption">
          2021-11-28 期
         </div>
         <img alt="腾讯出品" class="mark_v mark_v_腾讯出品" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_self_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_self_x2.png 2x"/>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_var:title:哈哈哈哈哈2" class="figure_title figure_title_two_row bold" href="http://v.qq.com/x/cover/mzc00200h593q8k/f004134rqar.html?videoMark=" target="_blank" title="哈哈哈哈哈2">
          哈哈哈哈哈2
         </a>
         <div class="figure_desc" title="陈赫要跟郭京飞比打嗝">
          陈赫要跟郭京飞比打嗝
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_var:img:毛雪汪·更新" class="figure" data-float="mzc00200jmpahk2" href="https://v.qq.com/x/cover/mzc00200jmpahk2.html?videoMark=" tabindex="-1" target="_blank">
         <img alt="毛雪汪·更新" class="figure_pic" loading="lazy" lz_src="//vc.qpic.cn/tpic/mtviuB6ogDxSG/91hu8189jqrb5784/250" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
         <div class="figure_caption">
          2021-11-29 期
         </div>
         <img alt="腾讯出品" class="mark_v mark_v_腾讯出品" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_self_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_self_x2.png 2x"/>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_var:title:毛雪汪·更新" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200jmpahk2.html?videoMark=" target="_blank" title="毛雪汪·更新">
          毛雪汪·更新
         </a>
         <div class="figure_desc" title="李雪琴邀尚九熙过年回家？">
          李雪琴邀尚九熙过年回家？
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_var:img:奇遇·人间角落" class="figure" data-float="mzc00200k86yn8f" href="https://v.qq.com/x/cover/mzc00200k86yn8f.html?videoMark=" tabindex="-1" target="_blank">
         <img alt="奇遇·人间角落" class="figure_pic" loading="lazy" lz_src="//vc.qpic.cn/tpic/mtviuB5ucYTWY/nsed8186uuy8j663/250" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
         <div class="figure_caption">
          2021-11-29 期
         </div>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_var:title:奇遇·人间角落" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200k86yn8f.html?videoMark=" target="_blank" title="奇遇·人间角落">
          奇遇·人间角落
         </a>
         <div class="figure_desc" title="娜娜参加藏族婚礼当伴娘">
          娜娜参加藏族婚礼当伴娘
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_var:img:朗读者 第3季" class="figure" data-float="mzc00200jupmohl" href="http://v.qq.com/x/cover/mzc00200jupmohl/o0041b3zlmy.html?videoMark=" tabindex="-1" target="_blank">
         <img alt="朗读者 第3季" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/media_img/lena/PIC4topsh_304_540/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
         <div class="figure_caption">
          2021-11-28 期
         </div>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_var:title:朗读者 第3季" class="figure_title figure_title_two_row bold" href="http://v.qq.com/x/cover/mzc00200jupmohl/o0041b3zlmy.html?videoMark=" target="_blank" title="朗读者 第3季">
          朗读者 第3季
         </a>
         <div class="figure_desc" title="“熊猫爷爷”守护濒危动物">
          “熊猫爷爷”守护濒危动物
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_var:img:我们的歌 第3季" class="figure" data-float="mzc00200iio896t" href="http://v.qq.com/x/cover/mzc00200iio896t/r0041ebx30s.html?videoMark=" tabindex="-1" target="_blank">
         <img alt="我们的歌 第3季" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/media_img/lena/PICx4fqcw_720_1280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
         <div class="figure_caption">
          2021-11-28 期
         </div>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_var:title:我们的歌 第3季" class="figure_title figure_title_two_row bold" href="http://v.qq.com/x/cover/mzc00200iio896t/r0041ebx30s.html?videoMark=" target="_blank" title="我们的歌 第3季">
          我们的歌 第3季
         </a>
         <div class="figure_desc" title="大张伟跳魔性洗澡舞">
          大张伟跳魔性洗澡舞
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_var:img:妙墨中国心" class="figure" data-float="mzc002006zyb5vi" href="http://v.qq.com/x/cover/mzc002006zyb5vi/b0041as6tbp.html?videoMark=" tabindex="-1" target="_blank">
         <img alt="妙墨中国心" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/media_img/lena/PIC8imn24_607_1080/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
         <div class="figure_caption">
          2021-11-28 期
         </div>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_var:title:妙墨中国心" class="figure_title figure_title_two_row bold" href="http://v.qq.com/x/cover/mzc002006zyb5vi/b0041as6tbp.html?videoMark=" target="_blank" title="妙墨中国心">
          妙墨中国心
         </a>
         <div class="figure_desc" title="世界武术冠军剑术表演太飒">
          世界武术冠军剑术表演太飒
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_var:img:齐鲁文化大会" class="figure" data-float="mzc00200ee6ihbt" href="http://v.qq.com/x/cover/mzc00200ee6ihbt/k00413dlu90.html?videoMark=" tabindex="-1" target="_blank">
         <img alt="齐鲁文化大会" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/media_img/lena/PIC2jus6j_607_1080/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
         <div class="figure_caption">
          2021-11-28 期
         </div>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_var:title:齐鲁文化大会" class="figure_title figure_title_two_row bold" href="http://v.qq.com/x/cover/mzc00200ee6ihbt/k00413dlu90.html?videoMark=" target="_blank" title="齐鲁文化大会">
          齐鲁文化大会
         </a>
         <div class="figure_desc" title="世界记忆大师记忆力炸场">
          世界记忆大师记忆力炸场
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_var:img:导演请指教" class="figure" data-float="mzc00200j97zo8g" href="http://v.qq.com/x/cover/mzc00200j97zo8g/d00412n8jlw.html?videoMark=" tabindex="-1" target="_blank">
         <img alt="导演请指教" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/media_img/lena/PICc7o0mh_720_1280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
         <div class="figure_caption">
          2021-11-27 期
         </div>
         <img alt="腾讯出品" class="mark_v mark_v_腾讯出品" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_self_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_self_x2.png 2x"/>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_var:title:导演请指教" class="figure_title figure_title_two_row bold" href="http://v.qq.com/x/cover/mzc00200j97zo8g/d00412n8jlw.html?videoMark=" target="_blank" title="导演请指教">
          导演请指教
         </a>
         <div class="figure_desc" title="李诚儒1句话评陈宥维">
          李诚儒1句话评陈宥维
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_var:img:青春环游记" class="figure" data-float="mzc00200b9zncs0" href="http://v.qq.com/x/cover/mzc00200b9zncs0/j0041efjljp.html?videoMark=" tabindex="-1" target="_blank">
         <img alt="青春环游记" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/media_img/lena/PICupnje2_304_540/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
         <div class="figure_caption">
          2021-11-27 期
         </div>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_var:title:青春环游记" class="figure_title figure_title_two_row bold" href="http://v.qq.com/x/cover/mzc00200b9zncs0/j0041efjljp.html?videoMark=" target="_blank" title="青春环游记">
          青春环游记
         </a>
         <div class="figure_desc" title="杨洋贾玲男女混合双打">
          杨洋贾玲男女混合双打
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_var:img:超燃美食记" class="figure" data-float="mzc00200oluvris" href="https://v.qq.com/x/cover/mzc00200oluvris/g0041yhb781.html?videoMark=" tabindex="-1" target="_blank">
         <img alt="超燃美食记" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/media_img/lena/PICqi25ty_304_540/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
         <div class="figure_caption">
          2021-11-27 期
         </div>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_var:title:超燃美食记" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200oluvris/g0041yhb781.html?videoMark=" target="_blank" title="超燃美食记">
          超燃美食记
         </a>
         <div class="figure_desc" title="杨九郎走心感谢德云社">
          杨九郎走心感谢德云社
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_var:img:国家宝藏·展演季" class="figure" data-float="mzc00200najg4o1" href="http://v.qq.com/x/cover/mzc00200najg4o1/s00418ow1c2.html?videoMark=" tabindex="-1" target="_blank">
         <img alt="国家宝藏·展演季" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/media_img/lena/PICrllmr9_108_192/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
         <div class="figure_caption">
          2021-11-26 期
         </div>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_var:title:国家宝藏·展演季" class="figure_title figure_title_two_row bold" href="http://v.qq.com/x/cover/mzc00200najg4o1/s00418ow1c2.html?videoMark=" target="_blank" title="国家宝藏·展演季">
          国家宝藏·展演季
         </a>
         <div class="figure_desc" title="湖南方言唱唐诗好苏">
          湖南方言唱唐诗好苏
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_var:img:最美中国戏" class="figure" data-float="mzc00200vprng4c" href="http://v.qq.com/x/cover/mzc00200vprng4c/c0041mlwnuw.html?videoMark=" tabindex="-1" target="_blank">
         <img alt="最美中国戏" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/media_img/lena/PICkqgt6g_607_1080/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
         <div class="figure_caption">
          2021-11-27 期
         </div>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_var:title:最美中国戏" class="figure_title figure_title_two_row bold" href="http://v.qq.com/x/cover/mzc00200vprng4c/c0041mlwnuw.html?videoMark=" target="_blank" title="最美中国戏">
          最美中国戏
         </a>
         <div class="figure_desc" title="这样的林黛玉你喜欢吗">
          这样的林黛玉你喜欢吗
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_var:img:奔跑吧黄河篇2" class="figure" data-float="mzc002001wzser7" href="http://v.qq.com/x/cover/mzc002001wzser7/s0041uhppmh.html?videoMark=" tabindex="-1" target="_blank">
         <img alt="奔跑吧黄河篇2" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/media_img/lena/PIC1bqdga_304_540/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
         <div class="figure_caption">
          2021-11-26 期
         </div>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_var:title:奔跑吧黄河篇2" class="figure_title figure_title_two_row bold" href="http://v.qq.com/x/cover/mzc002001wzser7/s0041uhppmh.html?videoMark=" target="_blank" title="奔跑吧黄河篇2">
          奔跑吧黄河篇2
         </a>
         <div class="figure_desc" title="林一翻跟头吓坏周深">
          林一翻跟头吓坏周深
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_var:img:2060" class="figure" data-float="mzc002006064xlv" href="http://v.qq.com/x/cover/mzc002006064xlv/f0041vz0lg5.html?videoMark=" tabindex="-1" target="_blank">
         <img alt="2060" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/media_img/lena/PICjzpn2x_720_1280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
         <div class="figure_caption">
          2021-11-26 期
         </div>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_var:title:2060" class="figure_title figure_title_two_row bold" href="http://v.qq.com/x/cover/mzc002006064xlv/f0041vz0lg5.html?videoMark=" target="_blank" title="2060">
          2060
         </a>
         <div class="figure_desc" title="周深电视鸡合唱达拉崩吧">
          周深电视鸡合唱达拉崩吧
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_var:img:美好的星城" class="figure" data-float="mzc0020047i574u" href="http://v.qq.com/x/cover/mzc0020047i574u/j0041rylg1d.html?videoMark=" tabindex="-1" target="_blank">
         <img alt="美好的星城" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/media_img/lena/PICj1zfkn_304_540/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
         <div class="figure_caption">
          2021-11-25 期
         </div>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_var:title:美好的星城" class="figure_title figure_title_two_row bold" href="http://v.qq.com/x/cover/mzc0020047i574u/j0041rylg1d.html?videoMark=" target="_blank" title="美好的星城">
          美好的星城
         </a>
         <div class="figure_desc" title="伍嘉成做皮影遇滑铁卢">
          伍嘉成做皮影遇滑铁卢
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_var:img:求职高手 第2季" class="figure" data-float="mzc00200xh1j2gk" href="https://v.qq.com/x/cover/mzc00200xh1j2gk.html?videoMark=" tabindex="-1" target="_blank">
         <img alt="求职高手 第2季" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/media_img/lena/PIC8rkl7o_304_540/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
         <div class="figure_caption">
          2021-11-24 期
         </div>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_var:title:求职高手 第2季" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200xh1j2gk.html?videoMark=" target="_blank" title="求职高手 第2季">
          求职高手 第2季
         </a>
         <div class="figure_desc" title="选手十余年心系公益">
          选手十余年心系公益
         </div>
        </div>
       </div>
      </div>
     </div>
    </div>
    <div class="mod_column_side">
     <div class="mod_hd mod_column_hd">
      <h2 class="mod_title">
       综艺热播排行榜
      </h2>
      <div class="bg_rank_ball">
      </div>
      <div class="mod_hd_action">
       <a _stat="new_vs_hot_var:通栏功能区:更多" class="action_item" href="https://v.qq.com/x/rank/#variety">
        更多
        <svg class="svg_icon svg_icon_next" height="10" viewbox="0 0 6 10" width="6">
         <path d="M4.6 4.7L1 1M4.7 5.3L1 9" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="1.4">
         </path>
        </svg>
       </a>
      </div>
     </div>
     <div class="mod_rank_list mod_rank_list_2column">
      <a __wind="" class="rank_item rank_item_1 cf" href="https://v.qq.com/x/cover/mzc00200q90natx.html" title="哈哈哈哈哈 第2季">
       <span class="rank_num rank_num_1">
        1
       </span>
       <span class="rank_title">
        哈哈哈哈哈 第2季
       </span>
       <span class="rank_desc">
        undefined
       </span>
       <span class="rank_update">
        2021-11-29
       </span>
      </a>
      <a __wind="" class="rank_item rank_item_2 cf" href="https://v.qq.com/x/cover/mzc002001wzser7.html" title="奔跑吧·黄河篇 第2季">
       <span class="rank_num rank_num_2">
        2
       </span>
       <span class="rank_title">
        奔跑吧·黄河篇 第2季
       </span>
       <span class="rank_desc">
        undefined
       </span>
       <span class="rank_update">
        2021-11-26
       </span>
      </a>
      <a __wind="" class="rank_item rank_item_3 cf" href="https://v.qq.com/x/cover/mzc00200b9zncs0.html" title="青春环游记 第3季">
       <span class="rank_num rank_num_3">
        3
       </span>
       <span class="rank_title">
        青春环游记 第3季
       </span>
       <span class="rank_desc">
        undefined
       </span>
       <span class="rank_update">
        2021-11-27
       </span>
      </a>
      <a __wind="" class="rank_item rank_item_4 cf" href="https://v.qq.com/x/cover/mzc00200b5jnlfp.html" title="令人心动的offer 第3季">
       <span class="rank_num rank_num_4">
        4
       </span>
       <span class="rank_title">
        令人心动的offer 第3季
       </span>
       <span class="rank_desc">
        undefined
       </span>
       <span class="rank_update">
        2021-12-02
       </span>
      </a>
      <a __wind="" class="rank_item rank_item_5 cf" href="https://v.qq.com/x/cover/mzc002008zmtofv.html" title="我们的歌 第3季">
       <span class="rank_num rank_num_5">
        5
       </span>
       <span class="rank_title">
        我们的歌 第3季
       </span>
       <span class="rank_desc">
        undefined
       </span>
       <span class="rank_update">
        2021-11-30
       </span>
      </a>
      <a __wind="" class="rank_item rank_item_6 cf" href="https://v.qq.com/x/cover/mzc002008mgejfh.html" title="德云斗笑社 第2季">
       <span class="rank_num rank_num_6">
        6
       </span>
       <span class="rank_title">
        德云斗笑社 第2季
       </span>
       <span class="rank_desc">
        undefined
       </span>
       <span class="rank_update">
        2021-11-05
       </span>
      </a>
      <a __wind="" class="rank_item rank_item_7 cf" href="https://v.qq.com/x/cover/mzc002002p4rpoc.html" title="王牌对王牌精编版">
       <span class="rank_num rank_num_7">
        7
       </span>
       <span class="rank_title">
        王牌对王牌精编版
       </span>
       <span class="rank_desc">
        undefined
       </span>
       <span class="rank_update">
        2021-07-04
       </span>
      </a>
      <a __wind="" class="rank_item rank_item_8 cf" href="https://v.qq.com/x/cover/mzc00200bergkk9.html" title="导演请指教">
       <span class="rank_num rank_num_8">
        8
       </span>
       <span class="rank_title">
        导演请指教
       </span>
       <span class="rank_desc">
        undefined
       </span>
       <span class="rank_update">
        2021-11-28
       </span>
      </a>
      <a __wind="" class="rank_item rank_item_9 cf" href="https://v.qq.com/x/cover/mzc00200wh0dnn0.html" title="脱口秀大会 第4季">
       <span class="rank_num rank_num_9">
        9
       </span>
       <span class="rank_title">
        脱口秀大会 第4季
       </span>
       <span class="rank_desc">
        undefined
       </span>
       <span class="rank_update">
        2021-10-19
       </span>
      </a>
      <a __wind="" class="rank_item rank_item_10 cf" href="https://v.qq.com/x/cover/mzc002009s30n6k.html" title="毛雪汪">
       <span class="rank_num rank_num_10">
        10
       </span>
       <span class="rank_title">
        毛雪汪
       </span>
       <span class="rank_desc">
        undefined
       </span>
       <span class="rank_update">
        2021-11-30
       </span>
      </a>
     </div>
    </div>
   </div>
  </div>
  <div _expose="new_vs_hot_cartoon" _wind="columnname=精选_动漫&amp;controlname=new_vs_hot_cartoon" class="mod_row_box" cur-page-num="0" data-context="3" data-istyle="7" has-next-page="false" id="new_vs_hot_cartoon">
   <div class="mod_bd cf _quickopen _quickopen_duration">
    <div class="mod_column_main">
     <div class="mod_hd mod_column_hd">
      <h2 class="mod_title">
       <a _stat="new_vs_hot_cartoon:通栏功能区:通栏标题" class="title_link" data-target="_blank" href="https://v.qq.com/channel/cartoon">
        动漫
       </a>
      </h2>
      <div class="mod_page_small none">
       <button _stat="new_vs_hot_cartoon:通栏功能区:上一页" class="btn_prev disabled" title="上一页" wind-click="100">
        <svg class="svg_icon svg_icon_prev" height="10" viewbox="0 0 6 10" width="6">
         <path d="M1.4 4.7L5 1M1.3 5.3L5 9" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="1.4">
         </path>
        </svg>
       </button>
       <span class="page_num" data-count="1" data-info="12 9" data-page="1">
        1/1
       </span>
       <button _stat="new_vs_hot_cartoon:通栏功能区:下一页" class="btn_next" title="下一页" wind-click="100">
        <svg class="svg_icon svg_icon_next" height="10" viewbox="0 0 6 10" width="6">
         <path d="M4.6 4.7L1 1M4.7 5.3L1 9" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="1.4">
         </path>
        </svg>
       </button>
      </div>
     </div>
     <div class="mod_column_bd">
      <div class="mod_figure mod_figure_v_default mod_figure_v_default_1row mod_figure_v_default mod_figure_scroll" data-rowcount="6" data-rowlen="1">
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_cartoon:img:紫川【定档12.21】" class="figure" data-float="mzc00200iawcmn2" href="https://v.qq.com/x/cover/mzc00200iawcmn2.html" tabindex="-1" target="_blank">
         <img alt="紫川【定档12.21】" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/mzc00200iawcmn21628407507851/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
         <div class="figure_caption">
         </div>
         <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_cartoon:title:紫川【定档12.21】" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200iawcmn2.html" target="_blank" title="紫川【定档12.21】">
          紫川【定档12.21】
         </a>
         <div class="figure_desc" title="紫川三杰纵横西川大陆">
          紫川三杰纵横西川大陆
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_cartoon:img:白月儿" class="figure" data-float="mzc002006l0blow" href="https://v.qq.com/x/cover/mzc002006l0blow.html" tabindex="-1" target="_blank">
         <img alt="白月儿" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/mzc002006l0blow1637116446965/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
         <div class="figure_caption">
          全1集
         </div>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_cartoon:title:白月儿" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc002006l0blow.html" target="_blank" title="白月儿">
          白月儿
         </a>
         <div class="figure_desc" title="口碑国漫！绝美水墨风">
          口碑国漫！绝美水墨风
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_cartoon:img:镜·双城" class="figure" data-float="mzc00200x2dwqa9" href="https://v.qq.com/x/cover/mzc00200x2dwqa9.html" tabindex="-1" target="_blank">
         <img alt="镜·双城" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/mzc00200x2dwqa91634095449/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
         <div class="figure_caption">
          更新至07集
         </div>
         <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_cartoon:title:镜·双城" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200x2dwqa9.html" target="_blank" title="镜·双城">
          镜·双城
         </a>
         <div class="figure_desc" title="首播！王子复仇归来">
          首播！王子复仇归来
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_cartoon:img:大王饶命【12.3首播】" class="figure" data-float="od1kjfd56e3s7n7" href="https://v.qq.com/x/cover/od1kjfd56e3s7n7.html" tabindex="-1" target="_blank">
         <img alt="大王饶命【12.3首播】" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/od1kjfd56e3s7n71628407965692/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
         <div class="figure_caption">
         </div>
         <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_cartoon:title:大王饶命【12.3首播】" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/od1kjfd56e3s7n7.html" target="_blank" title="大王饶命【12.3首播】">
          大王饶命【12.3首播】
         </a>
         <div class="figure_desc" title="灵气复苏，少年崛起">
          灵气复苏，少年崛起
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_cartoon:img:英雄联盟：双城之战" class="figure" data-float="mzc0020040co24e" href="https://v.qq.com/x/cover/mzc0020040co24e.html" tabindex="-1" target="_blank">
         <img alt="英雄联盟：双城之战" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/mzc0020040co24e1635306774822/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
         <div class="figure_caption">
          全9集
         </div>
         <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_cartoon:title:英雄联盟：双城之战" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc0020040co24e.html" target="_blank" title="英雄联盟：双城之战">
          英雄联盟：双城之战
         </a>
         <div class="figure_desc" title="六年制作，万张手稿！">
          六年制作，万张手稿！
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_cartoon:img:斗破苍穹三年之约" class="figure" data-float="mzc0020036ro0ux" href="https://v.qq.com/x/cover/mzc0020036ro0ux.html" tabindex="-1" target="_blank">
         <img alt="斗破苍穹三年之约" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/mzc0020036ro0ux1634437673075/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
         <div class="figure_caption">
          更新至06集
         </div>
         <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_cartoon:title:斗破苍穹三年之约" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc0020036ro0ux.html" target="_blank" title="斗破苍穹三年之约">
          斗破苍穹三年之约
         </a>
         <div class="figure_desc" title="赴三年之约 战云岚之巅">
          赴三年之约 战云岚之巅
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_cartoon:img:一人之下 第4季" class="figure" data-float="mzc00200ni38yk3" href="https://v.qq.com/x/cover/mzc00200ni38yk3.html" tabindex="-1" target="_blank">
         <img alt="一人之下 第4季" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/mzc00200ni38yk31628409211817/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
         <div class="figure_caption">
          更新至11集
         </div>
         <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_cartoon:title:一人之下 第4季" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200ni38yk3.html" target="_blank" title="一人之下 第4季">
          一人之下 第4季
         </a>
         <div class="figure_desc" title="“临时工”集结！">
          “临时工”集结！
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_cartoon:img:斗罗大陆" class="figure" data-float="m441e3rjq9kwpsc" href="https://v.qq.com/x/cover/m441e3rjq9kwpsc.html" tabindex="-1" target="_blank">
         <img alt="斗罗大陆" class="figure_pic" loading="lazy" lz_src="//i.gtimg.cn/qqlive/img/jpgcache/files/qqvideo/m/m441e3rjq9kwpsc_p.jpg" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
         <div class="figure_caption">
          更新至184集
         </div>
         <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_cartoon:title:斗罗大陆" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/m441e3rjq9kwpsc.html" target="_blank" title="斗罗大陆">
          斗罗大陆
         </a>
         <div class="figure_desc" title="特效爆表！战斗燃炸天际！">
          特效爆表！战斗燃炸天际！
         </div>
        </div>
       </div>
       <div __wind="" class="list_item">
        <a _stat="new_vs_hot_cartoon:img:完美世界" class="figure" data-float="mcv8hkc8zk8lnov" href="https://v.qq.com/x/cover/mcv8hkc8zk8lnov.html" tabindex="-1" target="_blank">
         <img alt="完美世界" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_vt_pic/0/mcv8hkc8zk8lnov1618565542604/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
         <div class="figure_caption">
          更新至34集
         </div>
         <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
        </a>
        <div class="figure_detail figure_detail_two_row">
         <a _stat="new_vs_hot_cartoon:title:完美世界" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mcv8hkc8zk8lnov.html" target="_blank" title="完美世界">
          完美世界
         </a>
         <div class="figure_desc" title="岁月淹埋，休想把我沉浮！">
          岁月淹埋，休想把我沉浮！
         </div>
        </div>
       </div>
      </div>
     </div>
    </div>
    <div class="mod_column_side">
     <div class="mod_hd mod_column_hd">
      <h2 class="mod_title">
       动漫热播排行榜
      </h2>
      <div class="bg_rank_ball">
      </div>
      <div class="mod_hd_action">
       <a _stat="new_vs_hot_cartoon:通栏功能区:更多" class="action_item" href="https://v.qq.com/x/rank/#anime">
        更多
        <svg class="svg_icon svg_icon_next" height="10" viewbox="0 0 6 10" width="6">
         <path d="M4.6 4.7L1 1M4.7 5.3L1 9" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="1.4">
         </path>
        </svg>
       </a>
      </div>
     </div>
     <div class="mod_rank_list mod_rank_list_ mod_rank_list_2column mod_rank_list_2column_v">
      <a __wind="" class="rank_item rank_item_1 cf" href="https://v.qq.com/x/cover/mzc0020036ro0ux.html" title="斗破苍穹三年之约">
       <span class="rank_num rank_num_1">
        1
       </span>
       <span class="rank_title">
        斗破苍穹三年之约
       </span>
       <span class="rank_desc">
        赴三年之约 战云岚之巅
       </span>
       <span class="rank_update">
        更新至06集
       </span>
      </a>
      <a __wind="" class="rank_item rank_item_2 cf" href="https://v.qq.com/x/cover/m441e3rjq9kwpsc.html" title="斗罗大陆">
       <span class="rank_num rank_num_2">
        2
       </span>
       <span class="rank_title">
        斗罗大陆
       </span>
       <span class="rank_desc">
        此生不悔入唐门
       </span>
       <span class="rank_update">
        更新至184集
       </span>
      </a>
      <a __wind="" class="rank_item rank_item_3 cf" href="https://v.qq.com/x/cover/mcv8hkc8zk8lnov.html" title="完美世界">
       <span class="rank_num rank_num_3">
        3
       </span>
       <span class="rank_title">
        完美世界
       </span>
       <span class="rank_desc">
        岁月淹埋，休想把我沉浮！
       </span>
       <span class="rank_update">
        更新至34集
       </span>
      </a>
      <a __wind="" class="rank_item rank_item_4 cf" href="https://v.qq.com/x/cover/mzc0020040co24e.html" title="英雄联盟：双城之战 普通话版">
       <span class="rank_num rank_num_4">
        4
       </span>
       <span class="rank_title">
        英雄联盟：双城之战 普通话版
       </span>
       <span class="rank_desc">
        六年制作，万张手稿！
       </span>
       <span class="rank_update">
        全9集
       </span>
      </a>
      <a __wind="" class="rank_item rank_item_5 cf" href="https://v.qq.com/x/cover/mzc00200ni38yk3.html" title="一人之下 第4季">
       <span class="rank_num rank_num_5">
        5
       </span>
       <span class="rank_title">
        一人之下 第4季
       </span>
       <span class="rank_desc">
        “临时工”集结！
       </span>
       <span class="rank_update">
        更新至11集
       </span>
      </a>
      <a __wind="" class="rank_item rank_item_6 cf" href="https://v.qq.com/x/cover/7q544xyrava3vxf.html" title="武神主宰">
       <span class="rank_num rank_num_6">
        6
       </span>
       <span class="rank_title">
        武神主宰
       </span>
       <span class="rank_desc">
        武神跌落，浴火少年再起
       </span>
       <span class="rank_update">
        更新至184集
       </span>
      </a>
      <a __wind="" class="rank_item rank_item_7 cf" href="https://v.qq.com/x/cover/2w2legt0g8z26al.html" title="灵剑尊">
       <span class="rank_num rank_num_7">
        7
       </span>
       <span class="rank_title">
        灵剑尊
       </span>
       <span class="rank_desc">
        天地三界，我为至尊！
       </span>
       <span class="rank_update">
        更新至232集
       </span>
      </a>
      <a __wind="" class="rank_item rank_item_8 cf" href="https://v.qq.com/x/cover/mzc00200ilydv1a.html" title="无上神帝">
       <span class="rank_num rank_num_8">
        8
       </span>
       <span class="rank_title">
        无上神帝
       </span>
       <span class="rank_desc">
        仙王觉醒，重归万界巅峰
       </span>
       <span class="rank_update">
        更新至122集
       </span>
      </a>
     </div>
    </div>
   </div>
  </div>
  <div _expose="new_vs_hot_child" _wind="columnname=精选_少儿&amp;controlname=new_vs_hot_child" class="mod_row_box" cur-page-num="0" data-context="3" data-istyle="7" has-next-page="false" id="new_vs_hot_child">
   <div class="mod_hd">
    <h2 class="mod_title">
     <a _stat="new_vs_hot_child:通栏功能区:通栏标题" class="title_link" data-target="_blank" href="https://v.qq.com/channel/child">
      少儿
     </a>
    </h2>
    <div class="mod_page_small">
     <button _stat="new_vs_hot_child:通栏功能区:上一页" class="btn_prev disabled" title="上一页" wind-click="100">
      <svg class="svg_icon svg_icon_prev" height="10" viewbox="0 0 6 10" width="6">
       <path d="M1.4 4.7L5 1M1.3 5.3L5 9" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="1.4">
       </path>
      </svg>
     </button>
     <span class="page_num" data-count="2" data-info="8 9" data-page="1">
      1/2
     </span>
     <button _stat="new_vs_hot_child:通栏功能区:下一页" class="btn_next" title="下一页" wind-click="100">
      <svg class="svg_icon svg_icon_next" height="10" viewbox="0 0 6 10" width="6">
       <path d="M4.6 4.7L1 1M4.7 5.3L1 9" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="1.4">
       </path>
      </svg>
     </button>
    </div>
   </div>
   <div class="mod_bd cf _quickopen _quickopen_duration">
    <div class="mod_figure mod_figure_v_default mod_figure_v_default_1row mod_figure_v_default mod_figure_scroll" data-rowcount="8" data-rowlen="1">
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_child:img:舒克贝塔第三季" class="figure" data-float="mzc00200b1774i4" href="https://v.qq.com/x/cover/mzc00200b1774i4.html" tabindex="-1" target="_blank">
       <img alt="舒克贝塔第三季" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/mzc00200b1774i41626771676635/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        更新至14集
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_child:title:舒克贝塔第三季" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200b1774i4.html" target="_blank" title="舒克贝塔第三季">
        舒克贝塔第三季
       </a>
       <div class="figure_desc" title="大战反派联盟">
        大战反派联盟
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_child:img:薇薇猫的日常" class="figure" data-float="mzc00200tunq679" href="https://v.qq.com/x/cover/mzc00200tunq679.html" tabindex="-1" target="_blank">
       <img alt="薇薇猫的日常" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/mzc00200tunq6791629446569706/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        更新至30集
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_child:title:薇薇猫的日常" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200tunq679.html" target="_blank" title="薇薇猫的日常">
        薇薇猫的日常
       </a>
       <div class="figure_desc" title="萌猫搞笑和治愈的生活">
        萌猫搞笑和治愈的生活
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_child:img:旗旗号巡洋舰2" class="figure" data-float="mzc00200dhzdql4" href="https://v.qq.com/x/cover/mzc00200dhzdql4.html" tabindex="-1" target="_blank">
       <img alt="旗旗号巡洋舰2" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/mzc00200dhzdql41627040570907/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        全52集
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_child:title:旗旗号巡洋舰2" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200dhzdql4.html" target="_blank" title="旗旗号巡洋舰2">
        旗旗号巡洋舰2
       </a>
       <div class="figure_desc" title="郑渊洁经典改编">
        郑渊洁经典改编
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_child:img:天真与功夫袜" class="figure" data-float="mzc00200dp5b9xf" href="https://v.qq.com/x/cover/mzc00200dp5b9xf.html" tabindex="-1" target="_blank">
       <img alt="天真与功夫袜" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/mzc00200dp5b9xf1627036356116/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        更新至26集
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_child:title:天真与功夫袜" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200dp5b9xf.html" target="_blank" title="天真与功夫袜">
        天真与功夫袜
       </a>
       <div class="figure_desc" title="8月3日平凡少女变身英雄">
        8月3日平凡少女变身英雄
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_child:img:故宫里的大怪兽" class="figure" data-float="mzc00200151n1zn" href="https://v.qq.com/x/cover/mzc00200151n1zn.html" tabindex="-1" target="_blank">
       <img alt="故宫里的大怪兽" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/mzc00200151n1zn1615183617202/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        全26集
       </div>
       <img alt="腾讯出品" class="mark_v mark_v_腾讯出品" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_self_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_self_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_child:title:故宫里的大怪兽" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200151n1zn.html" target="_blank" title="故宫里的大怪兽">
        故宫里的大怪兽
       </a>
       <div class="figure_desc" title="勇闯奇幻怪兽世界">
        勇闯奇幻怪兽世界
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_child:img:海底小纵队6" class="figure" data-float="mzc002008qoib55" href="https://v.qq.com/x/cover/mzc002008qoib55.html" tabindex="-1" target="_blank">
       <img alt="海底小纵队6" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/mzc002008qoib551624344410448/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        全26集
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_child:title:海底小纵队6" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc002008qoib55.html" target="_blank" title="海底小纵队6">
        海底小纵队6
       </a>
       <div class="figure_desc" title="海陆空全球总动员">
        海陆空全球总动员
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_child:img:米小圈动画古诗" class="figure" data-float="mzc00200r15dsn0" href="https://v.qq.com/x/cover/mzc00200r15dsn0.html" tabindex="-1" target="_blank">
       <img alt="米小圈动画古诗" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/yxhpn55vat42brh/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
       </div>
       <img alt="付费" class="mark_v mark_v_付费" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_pay_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_pay_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_child:title:米小圈动画古诗" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200r15dsn0.html" target="_blank" title="米小圈动画古诗">
        米小圈动画古诗
       </a>
       <div class="figure_desc" title="快乐看动画，轻松学古诗">
        快乐看动画，轻松学古诗
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_child:img:超迷你战士科学探险队航天篇" class="figure" data-float="mzc0020031zjs2c" href="https://v.qq.com/x/cover/mzc0020031zjs2c.html" tabindex="-1" target="_blank">
       <img alt="超迷你战士科学探险队航天篇" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/mzc0020031zjs2c1624007268103/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        全12集
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_child:title:超迷你战士科学探险队航天篇" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc0020031zjs2c.html" target="_blank" title="超迷你战士科学探险队航天篇">
        超迷你战士科学探险队航天篇
       </a>
       <div class="figure_desc" title="中国空间站是怎么建成的？">
        中国空间站是怎么建成的？
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_child:img:螺丝钉4" class="figure" data-float="mzc00200mhgrghr" href="https://v.qq.com/x/cover/mzc00200mhgrghr.html" tabindex="-1" target="_blank">
       <img alt="螺丝钉4" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_vt_pic/0/mzc00200mhgrghr1624421530814/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        更新至26集
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_child:title:螺丝钉4" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200mhgrghr.html" target="_blank" title="螺丝钉4">
        螺丝钉4
       </a>
       <div class="figure_desc" title="精通科学的小小修理工">
        精通科学的小小修理工
       </div>
      </div>
     </div>
    </div>
   </div>
  </div>
  <div _expose="new_vs_hot_doco" _wind="columnname=精选_纪录片&amp;controlname=new_vs_hot_doco" class="mod_row_box" cur-page-num="0" data-context="4" data-istyle="7" has-next-page="false" id="new_vs_hot_doco">
   <div class="mod_hd">
    <h2 class="mod_title">
     <a _stat="new_vs_hot_doco:通栏功能区:通栏标题" class="title_link" data-target="_blank" href="https://v.qq.com/channel/doco">
      纪录片
     </a>
    </h2>
    <div class="mod_page_small">
     <button _stat="new_vs_hot_doco:通栏功能区:上一页" class="btn_prev disabled" title="上一页" wind-click="100">
      <svg class="svg_icon svg_icon_prev" height="10" viewbox="0 0 6 10" width="6">
       <path d="M1.4 4.7L5 1M1.3 5.3L5 9" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="1.4">
       </path>
      </svg>
     </button>
     <span class="page_num" data-count="7" data-info="8 50" data-page="1">
      1/7
     </span>
     <button _stat="new_vs_hot_doco:通栏功能区:下一页" class="btn_next" title="下一页" wind-click="100">
      <svg class="svg_icon svg_icon_next" height="10" viewbox="0 0 6 10" width="6">
       <path d="M4.6 4.7L1 1M4.7 5.3L1 9" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="1.4">
       </path>
      </svg>
     </button>
    </div>
   </div>
   <div class="mod_bd cf _quickopen _quickopen_duration">
    <div class="mod_figure mod_figure_v_default mod_figure_v_default_1row mod_figure_v_default mod_figure_scroll" data-rowcount="8" data-rowlen="1">
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_doco:img:中国这么美" class="figure" data-float="mzc00200cl0prlg" href="https://v.qq.com/x/cover/mzc00200cl0prlg.html" tabindex="-1" target="_blank">
       <img alt="中国这么美" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/mzc00200cl0prlg1636681741913/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        01:02:41
       </div>
       <div class="figure_score">
        9.5
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_doco:title:中国这么美" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200cl0prlg.html" target="_blank" title="中国这么美">
        中国这么美
       </a>
       <div class="figure_desc" title="发现中国式生活美学">
        发现中国式生活美学
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_doco:img:勇敢者的征程" class="figure" data-float="mzc00200c905r3w" href="https://v.qq.com/x/cover/mzc00200c905r3w.html" tabindex="-1" target="_blank">
       <img alt="勇敢者的征程" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/mzc00200c905r3w1636009957772/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        33:32
       </div>
       <div class="figure_score">
        9.6
       </div>
       <img alt="腾讯出品" class="mark_v mark_v_腾讯出品" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_self_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_self_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_doco:title:勇敢者的征程" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200c905r3w.html" target="_blank" title="勇敢者的征程">
        勇敢者的征程
       </a>
       <div class="figure_desc" title="6位勇敢者重走荣光之路">
        6位勇敢者重走荣光之路
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_doco:img:料理的秘密" class="figure" data-float="mzc00200n0b2cg3" href="https://v.qq.com/x/cover/mzc00200n0b2cg3.html" tabindex="-1" target="_blank">
       <img alt="料理的秘密" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/mzc00200n0b2cg31637566435533/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        45:01
       </div>
       <div class="figure_score">
        8.7
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_doco:title:料理的秘密" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200n0b2cg3.html" target="_blank" title="料理的秘密">
        料理的秘密
       </a>
       <div class="figure_desc" title="八大亚洲美食制作密码揭晓">
        八大亚洲美食制作密码揭晓
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_doco:img:火线救援" class="figure" data-float="mzc00200s8wszxv" href="https://v.qq.com/x/cover/mzc00200s8wszxv.html" tabindex="-1" target="_blank">
       <img alt="火线救援" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/mzc00200s8wszxv1635820785935/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        44:57
       </div>
       <div class="figure_score">
        9.2
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_doco:title:火线救援" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200s8wszxv.html" target="_blank" title="火线救援">
        火线救援
       </a>
       <div class="figure_desc" title="第一视角看消防救援现场">
        第一视角看消防救援现场
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_doco:img:紫禁城" class="figure" data-float="mzc00200wp41jrg" href="https://v.qq.com/x/cover/mzc00200wp41jrg.html" tabindex="-1" target="_blank">
       <img alt="紫禁城" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/mzc00200wp41jrg1634740246247/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        01:01:34
       </div>
       <div class="figure_score">
        9.5
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_doco:title:紫禁城" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200wp41jrg.html" target="_blank" title="紫禁城">
        紫禁城
       </a>
       <div class="figure_desc" title="8K拍摄！揭秘紫禁城600年">
        8K拍摄！揭秘紫禁城600年
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_doco:img:素食行者" class="figure" data-float="mzc00200gzqtboe" href="https://v.qq.com/x/cover/mzc00200gzqtboe.html" tabindex="-1" target="_blank">
       <img alt="素食行者" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/mzc00200gzqtboe1637575526251/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        44:55
       </div>
       <div class="figure_score">
        7.5
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_doco:title:素食行者" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200gzqtboe.html" target="_blank" title="素食行者">
        素食行者
       </a>
       <div class="figure_desc" title="关爱生命，素食先行">
        关爱生命，素食先行
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_doco:img:震惊的真相：好莱坞凶案" class="figure" data-float="mzc00200isqophn" href="https://v.qq.com/x/cover/mzc00200isqophn.html" tabindex="-1" target="_blank">
       <img alt="震惊的真相：好莱坞凶案" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/mzc00200isqophn1635923362274/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        22:50
       </div>
       <div class="figure_score">
        9.0
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_doco:title:震惊的真相：好莱坞凶案" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200isqophn.html" target="_blank" title="震惊的真相：好莱坞凶案">
        震惊的真相：好莱坞凶案
       </a>
       <div class="figure_desc" title="揭秘真实谋杀事件">
        揭秘真实谋杀事件
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_doco:img:出发吧！去中国" class="figure" data-float="mzc0020078zqk6b" href="https://v.qq.com/x/cover/mzc0020078zqk6b.html" tabindex="-1" target="_blank">
       <img alt="出发吧！去中国" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/mzc0020078zqk6b1636080942140/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        14:57
       </div>
       <div class="figure_score">
        7.4
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_doco:title:出发吧！去中国" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc0020078zqk6b.html" target="_blank" title="出发吧！去中国">
        出发吧！去中国
       </a>
       <div class="figure_desc" title="老外的中国文化之旅">
        老外的中国文化之旅
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_doco:img:广东印记 第4季" class="figure" data-float="mzc002006detpb4" href="https://v.qq.com/x/cover/mzc002006detpb4.html" tabindex="-1" target="_blank">
       <img alt="广东印记 第4季" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_vt_pic/0/mzc002006detpb41635325386073/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        03:07
       </div>
       <div class="figure_score">
        7.5
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_doco:title:广东印记 第4季" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc002006detpb4.html" target="_blank" title="广东印记 第4季">
        广东印记 第4季
       </a>
       <div class="figure_desc" title="触摸岭南千年文明脉动">
        触摸岭南千年文明脉动
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_doco:img:中国杂技·吴桥" class="figure" data-float="mzc00200mdi9pvg" href="https://v.qq.com/x/cover/mzc00200mdi9pvg.html" tabindex="-1" target="_blank">
       <img alt="中国杂技·吴桥" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_vt_pic/0/mzc00200mdi9pvg1634474722978/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        43:50
       </div>
       <div class="figure_score">
        7.4
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_doco:title:中国杂技·吴桥" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200mdi9pvg.html" target="_blank" title="中国杂技·吴桥">
        中国杂技·吴桥
       </a>
       <div class="figure_desc" title="吴桥杂技演员的人生百味">
        吴桥杂技演员的人生百味
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_doco:img:千古风流人物 第1季" class="figure" data-float="mzc00200rwpg8pz" href="https://v.qq.com/x/cover/mzc00200rwpg8pz.html" tabindex="-1" target="_blank">
       <img alt="千古风流人物 第1季" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_vt_pic/0/mzc00200rwpg8pz1634186858171/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        34:13
       </div>
       <div class="figure_score">
        9.0
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_doco:title:千古风流人物 第1季" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200rwpg8pz.html" target="_blank" title="千古风流人物 第1季">
        千古风流人物 第1季
       </a>
       <div class="figure_desc" title="中国历史上现象级文化名人">
        中国历史上现象级文化名人
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_doco:img:是这样的，法官" class="figure" data-float="mzc002009s5aawf" href="https://v.qq.com/x/cover/mzc002009s5aawf.html" tabindex="-1" target="_blank">
       <img alt="是这样的，法官" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_vt_pic/0/mzc002009s5aawf1631012848766/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        39:22
       </div>
       <div class="figure_score">
        9.6
       </div>
       <img alt="腾讯出品" class="mark_v mark_v_腾讯出品" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_self_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_self_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_doco:title:是这样的，法官" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc002009s5aawf.html" target="_blank" title="是这样的，法官">
        是这样的，法官
       </a>
       <div class="figure_desc" title="善良的心是最好的法律">
        善良的心是最好的法律
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_doco:img:生命之歌" class="figure" data-float="mzc002003w72ksf" href="https://v.qq.com/x/cover/mzc002003w72ksf.html" tabindex="-1" target="_blank">
       <img alt="生命之歌" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_vt_pic/0/mzc002003w72ksf1634203546317/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        30:00
       </div>
       <div class="figure_score">
        8.7
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_doco:title:生命之歌" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc002003w72ksf.html" target="_blank" title="生命之歌">
        生命之歌
       </a>
       <div class="figure_desc" title="大美云南的千姿百态">
        大美云南的千姿百态
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_doco:img:蛮族崛起" class="figure" data-float="mzc00200de5wn9e" href="https://v.qq.com/x/cover/mzc00200de5wn9e.html" tabindex="-1" target="_blank">
       <img alt="蛮族崛起" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_vt_pic/0/mzc00200de5wn9e1630571211155/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        50:33
       </div>
       <div class="figure_score">
        9.6
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_doco:title:蛮族崛起" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200de5wn9e.html" target="_blank" title="蛮族崛起">
        蛮族崛起
       </a>
       <div class="figure_desc" title="罗马帝国的崩塌">
        罗马帝国的崩塌
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_doco:img:九零后" class="figure" data-float="mzc00200rspwfmm" href="https://v.qq.com/x/cover/mzc00200rspwfmm.html" tabindex="-1" target="_blank">
       <img alt="九零后" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_vt_pic/0/mzc00200rspwfmm1619150673919/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        01:49:34
       </div>
       <div class="figure_score">
        8.7
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_doco:title:九零后" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200rspwfmm.html" target="_blank" title="九零后">
        九零后
       </a>
       <div class="figure_desc" title="山河沦落处 群星闪耀时">
        山河沦落处 群星闪耀时
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_doco:img:功勋之国家先锋" class="figure" data-float="mzc00200xi9ouo9" href="https://v.qq.com/x/cover/mzc00200xi9ouo9.html" tabindex="-1" target="_blank">
       <img alt="功勋之国家先锋" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_vt_pic/0/mzc00200xi9ouo91632901673124/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        29:45
       </div>
       <div class="figure_score">
        8.9
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_doco:title:功勋之国家先锋" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200xi9ouo9.html" target="_blank" title="功勋之国家先锋">
        功勋之国家先锋
       </a>
       <div class="figure_desc" title="电视剧《功勋》全程幕后纪实">
        电视剧《功勋》全程幕后纪实
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_doco:img:风味时刻" class="figure" data-float="mzc00200na78gch" href="https://v.qq.com/x/cover/mzc00200na78gch.html" tabindex="-1" target="_blank">
       <img alt="风味时刻" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_vt_pic/0/mzc00200na78gch1633590347141/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        07:59
       </div>
       <div class="figure_score">
        8.5
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_doco:title:风味时刻" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200na78gch.html" target="_blank" title="风味时刻">
        风味时刻
       </a>
       <div class="figure_desc" title="在这一刻，吃懂一座城！">
        在这一刻，吃懂一座城！
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_doco:img:家乡宝返滇记" class="figure" data-float="mzc00200sqegz61" href="https://v.qq.com/x/cover/mzc00200sqegz61.html" tabindex="-1" target="_blank">
       <img alt="家乡宝返滇记" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_vt_pic/0/mzc00200sqegz611632733414620/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        16:06
       </div>
       <div class="figure_score">
        7.4
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_doco:title:家乡宝返滇记" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200sqegz61.html" target="_blank" title="家乡宝返滇记">
        家乡宝返滇记
       </a>
       <div class="figure_desc" title="身临其境感受物种多样性">
        身临其境感受物种多样性
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_doco:img:北极最后的避难所" class="figure" data-float="mzc002003mteg51" href="https://v.qq.com/x/cover/mzc002003mteg51.html" tabindex="-1" target="_blank">
       <img alt="北极最后的避难所" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_vt_pic/0/mzc002003mteg511632712219059/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        49:41
       </div>
       <div class="figure_score">
        8.9
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_doco:title:北极最后的避难所" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc002003mteg51.html" target="_blank" title="北极最后的避难所">
        北极最后的避难所
       </a>
       <div class="figure_desc" title="最具魅力的北极动物生活">
        最具魅力的北极动物生活
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_doco:img:内地港人·百人百事" class="figure" data-float="mzc00200ma0gpm5" href="https://v.qq.com/x/cover/mzc00200ma0gpm5.html" tabindex="-1" target="_blank">
       <img alt="内地港人·百人百事" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_vt_pic/0/mzc00200ma0gpm51632733811124/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        11:40
       </div>
       <div class="figure_score">
        7.4
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_doco:title:内地港人·百人百事" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200ma0gpm5.html" target="_blank" title="内地港人·百人百事">
        内地港人·百人百事
       </a>
       <div class="figure_desc" title="港人的内地生活图鉴">
        港人的内地生活图鉴
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_doco:img:风味菜谱" class="figure" data-float="mzc00200x6fe6l5" href="https://v.qq.com/x/cover/mzc00200x6fe6l5.html" tabindex="-1" target="_blank">
       <img alt="风味菜谱" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_vt_pic/0/mzc00200x6fe6l51631863547150/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        02:30
       </div>
       <div class="figure_score">
        7.5
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_doco:title:风味菜谱" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200x6fe6l5.html" target="_blank" title="风味菜谱">
        风味菜谱
       </a>
       <div class="figure_desc" title="上菜吧！风味大厨">
        上菜吧！风味大厨
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_doco:img:流动的中国" class="figure" data-float="mzc00200lils66d" href="https://v.qq.com/x/cover/mzc00200lils66d.html" tabindex="-1" target="_blank">
       <img alt="流动的中国" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_vt_pic/0/mzc00200lils66d1630985116047/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        46:25
       </div>
       <div class="figure_score">
        9.2
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_doco:title:流动的中国" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200lils66d.html" target="_blank" title="流动的中国">
        流动的中国
       </a>
       <div class="figure_desc" title="描摹奋斗中的当代国人群像">
        描摹奋斗中的当代国人群像
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_doco:img:我们的滚烫人声" class="figure" data-float="mzc0020023ebx7u" href="https://v.qq.com/x/cover/mzc0020023ebx7u.html" tabindex="-1" target="_blank">
       <img alt="我们的滚烫人声" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_vt_pic/0/mzc0020023ebx7u1632321773075/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
       </div>
       <div class="figure_score">
        9.0
       </div>
       <img alt="腾讯出品" class="mark_v mark_v_腾讯出品" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_self_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_self_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_doco:title:我们的滚烫人声" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc0020023ebx7u.html" target="_blank" title="我们的滚烫人声">
        我们的滚烫人声
       </a>
       <div class="figure_desc" title="首档30+男性寻声纪实节目">
        首档30+男性寻声纪实节目
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_doco:img:奇妙星球" class="figure" data-float="mzc002000c6yr6j" href="https://v.qq.com/x/cover/mzc002000c6yr6j.html" tabindex="-1" target="_blank">
       <img alt="奇妙星球" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_vt_pic/0/mzc002000c6yr6j1630979580103/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        49:43
       </div>
       <div class="figure_score">
        9.5
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_doco:title:奇妙星球" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc002000c6yr6j.html" target="_blank" title="奇妙星球">
        奇妙星球
       </a>
       <div class="figure_desc" title="开启神奇的地球探秘之旅">
        开启神奇的地球探秘之旅
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_doco:img:老西藏故事" class="figure" data-float="mzc00200l7bvyni" href="https://v.qq.com/x/cover/mzc00200l7bvyni.html" tabindex="-1" target="_blank">
       <img alt="老西藏故事" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_vt_pic/0/mzc00200l7bvyni1630852070563/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        03:30
       </div>
       <div class="figure_score">
        7.4
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_doco:title:老西藏故事" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200l7bvyni.html" target="_blank" title="老西藏故事">
        老西藏故事
       </a>
       <div class="figure_desc" title="史实呈现的“老西藏精神”">
        史实呈现的“老西藏精神”
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_doco:img:向着宵夜的方向 第2季" class="figure" data-float="mzc00200jwzaw07" href="https://v.qq.com/x/cover/mzc00200jwzaw07.html" tabindex="-1" target="_blank">
       <img alt="向着宵夜的方向 第2季" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_vt_pic/0/mzc00200jwzaw071628078116893/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        09:04
       </div>
       <div class="figure_score">
        9.6
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_doco:title:向着宵夜的方向 第2季" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200jwzaw07.html" target="_blank" title="向着宵夜的方向 第2季">
        向着宵夜的方向 第2季
       </a>
       <div class="figure_desc" title="解锁35座城极致宵夜美食">
        解锁35座城极致宵夜美食
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_doco:img:119请回答" class="figure" data-float="mzc00200m7o91am" href="https://v.qq.com/x/cover/mzc00200m7o91am.html" tabindex="-1" target="_blank">
       <img alt="119请回答" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_vt_pic/0/mzc00200m7o91am1626684063712/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        45:34
       </div>
       <div class="figure_score">
        9.6
       </div>
       <img alt="腾讯出品" class="mark_v mark_v_腾讯出品" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_self_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_self_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_doco:title:119请回答" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200m7o91am.html" target="_blank" title="119请回答">
        119请回答
       </a>
       <div class="figure_desc" title="在无常的世界里全力以赴">
        在无常的世界里全力以赴
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_doco:img:人间世 第1季" class="figure" data-float="mzc00200cdwdvzc" href="https://v.qq.com/x/cover/mzc00200cdwdvzc.html" tabindex="-1" target="_blank">
       <img alt="人间世 第1季" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_vt_pic/0/mzc00200cdwdvzc1630653358829/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        45:19
       </div>
       <div class="figure_score">
        9.7
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_doco:title:人间世 第1季" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200cdwdvzc.html" target="_blank" title="人间世 第1季">
        人间世 第1季
       </a>
       <div class="figure_desc" title="人间世态，深度展现">
        人间世态，深度展现
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_doco:img:我不知道啊" class="figure" data-float="mzc00200m6ya9tl" href="https://v.qq.com/x/cover/mzc00200m6ya9tl.html" tabindex="-1" target="_blank">
       <img alt="我不知道啊" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_vt_pic/0/mzc00200m6ya9tl1629809586554/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        50:40
       </div>
       <div class="figure_score">
        8.8
       </div>
       <img alt="独播" class="mark_v mark_v_独播" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_only_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_only_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_doco:title:我不知道啊" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200m6ya9tl.html" target="_blank" title="我不知道啊">
        我不知道啊
       </a>
       <div class="figure_desc" title="GQ编辑总监对话各界大咖">
        GQ编辑总监对话各界大咖
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_doco:img:文博中华" class="figure" data-float="mzc002000d8h7hg" href="https://v.qq.com/x/cover/mzc002000d8h7hg.html" tabindex="-1" target="_blank">
       <img alt="文博中华" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_vt_pic/0/mzc002000d8h7hg1628473434369/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        20:06
       </div>
       <div class="figure_score">
        7.3
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_doco:title:文博中华" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc002000d8h7hg.html" target="_blank" title="文博中华">
        文博中华
       </a>
       <div class="figure_desc" title="揭秘文物的前世传奇与今生故事">
        揭秘文物的前世传奇与今生故事
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_doco:img:迈进未来" class="figure" data-float="mzc002007eh6kf9" href="https://v.qq.com/x/cover/mzc002007eh6kf9.html" tabindex="-1" target="_blank">
       <img alt="迈进未来" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_vt_pic/0/mzc002007eh6kf91628823138587/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        46:53
       </div>
       <div class="figure_score">
        7.2
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_doco:title:迈进未来" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc002007eh6kf9.html" target="_blank" title="迈进未来">
        迈进未来
       </a>
       <div class="figure_desc" title="不是科幻，这些未来已来！">
        不是科幻，这些未来已来！
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_doco:img:巴西：街头的足球王国" class="figure" data-float="mzc00200sj0rvjm" href="https://v.qq.com/x/cover/mzc00200sj0rvjm.html" tabindex="-1" target="_blank">
       <img alt="巴西：街头的足球王国" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_vt_pic/0/mzc00200sj0rvjm1628736812206/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        07:33
       </div>
       <div class="figure_score">
        7.2
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_doco:title:巴西：街头的足球王国" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200sj0rvjm.html" target="_blank" title="巴西：街头的足球王国">
        巴西：街头的足球王国
       </a>
       <div class="figure_desc" title="实地揭秘！巴西足球为何强">
        实地揭秘！巴西足球为何强
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_doco:img:心外纪事" class="figure" data-float="mzc00200cm8ujt5" href="https://v.qq.com/x/cover/mzc00200cm8ujt5.html" tabindex="-1" target="_blank">
       <img alt="心外纪事" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_vt_pic/0/mzc00200cm8ujt51629334549895/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        37:49
       </div>
       <div class="figure_score">
        7.2
       </div>
       <img alt="独播" class="mark_v mark_v_独播" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_only_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_only_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_doco:title:心外纪事" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200cm8ujt5.html" target="_blank" title="心外纪事">
        心外纪事
       </a>
       <div class="figure_desc" title="北医三院高危病例治疗全纪录">
        北医三院高危病例治疗全纪录
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_doco:img:知味新疆 第1季" class="figure" data-float="mzc00200b89ckbn" href="https://v.qq.com/x/cover/mzc00200b89ckbn.html" tabindex="-1" target="_blank">
       <img alt="知味新疆 第1季" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_vt_pic/0/mzc00200b89ckbn1627825599654/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        26:35
       </div>
       <div class="figure_score">
        8.0
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_doco:title:知味新疆 第1季" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200b89ckbn.html" target="_blank" title="知味新疆 第1季">
        知味新疆 第1季
       </a>
       <div class="figure_desc" title="品尝西北美味，探索大美新疆！">
        品尝西北美味，探索大美新疆！
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_doco:img:边走边唱" class="figure" data-float="mzc00200yfsd9qu" href="https://v.qq.com/x/cover/mzc00200yfsd9qu.html" tabindex="-1" target="_blank">
       <img alt="边走边唱" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_vt_pic/0/mzc00200yfsd9qu1629027208734/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        29:44
       </div>
       <div class="figure_score">
        8.8
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_doco:title:边走边唱" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200yfsd9qu.html" target="_blank" title="边走边唱">
        边走边唱
       </a>
       <div class="figure_desc" title="游吟大地，边走边唱！">
        游吟大地，边走边唱！
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_doco:img:你叫什么？" class="figure" data-float="mzc00200oe4yzjt" href="https://v.qq.com/x/cover/mzc00200oe4yzjt.html" tabindex="-1" target="_blank">
       <img alt="你叫什么？" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_vt_pic/0/mzc00200oe4yzjt1627890027066/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        28:03
       </div>
       <div class="figure_score">
        7.2
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_doco:title:你叫什么？" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200oe4yzjt.html" target="_blank" title="你叫什么？">
        你叫什么？
       </a>
       <div class="figure_desc" title="妙趣横生的动物冷知识">
        妙趣横生的动物冷知识
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_doco:img:超凡未来：你不了解的中国科学故事" class="figure" data-float="mzc00200cu683i5" href="https://v.qq.com/x/cover/mzc00200cu683i5.html" tabindex="-1" target="_blank">
       <img alt="超凡未来：你不了解的中国科学故事" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_vt_pic/0/mzc00200cu683i51628509515590/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        52:47
       </div>
       <div class="figure_score">
        7.2
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_doco:title:超凡未来：你不了解的中国科学故事" class="figure_title figure_title_two_row" href="https://v.qq.com/x/cover/mzc00200cu683i5.html" target="_blank" title="超凡未来：你不了解的中国科学故事">
        超凡未来：你不了解的中国科学故事
       </a>
       <div class="figure_desc" title="中国科学家究竟有多牛？">
        中国科学家究竟有多牛？
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_doco:img:荣耀巅峰" class="figure" data-float="mzc00200pkhy2oj" href="https://v.qq.com/x/cover/mzc00200pkhy2oj.html" tabindex="-1" target="_blank">
       <img alt="荣耀巅峰" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_vt_pic/0/mzc00200pkhy2oj1627471395628/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        25:51
       </div>
       <div class="figure_score">
        8.8
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_doco:title:荣耀巅峰" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200pkhy2oj.html" target="_blank" title="荣耀巅峰">
        荣耀巅峰
       </a>
       <div class="figure_desc" title="中国赛艇队备战奥运纪实">
        中国赛艇队备战奥运纪实
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_doco:img:柴米油盐之上" class="figure" data-float="mzc002000qmsb4h" href="https://v.qq.com/x/cover/mzc002000qmsb4h.html" tabindex="-1" target="_blank">
       <img alt="柴米油盐之上" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_vt_pic/0/mzc002000qmsb4h1625565855668/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        35:52
       </div>
       <div class="figure_score">
        9.5
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_doco:title:柴米油盐之上" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc002000qmsb4h.html" target="_blank" title="柴米油盐之上">
        柴米油盐之上
       </a>
       <div class="figure_desc" title="致敬追寻美好生活的每个人">
        致敬追寻美好生活的每个人
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_doco:img:中国船谱" class="figure" data-float="mzc00200gim8f21" href="https://v.qq.com/x/cover/mzc00200gim8f21.html" tabindex="-1" target="_blank">
       <img alt="中国船谱" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_vt_pic/0/mzc00200gim8f211625886829857/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        25:00
       </div>
       <div class="figure_score">
        9.2
       </div>
       <img alt="独播" class="mark_v mark_v_独播" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_only_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_only_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_doco:title:中国船谱" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200gim8f21.html" target="_blank" title="中国船谱">
        中国船谱
       </a>
       <div class="figure_desc" title="一部恢弘的中国船舶发展史">
        一部恢弘的中国船舶发展史
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_doco:img:生命未来" class="figure" data-float="mzc00200xn152g6" href="https://v.qq.com/x/cover/mzc00200xn152g6.html" tabindex="-1" target="_blank">
       <img alt="生命未来" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_vt_pic/0/mzc00200xn152g61626749794800/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
       </div>
       <div class="figure_score">
        7.3
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_doco:title:生命未来" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200xn152g6.html" target="_blank" title="生命未来">
        生命未来
       </a>
       <div class="figure_desc" title="我们为什么需要学习科技史？">
        我们为什么需要学习科技史？
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_doco:img:携手，为人民" class="figure" data-float="mzc00200wds9vxc" href="https://v.qq.com/x/cover/mzc00200wds9vxc.html" tabindex="-1" target="_blank">
       <img alt="携手，为人民" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_vt_pic/0/mzc00200wds9vxc1625572055579/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        08:32
       </div>
       <div class="figure_score">
        7.1
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_doco:title:携手，为人民" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200wds9vxc.html" target="_blank" title="携手，为人民">
        携手，为人民
       </a>
       <div class="figure_desc" title="这就是中国共产党员的手">
        这就是中国共产党员的手
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_doco:img:滹沱记忆" class="figure" data-float="mzc00200rr9jo9y" href="https://v.qq.com/x/cover/mzc00200rr9jo9y.html" tabindex="-1" target="_blank">
       <img alt="滹沱记忆" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_vt_pic/0/mzc00200rr9jo9y1625481418053/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        49:00
       </div>
       <div class="figure_score">
        7.1
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_doco:title:滹沱记忆" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200rr9jo9y.html" target="_blank" title="滹沱记忆">
        滹沱记忆
       </a>
       <div class="figure_desc" title="追溯一条大河的抗战记忆">
        追溯一条大河的抗战记忆
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_doco:img:共和国医者" class="figure" data-float="mzc00200zhfrkew" href="https://v.qq.com/x/cover/mzc00200zhfrkew.html" tabindex="-1" target="_blank">
       <img alt="共和国医者" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_vt_pic/0/mzc00200zhfrkew1624870495287/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        32:30
       </div>
       <div class="figure_score">
        9.2
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_doco:title:共和国医者" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200zhfrkew.html" target="_blank" title="共和国医者">
        共和国医者
       </a>
       <div class="figure_desc" title="珍稀视角回首百年峥嵘岁月">
        珍稀视角回首百年峥嵘岁月
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_doco:img:无声的功勋" class="figure" data-float="mzc00200w9qrf4g" href="https://v.qq.com/x/cover/mzc00200w9qrf4g.html" tabindex="-1" target="_blank">
       <img alt="无声的功勋" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_vt_pic/0/mzc00200w9qrf4g1624958436662/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        08:55
       </div>
       <div class="figure_score">
        9.0
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_doco:title:无声的功勋" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200w9qrf4g.html" target="_blank" title="无声的功勋">
        无声的功勋
       </a>
       <div class="figure_desc" title="致敬隐蔽战线无名英雄">
        致敬隐蔽战线无名英雄
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_doco:img:风味原产地·贵阳" class="figure" data-float="mzc002006rwlwzl" href="https://v.qq.com/x/cover/mzc002006rwlwzl.html" tabindex="-1" target="_blank">
       <img alt="风味原产地·贵阳" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_vt_pic/0/mzc002006rwlwzl1623382431646/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        12:24
       </div>
       <div class="figure_score">
        9.1
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_doco:title:风味原产地·贵阳" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc002006rwlwzl.html" target="_blank" title="风味原产地·贵阳">
        风味原产地·贵阳
       </a>
       <div class="figure_desc" title="馋到爆！贵阳极致美食图鉴">
        馋到爆！贵阳极致美食图鉴
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_doco:img:雌雄有别" class="figure" data-float="mzc00200eagkput" href="https://v.qq.com/x/cover/mzc00200eagkput.html" tabindex="-1" target="_blank">
       <img alt="雌雄有别" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_vt_pic/0/mzc00200eagkput1624272454129/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        52:31
       </div>
       <div class="figure_score">
        9.1
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_doco:title:雌雄有别" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200eagkput.html" target="_blank" title="雌雄有别">
        雌雄有别
       </a>
       <div class="figure_desc" title="动物版“夫妻的世界”">
        动物版“夫妻的世界”
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_doco:img:广东非遗影像" class="figure" data-float="mzc00200nhlxkhw" href="https://v.qq.com/x/cover/mzc00200nhlxkhw.html" tabindex="-1" target="_blank">
       <img alt="广东非遗影像" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_vt_pic/0/mzc00200nhlxkhw1625211214536/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        05:23
       </div>
       <div class="figure_score">
        7.1
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_doco:title:广东非遗影像" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200nhlxkhw.html" target="_blank" title="广东非遗影像">
        广东非遗影像
       </a>
       <div class="figure_desc" title="带你云游岭南赏非遗">
        带你云游岭南赏非遗
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_doco:img:这煎饼还要做到什么时候" class="figure" data-float="mzc00200heriqzh" href="https://v.qq.com/x/cover/mzc00200heriqzh.html" tabindex="-1" target="_blank">
       <img alt="这煎饼还要做到什么时候" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_vt_pic/0/mzc00200heriqzh1624270376392/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        14:30
       </div>
       <div class="figure_score">
        8.4
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_doco:title:这煎饼还要做到什么时候" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200heriqzh.html" target="_blank" title="这煎饼还要做到什么时候">
        这煎饼还要做到什么时候
       </a>
       <div class="figure_desc" title="由煎饼引发的人生况味">
        由煎饼引发的人生况味
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_doco:img:文秀，你好" class="figure" data-float="mzc002005ojktuu" href="https://v.qq.com/x/cover/mzc002005ojktuu.html" tabindex="-1" target="_blank">
       <img alt="文秀，你好" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_vt_pic/0/mzc002005ojktuu1623746631963/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        01:13:45
       </div>
       <div class="figure_score">
        7.1
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_doco:title:文秀，你好" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc002005ojktuu.html" target="_blank" title="文秀，你好">
        文秀，你好
       </a>
       <div class="figure_desc" title="扶贫路上谱写青春之歌">
        扶贫路上谱写青春之歌
       </div>
      </div>
     </div>
    </div>
   </div>
  </div>
  <div _expose="choice_xcc_vshou" _wind="columnname=精选_为你精选&amp;controlname=choice_xcc_vshou" class="mod_row_box" cur-page-num="0" data-context="4" data-istyle="4" has-next-page="false" id="choice_xcc_vshou">
   <div class="mod_hd">
    <h2 class="mod_title">
     为你精选
    </h2>
    <div class="mod_page_small">
     <button _stat="choice_xcc_vshou:通栏功能区:上一页" class="btn_prev disabled" title="上一页" wind-click="100">
      <svg class="svg_icon svg_icon_prev" height="10" viewbox="0 0 6 10" width="6">
       <path d="M1.4 4.7L5 1M1.3 5.3L5 9" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="1.4">
       </path>
      </svg>
     </button>
     <span class="page_num" data-count="3" data-info="8 18" data-page="1">
      1/3
     </span>
     <button _stat="choice_xcc_vshou:通栏功能区:下一页" class="btn_next" title="下一页" wind-click="100">
      <svg class="svg_icon svg_icon_next" height="10" viewbox="0 0 6 10" width="6">
       <path d="M4.6 4.7L1 1M4.7 5.3L1 9" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="1.4">
       </path>
      </svg>
     </button>
    </div>
   </div>
   <div class="mod_bd cf _quickopen _quickopen_duration">
    <div class="mod_figure mod_figure_h_default mod_figure_h_default_1row mod_figure_h_default mod_figure_scroll" data-rowcount="8" data-rowlen="1">
     <div __wind="" class="list_item">
      <a _stat="choice_xcc_vshou:img:末日救援⚡灾难大片" class="figure" data-float="mzc00200mcm0lzz" href="https://v.qq.com/x/cover/mzc00200mcm0lzz.html" tabindex="-1" target="_blank">
       <img alt="末日救援⚡灾难大片" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_hz_pic/0/mzc00200mcm0lzz1638328958413/332" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        01:31:09
       </div>
       <div class="figure_score">
        7.9
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="choice_xcc_vshou:title:末日救援⚡灾难大片" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200mcm0lzz.html" target="_blank" title="末日救援⚡灾难大片">
        末日救援⚡灾难大片
       </a>
       <div class="figure_desc" title="外星巨鲲来袭！地球陷落">
        外星巨鲲来袭！地球陷落
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="choice_xcc_vshou:img:良言写意✨甜蜜新剧" class="figure" data-float="mzc00200ev05cth" href="https://v.qq.com/x/cover/mzc00200ev05cth.html" tabindex="-1" target="_blank">
       <img alt="良言写意✨甜蜜新剧" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_hz_pic/0/mzc00200ev05cth1632367977342/332" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        更新至12集
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="choice_xcc_vshou:title:良言写意✨甜蜜新剧" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200ev05cth.html" target="_blank" title="良言写意✨甜蜜新剧">
        良言写意✨甜蜜新剧
       </a>
       <div class="figure_desc" title="罗云熙程潇唯美星空吻">
        罗云熙程潇唯美星空吻
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="choice_xcc_vshou:img:斗罗大陆" class="figure" data-float="m441e3rjq9kwpsc" href="https://v.qq.com/x/cover/m441e3rjq9kwpsc.html" tabindex="-1" target="_blank">
       <img alt="斗罗大陆" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_hz_pic/0/m441e3rjq9kwpsc1543546765/332" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        更新至184集
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="choice_xcc_vshou:title:斗罗大陆" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/m441e3rjq9kwpsc.html" target="_blank" title="斗罗大陆">
        斗罗大陆
       </a>
       <div class="figure_desc" title="此生不悔入唐门">
        此生不悔入唐门
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="choice_xcc_vshou:img:故宫里的大怪兽" class="figure" data-float="mzc00200151n1zn" href="https://v.qq.com/x/cover/mzc00200151n1zn/t00409j922t.html" tabindex="-1" target="_blank">
       <img alt="故宫里的大怪兽" class="figure_pic" loading="lazy" lz_src="//vc.qpic.cn/tpic/mtviuyymHH12w/9dk97656zmrwc002/414" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        全26集
       </div>
       <img alt="腾讯出品" class="mark_v mark_v_腾讯出品" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_self_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_self_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="choice_xcc_vshou:title:故宫里的大怪兽" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200151n1zn/t00409j922t.html" target="_blank" title="故宫里的大怪兽">
        故宫里的大怪兽
       </a>
       <div class="figure_desc" title="小雨唤醒洞光宝石">
        小雨唤醒洞光宝石
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="choice_xcc_vshou:img:令人心动的offer3" class="figure" data-float="mzc0020027kt27b" href="https://v.qq.com/x/cover/mzc0020027kt27b.html" tabindex="-1" target="_blank">
       <img alt="令人心动的offer3" class="figure_pic" loading="lazy" lz_src="//vc.qpic.cn/tpic/mtviuBUb6bLfm/jn168359qwav8656/250" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        2021-12-01 期
       </div>
       <img alt="腾讯出品" class="mark_v mark_v_腾讯出品" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_self_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_self_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="choice_xcc_vshou:title:令人心动的offer3" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc0020027kt27b.html" target="_blank" title="令人心动的offer3">
        令人心动的offer3
       </a>
       <div class="figure_desc" title="张洽高能救场冯琛帅飞">
        张洽高能救场冯琛帅飞
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="choice_xcc_vshou:img:雪鹰领主" class="figure" data-float="sifd2an7kx2h9h8" href="https://v.qq.com/x/cover/sifd2an7kx2h9h8.html" tabindex="-1" target="_blank">
       <img alt="雪鹰领主" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_hz_pic/0/sifd2an7kx2h9h81522480414/332" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        全52集
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="choice_xcc_vshou:title:雪鹰领主" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/sifd2an7kx2h9h8.html" target="_blank" title="雪鹰领主">
        雪鹰领主
       </a>
       <div class="figure_desc" title="吞噬星空 神帝巅峰">
        吞噬星空 神帝巅峰
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="choice_xcc_vshou:img:雄兵连之诸天降临" class="figure" data-float="ei44lqqq0fsg5aq" href="https://v.qq.com/x/cover/ei44lqqq0fsg5aq.html" tabindex="-1" target="_blank">
       <img alt="雄兵连之诸天降临" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/tv/0/45599336_175100/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        全26集
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="choice_xcc_vshou:title:雄兵连之诸天降临" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/ei44lqqq0fsg5aq.html" target="_blank" title="雄兵连之诸天降临">
        雄兵连之诸天降临
       </a>
       <div class="figure_desc" title="【单人预告】天基王鹤熙前线快报">
        【单人预告】天基王鹤熙前线快报
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="choice_xcc_vshou:img:非人哉" class="figure" data-float="wk85h1a859a8350" href="https://v.qq.com/x/cover/wk85h1a859a8350.html" tabindex="-1" target="_blank">
       <img alt="非人哉" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_hz_pic/0/wk85h1a859a83501538015473/332" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        全96集
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="choice_xcc_vshou:title:非人哉" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/wk85h1a859a8350.html" target="_blank" title="非人哉">
        非人哉
       </a>
       <div class="figure_desc" title="神仙妖怪的爆笑日常">
        神仙妖怪的爆笑日常
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="choice_xcc_vshou:img:武动乾坤" class="figure" data-float="jg1skog3zvrv9ur" href="https://v.qq.com/x/cover/jg1skog3zvrv9ur.html" tabindex="-1" target="_blank">
       <img alt="武动乾坤" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_hz_pic/0/jg1skog3zvrv9ur1510104637/332" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        全24集
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="choice_xcc_vshou:title:武动乾坤" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/jg1skog3zvrv9ur.html" target="_blank" title="武动乾坤">
        武动乾坤
       </a>
       <div class="figure_desc" title="武之极，破苍穹，动乾坤">
        武之极，破苍穹，动乾坤
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="choice_xcc_vshou:img:星辰变 第1季" class="figure" data-float="0s8n49g3g1rv1oz" href="https://v.qq.com/x/cover/0s8n49g3g1rv1oz.html" tabindex="-1" target="_blank">
       <img alt="星辰变 第1季" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_hz_pic/0/0s8n49g3g1rv1oz1538703342/332" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        全36集
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="choice_xcc_vshou:title:星辰变 第1季" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/0s8n49g3g1rv1oz.html" target="_blank" title="星辰变 第1季">
        星辰变 第1季
       </a>
       <div class="figure_desc" title="少年逆天改命成王">
        少年逆天改命成王
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="choice_xcc_vshou:img:小伶玩具2" class="figure" data-float="mzc002008turnkk" href="https://v.qq.com/x/cover/mzc002008turnkk.html" tabindex="-1" target="_blank">
       <img alt="小伶玩具2" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_hz_pic/0/mzc002008turnkk1624327603206/332" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        更新至65集
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="choice_xcc_vshou:title:小伶玩具2" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc002008turnkk.html" target="_blank" title="小伶玩具2">
        小伶玩具2
       </a>
       <div class="figure_desc" title="伶可家族伴你快乐成长">
        伶可家族伴你快乐成长
       </div>
      </div>
     </div>
     <!--QQlive_SP_ZZSP_2017_div AD begin...."l=QQlive_SP_ZZSP_2017&log=off"-->
     <div class="l_qq_com" id="QQlive_SP_ZZSP_2017" style="width:240px;height:135px;display:none;">
     </div>
     <!--QQlive_SP_ZZSP_2017 AD end -->
     <!--[if !IE]>|xGv00|84ce96efa7d2c40294cbe2ccee97674e<![endif]-->
     <div __wind="" class="list_item">
      <a _stat="choice_xcc_vshou:img:快把我哥带走 普通话版" class="figure" data-float="1lcp2pf46ms2r3o" href="https://v.qq.com/x/cover/1lcp2pf46ms2r3o.html" tabindex="-1" target="_blank">
       <img alt="快把我哥带走 普通话版" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_hz_pic/0/1lcp2pf46ms2r3o1541993919/332" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        全60集
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="choice_xcc_vshou:title:快把我哥带走 普通话版" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/1lcp2pf46ms2r3o.html" target="_blank" title="快把我哥带走 普通话版">
        快把我哥带走 普通话版
       </a>
       <div class="figure_desc" title="暴力妹和二货哥开启新篇章">
        暴力妹和二货哥开启新篇章
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="choice_xcc_vshou:img:全职法师 第3季" class="figure" data-float="8vdu7i5hr7anq5q" href="https://v.qq.com/x/cover/8vdu7i5hr7anq5q.html" tabindex="-1" target="_blank">
       <img alt="全职法师 第3季" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_hz_pic/0/8vdu7i5hr7anq5q1535824631/332" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        全12集
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="choice_xcc_vshou:title:全职法师 第3季" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/8vdu7i5hr7anq5q.html" target="_blank" title="全职法师 第3季">
        全职法师 第3季
       </a>
       <div class="figure_desc" title="法师集结，决战狂魔">
        法师集结，决战狂魔
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="choice_xcc_vshou:img:我们的歌 第3季" class="figure" data-float="mzc00200iio896t" href="http://v.qq.com/x/cover/mzc00200iio896t/r0041ebx30s.html" tabindex="-1" target="_blank">
       <img alt="我们的歌 第3季" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/media_img/lena/PICx4fqcw_720_1280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        2021-11-28 期
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="choice_xcc_vshou:title:我们的歌 第3季" class="figure_title figure_title_two_row bold" href="http://v.qq.com/x/cover/mzc00200iio896t/r0041ebx30s.html" target="_blank" title="我们的歌 第3季">
        我们的歌 第3季
       </a>
       <div class="figure_desc" title="大张伟跳魔性洗澡舞">
        大张伟跳魔性洗澡舞
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="choice_xcc_vshou:img:画江湖之不良人3" class="figure" data-float="enj7gj9pcksq89p" href="https://v.qq.com/x/cover/enj7gj9pcksq89p.html" tabindex="-1" target="_blank">
       <img alt="画江湖之不良人3" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/38685606_175100/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        全40集
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="choice_xcc_vshou:title:画江湖之不良人3" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/enj7gj9pcksq89p.html" target="_blank" title="画江湖之不良人3">
        画江湖之不良人3
       </a>
       <div class="figure_desc" title="王者弈天下 大唐生死局">
        王者弈天下 大唐生死局
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="choice_xcc_vshou:img:假面骑士时王 普通话版" class="figure" data-float="8nw0d18461epaxc" href="https://v.qq.com/x/cover/8nw0d18461epaxc.html" tabindex="-1" target="_blank">
       <img alt="假面骑士时王 普通话版" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_hz_pic/0/8nw0d18461epaxc1542629567/332" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        全49集
       </div>
       <img alt="独播" class="mark_v mark_v_独播" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_only_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_only_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="choice_xcc_vshou:title:假面骑士时王 普通话版" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/8nw0d18461epaxc.html" target="_blank" title="假面骑士时王 普通话版">
        假面骑士时王 普通话版
       </a>
       <div class="figure_desc" title="集平成假面骑士之力">
        集平成假面骑士之力
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="choice_xcc_vshou:img:导演请指教" class="figure" data-float="mzc00200j97zo8g" href="http://v.qq.com/x/cover/mzc00200j97zo8g/x0041d6f83u.html" tabindex="-1" target="_blank">
       <img alt="导演请指教" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/media_img/lena/PICb8vo70_720_1280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        2021-11-27 期
       </div>
       <img alt="腾讯出品" class="mark_v mark_v_腾讯出品" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_self_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_self_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="choice_xcc_vshou:title:导演请指教" class="figure_title figure_title_two_row bold" href="http://v.qq.com/x/cover/mzc00200j97zo8g/x0041d6f83u.html" target="_blank" title="导演请指教">
        导演请指教
       </a>
       <div class="figure_desc" title="甜！少女迷恋校草帅哥">
        甜！少女迷恋校草帅哥
       </div>
      </div>
     </div>
    </div>
   </div>
  </div>
  <div _expose="choice_qsjd" _wind="columnname=精选_强势接档&amp;controlname=choice_qsjd" class="mod_row_box" cur-page-num="0" data-context="4" data-istyle="28" has-next-page="false" id="choice_qsjd">
   <div class="mod_hd">
    <h2 class="mod_title">
     强势接档
    </h2>
   </div>
   <div class="mod_bd cf _quickopen _quickopen_duration">
    <div class="mod_listings_title">
     <div class="title_item">
      <i class="dot dot_1">
      </i>
      <span class="title">
       今天
      </span>
      <span class="desc">
       12月2日首播
      </span>
     </div>
     <div class="title_item">
      <i class="dot dot_2">
      </i>
      <span class="title">
       本周五
      </span>
      <span class="desc">
       12月3日首播
      </span>
     </div>
     <div class="title_item">
      <i class="dot dot_3">
      </i>
      <span class="title">
       本周五
      </span>
      <span class="desc">
       12月3日首播
      </span>
     </div>
     <div class="title_item">
      <i class="dot dot_4">
      </i>
      <span class="title">
       本周六
      </span>
      <span class="desc">
       12月4日首播
      </span>
     </div>
     <div class="title_item">
      <i class="dot dot_5">
      </i>
      <span class="title">
       本周日
      </span>
      <span class="desc">
       12月5日首播
      </span>
     </div>
     <div class="title_item">
      <i class="dot dot_6">
      </i>
      <span class="title">
       下周二
      </span>
      <span class="desc">
       12月7日首播
      </span>
     </div>
     <div class="title_item">
      <i class="dot dot_7">
      </i>
      <span class="title">
       下周三
      </span>
      <i class="icon_aspect">
       有好戏
      </i>
      <span class="desc">
       12月8日首播
      </span>
     </div>
     <div class="title_item">
      <i class="dot dot_8">
      </i>
      <span class="title">
       12月10日
      </span>
      <span class="desc">
       首播
      </span>
     </div>
    </div>
    <div class="mod_figure mod_figure_v_default mod_figure_v_default_1row mod_figure_v_default mod_figure_scroll" data-rowcount="8" data-rowlen="1">
     <div __wind="" class="list_item">
      <a _stat="choice_qsjd:img:末日救援" class="figure" data-float="mzc00200mcm0lzz" href="https://v.qq.com/x/cover/mzc00200mcm0lzz.html" tabindex="-1" target="_blank">
       <img alt="末日救援" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/mzc00200mcm0lzz1637900530123/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <span class="figure_mask">
       </span>
       <span class="figure_thermometer">
        <i class="icon_thermometer">
         <i class="icon_thermometer_ball">
         </i>
         <i class="icon_thermometer_progress" style="height: 30%;">
         </i>
        </i>
        <span class="thermometer_info">
         <span class="text text1">
          期待指数
         </span>
         <span class="text text2">
          30%
         </span>
        </span>
       </span>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row figure_detail_collect">
       <a _stat="choice_qsjd:title:末日救援" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200mcm0lzz.html" target="_blank" title="末日救援">
        末日救援
       </a>
       <div class="figure_desc" title="巨鲲来袭！地球危在旦夕">
        巨鲲来袭！地球危在旦夕
       </div>
       <button _stat="choice_qsjd:加入收藏按钮" class="figure_collect" data-followlist="mzc00200mcm0lzz" data-followtype="2" data-modidx="0" title="加入收藏">
        <svg class="svg_icon svg_icon_collect" height="16" viewbox="0 0 16 16" width="16">
         <use class="svg_use_before svg_use_before_1" xlink:href="#svg_icon_collect">
         </use>
         <use class="svg_use_before svg_use_before_2" xlink:href="#svg_icon_collect_pure">
         </use>
         <use class="svg_use_after svg_use_after_1" xlink:href="#svg_icon_collected">
         </use>
         <use class="svg_use_after svg_use_after_2" xlink:href="#svg_icon_collected_cancel_pure">
         </use>
        </svg>
        <span class="icon_text">
         加入收藏
        </span>
       </button>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="choice_qsjd:img:大王饶命" class="figure" data-float="od1kjfd56e3s7n7" href="https://v.qq.com/x/cover/od1kjfd56e3s7n7.html" tabindex="-1" target="_blank">
       <img alt="大王饶命" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/od1kjfd56e3s7n71628407965692/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <span class="figure_mask">
       </span>
       <span class="figure_thermometer">
        <i class="icon_thermometer">
         <i class="icon_thermometer_ball">
         </i>
         <i class="icon_thermometer_progress" style="height: 69%;">
         </i>
        </i>
        <span class="thermometer_info">
         <span class="text text1">
          期待指数
         </span>
         <span class="text text2">
          69%
         </span>
        </span>
       </span>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row figure_detail_collect">
       <a _stat="choice_qsjd:title:大王饶命" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/od1kjfd56e3s7n7.html" target="_blank" title="大王饶命">
        大王饶命
       </a>
       <div class="figure_desc" title="灵气复苏，少年崛起">
        灵气复苏，少年崛起
       </div>
       <button _stat="choice_qsjd:加入收藏按钮" class="figure_collect" data-followlist="od1kjfd56e3s7n7" data-followtype="2" data-modidx="1" title="加入收藏">
        <svg class="svg_icon svg_icon_collect" height="16" viewbox="0 0 16 16" width="16">
         <use class="svg_use_before svg_use_before_1" xlink:href="#svg_icon_collect">
         </use>
         <use class="svg_use_before svg_use_before_2" xlink:href="#svg_icon_collect_pure">
         </use>
         <use class="svg_use_after svg_use_after_1" xlink:href="#svg_icon_collected">
         </use>
         <use class="svg_use_after svg_use_after_2" xlink:href="#svg_icon_collected_cancel_pure">
         </use>
        </svg>
        <span class="icon_text">
         加入收藏
        </span>
       </button>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="choice_qsjd:img:第一炉香" class="figure" data-float="mzc002006yay04o" href="https://v.qq.com/x/cover/mzc002006yay04o.html" tabindex="-1" target="_blank">
       <img alt="第一炉香" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/mzc002006yay04o1632293604985/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <span class="figure_mask">
       </span>
       <span class="figure_thermometer">
        <i class="icon_thermometer">
         <i class="icon_thermometer_ball">
         </i>
         <i class="icon_thermometer_progress" style="height: 48%;">
         </i>
        </i>
        <span class="thermometer_info">
         <span class="text text1">
          期待指数
         </span>
         <span class="text text2">
          48%
         </span>
        </span>
       </span>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row figure_detail_collect">
       <a _stat="choice_qsjd:title:第一炉香" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc002006yay04o.html" target="_blank" title="第一炉香">
        第一炉香
       </a>
       <div class="figure_desc" title="马思纯彭于晏命运沉浮">
        马思纯彭于晏命运沉浮
       </div>
       <button _stat="choice_qsjd:加入收藏按钮" class="figure_collect" data-followlist="mzc002006yay04o" data-followtype="2" data-modidx="2" title="加入收藏">
        <svg class="svg_icon svg_icon_collect" height="16" viewbox="0 0 16 16" width="16">
         <use class="svg_use_before svg_use_before_1" xlink:href="#svg_icon_collect">
         </use>
         <use class="svg_use_before svg_use_before_2" xlink:href="#svg_icon_collect_pure">
         </use>
         <use class="svg_use_after svg_use_after_1" xlink:href="#svg_icon_collected">
         </use>
         <use class="svg_use_after svg_use_after_2" xlink:href="#svg_icon_collected_cancel_pure">
         </use>
        </svg>
        <span class="icon_text">
         加入收藏
        </span>
       </button>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="choice_qsjd:img:疯狂海盗团" class="figure" data-float="mzc00200rmpyfmo" href="https://v.qq.com/x/cover/mzc00200rmpyfmo.html" tabindex="-1" target="_blank">
       <img alt="疯狂海盗团" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/mzc00200rmpyfmo1638322146961/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <span class="figure_mask">
       </span>
       <span class="figure_thermometer">
        <i class="icon_thermometer">
         <i class="icon_thermometer_ball">
         </i>
         <i class="icon_thermometer_progress" style="height: 25%;">
         </i>
        </i>
        <span class="thermometer_info">
         <span class="text text1">
          期待指数
         </span>
         <span class="text text2">
          25%
         </span>
        </span>
       </span>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row figure_detail_collect">
       <a _stat="choice_qsjd:title:疯狂海盗团" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200rmpyfmo.html" target="_blank" title="疯狂海盗团">
        疯狂海盗团
       </a>
       <div class="figure_desc" title="关于魔法钻石的故事">
        关于魔法钻石的故事
       </div>
       <button _stat="choice_qsjd:加入收藏按钮" class="figure_collect" data-followlist="mzc00200rmpyfmo" data-followtype="2" data-modidx="3" title="加入收藏">
        <svg class="svg_icon svg_icon_collect" height="16" viewbox="0 0 16 16" width="16">
         <use class="svg_use_before svg_use_before_1" xlink:href="#svg_icon_collect">
         </use>
         <use class="svg_use_before svg_use_before_2" xlink:href="#svg_icon_collect_pure">
         </use>
         <use class="svg_use_after svg_use_after_1" xlink:href="#svg_icon_collected">
         </use>
         <use class="svg_use_after svg_use_after_2" xlink:href="#svg_icon_collected_cancel_pure">
         </use>
        </svg>
        <span class="icon_text">
         加入收藏
        </span>
       </button>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="choice_qsjd:img:不老奇事" class="figure" data-float="v3305uw40gh" data-quickopen="true" href="https://v.qq.com/x/cover/l3685p4jfe8zkyi/v3305uw40gh.html" tabindex="-1" target="_blank">
       <img alt="不老奇事" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/l3685p4jfe8zkyi1634114615715/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <span class="figure_mask">
       </span>
       <span class="figure_thermometer">
        <i class="icon_thermometer">
         <i class="icon_thermometer_ball">
         </i>
         <i class="icon_thermometer_progress" style="height: 65%;">
         </i>
        </i>
        <span class="thermometer_info">
         <span class="text text1">
          期待指数
         </span>
         <span class="text text2">
          65%
         </span>
        </span>
       </span>
      </a>
      <div class="figure_detail figure_detail_two_row figure_detail_collect">
       <a _stat="choice_qsjd:title:不老奇事" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/l3685p4jfe8zkyi/v3305uw40gh.html" target="_blank" title="不老奇事">
        不老奇事
       </a>
       <div class="figure_desc" title="王传君王珞丹一生羁绊">
        王传君王珞丹一生羁绊
       </div>
       <button _stat="choice_qsjd:加入收藏按钮" class="figure_collect" data-followlist="l3685p4jfe8zkyi" data-followtype="2" data-modidx="4" title="加入收藏">
        <svg class="svg_icon svg_icon_collect" height="16" viewbox="0 0 16 16" width="16">
         <use class="svg_use_before svg_use_before_1" xlink:href="#svg_icon_collect">
         </use>
         <use class="svg_use_before svg_use_before_2" xlink:href="#svg_icon_collect_pure">
         </use>
         <use class="svg_use_after svg_use_after_1" xlink:href="#svg_icon_collected">
         </use>
         <use class="svg_use_after svg_use_after_2" xlink:href="#svg_icon_collected_cancel_pure">
         </use>
        </svg>
        <span class="icon_text">
         加入收藏
        </span>
       </button>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="choice_qsjd:img:九叔之古棺奇案1" class="figure" data-float="mzc00200aj0ldsy" href="https://v.qq.com/x/cover/mzc00200aj0ldsy.html" tabindex="-1" target="_blank">
       <img alt="九叔之古棺奇案1" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/mzc00200aj0ldsy1638254486793/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <span class="figure_mask">
       </span>
       <span class="figure_thermometer">
        <i class="icon_thermometer">
         <i class="icon_thermometer_ball">
         </i>
         <i class="icon_thermometer_progress" style="height: 0%;">
         </i>
        </i>
        <span class="thermometer_info">
         <span class="text text1">
          期待指数
         </span>
         <span class="text text2">
          0%
         </span>
        </span>
       </span>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row figure_detail_collect">
       <a _stat="choice_qsjd:title:九叔之古棺奇案1" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200aj0ldsy.html" target="_blank" title="九叔之古棺奇案1">
        九叔之古棺奇案1
       </a>
       <div class="figure_desc" title="驱魔道人大战蛇棺僵尸王">
        驱魔道人大战蛇棺僵尸王
       </div>
       <button _stat="choice_qsjd:加入收藏按钮" class="figure_collect" data-followlist="mzc00200aj0ldsy" data-followtype="2" data-modidx="5" title="加入收藏">
        <svg class="svg_icon svg_icon_collect" height="16" viewbox="0 0 16 16" width="16">
         <use class="svg_use_before svg_use_before_1" xlink:href="#svg_icon_collect">
         </use>
         <use class="svg_use_before svg_use_before_2" xlink:href="#svg_icon_collect_pure">
         </use>
         <use class="svg_use_after svg_use_after_1" xlink:href="#svg_icon_collected">
         </use>
         <use class="svg_use_after svg_use_after_2" xlink:href="#svg_icon_collected_cancel_pure">
         </use>
        </svg>
        <span class="icon_text">
         加入收藏
        </span>
       </button>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="choice_qsjd:img:蜀山奇仙录" class="figure" data-float="wp8dbx985lurofa" href="https://v.qq.com/x/cover/wp8dbx985lurofa.html" tabindex="-1" target="_blank">
       <img alt="蜀山奇仙录" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/wp8dbx985lurofa1637131621022/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <span class="figure_mask">
       </span>
       <span class="figure_thermometer">
        <i class="icon_thermometer">
         <i class="icon_thermometer_ball">
         </i>
         <i class="icon_thermometer_progress" style="height: 94%;">
         </i>
        </i>
        <span class="thermometer_info">
         <span class="text text1">
          期待指数
         </span>
         <span class="text text2">
          94%
         </span>
        </span>
       </span>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row figure_detail_collect">
       <a _stat="choice_qsjd:title:蜀山奇仙录" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/wp8dbx985lurofa.html" target="_blank" title="蜀山奇仙录">
        蜀山奇仙录
       </a>
       <div class="figure_desc" title="仙侠冒险，蜀山奇谈">
        仙侠冒险，蜀山奇谈
       </div>
       <button _stat="choice_qsjd:加入收藏按钮" class="figure_collect" data-followlist="wp8dbx985lurofa" data-followtype="2" data-modidx="6" title="加入收藏">
        <svg class="svg_icon svg_icon_collect" height="16" viewbox="0 0 16 16" width="16">
         <use class="svg_use_before svg_use_before_1" xlink:href="#svg_icon_collect">
         </use>
         <use class="svg_use_before svg_use_before_2" xlink:href="#svg_icon_collect_pure">
         </use>
         <use class="svg_use_after svg_use_after_1" xlink:href="#svg_icon_collected">
         </use>
         <use class="svg_use_after svg_use_after_2" xlink:href="#svg_icon_collected_cancel_pure">
         </use>
        </svg>
        <span class="icon_text">
         加入收藏
        </span>
       </button>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="choice_qsjd:img:二龙湖往事：惊魂夜" class="figure" data-float="t3310dg5jlx" data-quickopen="true" href="https://v.qq.com/x/cover/mzc00200ngpog3f/t3310dg5jlx.html" tabindex="-1" target="_blank">
       <img alt="二龙湖往事：惊魂夜" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/mzc00200ngpog3f1637920773813/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <span class="figure_mask">
       </span>
       <span class="figure_thermometer">
        <i class="icon_thermometer">
         <i class="icon_thermometer_ball">
         </i>
         <i class="icon_thermometer_progress" style="height: 25%;">
         </i>
        </i>
        <span class="thermometer_info">
         <span class="text text1">
          期待指数
         </span>
         <span class="text text2">
          25%
         </span>
        </span>
       </span>
      </a>
      <div class="figure_detail figure_detail_two_row figure_detail_collect">
       <a _stat="choice_qsjd:title:二龙湖往事：惊魂夜" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200ngpog3f/t3310dg5jlx.html" target="_blank" title="二龙湖往事：惊魂夜">
        二龙湖往事：惊魂夜
       </a>
       <div class="figure_desc" title="张浩逆袭成断案英雄">
        张浩逆袭成断案英雄
       </div>
       <button _stat="choice_qsjd:加入收藏按钮" class="figure_collect" data-followlist="mzc00200ngpog3f" data-followtype="2" data-modidx="7" title="加入收藏">
        <svg class="svg_icon svg_icon_collect" height="16" viewbox="0 0 16 16" width="16">
         <use class="svg_use_before svg_use_before_1" xlink:href="#svg_icon_collect">
         </use>
         <use class="svg_use_before svg_use_before_2" xlink:href="#svg_icon_collect_pure">
         </use>
         <use class="svg_use_after svg_use_after_1" xlink:href="#svg_icon_collected">
         </use>
         <use class="svg_use_after svg_use_after_2" xlink:href="#svg_icon_collected_cancel_pure">
         </use>
        </svg>
        <span class="icon_text">
         加入收藏
        </span>
       </button>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="choice_qsjd:img:且试天下" class="figure" data-float="mzc00200v3lnbmd" href="https://v.qq.com/x/cover/mzc00200v3lnbmd.html" tabindex="-1" target="_blank">
       <img alt="且试天下" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_vt_pic/0/mzc00200v3lnbmd1617811887830/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <span class="figure_mask">
       </span>
       <span class="figure_thermometer">
        <i class="icon_thermometer">
         <i class="icon_thermometer_ball">
         </i>
         <i class="icon_thermometer_progress" style="height: 95%;">
         </i>
        </i>
        <span class="thermometer_info">
         <span class="text text1">
          期待指数
         </span>
         <span class="text text2">
          95%
         </span>
        </span>
       </span>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row figure_detail_collect">
       <a _stat="choice_qsjd:title:且试天下" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200v3lnbmd.html" target="_blank" title="且试天下">
        且试天下
       </a>
       <div class="figure_desc" title="杨洋赵露思开启旷世奇旅">
        杨洋赵露思开启旷世奇旅
       </div>
       <button _stat="choice_qsjd:加入收藏按钮" class="figure_collect" data-followlist="mzc00200v3lnbmd" data-followtype="2" data-modidx="8" title="加入收藏">
        <svg class="svg_icon svg_icon_collect" height="16" viewbox="0 0 16 16" width="16">
         <use class="svg_use_before svg_use_before_1" xlink:href="#svg_icon_collect">
         </use>
         <use class="svg_use_before svg_use_before_2" xlink:href="#svg_icon_collect_pure">
         </use>
         <use class="svg_use_after svg_use_after_1" xlink:href="#svg_icon_collected">
         </use>
         <use class="svg_use_after svg_use_after_2" xlink:href="#svg_icon_collected_cancel_pure">
         </use>
        </svg>
        <span class="icon_text">
         加入收藏
        </span>
       </button>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="choice_qsjd:img:繁花" class="figure" data-float="mzc00200whsp9r6" href="https://v.qq.com/x/cover/mzc00200whsp9r6.html" tabindex="-1" target="_blank">
       <img alt="繁花" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_vt_pic/0/mzc00200whsp9r61596292669940/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <span class="figure_mask">
       </span>
       <span class="figure_thermometer">
        <i class="icon_thermometer">
         <i class="icon_thermometer_ball">
         </i>
         <i class="icon_thermometer_progress" style="height: 88%;">
         </i>
        </i>
        <span class="thermometer_info">
         <span class="text text1">
          期待指数
         </span>
         <span class="text text2">
          88%
         </span>
        </span>
       </span>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row figure_detail_collect">
       <a _stat="choice_qsjd:title:繁花" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200whsp9r6.html" target="_blank" title="繁花">
        繁花
       </a>
       <div class="figure_desc" title="胡歌回忆上海老味道">
        胡歌回忆上海老味道
       </div>
       <button _stat="choice_qsjd:加入收藏按钮" class="figure_collect" data-followlist="mzc00200whsp9r6" data-followtype="2" data-modidx="9" title="加入收藏">
        <svg class="svg_icon svg_icon_collect" height="16" viewbox="0 0 16 16" width="16">
         <use class="svg_use_before svg_use_before_1" xlink:href="#svg_icon_collect">
         </use>
         <use class="svg_use_before svg_use_before_2" xlink:href="#svg_icon_collect_pure">
         </use>
         <use class="svg_use_after svg_use_after_1" xlink:href="#svg_icon_collected">
         </use>
         <use class="svg_use_after svg_use_after_2" xlink:href="#svg_icon_collected_cancel_pure">
         </use>
        </svg>
        <span class="icon_text">
         加入收藏
        </span>
       </button>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="choice_qsjd:img:爱的二八定律" class="figure" data-float="mzc00200q0sewxi" href="https://v.qq.com/x/cover/mzc00200q0sewxi.html" tabindex="-1" target="_blank">
       <img alt="爱的二八定律" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_vt_pic/0/mzc00200q0sewxi1623059533221/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <span class="figure_mask">
       </span>
       <span class="figure_thermometer">
        <i class="icon_thermometer">
         <i class="icon_thermometer_ball">
         </i>
         <i class="icon_thermometer_progress" style="height: 93%;">
         </i>
        </i>
        <span class="thermometer_info">
         <span class="text text1">
          期待指数
         </span>
         <span class="text text2">
          93%
         </span>
        </span>
       </span>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row figure_detail_collect">
       <a _stat="choice_qsjd:title:爱的二八定律" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200q0sewxi.html" target="_blank" title="爱的二八定律">
        爱的二八定律
       </a>
       <div class="figure_desc" title="杨幂许凯先婚后爱">
        杨幂许凯先婚后爱
       </div>
       <button _stat="choice_qsjd:加入收藏按钮" class="figure_collect" data-followlist="mzc00200q0sewxi" data-followtype="2" data-modidx="10" title="加入收藏">
        <svg class="svg_icon svg_icon_collect" height="16" viewbox="0 0 16 16" width="16">
         <use class="svg_use_before svg_use_before_1" xlink:href="#svg_icon_collect">
         </use>
         <use class="svg_use_before svg_use_before_2" xlink:href="#svg_icon_collect_pure">
         </use>
         <use class="svg_use_after svg_use_after_1" xlink:href="#svg_icon_collected">
         </use>
         <use class="svg_use_after svg_use_after_2" xlink:href="#svg_icon_collected_cancel_pure">
         </use>
        </svg>
        <span class="icon_text">
         加入收藏
        </span>
       </button>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="choice_qsjd:img:梦华录" class="figure" data-float="mzc00200p51jpn7" href="https://v.qq.com/x/cover/mzc00200p51jpn7.html" tabindex="-1" target="_blank">
       <img alt="梦华录" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_vt_pic/0/mzc00200p51jpn71622966775674/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <span class="figure_mask">
       </span>
       <span class="figure_thermometer">
        <i class="icon_thermometer">
         <i class="icon_thermometer_ball">
         </i>
         <i class="icon_thermometer_progress" style="height: 92%;">
         </i>
        </i>
        <span class="thermometer_info">
         <span class="text text1">
          期待指数
         </span>
         <span class="text text2">
          92%
         </span>
        </span>
       </span>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row figure_detail_collect">
       <a _stat="choice_qsjd:title:梦华录" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200p51jpn7.html" target="_blank" title="梦华录">
        梦华录
       </a>
       <div class="figure_desc" title="刘亦菲陈晓携手成长">
        刘亦菲陈晓携手成长
       </div>
       <button _stat="choice_qsjd:加入收藏按钮" class="figure_collect" data-followlist="mzc00200p51jpn7" data-followtype="2" data-modidx="11" title="加入收藏">
        <svg class="svg_icon svg_icon_collect" height="16" viewbox="0 0 16 16" width="16">
         <use class="svg_use_before svg_use_before_1" xlink:href="#svg_icon_collect">
         </use>
         <use class="svg_use_before svg_use_before_2" xlink:href="#svg_icon_collect_pure">
         </use>
         <use class="svg_use_after svg_use_after_1" xlink:href="#svg_icon_collected">
         </use>
         <use class="svg_use_after svg_use_after_2" xlink:href="#svg_icon_collected_cancel_pure">
         </use>
        </svg>
        <span class="icon_text">
         加入收藏
        </span>
       </button>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="choice_qsjd:img:镜·双城" class="figure" data-float="mzc00200iyo8n07" href="https://v.qq.com/x/cover/mzc00200iyo8n07.html" tabindex="-1" target="_blank">
       <img alt="镜·双城" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_vt_pic/0/mzc00200iyo8n071596185158824/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <span class="figure_mask">
       </span>
       <span class="figure_thermometer">
        <i class="icon_thermometer">
         <i class="icon_thermometer_ball">
         </i>
         <i class="icon_thermometer_progress" style="height: 100%;">
         </i>
        </i>
        <span class="thermometer_info">
         <span class="text text1">
          期待指数
         </span>
         <span class="text text2">
          100%
         </span>
        </span>
       </span>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row figure_detail_collect">
       <a _stat="choice_qsjd:title:镜·双城" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200iyo8n07.html" target="_blank" title="镜·双城">
        镜·双城
       </a>
       <div class="figure_desc" title="李易峰陈钰琪演绎绝美神话">
        李易峰陈钰琪演绎绝美神话
       </div>
       <button _stat="choice_qsjd:加入收藏按钮" class="figure_collect" data-followlist="mzc00200iyo8n07" data-followtype="2" data-modidx="12" title="加入收藏">
        <svg class="svg_icon svg_icon_collect" height="16" viewbox="0 0 16 16" width="16">
         <use class="svg_use_before svg_use_before_1" xlink:href="#svg_icon_collect">
         </use>
         <use class="svg_use_before svg_use_before_2" xlink:href="#svg_icon_collect_pure">
         </use>
         <use class="svg_use_after svg_use_after_1" xlink:href="#svg_icon_collected">
         </use>
         <use class="svg_use_after svg_use_after_2" xlink:href="#svg_icon_collected_cancel_pure">
         </use>
        </svg>
        <span class="icon_text">
         加入收藏
        </span>
       </button>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="choice_qsjd:img:雪中悍刀行" class="figure" data-float="mzc0020020cyvqh" href="https://v.qq.com/x/cover/mzc0020020cyvqh.html" tabindex="-1" target="_blank">
       <img alt="雪中悍刀行" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_vt_pic/0/mzc0020020cyvqh1596358634763/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <span class="figure_mask">
       </span>
       <span class="figure_thermometer">
        <i class="icon_thermometer">
         <i class="icon_thermometer_ball">
         </i>
         <i class="icon_thermometer_progress" style="height: 100%;">
         </i>
        </i>
        <span class="thermometer_info">
         <span class="text text1">
          期待指数
         </span>
         <span class="text text2">
          100%
         </span>
        </span>
       </span>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row figure_detail_collect">
       <a _stat="choice_qsjd:title:雪中悍刀行" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc0020020cyvqh.html" target="_blank" title="雪中悍刀行">
        雪中悍刀行
       </a>
       <div class="figure_desc" title="张若昀王倦再联手">
        张若昀王倦再联手
       </div>
       <button _stat="choice_qsjd:加入收藏按钮" class="figure_collect" data-followlist="mzc0020020cyvqh" data-followtype="2" data-modidx="13" title="加入收藏">
        <svg class="svg_icon svg_icon_collect" height="16" viewbox="0 0 16 16" width="16">
         <use class="svg_use_before svg_use_before_1" xlink:href="#svg_icon_collect">
         </use>
         <use class="svg_use_before svg_use_before_2" xlink:href="#svg_icon_collect_pure">
         </use>
         <use class="svg_use_after svg_use_after_1" xlink:href="#svg_icon_collected">
         </use>
         <use class="svg_use_after svg_use_after_2" xlink:href="#svg_icon_collected_cancel_pure">
         </use>
        </svg>
        <span class="icon_text">
         加入收藏
        </span>
       </button>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="choice_qsjd:img:特战荣耀" class="figure" data-float="dt9oaxh09414471" href="https://v.qq.com/x/cover/dt9oaxh09414471.html" tabindex="-1" target="_blank">
       <img alt="特战荣耀" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_vt_pic/0/dt9oaxh094144711555661113/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <span class="figure_mask">
       </span>
       <span class="figure_thermometer">
        <i class="icon_thermometer">
         <i class="icon_thermometer_ball">
         </i>
         <i class="icon_thermometer_progress" style="height: 100%;">
         </i>
        </i>
        <span class="thermometer_info">
         <span class="text text1">
          期待指数
         </span>
         <span class="text text2">
          100%
         </span>
        </span>
       </span>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row figure_detail_collect">
       <a _stat="choice_qsjd:title:特战荣耀" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/dt9oaxh09414471.html" target="_blank" title="特战荣耀">
        特战荣耀
       </a>
       <div class="figure_desc" title="杨洋转型武警特战队员">
        杨洋转型武警特战队员
       </div>
       <button _stat="choice_qsjd:加入收藏按钮" class="figure_collect" data-followlist="dt9oaxh09414471" data-followtype="2" data-modidx="14" title="加入收藏">
        <svg class="svg_icon svg_icon_collect" height="16" viewbox="0 0 16 16" width="16">
         <use class="svg_use_before svg_use_before_1" xlink:href="#svg_icon_collect">
         </use>
         <use class="svg_use_before svg_use_before_2" xlink:href="#svg_icon_collect_pure">
         </use>
         <use class="svg_use_after svg_use_after_1" xlink:href="#svg_icon_collected">
         </use>
         <use class="svg_use_after svg_use_after_2" xlink:href="#svg_icon_collected_cancel_pure">
         </use>
        </svg>
        <span class="icon_text">
         加入收藏
        </span>
       </button>
      </div>
     </div>
    </div>
   </div>
  </div>
  <div _expose="new_vs3_fun" _wind="columnname=精选_最强笑点&amp;controlname=new_vs3_fun" class="mod_row_box" cur-page-num="0" data-context="5" data-istyle="4" has-next-page="false" id="new_vs3_fun">
   <div class="mod_hd">
    <h2 class="mod_title">
     <a _stat="new_vs3_fun:通栏功能区:通栏标题" class="title_link" data-target="_blank" href="https://v.qq.com/channel/fun">
      最强笑点
     </a>
    </h2>
    <div class="mod_page_small">
     <button _stat="new_vs3_fun:通栏功能区:上一页" class="btn_prev disabled" title="上一页" wind-click="100">
      <svg class="svg_icon svg_icon_prev" height="10" viewbox="0 0 6 10" width="6">
       <path d="M1.4 4.7L5 1M1.3 5.3L5 9" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="1.4">
       </path>
      </svg>
     </button>
     <span class="page_num" data-count="2" data-info="8 9" data-page="1">
      1/2
     </span>
     <button _stat="new_vs3_fun:通栏功能区:下一页" class="btn_next" title="下一页" wind-click="100">
      <svg class="svg_icon svg_icon_next" height="10" viewbox="0 0 6 10" width="6">
       <path d="M4.6 4.7L1 1M4.7 5.3L1 9" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="1.4">
       </path>
      </svg>
     </button>
    </div>
   </div>
   <div class="mod_bd cf _quickopen _quickopen_duration">
    <div class="mod_figure mod_figure_h_default mod_figure_h_default_1row mod_figure_h_default mod_figure_scroll" data-rowcount="8" data-rowlen="1">
     <div __wind="" class="list_item">
      <a _stat="new_vs3_fun:img:倍儿搞笑：雨天出门的我" class="figure" data-float="h09568quna3" data-quickopen="true" href="https://v.qq.com/x/cover/vmp7n9h5n5535c6/h09568quna3.html" tabindex="-1" target="_blank">
       <img alt="倍儿搞笑：雨天出门的我" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/qqvideo/0/h09568quna3/0?_=1588148517686" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        01:03
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_fun:title:倍儿搞笑：雨天出门的我" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/vmp7n9h5n5535c6/h09568quna3.html" target="_blank" title="倍儿搞笑：雨天出门的我">
        倍儿搞笑：雨天出门的我
       </a>
       <div class="figure_desc" title="谁能想到我被雷给吓哭了">
        谁能想到我被雷给吓哭了
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_fun:img:返校后马上就要考试" class="figure" data-float="f3101u31owy" data-quickopen="true" href="https://v.qq.com/x/cover/mzc00200nzlb5qv/f3101u31owy.html" tabindex="-1" target="_blank">
       <img alt="返校后马上就要考试" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vupload/0/1592557151751_g0jwl4lhwh.jpg/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        00:47
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_fun:title:返校后马上就要考试" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200nzlb5qv/f3101u31owy.html" target="_blank" title="返校后马上就要考试">
        返校后马上就要考试
       </a>
       <div class="figure_desc" title="这也太惨了！">
        这也太惨了！
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_fun:img:韬韬聊悲伤心事" class="figure" data-float="p3102cvi7ft" data-quickopen="true" href="https://v.qq.com/x/cover/mzc00200nzlb5qv/p3102cvi7ft.html" tabindex="-1" target="_blank">
       <img alt="韬韬聊悲伤心事" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vupload/0/1592823255398_xgc1cjgmhuk.jpg/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        00:47
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_fun:title:韬韬聊悲伤心事" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200nzlb5qv/p3102cvi7ft.html" target="_blank" title="韬韬聊悲伤心事">
        韬韬聊悲伤心事
       </a>
       <div class="figure_desc" title="被孙珍妮一句话扎心了！">
        被孙珍妮一句话扎心了！
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_fun:img:夏天的奇葩降温方式" class="figure" data-float="j310141ur4m" data-quickopen="true" href="https://v.qq.com/x/cover/mzc00200ufmnjjk/j310141ur4m.html" tabindex="-1" target="_blank">
       <img alt="夏天的奇葩降温方式" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vupload/0/1592823266609_s845obwn9g.jpg/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        01:12
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_fun:title:夏天的奇葩降温方式" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200ufmnjjk/j310141ur4m.html" target="_blank" title="夏天的奇葩降温方式">
        夏天的奇葩降温方式
       </a>
       <div class="figure_desc" title="这些人真是人才！">
        这些人真是人才！
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_fun:img:那些年见过的奇葩美甲" class="figure" data-float="x3101au7ab7" data-quickopen="true" href="https://v.qq.com/x/cover/mzc00200ufmnjjk/x3101au7ab7.html" tabindex="-1" target="_blank">
       <img alt="那些年见过的奇葩美甲" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vupload/0/1592823269550_tmjqaizzfb.jpg/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        01:13
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_fun:title:那些年见过的奇葩美甲" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200ufmnjjk/x3101au7ab7.html" target="_blank" title="那些年见过的奇葩美甲">
        那些年见过的奇葩美甲
       </a>
       <div class="figure_desc" title="你这造型不是开玩笑？">
        你这造型不是开玩笑？
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_fun:img:理发店剪出这些奇葩发型" class="figure" data-float="l3101781jav" data-quickopen="true" href="https://v.qq.com/x/cover/mzc00200ufmnjjk/l3101781jav.html" tabindex="-1" target="_blank">
       <img alt="理发店剪出这些奇葩发型" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vupload/0/1592823275539_74b18u44wc.jpg/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        01:17
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_fun:title:理发店剪出这些奇葩发型" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200ufmnjjk/l3101781jav.html" target="_blank" title="理发店剪出这些奇葩发型">
        理发店剪出这些奇葩发型
       </a>
       <div class="figure_desc" title="你们真不是得罪了发型师？">
        你们真不是得罪了发型师？
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_fun:img:张口要买私人飞机" class="figure" data-float="a3101e1ov95" data-quickopen="true" href="https://v.qq.com/x/cover/xbtoei1vdczrkjo/a3101e1ov95.html" tabindex="-1" target="_blank">
       <img alt="张口要买私人飞机" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vupload/0/1592557152838_y5gob5hknud.jpg/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        01:01
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_fun:title:张口要买私人飞机" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/xbtoei1vdczrkjo/a3101e1ov95.html" target="_blank" title="张口要买私人飞机">
        张口要买私人飞机
       </a>
       <div class="figure_desc" title="你太膨胀了吧？">
        你太膨胀了吧？
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_fun:img:如何自制“日式鳗鱼饭”？" class="figure" data-float="f31010s095d" data-quickopen="true" href="https://v.qq.com/x/cover/pyy9xj8ibzdrgri/f31010s095d.html" tabindex="-1" target="_blank">
       <img alt="如何自制“日式鳗鱼饭”？" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vupload/0/1592557153848_2v7160yo9ww.jpg/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        05:12
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_fun:title:如何自制“日式鳗鱼饭”？" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/pyy9xj8ibzdrgri/f31010s095d.html" target="_blank" title="如何自制“日式鳗鱼饭”？">
        如何自制“日式鳗鱼饭”？
       </a>
       <div class="figure_desc" title="买2斤的巨型鳗鱼后悔了！">
        买2斤的巨型鳗鱼后悔了！
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_fun:img:单身和穷必选一个" class="figure" data-float="e3100qy2zox" data-quickopen="true" href="https://v.qq.com/x/cover/mzc002002q08etm/e3100qy2zox.html" tabindex="-1" target="_blank">
       <img alt="单身和穷必选一个" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vupload/0/1592557155046_w9ropihtmj.jpg/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        03:37
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_fun:title:单身和穷必选一个" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc002002q08etm/e3100qy2zox.html" target="_blank" title="单身和穷必选一个">
        单身和穷必选一个
       </a>
       <div class="figure_desc" title="你会怎么选？">
        你会怎么选？
       </div>
      </div>
     </div>
    </div>
   </div>
  </div>
  <div _expose="new_vs3_life" _wind="columnname=精选_生活资讯&amp;controlname=new_vs3_life" class="mod_row_box" cur-page-num="0" data-context="5" data-istyle="4" has-next-page="false" id="new_vs3_life">
   <div class="mod_hd">
    <h2 class="mod_title">
     <a _stat="new_vs3_life:通栏功能区:通栏标题" class="title_link" data-target="_blank" href="https://v.qq.com/channel/life">
      生活资讯
     </a>
    </h2>
    <div class="mod_page_small">
     <button _stat="new_vs3_life:通栏功能区:上一页" class="btn_prev disabled" title="上一页" wind-click="100">
      <svg class="svg_icon svg_icon_prev" height="10" viewbox="0 0 6 10" width="6">
       <path d="M1.4 4.7L5 1M1.3 5.3L5 9" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="1.4">
       </path>
      </svg>
     </button>
     <span class="page_num" data-count="2" data-info="8 9" data-page="1">
      1/2
     </span>
     <button _stat="new_vs3_life:通栏功能区:下一页" class="btn_next" title="下一页" wind-click="100">
      <svg class="svg_icon svg_icon_next" height="10" viewbox="0 0 6 10" width="6">
       <path d="M4.6 4.7L1 1M4.7 5.3L1 9" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="1.4">
       </path>
      </svg>
     </button>
    </div>
   </div>
   <div class="mod_bd cf _quickopen _quickopen_duration">
    <div class="mod_figure mod_figure_h_default mod_figure_h_default_1row mod_figure_h_default mod_figure_scroll" data-rowcount="8" data-rowlen="1">
     <div __wind="" class="list_item">
      <a _stat="new_vs3_life:img:学科建设管理创新与实践" class="figure" href="https://v.qq.com/live/p/topic/128753/index.html" tabindex="-1" target="_blank">
       <img alt="学科建设管理创新与实践" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/media_img/lena/PICbqlno9_720_1280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_life:title:学科建设管理创新与实践" class="figure_title figure_title_two_row bold" href="https://v.qq.com/live/p/topic/128753/index.html" target="_blank" title="学科建设管理创新与实践">
        学科建设管理创新与实践
       </a>
       <div class="figure_desc" title="人民名医解读">
        人民名医解读
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_life:img:虎年十二生肖财富运" class="figure" data-float="e0041mzocfy" href="https://v.qq.com/x/cover/mzc00200d8nk29z/e0041mzocfy.html" tabindex="-1" target="_blank">
       <img alt="虎年十二生肖财富运" class="figure_pic" loading="lazy" lz_src="//vfiles.gtimg.cn/vupload/20211202/5f374d1638428106185.jpg" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        25:46
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_life:title:虎年十二生肖财富运" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200d8nk29z/e0041mzocfy.html" target="_blank" title="虎年十二生肖财富运">
        虎年十二生肖财富运
       </a>
       <div class="figure_desc" title="2022大师季">
        2022大师季
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_life:img:丰收了好村光" class="figure" data-float="p0041yj63z6" data-quickopen="true" href="http://v.qq.com/x/cover/mzc00200v5lhxat/a0041bq0zow.html" tabindex="-1" target="_blank">
       <img alt="丰收了好村光" class="figure_pic" loading="lazy" lz_src="//vfiles.gtimg.cn/vupload/20211201/9931751638327534793.jpg" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        06:16
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_life:title:丰收了好村光" class="figure_title figure_title_two_row bold" href="http://v.qq.com/x/cover/mzc00200v5lhxat/a0041bq0zow.html" target="_blank" title="丰收了好村光">
        丰收了好村光
       </a>
       <div class="figure_desc" title="来自三峡的“梦想之橙”">
        来自三峡的“梦想之橙”
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_life:img:试吃网投七大饺子" class="figure" data-float="s327524cqwj" data-quickopen="true" href="http://v.qq.com/x/cover/mzc00200iawg1el/s327524cqwj.html" tabindex="-1" target="_blank">
       <img alt="试吃网投七大饺子" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/media_img/lena/PICdw0zhv_720_1280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        07:48
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_life:title:试吃网投七大饺子" class="figure_title figure_title_two_row bold" href="http://v.qq.com/x/cover/mzc00200iawg1el/s327524cqwj.html" target="_blank" title="试吃网投七大饺子">
        试吃网投七大饺子
       </a>
       <div class="figure_desc" title="最后一名竟然赶上一天工资？">
        最后一名竟然赶上一天工资？
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_life:img:如果我的猫是兽医" class="figure" data-float="j3311jz6eoj" data-quickopen="true" href="https://v.qq.com/x/cover/mzc00200ykusi4g/j3311jz6eoj.html" tabindex="-1" target="_blank">
       <img alt="如果我的猫是兽医" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/media_img/lena/PIC8j4arw_720_1280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        01:24
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_life:title:如果我的猫是兽医" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200ykusi4g/j3311jz6eoj.html" target="_blank" title="如果我的猫是兽医">
        如果我的猫是兽医
       </a>
       <div class="figure_desc" title="萌宠微剧场">
        萌宠微剧场
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_life:img:7中传统风物做成绒花" class="figure" data-float="mzc00200ykusi4g" href="http://v.qq.com/x/cover/mzc0020013tpvxr/v3311xftf77.html" tabindex="-1" target="_blank">
       <img alt="7中传统风物做成绒花" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/media_img/lena/PICzuqw3u_720_1280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_life:title:7中传统风物做成绒花" class="figure_title figure_title_two_row bold" href="http://v.qq.com/x/cover/mzc0020013tpvxr/v3311xftf77.html" target="_blank" title="7中传统风物做成绒花">
        7中传统风物做成绒花
       </a>
       <div class="figure_desc" title="跟我一起做绒花：冬日祝愿">
        跟我一起做绒花：冬日祝愿
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_life:img:无辣不欢鸡蛋粿" class="figure" data-float="p3306h53o5d" data-quickopen="true" href="https://v.qq.com/x/cover/mzc00200tltri4g/p3306h53o5d.html" tabindex="-1" target="_blank">
       <img alt="无辣不欢鸡蛋粿" class="figure_pic" loading="lazy" lz_src="//vfiles.gtimg.cn/vupload/20211201/a8447c1638325240483.jpg" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        13:18
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_life:title:无辣不欢鸡蛋粿" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200tltri4g/p3306h53o5d.html" target="_blank" title="无辣不欢鸡蛋粿">
        无辣不欢鸡蛋粿
       </a>
       <div class="figure_desc" title="鸡蛋馅儿也要配辣椒！">
        鸡蛋馅儿也要配辣椒！
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_life:img:10W日元挑战奇葩扭蛋机" class="figure" data-float="l3310d8tofg" data-quickopen="true" href="http://v.qq.com/x/cover/mzc00200rali5o2/l3310d8tofg.html" tabindex="-1" target="_blank">
       <img alt="10W日元挑战奇葩扭蛋机" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/media_img/lena/PICc4sach_720_1280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        10:07
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_life:title:10W日元挑战奇葩扭蛋机" class="figure_title figure_title_two_row bold" href="http://v.qq.com/x/cover/mzc00200rali5o2/l3310d8tofg.html" target="_blank" title="10W日元挑战奇葩扭蛋机">
        10W日元挑战奇葩扭蛋机
       </a>
       <div class="figure_desc" title="本周带你开扭蛋：飞社长">
        本周带你开扭蛋：飞社长
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_life:img:标志物高肺癌会复发吗" class="figure" data-float="t3311tpixh9" data-quickopen="true" href="https://v.qq.com/x/page/t3311tpixh9.html" tabindex="-1" target="_blank">
       <img alt="标志物高肺癌会复发吗" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/media_img/lena/PICecauc3_720_1280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        05:11
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_life:title:标志物高肺癌会复发吗" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/page/t3311tpixh9.html" target="_blank" title="标志物高肺癌会复发吗">
        标志物高肺癌会复发吗
       </a>
       <div class="figure_desc" title="规避肺癌复发转移">
        规避肺癌复发转移
       </div>
      </div>
     </div>
    </div>
   </div>
  </div>
  <div _expose="new_vs3_banner2" _wind="columnname=精选_v首品牌专区&amp;controlname=new_vs3_banner2" class="mod_row_box mod_row_box_special" data-context="5" data-istyle="100">
   <div class="mod_ad_rect">
    <a __wind="" _stat="new_vs3_banner2:item" class="ad_rect_item" href="https://pro.m.jd.com/wq/active/3S53g25ji4mzEGVoeRiXxpmpAYjs/index.html?babelChannel=ttt4" target="_blank">
     <img alt="纯甄" class="pic" loading="lazy" lz_src="//puui.qpic.cn/tv/0/1236667189_580200/0" src="//puui.qpic.cn/vupload/0/common_blank.png/0"/>
     <div class="bottom-wrap">
      <span class="title">
       纯甄
      </span>
      <span class="desc">
       料实·材真 敢创敢真
      </span>
     </div>
     <div class="ad-icon">
      广告
     </div>
    </a>
    <a __wind="" _stat="new_vs3_banner2:item" class="ad_rect_item" href="https://pro.jd.com/mall/active/3g9t5gJXFk1wE7gt937s81iwo24v/index.html" target="_blank">
     <img alt="金典" class="pic" loading="lazy" lz_src="//puui.qpic.cn/tv/0/1236667209_580200/0" src="//puui.qpic.cn/vupload/0/common_blank.png/0"/>
     <div class="bottom-wrap">
      <span class="title">
       金典
      </span>
      <span class="desc">
       有机生活 有我定义
      </span>
     </div>
     <div class="ad-icon">
      广告
     </div>
    </a>
    <a __wind="" _stat="new_vs3_banner2:item" class="ad_rect_item" href="https://item.jd.com/6544256.html" target="_blank">
     <img alt="勇闯天涯superX" class="pic" loading="lazy" lz_src="//vc.qpic.cn/tpic/mtviunV68acqu/tviunV68fz8o.png/580" src="//puui.qpic.cn/vupload/0/common_blank.png/0"/>
     <div class="bottom-wrap">
      <span class="title">
       勇闯天涯superX
      </span>
      <span class="desc">
       生而无畏
      </span>
     </div>
     <div class="ad-icon">
      广告
     </div>
    </a>
    <a __wind="" _stat="new_vs3_banner2:item" class="ad_rect_item" href="https://mall.jd.com/index-1000078147.html" target="_blank">
     <img alt="香飘飘" class="pic" loading="lazy" lz_src="//vc.qpic.cn/tpic/mtviunV6hN7KA/tviunV6hYSao.png/580" src="//puui.qpic.cn/vupload/0/common_blank.png/0"/>
     <div class="bottom-wrap">
      <span class="title">
       香飘飘
      </span>
      <span class="desc">
       小饿小困 喝点香飘飘
      </span>
     </div>
     <div class="ad-icon">
      广告
     </div>
    </a>
    <a __wind="" _stat="new_vs3_banner2:item" class="ad_rect_item" href="https://www.fotile.com/" target="_blank">
     <img alt="方太" class="pic" loading="lazy" lz_src="//vc.qpic.cn/tpic/mtviunV6sfhFb/tviunV6sr35Y.png/580" src="//puui.qpic.cn/vupload/0/common_blank.png/0"/>
     <div class="bottom-wrap">
      <span class="title">
       方太
      </span>
      <span class="desc">
       因爱伟大
      </span>
     </div>
     <div class="ad-icon">
      广告
     </div>
    </a>
    <a __wind="" _stat="new_vs3_banner2:item" class="ad_rect_item" href="https://www.vmall.com/honor" target="_blank">
     <img alt="荣耀10" class="pic" loading="lazy" lz_src="//vc.qpic.cn/tpic/mtviunV6Cak7Y/tviunV6Cm5wL.png/580" src="//puui.qpic.cn/vupload/0/common_blank.png/0"/>
     <div class="bottom-wrap">
      <span class="title">
       荣耀10
      </span>
      <span class="desc">
       潮拍美一刻
      </span>
     </div>
     <div class="ad-icon">
      广告
     </div>
    </a>
   </div>
  </div>
  <div _expose="new_vs3_games" _wind="columnname=精选_精品游戏&amp;controlname=new_vs3_games" class="mod_row_box" cur-page-num="0" data-context="6" data-istyle="4" has-next-page="false" id="new_vs3_games">
   <div class="mod_hd">
    <h2 class="mod_title">
     <a _stat="new_vs3_games:通栏功能区:通栏标题" class="title_link" data-target="_blank" href="https://v.qq.com/channel/games">
      精品游戏
     </a>
    </h2>
    <div class="mod_page_small">
     <button _stat="new_vs3_games:通栏功能区:上一页" class="btn_prev disabled" title="上一页" wind-click="100">
      <svg class="svg_icon svg_icon_prev" height="10" viewbox="0 0 6 10" width="6">
       <path d="M1.4 4.7L5 1M1.3 5.3L5 9" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="1.4">
       </path>
      </svg>
     </button>
     <span class="page_num" data-count="2" data-info="8 9" data-page="1">
      1/2
     </span>
     <button _stat="new_vs3_games:通栏功能区:下一页" class="btn_next" title="下一页" wind-click="100">
      <svg class="svg_icon svg_icon_next" height="10" viewbox="0 0 6 10" width="6">
       <path d="M4.6 4.7L1 1M4.7 5.3L1 9" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="1.4">
       </path>
      </svg>
     </button>
    </div>
   </div>
   <div class="mod_bd cf _quickopen _quickopen_duration">
    <div class="mod_figure mod_figure_h_default mod_figure_h_default_1row mod_figure_h_default mod_figure_scroll" data-rowcount="8" data-rowlen="1">
     <div __wind="" class="list_item">
      <a _stat="new_vs3_games:img:揭秘游戏行业背后" class="figure" data-float="s3309ljqcxv" href="https://v.qq.com/x/cover/mzc002007g1gt28/s3309ljqcxv.html" tabindex="-1" target="_blank">
       <img alt="揭秘游戏行业背后" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/media_img/lena/PIC43ij2z_720_1280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        30:24
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_games:title:揭秘游戏行业背后" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc002007g1gt28/s3309ljqcxv.html" target="_blank" title="揭秘游戏行业背后">
        揭秘游戏行业背后
       </a>
       <div class="figure_desc" title="26位游戏人的心里话">
        26位游戏人的心里话
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_games:img:双城之战·顶流祖安姐妹" class="figure" data-float="p0041rf2i3n" data-quickopen="true" href="https://v.qq.com/x/cover/mzc00200vbrp9p7/p0041rf2i3n.html" tabindex="-1" target="_blank">
       <img alt="双城之战·顶流祖安姐妹" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/media_img/lena/PICiol467_720_1280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        10:55
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_games:title:双城之战·顶流祖安姐妹" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200vbrp9p7/p0041rf2i3n.html" target="_blank" title="双城之战·顶流祖安姐妹">
        双城之战·顶流祖安姐妹
       </a>
       <div class="figure_desc" title="首季收官口碑爆棚！">
        首季收官口碑爆棚！
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_games:img:LOL手游技能爆改" class="figure" data-float="c0041v75561" data-quickopen="true" href="https://v.qq.com/x/cover/mzc00200vnfpldv/c0041v75561.html" tabindex="-1" target="_blank">
       <img alt="LOL手游技能爆改" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/media_img/lena/PIC780z94_720_1280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        09:38
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_games:title:LOL手游技能爆改" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200vnfpldv/c0041v75561.html" target="_blank" title="LOL手游技能爆改">
        LOL手游技能爆改
       </a>
       <div class="figure_desc" title="寒冰大招竟然能拐弯？">
        寒冰大招竟然能拐弯？
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_games:img:灵药LOL手游·鳄鱼" class="figure" data-float="k00417dyyrg" href="https://v.qq.com/x/cover/mzc00200ggsgkk8/k00417dyyrg.html" tabindex="-1" target="_blank">
       <img alt="灵药LOL手游·鳄鱼" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/media_img/lena/PICrq0bgb_720_1280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        19:17
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_games:title:灵药LOL手游·鳄鱼" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200ggsgkk8/k00417dyyrg.html" target="_blank" title="灵药LOL手游·鳄鱼">
        灵药LOL手游·鳄鱼
       </a>
       <div class="figure_desc" title="坦伤兼备上单霸主！">
        坦伤兼备上单霸主！
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_games:img:双城之战深度解析" class="figure" data-float="k0041ag5gqw" href="https://v.qq.com/x/cover/mzc00200pa7yn8e/k0041ag5gqw.html" tabindex="-1" target="_blank">
       <img alt="双城之战深度解析" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/media_img/lena/PIC05np2k_720_1280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        15:04
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_games:title:双城之战深度解析" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200pa7yn8e/k0041ag5gqw.html" target="_blank" title="双城之战深度解析">
        双城之战深度解析
       </a>
       <div class="figure_desc" title="最佳动画里的Balance">
        最佳动画里的Balance
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_games:img:对话中国电竞" class="figure" data-float="j00415pc7o5" href="https://v.qq.com/x/cover/mzc00200i1ep15c/j00415pc7o5.html" tabindex="-1" target="_blank">
       <img alt="对话中国电竞" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/media_img/lena/PICv7z25o_720_1280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        30:00
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_games:title:对话中国电竞" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200i1ep15c/j00415pc7o5.html" target="_blank" title="对话中国电竞">
        对话中国电竞
       </a>
       <div class="figure_desc" title="中国电竞在初级阶段？">
        中国电竞在初级阶段？
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_games:img:谭警官自曝LOL趣事" class="figure" data-float="p0041ri6i0l" href="https://v.qq.com/x/cover/mzc00200ryhagh9/p0041ri6i0l.html" tabindex="-1" target="_blank">
       <img alt="谭警官自曝LOL趣事" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/media_img/lena/PIC2dvs8g_720_1280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        15:36
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_games:title:谭警官自曝LOL趣事" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200ryhagh9/p0041ri6i0l.html" target="_blank" title="谭警官自曝LOL趣事">
        谭警官自曝LOL趣事
       </a>
       <div class="figure_desc" title="靠LOL“匹配”到老婆">
        靠LOL“匹配”到老婆
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_games:img:拳皇15公测爷青回" class="figure" data-float="d0041pwqvpo" href="https://v.qq.com/x/cover/mzc00200d2h0qc9/d0041pwqvpo.html" tabindex="-1" target="_blank">
       <img alt="拳皇15公测爷青回" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/media_img/lena/PICn20wf1_720_1280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        15:02
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_games:title:拳皇15公测爷青回" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200d2h0qc9/d0041pwqvpo.html" target="_blank" title="拳皇15公测爷青回">
        拳皇15公测爷青回
       </a>
       <div class="figure_desc" title="全系列人物关系大盘点">
        全系列人物关系大盘点
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_games:img:非遗鼓乐·孤勇者" class="figure" data-float="i0041jwcvfw" data-quickopen="true" href="https://v.qq.com/x/cover/mzc002006hgz54o/i0041jwcvfw.html" tabindex="-1" target="_blank">
       <img alt="非遗鼓乐·孤勇者" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/media_img/lena/PIC1rbmrp_720_1280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        03:26
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_games:title:非遗鼓乐·孤勇者" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc002006hgz54o/i0041jwcvfw.html" target="_blank" title="非遗鼓乐·孤勇者">
        非遗鼓乐·孤勇者
       </a>
       <div class="figure_desc" title="乐声悠扬彰显绝美国风">
        乐声悠扬彰显绝美国风
       </div>
      </div>
     </div>
    </div>
   </div>
  </div>
  <div _expose="new_vs3_banner1" _wind="columnname=精选_剧场入口广告&amp;controlname=new_vs3_banner1" class="mod_row_box mod_row_box_special" data-context="6" id="new_vs3_banner1">
   <div class="mod_ad_spread">
    <div __wind="" class="spread_item spread_item_0">
     <a _stat="new_vs3_banner1:item" class="pic_block" href="https://v.qq.com/x/cover/mzc002006gqcd5z.html" target="_blank">
      <img alt="奇遇·人间角落" class="pic1" loading="lazy" lz_src="//vc.qpic.cn/tpic/mtviust3rPuB3/tviust3s1f1Q.png/580" src="//puui.qpic.cn/vupload/0/common_blank.png/0"/>
      <img alt="奇遇·人间角落" class="pic2" loading="lazy" lz_src="//puui.qpic.cn/tv/0/1236957332/0" src="//puui.qpic.cn/vupload/0/common_blank.png/0"/>
     </a>
    </div>
    <div __wind="" class="spread_item spread_item_1">
     <a _stat="new_vs3_banner1:item" class="pic_block" href="http://v.qq.com/x/cover/mzc002003cloofr.html" target="_blank">
      <img alt="京东双11沸腾之夜" class="pic1" loading="lazy" lz_src="//vc.qpic.cn/tpic/mtviup8GtWLRE/tviup99EUsLQ.png/580" src="//puui.qpic.cn/vupload/0/common_blank.png/0"/>
      <img alt="京东双11沸腾之夜" class="pic2" loading="lazy" lz_src="//puui.qpic.cn/tv/0/1236731287/0" src="//puui.qpic.cn/vupload/0/common_blank.png/0"/>
     </a>
    </div>
    <div __wind="" class="spread_item spread_item_2">
     <a _stat="new_vs3_banner1:item" class="pic_block" href="http://v.qq.com/detail/8/89859.html" target="_blank">
      <img alt="明日创作计划" class="pic1" loading="lazy" lz_src="//puui.qpic.cn/tv/0/1234482475_580200/0" src="//puui.qpic.cn/vupload/0/common_blank.png/0"/>
      <img alt="明日创作计划" class="pic2" loading="lazy" lz_src="//puui.qpic.cn/tv/0/1234482476/0" src="//puui.qpic.cn/vupload/0/common_blank.png/0"/>
     </a>
    </div>
    <div __wind="" class="spread_item spread_item_3">
     <a _stat="new_vs3_banner1:item" class="pic_block" href="http://v.qq.com/x/cover/mzc00200x6l0iix.html" target="_blank">
      <img alt="脱口秀大会4" class="pic1" loading="lazy" lz_src="//puui.qpic.cn/tv/0/1234379926_580200/0" src="//puui.qpic.cn/vupload/0/common_blank.png/0"/>
      <img alt="脱口秀大会4" class="pic2" loading="lazy" lz_src="//puui.qpic.cn/tv/0/1234388576/0" src="//puui.qpic.cn/vupload/0/common_blank.png/0"/>
     </a>
    </div>
    <div __wind="" class="spread_item spread_item_4">
     <a _stat="new_vs3_banner1:item" class="pic_block" href="http://v.qq.com/detail/9/90019.html" target="_blank">
      <img alt="姐妹们的奇幻沙龙" class="pic1" loading="lazy" lz_src="//puui.qpic.cn/tv/0/1235292218_580200/0" src="//puui.qpic.cn/vupload/0/common_blank.png/0"/>
      <img alt="姐妹们的奇幻沙龙" class="pic2" loading="lazy" lz_src="//puui.qpic.cn/tv/0/1235292221/0" src="//puui.qpic.cn/vupload/0/common_blank.png/0"/>
     </a>
    </div>
    <div __wind="" class="spread_item spread_item_5">
     <a _stat="new_vs3_banner1:item" class="pic_block" href="https://v.qq.com/detail/8/89608.html" target="_blank">
      <img alt="极限挑战" class="pic1" loading="lazy" lz_src="//puui.qpic.cn/tv/0/1230462823_580200/0" src="//puui.qpic.cn/vupload/0/common_blank.png/0"/>
      <img alt="极限挑战" class="pic2" loading="lazy" lz_src="//puui.qpic.cn/tv/0/1230463384/0" src="//puui.qpic.cn/vupload/0/common_blank.png/0"/>
     </a>
    </div>
   </div>
  </div>
  <div _expose="new_vs_hot_movie1" _wind="columnname=精选_电影预告&amp;controlname=new_vs_hot_movie1" class="mod_row_box" cur-page-num="0" data-context="6" data-istyle="4" has-next-page="false" id="new_vs_hot_movie1">
   <div class="mod_hd">
    <h2 class="mod_title">
     <a _stat="new_vs_hot_movie1:通栏功能区:通栏标题" class="title_link" data-target="_blank" href="https://v.qq.com/channel/movie_trailer">
      电影预告
     </a>
    </h2>
    <div class="mod_page_small">
     <button _stat="new_vs_hot_movie1:通栏功能区:上一页" class="btn_prev disabled" title="上一页" wind-click="100">
      <svg class="svg_icon svg_icon_prev" height="10" viewbox="0 0 6 10" width="6">
       <path d="M1.4 4.7L5 1M1.3 5.3L5 9" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="1.4">
       </path>
      </svg>
     </button>
     <span class="page_num" data-count="8" data-info="8 61" data-page="1">
      1/8
     </span>
     <button _stat="new_vs_hot_movie1:通栏功能区:下一页" class="btn_next" title="下一页" wind-click="100">
      <svg class="svg_icon svg_icon_next" height="10" viewbox="0 0 6 10" width="6">
       <path d="M4.6 4.7L1 1M4.7 5.3L1 9" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="1.4">
       </path>
      </svg>
     </button>
    </div>
   </div>
   <div class="mod_bd cf _quickopen _quickopen_duration">
    <div class="mod_figure mod_figure_h_default mod_figure_h_default_1row mod_figure_h_default mod_figure_scroll" data-rowcount="8" data-rowlen="1">
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_movie1:img:二龙湖惊魂夜|定档12月10日" class="figure" data-float="a3311fsdssx" href="https://v.qq.com/x/cover/mzc00200ngpog3f/a3311fsdssx.html" tabindex="-1" target="_blank">
       <img alt="二龙湖惊魂夜|定档12月10日" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/tv/0/1237772499_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
       <div class="figure_score">
        7.5
       </div>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_movie1:title:二龙湖惊魂夜|定档12月10日" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200ngpog3f/a3311fsdssx.html" target="_blank" title="二龙湖惊魂夜|定档12月10日">
        二龙湖惊魂夜|定档12月10日
       </a>
       <div class="figure_desc" title="浩哥夜半惊魂爆笑斗“鬼”">
        浩哥夜半惊魂爆笑斗“鬼”
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_movie1:img:九叔之古棺奇案•1207" class="figure" data-float="n33117a6s7j" href="https://v.qq.com/x/cover/mzc00200aj0ldsy/n33117a6s7j.html" tabindex="-1" target="_blank">
       <img alt="九叔之古棺奇案•1207" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/tv/0/1237808127_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_movie1:title:九叔之古棺奇案•1207" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200aj0ldsy/n33117a6s7j.html" target="_blank" title="九叔之古棺奇案•1207">
        九叔之古棺奇案•1207
       </a>
       <div class="figure_desc" title="九叔回归激战蛇棺僵尸王">
        九叔回归激战蛇棺僵尸王
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_movie1:img:末日救援·正在热播" class="figure" data-float="k3311bsfbuf" href="https://v.qq.com/x/cover/mzc00200mcm0lzz/k3311bsfbuf.html" tabindex="-1" target="_blank">
       <img alt="末日救援·正在热播" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/tv/0/1237820079_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        01:31:09
       </div>
       <div class="figure_score">
        7.9
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_movie1:title:末日救援·正在热播" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200mcm0lzz/k3311bsfbuf.html" target="_blank" title="末日救援·正在热播">
        末日救援·正在热播
       </a>
       <div class="figure_desc" title="中国战士对抗外星虫群！">
        中国战士对抗外星虫群！
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_movie1:img:古董局中局·推广曲" class="figure" data-float="b33110ntng1" href="https://v.qq.com/x/cover/mzc00200vazcfrs/b33110ntng1.html" tabindex="-1" target="_blank">
       <img alt="古董局中局·推广曲" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/tv/0/1237818670_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
       <div class="figure_score">
        7.5
       </div>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_movie1:title:古董局中局·推广曲" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200vazcfrs/b33110ntng1.html" target="_blank" title="古董局中局·推广曲">
        古董局中局·推广曲
       </a>
       <div class="figure_desc" title="黄贯中重唱Beyond名曲">
        黄贯中重唱Beyond名曲
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_movie1:img:文牧野指导奇迹·预告" class="figure" data-float="u3311itfheh" href="https://v.qq.com/x/cover/mzc002001uvqi5d/u3311itfheh.html" tabindex="-1" target="_blank">
       <img alt="文牧野指导奇迹·预告" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/tv/0/1237809688_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
       <div class="figure_score">
        7.0
       </div>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_movie1:title:文牧野指导奇迹·预告" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc002001uvqi5d/u3311itfheh.html" target="_blank" title="文牧野指导奇迹·预告">
        文牧野指导奇迹·预告
       </a>
       <div class="figure_desc" title="易烊千玺热血组队拆手机">
        易烊千玺热血组队拆手机
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_movie1:img:我们是第一书记" class="figure" data-float="j33116lsuek" href="https://v.qq.com/x/cover/mzc002002lkr9mg/j33116lsuek.html" tabindex="-1" target="_blank">
       <img alt="我们是第一书记" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/tv/0/1237818721_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
       <div class="figure_score">
        7.2
       </div>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_movie1:title:我们是第一书记" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc002002lkr9mg/j33116lsuek.html" target="_blank" title="我们是第一书记">
        我们是第一书记
       </a>
       <div class="figure_desc" title="用歌声致敬第一书记">
        用歌声致敬第一书记
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_movie1:img:暗恋·橘生淮南定档" class="figure" data-float="z3311dcl41l" href="https://v.qq.com/x/cover/mzc00200adi5d10/z3311dcl41l.html" tabindex="-1" target="_blank">
       <img alt="暗恋·橘生淮南定档" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/tv/0/1237817028_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
       <div class="figure_score">
        7.3
       </div>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_movie1:title:暗恋·橘生淮南定档" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200adi5d10/z3311dcl41l.html" target="_blank" title="暗恋·橘生淮南定档">
        暗恋·橘生淮南定档
       </a>
       <div class="figure_desc" title="明年5·20大胆说出我爱你">
        明年5·20大胆说出我爱你
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_movie1:img:反贪风暴5·最新特辑" class="figure" data-float="l3311fjb7en" href="https://v.qq.com/x/cover/mzc00200md6p11k/l3311fjb7en.html" tabindex="-1" target="_blank">
       <img alt="反贪风暴5·最新特辑" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/tv/0/1237811659_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
       <div class="figure_score">
        7.4
       </div>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_movie1:title:反贪风暴5·最新特辑" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200md6p11k/l3311fjb7en.html" target="_blank" title="反贪风暴5·最新特辑">
        反贪风暴5·最新特辑
       </a>
       <div class="figure_desc" title="古天乐首支片场vlog">
        古天乐首支片场vlog
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_movie1:img:以年为单位的恋爱·实验" class="figure" data-float="s3311jz3cvs" href="https://v.qq.com/x/cover/mzc002005lp75rn/s3311jz3cvs.html" tabindex="-1" target="_blank">
       <img alt="以年为单位的恋爱·实验" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1237810854_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
       <div class="figure_score">
        7.4
       </div>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_movie1:title:以年为单位的恋爱·实验" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc002005lp75rn/s3311jz3cvs.html" target="_blank" title="以年为单位的恋爱·实验">
        以年为单位的恋爱·实验
       </a>
       <div class="figure_desc" title="30对情侣现场互换手机">
        30对情侣现场互换手机
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_movie1:img:摇滚藏獒：蓝色光芒" class="figure" data-float="a3311v878fi" href="https://v.qq.com/x/cover/mzc002002ry7kot/a3311v878fi.html" tabindex="-1" target="_blank">
       <img alt="摇滚藏獒：蓝色光芒" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1237809484_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
       <div class="figure_score">
        7.1
       </div>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_movie1:title:摇滚藏獒：蓝色光芒" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc002002ry7kot/a3311v878fi.html" target="_blank" title="摇滚藏獒：蓝色光芒">
        摇滚藏獒：蓝色光芒
       </a>
       <div class="figure_desc" title="主题曲MV暖心上线">
        主题曲MV暖心上线
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_movie1:img:李茂换太子·新预告" class="figure" data-float="a3311lgknlr" href="https://v.qq.com/x/cover/mzc00200p3jnizm/a3311lgknlr.html" tabindex="-1" target="_blank">
       <img alt="李茂换太子·新预告" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1237772899_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
       <div class="figure_score">
        7.5
       </div>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_movie1:title:李茂换太子·新预告" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200p3jnizm/a3311lgknlr.html" target="_blank" title="李茂换太子·新预告">
        李茂换太子·新预告
       </a>
       <div class="figure_desc" title="马丽常远大笑跨年">
        马丽常远大笑跨年
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_movie1:img:哦！文姬·12.3" class="figure" data-float="s33114odimd" href="https://v.qq.com/x/cover/mzc0020078xsxys/s33114odimd.html" tabindex="-1" target="_blank">
       <img alt="哦！文姬·12.3" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1237775120_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_movie1:title:哦！文姬·12.3" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc0020078xsxys/s33114odimd.html" target="_blank" title="哦！文姬·12.3">
        哦！文姬·12.3
       </a>
       <div class="figure_desc" title="韩国“国民奶奶”内地银幕首秀">
        韩国“国民奶奶”内地银幕首秀
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_movie1:img:人生大事·定档2022清明" class="figure" data-float="l3311yk36sz" href="https://v.qq.com/x/cover/mzc00200zlh907s/l3311yk36sz.html" tabindex="-1" target="_blank">
       <img alt="人生大事·定档2022清明" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1237779124_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
       <div class="figure_score">
        7.1
       </div>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_movie1:title:人生大事·定档2022清明" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200zlh907s/l3311yk36sz.html" target="_blank" title="人生大事·定档2022清明">
        人生大事·定档2022清明
       </a>
       <div class="figure_desc" title="殡葬师与孤儿的治愈温情">
        殡葬师与孤儿的治愈温情
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_movie1:img:黑马续作·密室逃生2" class="figure" data-float="s3311iqz0m6" href="https://v.qq.com/x/cover/mzc0020051fdx8v/s3311iqz0m6.html" tabindex="-1" target="_blank">
       <img alt="黑马续作·密室逃生2" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1237772601_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
       <div class="figure_score">
        7.3
       </div>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_movie1:title:黑马续作·密室逃生2" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc0020051fdx8v/s3311iqz0m6.html" target="_blank" title="黑马续作·密室逃生2">
        黑马续作·密室逃生2
       </a>
       <div class="figure_desc" title="玩家再陷死亡陷阱">
        玩家再陷死亡陷阱
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_movie1:img:无尽攀登·vlog" class="figure" data-float="u3311xsty9i" href="https://v.qq.com/x/cover/mzc00200m1c3dg4/u3311xsty9i.html" tabindex="-1" target="_blank">
       <img alt="无尽攀登·vlog" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1237773821_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_movie1:title:无尽攀登·vlog" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200m1c3dg4/u3311xsty9i.html" target="_blank" title="无尽攀登·vlog">
        无尽攀登·vlog
       </a>
       <div class="figure_desc" title="夏伯渝探班流浪地球2剧组">
        夏伯渝探班流浪地球2剧组
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_movie1:img:爱情神话·女性特辑" class="figure" data-float="v3311acugcp" href="https://v.qq.com/x/cover/mzc00200ynev53m/v3311acugcp.html" tabindex="-1" target="_blank">
       <img alt="爱情神话·女性特辑" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1237772823_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
       <div class="figure_score">
        7.4
       </div>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_movie1:title:爱情神话·女性特辑" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200ynev53m/v3311acugcp.html" target="_blank" title="爱情神话·女性特辑">
        爱情神话·女性特辑
       </a>
       <div class="figure_desc" title="马伊琍吴越倪虹洁结同盟">
        马伊琍吴越倪虹洁结同盟
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_movie1:img:笨鸟大冒险·共同飞翔" class="figure" data-float="p331152vyii" href="https://v.qq.com/x/cover/mzc00200pujeihd/p331152vyii.html" tabindex="-1" target="_blank">
       <img alt="笨鸟大冒险·共同飞翔" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1237772538_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
       <div class="figure_score">
        7.2
       </div>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_movie1:title:笨鸟大冒险·共同飞翔" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200pujeihd/p331152vyii.html" target="_blank" title="笨鸟大冒险·共同飞翔">
        笨鸟大冒险·共同飞翔
       </a>
       <div class="figure_desc" title="12.4勇敢迈出第一步">
        12.4勇敢迈出第一步
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_movie1:img:曾经相爱的我们·预告" class="figure" data-float="n33115sq7ei" href="https://v.qq.com/x/cover/mzc00200ormlsvr/n33115sq7ei.html" tabindex="-1" target="_blank">
       <img alt="曾经相爱的我们·预告" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1237772728_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_movie1:title:曾经相爱的我们·预告" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200ormlsvr/n33115sq7ei.html" target="_blank" title="曾经相爱的我们·预告">
        曾经相爱的我们·预告
       </a>
       <div class="figure_desc" title="陈柏霖郭采洁陷难题">
        陈柏霖郭采洁陷难题
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_movie1:img:寻龙之幽冥地府" class="figure" data-float="k3311xlh1ji" href="https://v.qq.com/x/cover/mzc00200vqn8ki5/k3311xlh1ji.html" tabindex="-1" target="_blank">
       <img alt="寻龙之幽冥地府" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1237731277_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
       <div class="figure_score">
        6.6
       </div>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_movie1:title:寻龙之幽冥地府" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200vqn8ki5/k3311xlh1ji.html" target="_blank" title="寻龙之幽冥地府">
        寻龙之幽冥地府
       </a>
       <div class="figure_desc" title="12月5日闯葬龙墓穴">
        12月5日闯葬龙墓穴
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_movie1:img:古董局中局·预告" class="figure" data-float="w3311828u1z" href="https://v.qq.com/x/cover/mzc00200vazcfrs/w3311828u1z.html" tabindex="-1" target="_blank">
       <img alt="古董局中局·预告" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1237731316_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
       <div class="figure_score">
        7.5
       </div>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_movie1:title:古董局中局·预告" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200vazcfrs/w3311828u1z.html" target="_blank" title="古董局中局·预告">
        古董局中局·预告
       </a>
       <div class="figure_desc" title="雷佳音李现狭路相逢燃斗江湖">
        雷佳音李现狭路相逢燃斗江湖
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_movie1:img:梅艳芳·《歌之女》MV" class="figure" data-float="p3311jkjqqw" href="https://v.qq.com/x/cover/mzc00200kbornzq/p3311jkjqqw.html" tabindex="-1" target="_blank">
       <img alt="梅艳芳·《歌之女》MV" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1237731443_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
       <div class="figure_score">
        7.6
       </div>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_movie1:title:梅艳芳·《歌之女》MV" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200kbornzq/p3311jkjqqw.html" target="_blank" title="梅艳芳·《歌之女》MV">
        梅艳芳·《歌之女》MV
       </a>
       <div class="figure_desc" title="催泪女性传奇句句戳心">
        催泪女性传奇句句戳心
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_movie1:img:穿过寒冬拥抱你·新预告" class="figure" data-float="h3311bv9mch" href="https://v.qq.com/x/cover/mzc00200gjcj7je/h3311bv9mch.html" tabindex="-1" target="_blank">
       <img alt="穿过寒冬拥抱你·新预告" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1237731402_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
       <div class="figure_score">
        7.4
       </div>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_movie1:title:穿过寒冬拥抱你·新预告" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200gjcj7je/h3311bv9mch.html" target="_blank" title="穿过寒冬拥抱你·新预告">
        穿过寒冬拥抱你·新预告
       </a>
       <div class="figure_desc" title="黄渤给儿子的语音拥抱跨年">
        黄渤给儿子的语音拥抱跨年
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_movie1:img:雄狮少年·崛起版预告" class="figure" data-float="x3311ud103b" href="https://v.qq.com/x/cover/mzc00200mu0cw18/x3311ud103b.html" tabindex="-1" target="_blank">
       <img alt="雄狮少年·崛起版预告" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1237731385_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
       <div class="figure_score">
        7.3
       </div>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_movie1:title:雄狮少年·崛起版预告" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200mu0cw18/x3311ud103b.html" target="_blank" title="雄狮少年·崛起版预告">
        雄狮少年·崛起版预告
       </a>
       <div class="figure_desc" title="高能舞狮燃爆岁末">
        高能舞狮燃爆岁末
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_movie1:img:你的世界如果没有我·预告" class="figure" data-float="k3311m5a4rh" href="https://v.qq.com/x/cover/mzc002005n3v2zu/k3311m5a4rh.html" tabindex="-1" target="_blank">
       <img alt="你的世界如果没有我·预告" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1237731464_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
       <div class="figure_score">
        7.3
       </div>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_movie1:title:你的世界如果没有我·预告" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc002005n3v2zu/k3311m5a4rh.html" target="_blank" title="你的世界如果没有我·预告">
        你的世界如果没有我·预告
       </a>
       <div class="figure_desc" title="爱而不得展现青春常态">
        爱而不得展现青春常态
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_movie1:img:末日救援·1202" class="figure" data-float="t3310f6aafo" href="https://v.qq.com/x/cover/mzc00200mcm0lzz/t3310f6aafo.html" tabindex="-1" target="_blank">
       <img alt="末日救援·1202" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1237580826_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        01:31:09
       </div>
       <div class="figure_score">
        7.9
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_movie1:title:末日救援·1202" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200mcm0lzz/t3310f6aafo.html" target="_blank" title="末日救援·1202">
        末日救援·1202
       </a>
       <div class="figure_desc" title="中国战士血战异星虫潮">
        中国战士血战异星虫潮
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_movie1:img:铁道英雄·正片片段" class="figure" data-float="t331143cxvp" href="https://v.qq.com/x/cover/mzc00200z19pfwv/t331143cxvp.html" tabindex="-1" target="_blank">
       <img alt="铁道英雄·正片片段" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1237691738_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
       <div class="figure_score">
        7.6
       </div>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_movie1:title:铁道英雄·正片片段" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200z19pfwv/t331143cxvp.html" target="_blank" title="铁道英雄·正片片段">
        铁道英雄·正片片段
       </a>
       <div class="figure_desc" title="庄严宣誓镜头传递信仰的力量">
        庄严宣誓镜头传递信仰的力量
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_movie1:img:无尽攀登·口碑特辑" class="figure" data-float="b3311vmmriw" href="https://v.qq.com/x/cover/mzc00200m1c3dg4/b3311vmmriw.html" tabindex="-1" target="_blank">
       <img alt="无尽攀登·口碑特辑" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1237691762_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_movie1:title:无尽攀登·口碑特辑" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200m1c3dg4/b3311vmmriw.html" target="_blank" title="无尽攀登·口碑特辑">
        无尽攀登·口碑特辑
       </a>
       <div class="figure_desc" title="夏伯渝激励癌症患者">
        夏伯渝激励癌症患者
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_movie1:img:只要你过的比我好·预告" class="figure" data-float="h3309qubqbw" href="https://v.qq.com/x/cover/mzc002001fv7inu/h3309qubqbw.html" tabindex="-1" target="_blank">
       <img alt="只要你过的比我好·预告" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1237691793_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
       <div class="figure_score">
        7.4
       </div>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_movie1:title:只要你过的比我好·预告" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc002001fv7inu/h3309qubqbw.html" target="_blank" title="只要你过的比我好·预告">
        只要你过的比我好·预告
       </a>
       <div class="figure_desc" title="双向守护父子情引爆泪腺">
        双向守护父子情引爆泪腺
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_movie1:img:神龟岛·剧情MV" class="figure" data-float="q3310cujg9x" href="https://v.qq.com/x/cover/mzc00200j13nsmc/q3310cujg9x.html" tabindex="-1" target="_blank">
       <img alt="神龟岛·剧情MV" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1237633507_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        01:08:41
       </div>
       <div class="figure_score">
        7.7
       </div>
       <img alt="独播" class="mark_v mark_v_独播" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_only_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_only_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_movie1:title:神龟岛·剧情MV" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200j13nsmc/q3310cujg9x.html" target="_blank" title="神龟岛·剧情MV">
        神龟岛·剧情MV
       </a>
       <div class="figure_desc" title="汪卓成赖雨濛仙侠CP大战巨龟">
        汪卓成赖雨濛仙侠CP大战巨龟
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_movie1:img:误杀2·爸爸的礼物" class="figure" data-float="m3310ojvse3" href="https://v.qq.com/x/cover/mzc00200b3hvcjq/m3310ojvse3.html" tabindex="-1" target="_blank">
       <img alt="误杀2·爸爸的礼物" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1237575939_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
       <div class="figure_score">
        7.5
       </div>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_movie1:title:误杀2·爸爸的礼物" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200b3hvcjq/m3310ojvse3.html" target="_blank" title="误杀2·爸爸的礼物">
        误杀2·爸爸的礼物
       </a>
       <div class="figure_desc" title="肖央演绎全新父爱故事">
        肖央演绎全新父爱故事
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_movie1:img:门锁·“独居女走夜路”片段" class="figure" data-float="e33104ptpmw" href="https://v.qq.com/x/cover/mzc00200dhz1q3s/e33104ptpmw.html" tabindex="-1" target="_blank">
       <img alt="门锁·“独居女走夜路”片段" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1237575998_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
       <div class="figure_score">
        7.6
       </div>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_movie1:title:门锁·“独居女走夜路”片段" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200dhz1q3s/e33104ptpmw.html" target="_blank" title="门锁·“独居女走夜路”片段">
        门锁·“独居女走夜路”片段
       </a>
       <div class="figure_desc" title="引发高校打卡热潮">
        引发高校打卡热潮
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_movie1:img:银行家·口碑特辑" class="figure" data-float="o33103dq8k7" href="https://v.qq.com/x/cover/mzc00200975hawm/o33103dq8k7.html" tabindex="-1" target="_blank">
       <img alt="银行家·口碑特辑" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1237544200_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
       <div class="figure_score">
        7.4
       </div>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_movie1:title:银行家·口碑特辑" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200975hawm/o33103dq8k7.html" target="_blank" title="银行家·口碑特辑">
        银行家·口碑特辑
       </a>
       <div class="figure_desc" title="漫威粉提前过年">
        漫威粉提前过年
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_movie1:img:平原上的火焰·创作特辑" class="figure" data-float="j3310tp42y5" href="https://v.qq.com/x/cover/mzc002000r2t2ht/j3310tp42y5.html" tabindex="-1" target="_blank">
       <img alt="平原上的火焰·创作特辑" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1237537451_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
       <div class="figure_score">
        7.5
       </div>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_movie1:title:平原上的火焰·创作特辑" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc002000r2t2ht/j3310tp42y5.html" target="_blank" title="平原上的火焰·创作特辑">
        平原上的火焰·创作特辑
       </a>
       <div class="figure_desc" title="周冬雨刘昊然拍摄现场直击">
        周冬雨刘昊然拍摄现场直击
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_movie1:img:十年一品温如言·新预告" class="figure" data-float="h3310td4if2" href="https://v.qq.com/x/cover/mzc0020008coaim/h3310td4if2.html" tabindex="-1" target="_blank">
       <img alt="十年一品温如言·新预告" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1237537463_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
       <div class="figure_score">
        7.4
       </div>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_movie1:title:十年一品温如言·新预告" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc0020008coaim/h3310td4if2.html" target="_blank" title="十年一品温如言·新预告">
        十年一品温如言·新预告
       </a>
       <div class="figure_desc" title="丁禹兮任敏十年虐恋意难平">
        丁禹兮任敏十年虐恋意难平
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_movie1:img:芒咕的动物城-酒店追逐" class="figure" data-float="h3310zf9ey5" href="https://v.qq.com/x/cover/mzc00200ewo6hkz/h3310zf9ey5.html" tabindex="-1" target="_blank">
       <img alt="芒咕的动物城-酒店追逐" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1237544246_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
       <div class="figure_score">
        7.3
       </div>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_movie1:title:芒咕的动物城-酒店追逐" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200ewo6hkz/h3310zf9ey5.html" target="_blank" title="芒咕的动物城-酒店追逐">
        芒咕的动物城-酒店追逐
       </a>
       <div class="figure_desc" title="驴王冒险惊险又搞笑">
        驴王冒险惊险又搞笑
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_movie1:img:只要你过得比我好·片段" class="figure" data-float="p3310l5u1kl" href="https://v.qq.com/x/cover/mzc002001fv7inu/p3310l5u1kl.html" tabindex="-1" target="_blank">
       <img alt="只要你过得比我好·片段" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1237537486_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
       <div class="figure_score">
        7.4
       </div>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_movie1:title:只要你过得比我好·片段" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc002001fv7inu/p3310l5u1kl.html" target="_blank" title="只要你过得比我好·片段">
        只要你过得比我好·片段
       </a>
       <div class="figure_desc" title="“买你一天的时间”令人哭崩">
        “买你一天的时间”令人哭崩
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_movie1:img:末日救援·定档1202" class="figure" data-float="m3310g8291p" href="https://v.qq.com/x/cover/mzc00200mcm0lzz/m3310g8291p.html" tabindex="-1" target="_blank">
       <img alt="末日救援·定档1202" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1237496889_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        01:31:09
       </div>
       <div class="figure_score">
        7.9
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_movie1:title:末日救援·定档1202" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200mcm0lzz/m3310g8291p.html" target="_blank" title="末日救援·定档1202">
        末日救援·定档1202
       </a>
       <div class="figure_desc" title="李大嘴吕秀才血战外星虫潮">
        李大嘴吕秀才血战外星虫潮
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_movie1:img:侏罗纪世界3·序章" class="figure" data-float="j33102p8e2v" href="https://v.qq.com/x/cover/mzc00200x1t7a8o/j33102p8e2v.html" tabindex="-1" target="_blank">
       <img alt="侏罗纪世界3·序章" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1237496821_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
       <div class="figure_score">
        7.4
       </div>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_movie1:title:侏罗纪世界3·序章" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200x1t7a8o/j33102p8e2v.html" target="_blank" title="侏罗纪世界3·序章">
        侏罗纪世界3·序章
       </a>
       <div class="figure_desc" title="7种新恐龙亮相">
        7种新恐龙亮相
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_movie1:img:误杀2·“博弈”版特辑" class="figure" data-float="c33100s2q0f" href="https://v.qq.com/x/cover/mzc00200b3hvcjq/c33100s2q0f.html" tabindex="-1" target="_blank">
       <img alt="误杀2·“博弈”版特辑" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1237506049_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
       <div class="figure_score">
        7.5
       </div>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_movie1:title:误杀2·“博弈”版特辑" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200b3hvcjq/c33100s2q0f.html" target="_blank" title="误杀2·“博弈”版特辑">
        误杀2·“博弈”版特辑
       </a>
       <div class="figure_desc" title="肖央和任达华隔窗飙演技">
        肖央和任达华隔窗飙演技
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_movie1:img:古董局中局·预售开启" class="figure" data-float="a3310rkyemx" href="https://v.qq.com/x/cover/mzc00200vazcfrs/a3310rkyemx.html" tabindex="-1" target="_blank">
       <img alt="古董局中局·预售开启" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1237496906_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
       <div class="figure_score">
        7.5
       </div>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_movie1:title:古董局中局·预售开启" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200vazcfrs/a3310rkyemx.html" target="_blank" title="古董局中局·预售开启">
        古董局中局·预售开启
       </a>
       <div class="figure_desc" title="雷佳音李现辛芷蕾认葛优当爸">
        雷佳音李现辛芷蕾认葛优当爸
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_movie1:img:暗杀风暴·悬案版预告" class="figure" data-float="c3310yueu4f" href="https://v.qq.com/x/cover/mzc00200vhbfw60/c3310yueu4f.html" tabindex="-1" target="_blank">
       <img alt="暗杀风暴·悬案版预告" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1237496930_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
       <div class="figure_score">
        7.4
       </div>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_movie1:title:暗杀风暴·悬案版预告" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200vhbfw60/c3310yueu4f.html" target="_blank" title="暗杀风暴·悬案版预告">
        暗杀风暴·悬案版预告
       </a>
       <div class="figure_desc" title="古天乐张智霖吴镇宇追查真相">
        古天乐张智霖吴镇宇追查真相
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_movie1:img:门锁·范丞丞“人狠话不多”" class="figure" data-float="c3310ktb3mo" href="https://v.qq.com/x/cover/mzc00200dhz1q3s/c3310ktb3mo.html" tabindex="-1" target="_blank">
       <img alt="门锁·范丞丞“人狠话不多”" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1237497003_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
       <div class="figure_score">
        7.6
       </div>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_movie1:title:门锁·范丞丞“人狠话不多”" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200dhz1q3s/c3310ktb3mo.html" target="_blank" title="门锁·范丞丞“人狠话不多”">
        门锁·范丞丞“人狠话不多”
       </a>
       <div class="figure_desc" title="高空坠落吊脖戏只为真实">
        高空坠落吊脖戏只为真实
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_movie1:img:铁道英雄·正片片段" class="figure" data-float="z3310aljnm1" href="https://v.qq.com/x/cover/mzc00200z19pfwv/z3310aljnm1.html" tabindex="-1" target="_blank">
       <img alt="铁道英雄·正片片段" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1237497041_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
       <div class="figure_score">
        7.6
       </div>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_movie1:title:铁道英雄·正片片段" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200z19pfwv/z3310aljnm1.html" target="_blank" title="铁道英雄·正片片段">
        铁道英雄·正片片段
       </a>
       <div class="figure_desc" title="范伟周政杰对话直戳泪点">
        范伟周政杰对话直戳泪点
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_movie1:img:你的世界如果没有我" class="figure" data-float="r3310r1fjty" href="https://v.qq.com/x/cover/mzc002005n3v2zu/r3310r1fjty.html" tabindex="-1" target="_blank">
       <img alt="你的世界如果没有我" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1237496972_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
       <div class="figure_score">
        7.3
       </div>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_movie1:title:你的世界如果没有我" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc002005n3v2zu/r3310r1fjty.html" target="_blank" title="你的世界如果没有我">
        你的世界如果没有我
       </a>
       <div class="figure_desc" title="萧敬腾献唱《如果没有你》">
        萧敬腾献唱《如果没有你》
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_movie1:img:神龟岛·11.26" class="figure" data-float="d3310kbd4q6" href="https://v.qq.com/x/cover/mzc00200j13nsmc/d3310kbd4q6.html" tabindex="-1" target="_blank">
       <img alt="神龟岛·11.26" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1237455483_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        01:08:41
       </div>
       <div class="figure_score">
        7.7
       </div>
       <img alt="独播" class="mark_v mark_v_独播" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_only_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_only_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_movie1:title:神龟岛·11.26" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200j13nsmc/d3310kbd4q6.html" target="_blank" title="神龟岛·11.26">
        神龟岛·11.26
       </a>
       <div class="figure_desc" title="汪卓成赖雨濛上演渡气甜吻">
        汪卓成赖雨濛上演渡气甜吻
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_movie1:img:二捕出山｜定档11.28" class="figure" data-float="i3309vv8iuu" href="https://v.qq.com/x/cover/mzc00200tz3zq5m/i3309vv8iuu.html" tabindex="-1" target="_blank">
       <img alt="二捕出山｜定档11.28" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1237455109_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        01:18:53
       </div>
       <div class="figure_score">
        7.7
       </div>
       <img alt="独播" class="mark_v mark_v_独播" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_only_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_only_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_movie1:title:二捕出山｜定档11.28" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200tz3zq5m/i3309vv8iuu.html" target="_blank" title="二捕出山｜定档11.28">
        二捕出山｜定档11.28
       </a>
       <div class="figure_desc" title="开心麻花金牌笑匠爆笑探案">
        开心麻花金牌笑匠爆笑探案
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_movie1:img:熊出没·重返地球" class="figure" data-float="o33101ukgn0" href="https://v.qq.com/x/cover/mzc00200w20inn5/o33101ukgn0.html" tabindex="-1" target="_blank">
       <img alt="熊出没·重返地球" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1237455503_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
       <div class="figure_score">
        7.5
       </div>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_movie1:title:熊出没·重返地球" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200w20inn5/o33101ukgn0.html" target="_blank" title="熊出没·重返地球">
        熊出没·重返地球
       </a>
       <div class="figure_desc" title="2022大年初一守卫家园">
        2022大年初一守卫家园
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_movie1:img:门锁·掀起打卡风潮" class="figure" data-float="a3310av6w6f" href="https://v.qq.com/x/cover/mzc00200dhz1q3s/a3310av6w6f.html" tabindex="-1" target="_blank">
       <img alt="门锁·掀起打卡风潮" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1237460066_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
       <div class="figure_score">
        7.6
       </div>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_movie1:title:门锁·掀起打卡风潮" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200dhz1q3s/a3310av6w6f.html" target="_blank" title="门锁·掀起打卡风潮">
        门锁·掀起打卡风潮
       </a>
       <div class="figure_desc" title="白客变身“王坏锤”">
        白客变身“王坏锤”
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_movie1:img:野马分鬃·终极预告" class="figure" data-float="d3310hemmae" href="https://v.qq.com/x/cover/mzc00200xyhcmeh/d3310hemmae.html" tabindex="-1" target="_blank">
       <img alt="野马分鬃·终极预告" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1237459862_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
       <div class="figure_score">
        7.5
       </div>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_movie1:title:野马分鬃·终极预告" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200xyhcmeh/d3310hemmae.html" target="_blank" title="野马分鬃·终极预告">
        野马分鬃·终极预告
       </a>
       <div class="figure_desc" title="首映礼掀“青春狂潮”">
        首映礼掀“青春狂潮”
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_movie1:img:寻龙之发丘天棺·24日独播" class="figure" data-float="p3310awbopm" href="https://v.qq.com/x/cover/mzc002006fqrk2l/p3310awbopm.html" tabindex="-1" target="_blank">
       <img alt="寻龙之发丘天棺·24日独播" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1237426896_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        01:19:44
       </div>
       <div class="figure_score">
        7.7
       </div>
       <img alt="独播" class="mark_v mark_v_独播" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_only_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_only_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_movie1:title:寻龙之发丘天棺·24日独播" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc002006fqrk2l/p3310awbopm.html" target="_blank" title="寻龙之发丘天棺·24日独播">
        寻龙之发丘天棺·24日独播
       </a>
       <div class="figure_desc" title="万年古墓惊现食人巨蛇">
        万年古墓惊现食人巨蛇
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_movie1:img:捞世界·推广曲《捞》" class="figure" data-float="d3310ukn3rs" href="https://v.qq.com/x/cover/mzc00200zg10grf/d3310ukn3rs.html" tabindex="-1" target="_blank">
       <img alt="捞世界·推广曲《捞》" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1237423970_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
       <div class="figure_score">
        7.3
       </div>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_movie1:title:捞世界·推广曲《捞》" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200zg10grf/d3310ukn3rs.html" target="_blank" title="捞世界·推广曲《捞》">
        捞世界·推广曲《捞》
       </a>
       <div class="figure_desc" title="黄才伦带兄弟爆笑挣大钱">
        黄才伦带兄弟爆笑挣大钱
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_movie1:img:狙击手·2022大年初一" class="figure" data-float="w0041c0yz18" href="https://v.qq.com/x/cover/mzc0020035l5vcf/w0041c0yz18.html" tabindex="-1" target="_blank">
       <img alt="狙击手·2022大年初一" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1237413621_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
       <div class="figure_score">
        7.4
       </div>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_movie1:title:狙击手·2022大年初一" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc0020035l5vcf/w0041c0yz18.html" target="_blank" title="狙击手·2022大年初一">
        狙击手·2022大年初一
       </a>
       <div class="figure_desc" title="万家灯火，献给最可爱的人">
        万家灯火，献给最可爱的人
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_movie1:img:铁道英雄·“有来无回”" class="figure" data-float="w3310hzvxpv" href="https://v.qq.com/x/cover/mzc00200z19pfwv/w3310hzvxpv.html" tabindex="-1" target="_blank">
       <img alt="铁道英雄·“有来无回”" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1237413635_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
       <div class="figure_score">
        7.6
       </div>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_movie1:title:铁道英雄·“有来无回”" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200z19pfwv/w3310hzvxpv.html" target="_blank" title="铁道英雄·“有来无回”">
        铁道英雄·“有来无回”
       </a>
       <div class="figure_desc" title="张涵予范伟誓驱日寇">
        张涵予范伟誓驱日寇
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_movie1:img:扬名立万·删减片段" class="figure" data-float="h3310zehwy0" href="https://v.qq.com/x/cover/mzc00200v3x7zg9/h3310zehwy0.html" tabindex="-1" target="_blank">
       <img alt="扬名立万·删减片段" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1237413656_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
       <div class="figure_score">
        7.6
       </div>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_movie1:title:扬名立万·删减片段" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200v3x7zg9/h3310zehwy0.html" target="_blank" title="扬名立万·删减片段">
        扬名立万·删减片段
       </a>
       <div class="figure_desc" title="尹正尽显“毒舌”本色">
        尹正尽显“毒舌”本色
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_movie1:img:只要你过得比我好·提档" class="figure" data-float="o3310232fcu" href="https://v.qq.com/x/cover/mzc002001fv7inu/o3310232fcu.html" tabindex="-1" target="_blank">
       <img alt="只要你过得比我好·提档" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1237414751_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
       <div class="figure_score">
        7.4
       </div>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_movie1:title:只要你过得比我好·提档" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc002001fv7inu/o3310232fcu.html" target="_blank" title="只要你过得比我好·提档">
        只要你过得比我好·提档
       </a>
       <div class="figure_desc" title="12.3父子情深令人共情">
        12.3父子情深令人共情
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_movie1:img:门锁·热映" class="figure" data-float="t3310myqxko" href="https://v.qq.com/x/cover/mzc00200dhz1q3s/t3310myqxko.html" tabindex="-1" target="_blank">
       <img alt="门锁·热映" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1237413684_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
       <div class="figure_score">
        7.6
       </div>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_movie1:title:门锁·热映" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200dhz1q3s/t3310myqxko.html" target="_blank" title="门锁·热映">
        门锁·热映
       </a>
       <div class="figure_desc" title="真实代入感看出后遗症">
        真实代入感看出后遗症
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_movie1:img:《门锁》专访白百何" class="figure" data-float="e3310s5c0nd" href="https://v.qq.com/x/cover/k6imy80rx6jjlno/e3310s5c0nd.html" tabindex="-1" target="_blank">
       <img alt="《门锁》专访白百何" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1237377099_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
       <div class="figure_score">
        7.6
       </div>
       <img alt="腾讯出品" class="mark_v mark_v_腾讯出品" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_self_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_self_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_movie1:title:《门锁》专访白百何" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/k6imy80rx6jjlno/e3310s5c0nd.html" target="_blank" title="《门锁》专访白百何">
        《门锁》专访白百何
       </a>
       <div class="figure_desc" title="拍ootd竟是为缓解压力">
        拍ootd竟是为缓解压力
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_movie1:img:神龟岛·11.26独播" class="figure" data-float="z33086h5638" href="https://v.qq.com/x/cover/mzc00200j13nsmc/z33086h5638.html" tabindex="-1" target="_blank">
       <img alt="神龟岛·11.26独播" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1237298276_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        01:08:41
       </div>
       <div class="figure_score">
        7.7
       </div>
       <img alt="独播" class="mark_v mark_v_独播" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_only_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_only_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_movie1:title:神龟岛·11.26独播" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200j13nsmc/z33086h5638.html" target="_blank" title="神龟岛·11.26独播">
        神龟岛·11.26独播
       </a>
       <div class="figure_desc" title="汪卓成赖雨濛闯仙岛战巨龟">
        汪卓成赖雨濛闯仙岛战巨龟
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_movie1:img:古董局中局·1203上映" class="figure" data-float="b3309habbe3" href="https://v.qq.com/x/cover/mzc00200vazcfrs/b3309habbe3.html" tabindex="-1" target="_blank">
       <img alt="古董局中局·1203上映" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1237338935_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
       <div class="figure_score">
        7.5
       </div>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_movie1:title:古董局中局·1203上映" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200vazcfrs/b3309habbe3.html" target="_blank" title="古董局中局·1203上映">
        古董局中局·1203上映
       </a>
       <div class="figure_desc" title="雷佳音李现智破惊世骗局">
        雷佳音李现智破惊世骗局
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_movie1:img:铁道英雄·正片片段" class="figure" data-float="g3309aww7vv" href="https://v.qq.com/x/cover/mzc00200z19pfwv/g3309aww7vv.html" tabindex="-1" target="_blank">
       <img alt="铁道英雄·正片片段" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1237348147_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
       <div class="figure_score">
        7.6
       </div>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_movie1:title:铁道英雄·正片片段" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200z19pfwv/g3309aww7vv.html" target="_blank" title="铁道英雄·正片片段">
        铁道英雄·正片片段
       </a>
       <div class="figure_desc" title="范伟笑怼日寇演技超稳">
        范伟笑怼日寇演技超稳
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_movie1:img:门锁·公映" class="figure" data-float="f3309gb8e8k" href="https://v.qq.com/x/cover/mzc00200dhz1q3s/f3309gb8e8k.html" tabindex="-1" target="_blank">
       <img alt="门锁·公映" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1237310268_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
       <div class="figure_score">
        7.6
       </div>
       <img alt="预告片" class="mark_v mark_v_预告片" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_trailer_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_movie1:title:门锁·公映" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200dhz1q3s/f3309gb8e8k.html" target="_blank" title="门锁·公映">
        门锁·公映
       </a>
       <div class="figure_desc" title="解锁独居女性生存现状">
        解锁独居女性生存现状
       </div>
      </div>
     </div>
    </div>
   </div>
  </div>
  <div _expose="ad_qll_width1" class="mod_row_box mod_row_box_special mod_row_box_ad" data-context="7" data-istyle="11" id="ad_qll_width1">
   <div _stat="ad_qll_width1:ad_l" class="mod_ad_main">
    <!--$loc$_div AD begin...."l=$loc$&log=off"-->
    <div class="l_qq_com" data-index="1" data-loc="QQlive_SP_QLL_Width" id="QQlive_SP_QLL_Width:1" style="width:960px;height:90px;">
    </div>
    <!--$loc$ AD end -->
    <!--[if !IE]>|xGv00|2016c4b2c1bf192b2958128130e433a3<![endif]-->
   </div>
   <div _stat="ad_qll_width1:ad_r" class="mod_ad_side">
    <a class="ad1" href="https://v.qq.com/x/cover/vbb35hm6m6da1wc.html" target="_blank">
     <img loading="lazy" lz_src="//puui.qpic.cn/tv/0/151620407_73090/0" src="//puui.qpic.cn/vupload/0/common_blank.png/0"/>
    </a>
    <a class="ad2" href="https://v.qq.com/x/cover/vbb35hm6m6da1wc.html" target="_blank">
     <img loading="lazy" lz_src="//puui.qpic.cn/tv/0/151620415/0" src="//puui.qpic.cn/vupload/0/common_blank.png/0"/>
    </a>
    <a class="ad3" href="https://v.qq.com/x/cover/vbb35hm6m6da1wc.html" target="_blank">
     <img loading="lazy" lz_src="//puui.qpic.cn/tv/0/151620410/0" src="//puui.qpic.cn/vupload/0/common_blank.png/0"/>
    </a>
   </div>
  </div>
  <div _expose="new_vs_hot_tv1" _wind="columnname=精选_花絮·剧透·预告片&amp;controlname=new_vs_hot_tv1" class="mod_row_box" cur-page-num="0" data-context="7" data-istyle="4" has-next-page="false" id="new_vs_hot_tv1">
   <div class="mod_hd">
    <h2 class="mod_title">
     花絮·剧透·预告片
    </h2>
    <div class="mod_page_small">
     <button _stat="new_vs_hot_tv1:通栏功能区:上一页" class="btn_prev disabled" title="上一页" wind-click="100">
      <svg class="svg_icon svg_icon_prev" height="10" viewbox="0 0 6 10" width="6">
       <path d="M1.4 4.7L5 1M1.3 5.3L5 9" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="1.4">
       </path>
      </svg>
     </button>
     <span class="page_num" data-count="2" data-info="8 9" data-page="1">
      1/2
     </span>
     <button _stat="new_vs_hot_tv1:通栏功能区:下一页" class="btn_next" title="下一页" wind-click="100">
      <svg class="svg_icon svg_icon_next" height="10" viewbox="0 0 6 10" width="6">
       <path d="M4.6 4.7L1 1M4.7 5.3L1 9" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="1.4">
       </path>
      </svg>
     </button>
    </div>
   </div>
   <div class="mod_bd cf _quickopen _quickopen_duration">
    <div class="mod_figure mod_figure_h_default mod_figure_h_default_1row mod_figure_h_default mod_figure_scroll" data-rowcount="8" data-rowlen="1">
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_tv1:img:入戏·宋祖儿" class="figure" data-float="k3311paosz2" data-quickopen="true" href="https://v.qq.com/x/cover/6q6xn0f30eicfg6/k3311paosz2.html?ptag=qqbrowser" tabindex="-1" target="_blank">
       <img alt="入戏·宋祖儿" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/media_img/lena/PICp9iy3e_304_540/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        06:44
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_tv1:title:入戏·宋祖儿" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/6q6xn0f30eicfg6/k3311paosz2.html?ptag=qqbrowser" target="_blank" title="入戏·宋祖儿">
        入戏·宋祖儿
       </a>
       <div class="figure_desc" title="王安宇和邵北笙一样自恋">
        王安宇和邵北笙一样自恋
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_tv1:img:雪中悍刀行·江湖预告" class="figure" data-float="u0041idg0en" data-quickopen="true" href="https://v.qq.com/x/cover/mzc0020020cyvqh/u0041idg0en.html" tabindex="-1" target="_blank">
       <img alt="雪中悍刀行·江湖预告" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_hz_pic/0/mzc0020020cyvqh1635910491548/332" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        02:03
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_tv1:title:雪中悍刀行·江湖预告" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc0020020cyvqh/u0041idg0en.html" target="_blank" title="雪中悍刀行·江湖预告">
        雪中悍刀行·江湖预告
       </a>
       <div class="figure_desc" title="江湖请指教！张若昀来啦">
        江湖请指教！张若昀来啦
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_tv1:img:三体·首发预告" class="figure" data-float="k00412hpxcq" data-quickopen="true" href="https://v.qq.com/x/cover/mzc002007knmh3g/k00412hpxcq.html" tabindex="-1" target="_blank">
       <img alt="三体·首发预告" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_hz_pic/0/mzc002007knmh3g1635921845033/332" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        03:13
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_tv1:title:三体·首发预告" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc002007knmh3g/k00412hpxcq.html" target="_blank" title="三体·首发预告">
        三体·首发预告
       </a>
       <div class="figure_desc" title="宇宙两大文明生死博弈打响">
        宇宙两大文明生死博弈打响
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_tv1:img:我们的婚姻·片花" class="figure" data-float="l00413excce" data-quickopen="true" href="https://v.qq.com/x/cover/mzc00200c0cgfxj/l00413excce.html" tabindex="-1" target="_blank">
       <img alt="我们的婚姻·片花" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/media_img/lena/PIC0wub09_720_1280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        01:40
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_tv1:title:我们的婚姻·片花" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200c0cgfxj/l00413excce.html" target="_blank" title="我们的婚姻·片花">
        我们的婚姻·片花
       </a>
       <div class="figure_desc" title="白百何佟大为演绎婚姻真相">
        白百何佟大为演绎婚姻真相
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_tv1:img:嘉南传·独家MV" class="figure" data-float="l00407ysa7h" data-quickopen="true" href="https://v.qq.com/x/page/l00407ysa7h.html" tabindex="-1" target="_blank">
       <img alt="嘉南传·独家MV" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/media_img/lena/PICcdlzbw_720_1280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        02:43
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_tv1:title:嘉南传·独家MV" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/page/l00407ysa7h.html" target="_blank" title="嘉南传·独家MV">
        嘉南传·独家MV
       </a>
       <div class="figure_desc" title="好听！鞠婧祎曾舜晞合唱">
        好听！鞠婧祎曾舜晞合唱
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_tv1:img:谢谢你医生·先导预告" class="figure" data-float="k0040wk18kf" data-quickopen="true" href="https://v.qq.com/x/page/k0040wk18kf.html" tabindex="-1" target="_blank">
       <img alt="谢谢你医生·先导预告" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/media_img/lena/PIC6ha0h5_720_1280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        01:37
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_tv1:title:谢谢你医生·先导预告" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/page/k0040wk18kf.html" target="_blank" title="谢谢你医生·先导预告">
        谢谢你医生·先导预告
       </a>
       <div class="figure_desc" title="杨幂白宇为生命暖心护航">
        杨幂白宇为生命暖心护航
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_tv1:img:妈妈的战争·杀青" class="figure" data-float="o3278bljjgk" data-quickopen="true" href="https://v.qq.com/x/page/o3278bljjgk.html" tabindex="-1" target="_blank">
       <img alt="妈妈的战争·杀青" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/media_img/lena/PICkq7brs_720_1280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        03:21
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_tv1:title:妈妈的战争·杀青" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/page/o3278bljjgk.html" target="_blank" title="妈妈的战争·杀青">
        妈妈的战争·杀青
       </a>
       <div class="figure_desc" title="张雨绮吴越董洁敬请期待">
        张雨绮吴越董洁敬请期待
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_tv1:img:爱的二八定律·杀青特辑" class="figure" data-float="z3255ublatb" data-quickopen="true" href="https://v.qq.com/x/page/z3255ublatb.html" tabindex="-1" target="_blank">
       <img alt="爱的二八定律·杀青特辑" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/media_img/lena/PICc8rru2_720_1280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        01:31
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_tv1:title:爱的二八定律·杀青特辑" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/page/z3255ublatb.html" target="_blank" title="爱的二八定律·杀青特辑">
        爱的二八定律·杀青特辑
       </a>
       <div class="figure_desc" title="以爱交锋！杨幂许凯婚内恋爱">
        以爱交锋！杨幂许凯婚内恋爱
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_tv1:img:梦华录·杀青特辑" class="figure" data-float="y3257x5eg33" data-quickopen="true" href="https://v.qq.com/x/page/y3257x5eg33.html" tabindex="-1" target="_blank">
       <img alt="梦华录·杀青特辑" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1233283990_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        02:17
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_tv1:title:梦华录·杀青特辑" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/page/y3257x5eg33.html" target="_blank" title="梦华录·杀青特辑">
        梦华录·杀青特辑
       </a>
       <div class="figure_desc" title="刘亦菲水戏首曝 陈晓打戏燃炸">
        刘亦菲水戏首曝 陈晓打戏燃炸
       </div>
      </div>
     </div>
    </div>
   </div>
  </div>
  <div _expose="ad_qll_width2" class="mod_row_box mod_row_box_special mod_row_box_ad" data-context="7" data-istyle="11" id="ad_qll_width2">
   <div _stat="ad_qll_width2:ad_l" class="mod_ad_main">
    <!--$loc$_div AD begin...."l=$loc$&log=off"-->
    <div class="l_qq_com" data-index="2" data-loc="QQlive_SP_QLL_Width" id="QQlive_SP_QLL_Width:2" style="width:960px;height:90px;">
    </div>
    <!--$loc$ AD end -->
    <!--[if !IE]>|xGv00|cafd564dc3de68a529ae903f7bacfbe7<![endif]-->
   </div>
   <div _stat="ad_qll_width2:ad_r" class="mod_ad_side">
    <a class="ad1" href="https://v.qq.com/x/cover/vbb35hm6m6da1wc.html" target="_blank">
     <img loading="lazy" lz_src="//puui.qpic.cn/tv/0/151620492_73090/0" src="//puui.qpic.cn/vupload/0/common_blank.png/0"/>
    </a>
    <a class="ad2" href="https://v.qq.com/x/cover/vbb35hm6m6da1wc.html" target="_blank">
     <img loading="lazy" lz_src="//puui.qpic.cn/tv/0/151620503/0" src="//puui.qpic.cn/vupload/0/common_blank.png/0"/>
    </a>
    <a class="ad3" href="https://v.qq.com/x/cover/vbb35hm6m6da1wc.html" target="_blank">
     <img loading="lazy" lz_src="//puui.qpic.cn/tv/0/151620495/0" src="//puui.qpic.cn/vupload/0/common_blank.png/0"/>
    </a>
   </div>
  </div>
  <div _expose="new_vs_hot_var1" _wind="columnname=精选_综艺会员尊享&amp;controlname=new_vs_hot_var1" class="mod_row_box" cur-page-num="0" data-context="8" data-istyle="4" has-next-page="false" id="new_vs_hot_var1">
   <div class="mod_hd">
    <h2 class="mod_title">
     <a _stat="new_vs_hot_var1:通栏功能区:通栏标题" class="title_link" data-target="_blank" href="https://film.qq.com/">
      综艺会员尊享
     </a>
    </h2>
    <div class="mod_page_small">
     <button _stat="new_vs_hot_var1:通栏功能区:上一页" class="btn_prev disabled" title="上一页" wind-click="100">
      <svg class="svg_icon svg_icon_prev" height="10" viewbox="0 0 6 10" width="6">
       <path d="M1.4 4.7L5 1M1.3 5.3L5 9" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="1.4">
       </path>
      </svg>
     </button>
     <span class="page_num" data-count="2" data-info="8 9" data-page="1">
      1/2
     </span>
     <button _stat="new_vs_hot_var1:通栏功能区:下一页" class="btn_next" title="下一页" wind-click="100">
      <svg class="svg_icon svg_icon_next" height="10" viewbox="0 0 6 10" width="6">
       <path d="M4.6 4.7L1 1M4.7 5.3L1 9" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="1.4">
       </path>
      </svg>
     </button>
    </div>
   </div>
   <div class="mod_bd cf _quickopen _quickopen_duration">
    <div class="mod_figure mod_figure_h_default mod_figure_h_default_1row mod_figure_h_default mod_figure_scroll" data-rowcount="8" data-rowlen="1">
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_var1:img:哈哈哈哈哈 第2季" class="figure" data-float="mzc00200q90natx" href="https://v.qq.com/x/cover/mzc00200q90natx.html?videoMark=" tabindex="-1" target="_blank">
       <img alt="哈哈哈哈哈 第2季" class="figure_pic" loading="lazy" lz_src="//vc.qpic.cn/tpic/mtviuB5x9ttmC/i6nw8186p3vcj709/250" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        2021-11-29 期
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_var1:title:哈哈哈哈哈 第2季" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200q90natx.html?videoMark=" target="_blank" title="哈哈哈哈哈 第2季">
        哈哈哈哈哈 第2季
       </a>
       <div class="figure_desc" title="郭京飞陈赫纸飞机挑战">
        郭京飞陈赫纸飞机挑战
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_var1:img:我们的歌·加更" class="figure" data-float="mzc002008zmtofv" href="https://v.qq.com/x/cover/mzc002008zmtofv.html?videoMark=" tabindex="-1" target="_blank">
       <img alt="我们的歌·加更" class="figure_pic" loading="lazy" lz_src="//vc.qpic.cn/tpic/mtviuBuZS3CxJ/r5mj8275fi87f514/250" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        2021-11-30 期
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_var1:title:我们的歌·加更" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc002008zmtofv.html?videoMark=" target="_blank" title="我们的歌·加更">
        我们的歌·加更
       </a>
       <div class="figure_desc" title="胡夏做手工送林子祥">
        胡夏做手工送林子祥
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_var1:img:毛雪汪·加更" class="figure" data-float="mzc00200d795ymu" href="https://v.qq.com/x/cover/mzc00200d795ymu.html?videoMark=" tabindex="-1" target="_blank">
       <img alt="毛雪汪·加更" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_hz_pic/0/mzc00200d795ymu1637658325759/332" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        2021-11-23 期
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_var1:title:毛雪汪·加更" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200d795ymu.html?videoMark=" target="_blank" title="毛雪汪·加更">
        毛雪汪·加更
       </a>
       <div class="figure_desc" title="毛不易晓卉相识竟因脱口秀">
        毛不易晓卉相识竟因脱口秀
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_var1:img:导演秘籍" class="figure" data-float="mzc002004youj1p" href="https://v.qq.com/x/cover/mzc002004youj1p.html?videoMark=" tabindex="-1" target="_blank">
       <img alt="导演秘籍" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_hz_pic/0/mzc002004youj1p1637318517223/332" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        2021-11-19 期
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_var1:title:导演秘籍" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc002004youj1p.html?videoMark=" target="_blank" title="导演秘籍">
        导演秘籍
       </a>
       <div class="figure_desc" title="关锦鹏：最懂女人的导演">
        关锦鹏：最懂女人的导演
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_var1:img:导演说" class="figure" data-float="mzc00200nhlxkzw" href="https://v.qq.com/x/cover/mzc00200nhlxkzw.html?videoMark=" tabindex="-1" target="_blank">
       <img alt="导演说" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_hz_pic/0/mzc00200nhlxkzw1636716979333/332" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        2021-11-05 期
       </div>
       <img alt="腾讯出品" class="mark_v mark_v_腾讯出品" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_self_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_self_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_var1:title:导演说" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200nhlxkzw.html?videoMark=" target="_blank" title="导演说">
        导演说
       </a>
       <div class="figure_desc" title="曾赠谈改编《大话西游》初衷">
        曾赠谈改编《大话西游》初衷
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_var1:img:青春环游记" class="figure" data-float="a0041yfqwzn" href="https://v.qq.com/x/cover/mzc002003kpckj7/a0041yfqwzn.html?videoMark=" tabindex="-1" target="_blank">
       <img alt="青春环游记" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/media_img/lena/PIC9i2yeo_580_1680/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        01:15:08
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_var1:title:青春环游记" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc002003kpckj7/a0041yfqwzn.html?videoMark=" target="_blank" title="青春环游记">
        青春环游记
       </a>
       <div class="figure_desc" title="杨洋学宋小宝上头了">
        杨洋学宋小宝上头了
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_var1:img:offer加更·大社死" class="figure" data-float="mzc00200ujqj1bu" href="https://v.qq.com/x/cover/mzc00200ujqj1bu.html?videoMark=" tabindex="-1" target="_blank">
       <img alt="offer加更·大社死" class="figure_pic" loading="lazy" lz_src="//vc.qpic.cn/tpic/mtviutKhZ7Ddu/tviutKhZioCh.jpeg/250" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        2021-11-11 期
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_var1:title:offer加更·大社死" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200ujqj1bu.html?videoMark=" target="_blank" title="offer加更·大社死">
        offer加更·大社死
       </a>
       <div class="figure_desc" title="高尚问张洽：张洽呢？">
        高尚问张洽：张洽呢？
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_var1:img:奔跑吧·黄河篇2" class="figure" data-float="mzc002005ibqup9" href="https://v.qq.com/x/cover/mzc002005ibqup9.html?videoMark=" tabindex="-1" target="_blank">
       <img alt="奔跑吧·黄河篇2" class="figure_pic" loading="lazy" lz_src="//vc.qpic.cn/tpic/mtviurVmj9rJy/tviurVmjkc9m.jpeg/250" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        2021-11-07 期
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_var1:title:奔跑吧·黄河篇2" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc002005ibqup9.html?videoMark=" target="_blank" title="奔跑吧·黄河篇2">
        奔跑吧·黄河篇2
       </a>
       <div class="figure_desc" title="秦霄贤不顾形象大声吃面">
        秦霄贤不顾形象大声吃面
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_var1:img:脱口秀小会·冠军庆功宴" class="figure" data-float="mzc00200xjzbmny" href="https://v.qq.com/x/cover/mzc00200xjzbmny.html?videoMark=" tabindex="-1" target="_blank">
       <img alt="脱口秀小会·冠军庆功宴" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_hz_pic/0/mzc00200xjzbmny1634125807906/332" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        2021-10-14 期
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_var1:title:脱口秀小会·冠军庆功宴" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200xjzbmny.html?videoMark=" target="_blank" title="脱口秀小会·冠军庆功宴">
        脱口秀小会·冠军庆功宴
       </a>
       <div class="figure_desc" title="脱口秀女王杨笠VS大王周奇墨">
        脱口秀女王杨笠VS大王周奇墨
       </div>
      </div>
     </div>
    </div>
   </div>
  </div>
  <div _expose="new_vs_hot_usuk" _wind="columnname=精选_英美剧&amp;controlname=new_vs_hot_usuk" class="mod_row_box" cur-page-num="0" data-context="8" data-istyle="7" has-next-page="false" id="new_vs_hot_usuk">
   <div class="mod_hd">
    <h2 class="mod_title">
     英美剧
    </h2>
    <div class="mod_page_small">
     <button _stat="new_vs_hot_usuk:通栏功能区:上一页" class="btn_prev disabled" title="上一页" wind-click="100">
      <svg class="svg_icon svg_icon_prev" height="10" viewbox="0 0 6 10" width="6">
       <path d="M1.4 4.7L5 1M1.3 5.3L5 9" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="1.4">
       </path>
      </svg>
     </button>
     <span class="page_num" data-count="2" data-info="8 9" data-page="1">
      1/2
     </span>
     <button _stat="new_vs_hot_usuk:通栏功能区:下一页" class="btn_next" title="下一页" wind-click="100">
      <svg class="svg_icon svg_icon_next" height="10" viewbox="0 0 6 10" width="6">
       <path d="M4.6 4.7L1 1M4.7 5.3L1 9" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="1.4">
       </path>
      </svg>
     </button>
    </div>
   </div>
   <div class="mod_bd cf _quickopen _quickopen_duration">
    <div class="mod_figure mod_figure_v_default mod_figure_v_default_1row mod_figure_v_default mod_figure_scroll" data-rowcount="8" data-rowlen="1">
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_usuk:img:离婚第三季" class="figure" data-float="mzc00200yvavnb8" href="https://v.qq.com/x/cover/mzc00200yvavnb8.html" tabindex="-1" target="_blank">
       <img alt="离婚第三季" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/mzc00200yvavnb81594605019/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        全6集
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_usuk:title:离婚第三季" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200yvavnb8.html" target="_blank" title="离婚第三季">
        离婚第三季
       </a>
       <div class="figure_desc" title="中年离婚如何重启新生活？">
        中年离婚如何重启新生活？
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_usuk:img:少年特工亚历克斯" class="figure" data-float="mzc00200azajs81" href="https://v.qq.com/x/cover/mzc00200azajs81.html" tabindex="-1" target="_blank">
       <img alt="少年特工亚历克斯" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/mzc00200azajs811603952313243/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        全8集
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_usuk:title:少年特工亚历克斯" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200azajs81.html" target="_blank" title="少年特工亚历克斯">
        少年特工亚历克斯
       </a>
       <div class="figure_desc" title="少年007王牌出击！">
        少年007王牌出击！
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_usuk:img:切尔诺贝利" class="figure" data-float="ix6w4wausx518m8" href="https://v.qq.com/x/cover/ix6w4wausx518m8.html" tabindex="-1" target="_blank">
       <img alt="切尔诺贝利" class="figure_pic" loading="lazy" lz_src="//i.gtimg.cn/qqlive/img/jpgcache/files/qqvideo/i/ix6w4wausx518m8_p.jpg" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        全5集
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_usuk:title:切尔诺贝利" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/ix6w4wausx518m8.html" target="_blank" title="切尔诺贝利">
        切尔诺贝利
       </a>
       <div class="figure_desc" title="豆瓣9.6 灾难神作">
        豆瓣9.6 灾难神作
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_usuk:img:权力的游戏[会员全集]" class="figure" data-float="zf2z0xpqcculhcz" href="https://v.qq.com/x/cover/zf2z0xpqcculhcz.html" tabindex="-1" target="_blank">
       <img alt="权力的游戏[会员全集]" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/zf2z0xpqcculhcz1491532394/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        更新至72集
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_usuk:title:权力的游戏[会员全集]" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/zf2z0xpqcculhcz.html" target="_blank" title="权力的游戏[会员全集]">
        权力的游戏[会员全集]
       </a>
       <div class="figure_desc" title="HBO奇幻史诗巨作">
        HBO奇幻史诗巨作
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_usuk:img:西部世界3[会员看全集]" class="figure" data-float="oh3vi7bslpzhj9j" href="https://v.qq.com/x/cover/oh3vi7bslpzhj9j.html" tabindex="-1" target="_blank">
       <img alt="西部世界3[会员看全集]" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/oh3vi7bslpzhj9j1564027738/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        全8集
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_usuk:title:西部世界3[会员看全集]" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/oh3vi7bslpzhj9j.html" target="_blank" title="西部世界3[会员看全集]">
        西部世界3[会员看全集]
       </a>
       <div class="figure_desc" title="人工智能终极复仇">
        人工智能终极复仇
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_usuk:img:守望者[会员看全集]" class="figure" data-float="s8e74p6zew8k7zb" href="https://v.qq.com/x/cover/s8e74p6zew8k7zb.html" tabindex="-1" target="_blank">
       <img alt="守望者[会员看全集]" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/s8e74p6zew8k7zb1591586059097/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        全9集
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_usuk:title:守望者[会员看全集]" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/s8e74p6zew8k7zb.html" target="_blank" title="守望者[会员看全集]">
        守望者[会员看全集]
       </a>
       <div class="figure_desc" title="HBO高口碑佳作DC漫改剧">
        HBO高口碑佳作DC漫改剧
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_usuk:img:我的天才女友[会员看全集]" class="figure" data-float="mzc0020046q4d6r" href="https://v.qq.com/x/cover/mzc0020046q4d6r.html" tabindex="-1" target="_blank">
       <img alt="我的天才女友[会员看全集]" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/mzc0020046q4d6r1586318327887/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        全8集
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_usuk:title:我的天才女友[会员看全集]" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc0020046q4d6r.html" target="_blank" title="我的天才女友[会员看全集]">
        我的天才女友[会员看全集]
       </a>
       <div class="figure_desc" title="塑料闺蜜携手前行">
        塑料闺蜜携手前行
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_usuk:img:黑暗物质[会员看全集]" class="figure" data-float="mzc00200xole3rw" href="https://v.qq.com/x/cover/mzc00200xole3rw.html" tabindex="-1" target="_blank">
       <img alt="黑暗物质[会员看全集]" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_vt_pic/0/mzc00200xole3rw1576750034/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        全8集
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_usuk:title:黑暗物质[会员看全集]" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200xole3rw.html" target="_blank" title="黑暗物质[会员看全集]">
        黑暗物质[会员看全集]
       </a>
       <div class="figure_desc" title="詹一美&amp;小狼女探秘多重世界">
        詹一美&amp;小狼女探秘多重世界
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_usuk:img:继承之战2[会员看全集]" class="figure" data-float="mzc00200f6j4ysj" href="https://v.qq.com/x/cover/mzc00200f6j4ysj.html" tabindex="-1" target="_blank">
       <img alt="继承之战2[会员看全集]" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_vt_pic/0/mzc00200f6j4ysj1576477293/350" onerror="picerr(this,'v')" src="//puui.qpic.cn/vupload/0/common_pic_v.png/0"/>
       <div class="figure_caption">
        全10集
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_usuk:title:继承之战2[会员看全集]" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200f6j4ysj.html" target="_blank" title="继承之战2[会员看全集]">
        继承之战2[会员看全集]
       </a>
       <div class="figure_desc" title="传媒巨头家族争产大战">
        传媒巨头家族争产大战
       </div>
      </div>
     </div>
    </div>
   </div>
  </div>
  <div _expose="Thai_series" _wind="columnname=精选_泰剧&amp;controlname=Thai_series" class="mod_row_box" cur-page-num="0" data-context="8" data-istyle="4" has-next-page="false" id="Thai_series">
   <div class="mod_hd">
    <h2 class="mod_title">
     泰剧
    </h2>
    <div class="mod_page_small">
     <button _stat="Thai_series:通栏功能区:上一页" class="btn_prev disabled" title="上一页" wind-click="100">
      <svg class="svg_icon svg_icon_prev" height="10" viewbox="0 0 6 10" width="6">
       <path d="M1.4 4.7L5 1M1.3 5.3L5 9" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="1.4">
       </path>
      </svg>
     </button>
     <span class="page_num" data-count="4" data-info="8 25" data-page="1">
      1/4
     </span>
     <button _stat="Thai_series:通栏功能区:下一页" class="btn_next" title="下一页" wind-click="100">
      <svg class="svg_icon svg_icon_next" height="10" viewbox="0 0 6 10" width="6">
       <path d="M4.6 4.7L1 1M4.7 5.3L1 9" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="1.4">
       </path>
      </svg>
     </button>
    </div>
   </div>
   <div class="mod_bd cf _quickopen _quickopen_duration">
    <div class="mod_figure mod_figure_h_default mod_figure_h_default_1row mod_figure_h_default mod_figure_scroll" data-rowcount="8" data-rowlen="1">
     <div __wind="" class="list_item">
      <a _stat="Thai_series:img:泰版星你[会员全集]" class="figure" data-float="mzc0020004a6u7q" href="https://v.qq.com/x/cover/mzc0020004a6u7q.html" tabindex="-1" target="_blank">
       <img alt="泰版星你[会员全集]" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/tv/0/1234016990_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        全45集
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="Thai_series:title:泰版星你[会员全集]" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc0020004a6u7q.html" target="_blank" title="泰版星你[会员全集]">
        泰版星你[会员全集]
       </a>
       <div class="figure_desc" title="经典回归！外星人与大明星寻爱">
        经典回归！外星人与大明星寻爱
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="Thai_series:img:王子变青蛙" class="figure" data-float="mzc00200aooqwdy" href="https://v.qq.com/x/cover/mzc00200aooqwdy.html" tabindex="-1" target="_blank">
       <img alt="王子变青蛙" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/tv/0/1226848607_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        全26集
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="Thai_series:title:王子变青蛙" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200aooqwdy.html" target="_blank" title="王子变青蛙">
        王子变青蛙
       </a>
       <div class="figure_desc" title="失忆公子恋上平凡少女">
        失忆公子恋上平凡少女
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="Thai_series:img:直到天空迎来太阳" class="figure" data-float="mzc002004b4fael" href="https://v.qq.com/x/cover/mzc002004b4fael.html" tabindex="-1" target="_blank">
       <img alt="直到天空迎来太阳" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/tv/0/1225839213_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        全38集
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="Thai_series:title:直到天空迎来太阳" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc002004b4fael.html" target="_blank" title="直到天空迎来太阳">
        直到天空迎来太阳
       </a>
       <div class="figure_desc" title="霸气总裁恋上彪悍萌妹">
        霸气总裁恋上彪悍萌妹
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="Thai_series:img:诱爱入局" class="figure" data-float="mzc00200xmdsx7c" href="https://v.qq.com/x/cover/mzc00200xmdsx7c.html" tabindex="-1" target="_blank">
       <img alt="诱爱入局" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/tv/0/1225839249_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        全34集
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="Thai_series:title:诱爱入局" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200xmdsx7c.html" target="_blank" title="诱爱入局">
        诱爱入局
       </a>
       <div class="figure_desc" title="精英律师恋上有夫之妇">
        精英律师恋上有夫之妇
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="Thai_series:img:星途叵测第二季" class="figure" data-float="mzc00200vs5sroe" href="https://v.qq.com/x/cover/mzc00200vs5sroe.html" tabindex="-1" target="_blank">
       <img alt="星途叵测第二季" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/tv/0/1225839294_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        全18集
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="Thai_series:title:星途叵测第二季" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200vs5sroe.html" target="_blank" title="星途叵测第二季">
        星途叵测第二季
       </a>
       <div class="figure_desc" title="抓马当道 泰娱圈风云再起">
        抓马当道 泰娱圈风云再起
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="Thai_series:img:玫瑰奇缘" class="figure" data-float="mzc00200k0uad8t" href="https://v.qq.com/x/cover/mzc00200k0uad8t.html" tabindex="-1" target="_blank">
       <img alt="玫瑰奇缘" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/tv/0/1225839339_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        全39集
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="Thai_series:title:玫瑰奇缘" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200k0uad8t.html" target="_blank" title="玫瑰奇缘">
        玫瑰奇缘
       </a>
       <div class="figure_desc" title="大明星与占卜师的奇幻爱恋">
        大明星与占卜师的奇幻爱恋
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="Thai_series:img:爱在旅途" class="figure" data-float="mzc002005v5twmk" href="https://v.qq.com/x/cover/mzc002005v5twmk.html" tabindex="-1" target="_blank">
       <img alt="爱在旅途" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/tv/0/1225839417_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        全26集
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="Thai_series:title:爱在旅途" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc002005v5twmk.html" target="_blank" title="爱在旅途">
        爱在旅途
       </a>
       <div class="figure_desc" title="Esther女扮男装演反转爱情">
        Esther女扮男装演反转爱情
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="Thai_series:img:法定丈夫" class="figure" data-float="mzc00200ibqz3tc" href="https://v.qq.com/x/cover/mzc00200ibqz3tc.html" tabindex="-1" target="_blank">
       <img alt="法定丈夫" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/tv/0/841100946_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        全45集
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="Thai_series:title:法定丈夫" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200ibqz3tc.html" target="_blank" title="法定丈夫">
        法定丈夫
       </a>
       <div class="figure_desc" title="逗趣小夫妻先婚后爱">
        逗趣小夫妻先婚后爱
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="Thai_series:img:爱恨之火" class="figure" data-float="mzc00200rxjza4q" href="https://v.qq.com/x/cover/mzc00200rxjza4q.html" tabindex="-1" target="_blank">
       <img alt="爱恨之火" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1225839458_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        全42集
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="Thai_series:title:爱恨之火" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200rxjza4q.html" target="_blank" title="爱恨之火">
        爱恨之火
       </a>
       <div class="figure_desc" title="两姐妹大打出手上演夺夫战">
        两姐妹大打出手上演夺夫战
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="Thai_series:img:我可能不会爱你" class="figure" data-float="mzc002002wa4fx9" href="https://v.qq.com/x/cover/mzc002002wa4fx9.html" tabindex="-1" target="_blank">
       <img alt="我可能不会爱你" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/498687959_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        全24集
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="Thai_series:title:我可能不会爱你" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc002002wa4fx9.html" target="_blank" title="我可能不会爱你">
        我可能不会爱你
       </a>
       <div class="figure_desc" title="泰版大仁又青的绝美爱情">
        泰版大仁又青的绝美爱情
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="Thai_series:img:妻子2018" class="figure" data-float="mzc00200iqmuemm" href="https://v.qq.com/x/cover/mzc00200iqmuemm.html" tabindex="-1" target="_blank">
       <img alt="妻子2018" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1225839493_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        全29集
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="Thai_series:title:妻子2018" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200iqmuemm.html" target="_blank" title="妻子2018">
        妻子2018
       </a>
       <div class="figure_desc" title="围观大型狗血出轨现场">
        围观大型狗血出轨现场
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="Thai_series:img:鲜花宝座" class="figure" data-float="31x5q2bchbbj487" href="https://v.qq.com/x/cover/31x5q2bchbbj487.html" tabindex="-1" target="_blank">
       <img alt="鲜花宝座" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/432671635_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        全42集
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="Thai_series:title:鲜花宝座" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/31x5q2bchbbj487.html" target="_blank" title="鲜花宝座">
        鲜花宝座
       </a>
       <div class="figure_desc" title="马里奥变身小奶狗恋女总裁">
        马里奥变身小奶狗恋女总裁
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="Thai_series:img:匆匆那年" class="figure" data-float="lqz8bdnjk05bfqg" href="https://v.qq.com/x/cover/lqz8bdnjk05bfqg.html" tabindex="-1" target="_blank">
       <img alt="匆匆那年" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1226101157_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        全40集
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="Thai_series:title:匆匆那年" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/lqz8bdnjk05bfqg.html" target="_blank" title="匆匆那年">
        匆匆那年
       </a>
       <div class="figure_desc" title="陈寻方茴青春时代勇敢追爱">
        陈寻方茴青春时代勇敢追爱
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="Thai_series:img:美人计" class="figure" data-float="eqrjlmqa0x66vr7" href="https://v.qq.com/x/cover/eqrjlmqa0x66vr7.html" tabindex="-1" target="_blank">
       <img alt="美人计" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1226101189_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        全24集
       </div>
       <img alt="独播" class="mark_v mark_v_独播" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_only_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_only_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="Thai_series:title:美人计" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/eqrjlmqa0x66vr7.html" target="_blank" title="美人计">
        美人计
       </a>
       <div class="figure_desc" title="欢喜冤家恋爱了">
        欢喜冤家恋爱了
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="Thai_series:img:心之影" class="figure" data-float="pzdfvy7nsdsb4f4" href="https://v.qq.com/x/cover/pzdfvy7nsdsb4f4.html" tabindex="-1" target="_blank">
       <img alt="心之影" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1226101200_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        全30集
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="Thai_series:title:心之影" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/pzdfvy7nsdsb4f4.html" target="_blank" title="心之影">
        心之影
       </a>
       <div class="figure_desc" title="替身富二代恩宠小娇妻">
        替身富二代恩宠小娇妻
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="Thai_series:img:超级巨星" class="figure" data-float="0jmq8ko4k15qb07" href="https://v.qq.com/x/cover/0jmq8ko4k15qb07.html" tabindex="-1" target="_blank">
       <img alt="超级巨星" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1226101210_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        全28集
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="Thai_series:title:超级巨星" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/0jmq8ko4k15qb07.html" target="_blank" title="超级巨星">
        超级巨星
       </a>
       <div class="figure_desc" title="菜鸟替身与超级巨星同居记">
        菜鸟替身与超级巨星同居记
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="Thai_series:img:丑小鸭" class="figure" data-float="zp8aajb6aus6nuk" href="https://v.qq.com/x/cover/zp8aajb6aus6nuk.html" tabindex="-1" target="_blank">
       <img alt="丑小鸭" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1226101227_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        全30集
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="Thai_series:title:丑小鸭" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/zp8aajb6aus6nuk.html" target="_blank" title="丑小鸭">
        丑小鸭
       </a>
       <div class="figure_desc" title="灰姑娘集体邂逅美好爱情">
        灰姑娘集体邂逅美好爱情
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="Thai_series:img:你是我的毒玫瑰" class="figure" data-float="r2v3k3icklt2htu" href="https://v.qq.com/x/cover/r2v3k3icklt2htu.html" tabindex="-1" target="_blank">
       <img alt="你是我的毒玫瑰" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1226101244_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        全26集
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="Thai_series:title:你是我的毒玫瑰" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/r2v3k3icklt2htu.html" target="_blank" title="你是我的毒玫瑰">
        你是我的毒玫瑰
       </a>
       <div class="figure_desc" title="毒舌男医生恋上娇蛮大明星">
        毒舌男医生恋上娇蛮大明星
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="Thai_series:img:彩象岛的女孩" class="figure" data-float="nqrzbz0wku40ct6" href="https://v.qq.com/x/cover/nqrzbz0wku40ct6.html" tabindex="-1" target="_blank">
       <img alt="彩象岛的女孩" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1226101263_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        全34集
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="Thai_series:title:彩象岛的女孩" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/nqrzbz0wku40ct6.html" target="_blank" title="彩象岛的女孩">
        彩象岛的女孩
       </a>
       <div class="figure_desc" title="浪漫又现实的泰国写照">
        浪漫又现实的泰国写照
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="Thai_series:img:命中注定我爱你[泰国版]" class="figure" data-float="vo72n2vk1pwllh6" href="https://v.qq.com/x/cover/vo72n2vk1pwllh6.html" tabindex="-1" target="_blank">
       <img alt="命中注定我爱你[泰国版]" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1226101267_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        全34集
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="Thai_series:title:命中注定我爱你[泰国版]" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/vo72n2vk1pwllh6.html" target="_blank" title="命中注定我爱你[泰国版]">
        命中注定我爱你[泰国版]
       </a>
       <div class="figure_desc" title="霸道总裁和他的便利贴女孩">
        霸道总裁和他的便利贴女孩
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="Thai_series:img:我爸爸是超级大明星" class="figure" data-float="nh9s2yd6u75cuvn" href="https://v.qq.com/x/cover/nh9s2yd6u75cuvn.html" tabindex="-1" target="_blank">
       <img alt="我爸爸是超级大明星" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1226101280_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        全38集
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="Thai_series:title:我爸爸是超级大明星" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/nh9s2yd6u75cuvn.html" target="_blank" title="我爸爸是超级大明星">
        我爸爸是超级大明星
       </a>
       <div class="figure_desc" title="帅气老爸与小萝莉爆笑来袭">
        帅气老爸与小萝莉爆笑来袭
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="Thai_series:img:撕心裂爱" class="figure" data-float="j7p3j29b1cpqlug" href="https://v.qq.com/x/cover/j7p3j29b1cpqlug.html" tabindex="-1" target="_blank">
       <img alt="撕心裂爱" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1226101338_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        全20集
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="Thai_series:title:撕心裂爱" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/j7p3j29b1cpqlug.html" target="_blank" title="撕心裂爱">
        撕心裂爱
       </a>
       <div class="figure_desc" title="又名“闺蜜男友我都要抢”">
        又名“闺蜜男友我都要抢”
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="Thai_series:img:千方百计爱上你" class="figure" data-float="4xejxtj554aysi2" href="https://v.qq.com/x/cover/4xejxtj554aysi2.html" tabindex="-1" target="_blank">
       <img alt="千方百计爱上你" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1226101347_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        全28集
       </div>
       <img alt="独播" class="mark_v mark_v_独播" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_only_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_only_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="Thai_series:title:千方百计爱上你" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/4xejxtj554aysi2.html" target="_blank" title="千方百计爱上你">
        千方百计爱上你
       </a>
       <div class="figure_desc" title="梨涡男神复仇记">
        梨涡男神复仇记
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="Thai_series:img:公主罗曼史" class="figure" data-float="s1nxlfvzkkb3kvh" href="https://v.qq.com/x/cover/s1nxlfvzkkb3kvh.html" tabindex="-1" target="_blank">
       <img alt="公主罗曼史" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1226101360_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        全36集
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="Thai_series:title:公主罗曼史" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/s1nxlfvzkkb3kvh.html" target="_blank" title="公主罗曼史">
        公主罗曼史
       </a>
       <div class="figure_desc" title="傲娇公主与平民先婚后爱">
        傲娇公主与平民先婚后爱
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="Thai_series:img:宫[泰国版]" class="figure" data-float="095uo1tgrua3x5q" href="https://v.qq.com/x/cover/095uo1tgrua3x5q.html" tabindex="-1" target="_blank">
       <img alt="宫[泰国版]" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1226101392_498280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        全20集
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="Thai_series:title:宫[泰国版]" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/095uo1tgrua3x5q.html" target="_blank" title="宫[泰国版]">
        宫[泰国版]
       </a>
       <div class="figure_desc" title="灰姑娘一夜逆袭成王妃">
        灰姑娘一夜逆袭成王妃
       </div>
      </div>
     </div>
    </div>
   </div>
  </div>
  <div _expose="new_vs_edu" _wind="columnname=精选_教育精选&amp;controlname=new_vs_edu" class="mod_row_box" cur-page-num="0" data-context="9" data-istyle="4" has-next-page="false" id="new_vs_edu">
   <div class="mod_hd">
    <h2 class="mod_title">
     <a _stat="new_vs_edu:通栏功能区:通栏标题" class="title_link" data-target="_blank" href="https://v.qq.com/channel/education">
      教育精选
     </a>
    </h2>
    <div class="mod_page_small">
     <button _stat="new_vs_edu:通栏功能区:上一页" class="btn_prev disabled" title="上一页" wind-click="100">
      <svg class="svg_icon svg_icon_prev" height="10" viewbox="0 0 6 10" width="6">
       <path d="M1.4 4.7L5 1M1.3 5.3L5 9" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="1.4">
       </path>
      </svg>
     </button>
     <span class="page_num" data-count="2" data-info="8 15" data-page="1">
      1/2
     </span>
     <button _stat="new_vs_edu:通栏功能区:下一页" class="btn_next" title="下一页" wind-click="100">
      <svg class="svg_icon svg_icon_next" height="10" viewbox="0 0 6 10" width="6">
       <path d="M4.6 4.7L1 1M4.7 5.3L1 9" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="1.4">
       </path>
      </svg>
     </button>
    </div>
   </div>
   <div class="mod_bd cf _quickopen _quickopen_duration">
    <div class="mod_figure mod_figure_h_default mod_figure_h_default_1row mod_figure_h_default mod_figure_scroll" data-rowcount="8" data-rowlen="1">
     <div __wind="" class="list_item">
      <a _stat="new_vs_edu:img:国考笔试开考" class="figure" data-float="d004105jzgm" data-quickopen="true" href="https://v.qq.com/x/page/d004105jzgm.html" tabindex="-1" target="_blank">
       <img alt="国考笔试开考" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/qqvideo_ori/0/d004105jzgm_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        03:05
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_edu:title:国考笔试开考" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/page/d004105jzgm.html" target="_blank" title="国考笔试开考">
        国考笔试开考
       </a>
       <div class="figure_desc" title="多地要求学生准备核酸证明">
        多地要求学生准备核酸证明
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_edu:img:北大物理硕士毕业做中学老师" class="figure" data-float="z004182l3m5" data-quickopen="true" href="https://v.qq.com/x/page/z004182l3m5.html" tabindex="-1" target="_blank">
       <img alt="北大物理硕士毕业做中学老师" class="figure_pic" loading="lazy" lz_src="//vc.qpic.cn/tpic/mtviuAUyw9XwG/txdi81503xmmh490/220" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        02:00
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_edu:title:北大物理硕士毕业做中学老师" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/page/z004182l3m5.html" target="_blank" title="北大物理硕士毕业做中学老师">
        北大物理硕士毕业做中学老师
       </a>
       <div class="figure_desc" title="科研经历开阔学生视野">
        科研经历开阔学生视野
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_edu:img:小学生讲述心路历程好暖心" class="figure" data-float="b3310d9ex7y" href="https://v.qq.com/x/page/b3310d9ex7y.html" tabindex="-1" target="_blank">
       <img alt="小学生讲述心路历程好暖心" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/qqvideo_ori/0/b3310d9ex7y_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        01:01:30
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_edu:title:小学生讲述心路历程好暖心" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/page/b3310d9ex7y.html" target="_blank" title="小学生讲述心路历程好暖心">
        小学生讲述心路历程好暖心
       </a>
       <div class="figure_desc" title="希望之星暨希语盛典">
        希望之星暨希语盛典
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_edu:img:高校不得举办课程进修班" class="figure" data-float="o0041bduiwd" data-quickopen="true" href="https://v.qq.com/x/page/o0041bduiwd.html" tabindex="-1" target="_blank">
       <img alt="高校不得举办课程进修班" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/qqvideo_ori/0/o0041bduiwd_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        03:53
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_edu:title:高校不得举办课程进修班" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/page/o0041bduiwd.html" target="_blank" title="高校不得举办课程进修班">
        高校不得举办课程进修班
       </a>
       <div class="figure_desc" title="【鹅眼Live】">
        【鹅眼Live】
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_edu:img:小伙支教6年救助29名残病儿" class="figure" data-float="o0041eaacwx" data-quickopen="true" href="https://v.qq.com/x/page/o0041eaacwx.html" tabindex="-1" target="_blank">
       <img alt="小伙支教6年救助29名残病儿" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/qqvideo_ori/0/o0041eaacwx_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        01:50
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_edu:title:小伙支教6年救助29名残病儿" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/page/o0041eaacwx.html" target="_blank" title="小伙支教6年救助29名残病儿">
        小伙支教6年救助29名残病儿
       </a>
       <div class="figure_desc" title="【鹅老师Talk90s】">
        【鹅老师Talk90s】
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_edu:img:10后萌娃表演个人技" class="figure" data-float="v3309fl3r6i" href="https://v.qq.com/x/page/v3309fl3r6i.html" tabindex="-1" target="_blank">
       <img alt="10后萌娃表演个人技" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/qqvideo_ori/0/v3309fl3r6i_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        01:00:00
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_edu:title:10后萌娃表演个人技" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/page/v3309fl3r6i.html" target="_blank" title="10后萌娃表演个人技">
        10后萌娃表演个人技
       </a>
       <div class="figure_desc" title="嘉宾笑得合不拢嘴！">
        嘉宾笑得合不拢嘴！
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_edu:img:专访北京致知学校校长张晔" class="figure" data-float="k0040bm8tf7" href="https://v.qq.com/x/page/k0040bm8tf7.html" tabindex="-1" target="_blank">
       <img alt="专访北京致知学校校长张晔" class="figure_pic" loading="lazy" lz_src="//vc.qpic.cn/tpic/mtviuocUmqD71/tviuocUmBovN.png/220" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        19:32
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_edu:title:专访北京致知学校校长张晔" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/page/k0040bm8tf7.html" target="_blank" title="专访北京致知学校校长张晔">
        专访北京致知学校校长张晔
       </a>
       <div class="figure_desc" title="时光不语，静待花开（下）">
        时光不语，静待花开（下）
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_edu:img:神尔国学小课堂" class="figure" data-float="mzc00200x8j42pn" href="https://v.qq.com/x/cover/mzc00200x8j42pn.html" tabindex="-1" target="_blank">
       <img alt="神尔国学小课堂" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/tv/0/1236526077_220123/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
       <img alt="付费" class="mark_v mark_v_付费" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_pay_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_pay_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_edu:title:神尔国学小课堂" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200x8j42pn.html" target="_blank" title="神尔国学小课堂">
        神尔国学小课堂
       </a>
       <div class="figure_desc" title="游玩国学海洋">
        游玩国学海洋
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_edu:img:沉浸式外教在线青少英语课堂" class="figure" data-float="mzc00200dqbiexl" href="https://v.qq.com/x/cover/mzc00200dqbiexl.html" tabindex="-1" target="_blank">
       <img alt="沉浸式外教在线青少英语课堂" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1236526716_220123/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
       <img alt="付费" class="mark_v mark_v_付费" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_pay_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_pay_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_edu:title:沉浸式外教在线青少英语课堂" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200dqbiexl.html" target="_blank" title="沉浸式外教在线青少英语课堂">
        沉浸式外教在线青少英语课堂
       </a>
       <div class="figure_desc" title="Amy姐姐带你玩英语课堂">
        Amy姐姐带你玩英语课堂
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_edu:img:幼儿园现“招生难”" class="figure" data-float="w0040dnpnio" data-quickopen="true" href="https://v.qq.com/x/page/w0040dnpnio.html" tabindex="-1" target="_blank">
       <img alt="幼儿园现“招生难”" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo_ori/0/w0040dnpnio_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        02:21
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_edu:title:幼儿园现“招生难”" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/page/w0040dnpnio.html" target="_blank" title="幼儿园现“招生难”">
        幼儿园现“招生难”
       </a>
       <div class="figure_desc" title="2020年全国民办园数量大减">
        2020年全国民办园数量大减
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_edu:img:深度对话清华附中副校长辛颖" class="figure" data-float="y0040s8ezkw" data-quickopen="true" href="https://v.qq.com/x/page/y0040s8ezkw.html" tabindex="-1" target="_blank">
       <img alt="深度对话清华附中副校长辛颖" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/tv/0/1235031598_220123/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        13:45
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_edu:title:深度对话清华附中副校长辛颖" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/page/y0040s8ezkw.html" target="_blank" title="深度对话清华附中副校长辛颖">
        深度对话清华附中副校长辛颖
       </a>
       <div class="figure_desc" title="因为热爱，所以坚持（下）">
        因为热爱，所以坚持（下）
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_edu:img:二年级上册语文课文同步动画" class="figure" data-float="mzc00200b6n4oy5" href="https://v.qq.com/x/cover/mzc00200b6n4oy5.html" tabindex="-1" target="_blank">
       <img alt="二年级上册语文课文同步动画" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_hz_pic/0/h2guy9jma2r9cu3/332" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
       <img alt="付费" class="mark_v mark_v_付费" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_pay_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_pay_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_edu:title:二年级上册语文课文同步动画" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200b6n4oy5.html" target="_blank" title="二年级上册语文课文同步动画">
        二年级上册语文课文同步动画
       </a>
       <div class="figure_desc" title="看课文动画，学小学语文">
        看课文动画，学小学语文
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_edu:img:深度对话学霸校长李颖博士" class="figure" data-float="z0040w87cvk" href="https://v.qq.com/x/page/z0040w87cvk.html" tabindex="-1" target="_blank">
       <img alt="深度对话学霸校长李颖博士" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo_ori/0/z0040w87cvk_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        23:32
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_edu:title:深度对话学霸校长李颖博士" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/page/z0040w87cvk.html" target="_blank" title="深度对话学霸校长李颖博士">
        深度对话学霸校长李颖博士
       </a>
       <div class="figure_desc" title="成长自己，成就他人（下）">
        成长自己，成就他人（下）
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_edu:img:新的教育模式让孩子爱上学习" class="figure" data-float="y3274j451x9" href="https://v.qq.com/x/page/y3274j451x9.html" tabindex="-1" target="_blank">
       <img alt="新的教育模式让孩子爱上学习" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo_ori/0/y3274j451x9_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        16:14
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_edu:title:新的教育模式让孩子爱上学习" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/page/y3274j451x9.html" target="_blank" title="新的教育模式让孩子爱上学习">
        新的教育模式让孩子爱上学习
       </a>
       <div class="figure_desc" title="对话著名教学专家黄微">
        对话著名教学专家黄微
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_edu:img:小学语文能力提升动画课" class="figure" data-float="mzc00200bk9wkt7" href="https://v.qq.com/x/cover/mzc00200bk9wkt7.html" tabindex="-1" target="_blank">
       <img alt="小学语文能力提升动画课" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_hz_pic/0/m7btbsfiddh5266/332" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
       <img alt="付费" class="mark_v mark_v_付费" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_pay_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_pay_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_edu:title:小学语文能力提升动画课" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200bk9wkt7.html" target="_blank" title="小学语文能力提升动画课">
        小学语文能力提升动画课
       </a>
       <div class="figure_desc" title="走进经典的语言世界">
        走进经典的语言世界
       </div>
      </div>
     </div>
    </div>
   </div>
  </div>
  <div _expose="new_vs3_travel" _wind="columnname=精选_旅游精选&amp;controlname=new_vs3_travel" class="mod_row_box" cur-page-num="0" data-context="9" data-istyle="4" has-next-page="false" id="new_vs3_travel">
   <div class="mod_hd">
    <h2 class="mod_title">
     <a _stat="new_vs3_travel:通栏功能区:通栏标题" class="title_link" data-target="_blank" href="https://v.qq.com/channel/travel">
      旅游精选
     </a>
    </h2>
    <div class="mod_page_small">
     <button _stat="new_vs3_travel:通栏功能区:上一页" class="btn_prev disabled" title="上一页" wind-click="100">
      <svg class="svg_icon svg_icon_prev" height="10" viewbox="0 0 6 10" width="6">
       <path d="M1.4 4.7L5 1M1.3 5.3L5 9" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="1.4">
       </path>
      </svg>
     </button>
     <span class="page_num" data-count="2" data-info="8 9" data-page="1">
      1/2
     </span>
     <button _stat="new_vs3_travel:通栏功能区:下一页" class="btn_next" title="下一页" wind-click="100">
      <svg class="svg_icon svg_icon_next" height="10" viewbox="0 0 6 10" width="6">
       <path d="M4.6 4.7L1 1M4.7 5.3L1 9" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="1.4">
       </path>
      </svg>
     </button>
    </div>
   </div>
   <div class="mod_bd cf _quickopen _quickopen_duration">
    <div class="mod_figure mod_figure_h_default mod_figure_h_default_1row mod_figure_h_default mod_figure_scroll" data-rowcount="8" data-rowlen="1">
     <div __wind="" class="list_item">
      <a _stat="new_vs3_travel:img:旅行团的速度与激情" class="figure" data-float="d33019dvadb" href="https://v.qq.com/x/page/d33019dvadb.html" tabindex="-1" target="_blank">
       <img alt="旅行团的速度与激情" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/tv/0/1236296846_250140/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        24:06
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_travel:title:旅行团的速度与激情" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/page/d33019dvadb.html" target="_blank" title="旅行团的速度与激情">
        旅行团的速度与激情
       </a>
       <div class="figure_desc" title="高嘉朗战略性抓鸡">
        高嘉朗战略性抓鸡
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_travel:img:隐于天津的童话城堡" class="figure" data-float="a3310xqj2t2" data-quickopen="true" href="https://v.qq.com/x/page/a3310xqj2t2.html" tabindex="-1" target="_blank">
       <img alt="隐于天津的童话城堡" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/qqvideo_ori/0/a3310xqj2t2_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        02:39
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_travel:title:隐于天津的童话城堡" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/page/a3310xqj2t2.html" target="_blank" title="隐于天津的童话城堡">
        隐于天津的童话城堡
       </a>
       <div class="figure_desc" title="当一次在逃公主">
        当一次在逃公主
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_travel:img:原汁原味的泰国水灯节" class="figure" data-float="q33102t3ees" data-quickopen="true" href="https://v.qq.com/x/page/q33102t3ees.html" tabindex="-1" target="_blank">
       <img alt="原汁原味的泰国水灯节" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/qqvideo_ori/0/q33102t3ees_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        02:17
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_travel:title:原汁原味的泰国水灯节" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/page/q33102t3ees.html" target="_blank" title="原汁原味的泰国水灯节">
        原汁原味的泰国水灯节
       </a>
       <div class="figure_desc" title="在家门口就过了一个">
        在家门口就过了一个
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_travel:img:成都四日游攻略" class="figure" data-float="k3211wv1xmk" data-quickopen="true" href="https://v.qq.com/x/page/k3211wv1xmk.html" tabindex="-1" target="_blank">
       <img alt="成都四日游攻略" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/qqvideo_ori/0/k3211wv1xmk_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        09:12
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_travel:title:成都四日游攻略" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/page/k3211wv1xmk.html" target="_blank" title="成都四日游攻略">
        成都四日游攻略
       </a>
       <div class="figure_desc" title="一站体验 巴适得很">
        一站体验 巴适得很
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_travel:img:天津有座小山村" class="figure" data-float="b3310ofqy4n" data-quickopen="true" href="https://v.qq.com/x/page/b3310ofqy4n.html" tabindex="-1" target="_blank">
       <img alt="天津有座小山村" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/qqvideo_ori/0/b3310ofqy4n_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        02:13
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_travel:title:天津有座小山村" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/page/b3310ofqy4n.html" target="_blank" title="天津有座小山村">
        天津有座小山村
       </a>
       <div class="figure_desc" title="用8亿年前的石头盖房子">
        用8亿年前的石头盖房子
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_travel:img:每个人心中都有一座城" class="figure" data-float="y3309zz05om" data-quickopen="true" href="https://v.qq.com/x/page/y3309zz05om.html" tabindex="-1" target="_blank">
       <img alt="每个人心中都有一座城" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/qqvideo_ori/0/y3309zz05om_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        00:24
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_travel:title:每个人心中都有一座城" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/page/y3309zz05om.html" target="_blank" title="每个人心中都有一座城">
        每个人心中都有一座城
       </a>
       <div class="figure_desc" title="每座城都有自己的故事">
        每座城都有自己的故事
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_travel:img:超火热的大湾区" class="figure" data-float="s3309gx6x2w" data-quickopen="true" href="https://v.qq.com/x/page/s3309gx6x2w.html" tabindex="-1" target="_blank">
       <img alt="超火热的大湾区" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/qqvideo_ori/0/s3309gx6x2w_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        00:59
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_travel:title:超火热的大湾区" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/page/s3309gx6x2w.html" target="_blank" title="超火热的大湾区">
        超火热的大湾区
       </a>
       <div class="figure_desc" title="跟着花花来打卡这3城">
        跟着花花来打卡这3城
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_travel:img:携手环游30国之后" class="figure" data-float="n3308zrdr7n" data-quickopen="true" href="https://v.qq.com/x/page/n3308zrdr7n.html" tabindex="-1" target="_blank">
       <img alt="携手环游30国之后" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/qqvideo_ori/0/n3308zrdr7n_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        03:21
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_travel:title:携手环游30国之后" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/page/n3308zrdr7n.html" target="_blank" title="携手环游30国之后">
        携手环游30国之后
       </a>
       <div class="figure_desc" title="我们终于重启了人生">
        我们终于重启了人生
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_travel:img:和老曹的成都VLOG" class="figure" data-float="e33078x5kzb" data-quickopen="true" href="https://v.qq.com/x/page/e33078x5kzb.html" tabindex="-1" target="_blank">
       <img alt="和老曹的成都VLOG" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo_ori/0/e33078x5kzb_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        03:52
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_travel:title:和老曹的成都VLOG" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/page/e33078x5kzb.html" target="_blank" title="和老曹的成都VLOG">
        和老曹的成都VLOG
       </a>
       <div class="figure_desc" title="成都旅行要这样玩">
        成都旅行要这样玩
       </div>
      </div>
     </div>
    </div>
   </div>
  </div>
  <div _expose="new_vs3_fashion" _wind="columnname=精选_时尚热度榜&amp;controlname=new_vs3_fashion" class="mod_row_box" cur-page-num="0" data-context="9" data-istyle="4" has-next-page="false" id="new_vs3_fashion">
   <div class="mod_hd">
    <h2 class="mod_title">
     <a _stat="new_vs3_fashion:通栏功能区:通栏标题" class="title_link" data-target="_blank" href="https://v.qq.com/channel/fashion">
      时尚热度榜
     </a>
    </h2>
    <div class="mod_page_small">
     <button _stat="new_vs3_fashion:通栏功能区:上一页" class="btn_prev disabled" title="上一页" wind-click="100">
      <svg class="svg_icon svg_icon_prev" height="10" viewbox="0 0 6 10" width="6">
       <path d="M1.4 4.7L5 1M1.3 5.3L5 9" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="1.4">
       </path>
      </svg>
     </button>
     <span class="page_num" data-count="2" data-info="8 9" data-page="1">
      1/2
     </span>
     <button _stat="new_vs3_fashion:通栏功能区:下一页" class="btn_next" title="下一页" wind-click="100">
      <svg class="svg_icon svg_icon_next" height="10" viewbox="0 0 6 10" width="6">
       <path d="M4.6 4.7L1 1M4.7 5.3L1 9" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="1.4">
       </path>
      </svg>
     </button>
    </div>
   </div>
   <div class="mod_bd cf _quickopen _quickopen_duration">
    <div class="mod_figure mod_figure_h_default mod_figure_h_default_1row mod_figure_h_default mod_figure_scroll" data-rowcount="8" data-rowlen="1">
     <div __wind="" class="list_item">
      <a _stat="new_vs3_fashion:img:女神爱上男友风" class="figure" data-float="c3311xnojkc" data-quickopen="true" href="https://v.qq.com/x/cover/mzc00200dktee6z/c3311xnojkc.html" tabindex="-1" target="_blank">
       <img alt="女神爱上男友风" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/media_img/lena/PICibb2o4_140_250/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        01:58
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_fashion:title:女神爱上男友风" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200dktee6z/c3311xnojkc.html" target="_blank" title="女神爱上男友风">
        女神爱上男友风
       </a>
       <div class="figure_desc" title="热巴杨幂宋茜超A look">
        热巴杨幂宋茜超A look
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_fashion:img:麦浚龙「终极」收藏奥义" class="figure" data-float="y3311entlqe" data-quickopen="true" href="https://v.qq.com/x/page/y3311entlqe.html" tabindex="-1" target="_blank">
       <img alt="麦浚龙「终极」收藏奥义" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/media_img/lena/PIC93xqbk_140_250/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        12:20
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_fashion:title:麦浚龙「终极」收藏奥义" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/page/y3311entlqe.html" target="_blank" title="麦浚龙「终极」收藏奥义">
        麦浚龙「终极」收藏奥义
       </a>
       <div class="figure_desc" title="COLLECTIONS收藏在哪里">
        COLLECTIONS收藏在哪里
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_fashion:img:潮流的终结？" class="figure" data-float="w33117tlhmf" data-quickopen="true" href="https://v.qq.com/x/cover/mzc00200hfl575r/w33117tlhmf.html" tabindex="-1" target="_blank">
       <img alt="潮流的终结？" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/media_img/lena/PICt62jjt_720_1280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        06:12
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_fashion:title:潮流的终结？" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200hfl575r/w33117tlhmf.html" target="_blank" title="潮流的终结？">
        潮流的终结？
       </a>
       <div class="figure_desc" title="Virgil Abloh的41年人生">
        Virgil Abloh的41年人生
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_fashion:img:程潇职场造型超级美艳" class="figure" data-float="b3311aae3mh" data-quickopen="true" href="https://v.qq.com/x/cover/mzc00200nh7nuoa/b3311aae3mh.html" tabindex="-1" target="_blank">
       <img alt="程潇职场造型超级美艳" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/media_img/lena/PICml888h_720_1280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        01:06
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_fashion:title:程潇职场造型超级美艳" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200nh7nuoa/b3311aae3mh.html" target="_blank" title="程潇职场造型超级美艳">
        程潇职场造型超级美艳
       </a>
       <div class="figure_desc" title="罗云熙程潇演绎悬疑爱恋">
        罗云熙程潇演绎悬疑爱恋
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_fashion:img:鞠婧祎甜美出击活力满分" class="figure" data-float="g33112l0kw7" data-quickopen="true" href="https://v.qq.com/x/cover/mzc002000zy9zga/g33112l0kw7.html" tabindex="-1" target="_blank">
       <img alt="鞠婧祎甜美出击活力满分" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/media_img/lena/PICu998k5_720_1280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        01:04
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_fashion:title:鞠婧祎甜美出击活力满分" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc002000zy9zga/g33112l0kw7.html" target="_blank" title="鞠婧祎甜美出击活力满分">
        鞠婧祎甜美出击活力满分
       </a>
       <div class="figure_desc" title="粉色短裙搭挑染发俏丽甜美">
        粉色短裙搭挑染发俏丽甜美
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_fashion:img:欧阳娜娜：密码211042" class="figure" data-float="s00413qic4k" data-quickopen="true" href="https://v.qq.com/x/page/s00413qic4k.html" tabindex="-1" target="_blank">
       <img alt="欧阳娜娜：密码211042" class="figure_pic" loading="lazy" lz_src="//vfiles.gtimg.cn/vupload/20211125/524a641637831758774.jpg" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        14:59
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_fashion:title:欧阳娜娜：密码211042" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/page/s00413qic4k.html" target="_blank" title="欧阳娜娜：密码211042">
        欧阳娜娜：密码211042
       </a>
       <div class="figure_desc" title="《共同说》第8期">
        《共同说》第8期
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_fashion:img:LV春夏22男装秀" class="figure" href="http://v.qq.com/live/p/topic/131028/index.html" tabindex="-1" target="_blank">
       <img alt="LV春夏22男装秀" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/media_img/lena/PICqgovaj_140_250/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_fashion:title:LV春夏22男装秀" class="figure_title figure_title_two_row bold" href="http://v.qq.com/live/p/topic/131028/index.html" target="_blank" title="LV春夏22男装秀">
        LV春夏22男装秀
       </a>
       <div class="figure_desc" title="直击迈阿密大秀现场">
        直击迈阿密大秀现场
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_fashion:img:深度解析巴黎世家骇客系列" class="figure" data-float="o3310bqqfum" data-quickopen="true" href="https://v.qq.com/x/cover/mzc00200yq88t6t/o3310bqqfum.html" tabindex="-1" target="_blank">
       <img alt="深度解析巴黎世家骇客系列" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/media_img/lena/PIC68j3r7_720_1280/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        11:28
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_fashion:title:深度解析巴黎世家骇客系列" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200yq88t6t/o3310bqqfum.html" target="_blank" title="深度解析巴黎世家骇客系列">
        深度解析巴黎世家骇客系列
       </a>
       <div class="figure_desc" title="时尚史上的最“骚”操作">
        时尚史上的最“骚”操作
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_fashion:img:探索中国时尚新星" class="figure" data-float="i0041djz23v" href="https://v.qq.com/x/cover/mzc0020031zvsko/i0041djz23v.html" tabindex="-1" target="_blank">
       <img alt="探索中国时尚新星" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/media_img/lena/PICq8l9y3_137_256/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        01:42:35
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_fashion:title:探索中国时尚新星" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc0020031zvsko/i0041djz23v.html" target="_blank" title="探索中国时尚新星">
        探索中国时尚新星
       </a>
       <div class="figure_desc" title="NEXT FACE模特大赛总决赛">
        NEXT FACE模特大赛总决赛
       </div>
      </div>
     </div>
    </div>
   </div>
  </div>
  <div _expose="new_vs3_ych" _wind="columnname=精选_音乐·演唱会&amp;controlname=new_vs3_ych" class="mod_row_box" cur-page-num="0" data-context="10" data-istyle="4" has-next-page="false" id="new_vs3_ych">
   <div class="mod_hd">
    <h2 class="mod_title">
     <a _stat="new_vs3_ych:通栏功能区:通栏标题" class="title_link" data-target="_blank" href="https://v.qq.com/channel/music">
      音乐·演唱会
     </a>
    </h2>
    <div class="mod_page_small">
     <button _stat="new_vs3_ych:通栏功能区:上一页" class="btn_prev disabled" title="上一页" wind-click="100">
      <svg class="svg_icon svg_icon_prev" height="10" viewbox="0 0 6 10" width="6">
       <path d="M1.4 4.7L5 1M1.3 5.3L5 9" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="1.4">
       </path>
      </svg>
     </button>
     <span class="page_num" data-count="2" data-info="8 9" data-page="1">
      1/2
     </span>
     <button _stat="new_vs3_ych:通栏功能区:下一页" class="btn_next" title="下一页" wind-click="100">
      <svg class="svg_icon svg_icon_next" height="10" viewbox="0 0 6 10" width="6">
       <path d="M4.6 4.7L1 1M4.7 5.3L1 9" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="1.4">
       </path>
      </svg>
     </button>
    </div>
   </div>
   <div class="mod_bd cf _quickopen _quickopen_duration">
    <div class="mod_figure mod_figure_h_default mod_figure_h_default_1row mod_figure_h_default mod_figure_scroll" data-rowcount="8" data-rowlen="1">
     <div __wind="" class="list_item">
      <a _stat="new_vs3_ych:img:TMEA腾讯音乐娱乐盛典" class="figure" href="http://v.qq.com/live/p/topic/131037/preview.html" tabindex="-1" target="_blank">
       <img alt="TMEA腾讯音乐娱乐盛典" class="figure_pic" loading="lazy" lz_src="//vc.qpic.cn/tpic/mtviuCfJSxnxw/yrfp8434qsdvw318/250" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_ych:title:TMEA腾讯音乐娱乐盛典" class="figure_title figure_title_two_row bold" href="http://v.qq.com/live/p/topic/131037/preview.html" target="_blank" title="TMEA腾讯音乐娱乐盛典">
        TMEA腾讯音乐娱乐盛典
       </a>
       <div class="figure_desc" title="12.11直播·年度音乐盛宴">
        12.11直播·年度音乐盛宴
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_ych:img:相信音乐全系MV来了" class="figure" href="https://v.qq.com/biu/creator/home?vcuid=9000125699" tabindex="-1" target="_blank">
       <img alt="相信音乐全系MV来了" class="figure_pic" loading="lazy" lz_src="//vc.qpic.cn/tpic/mtviuBvrrBn7q/9ryg8277x95tn115/250" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_ych:title:相信音乐全系MV来了" class="figure_title figure_title_two_row bold" href="https://v.qq.com/biu/creator/home?vcuid=9000125699" target="_blank" title="相信音乐全系MV来了">
        相信音乐全系MV来了
       </a>
       <div class="figure_desc" title="五月天、李宗盛等看个够">
        五月天、李宗盛等看个够
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_ych:img:重塑雕像的权利2021上海专场纪录片" class="figure" data-float="w3311yj4noa" href="https://v.qq.com/x/page/w3311yj4noa.html" tabindex="-1" target="_blank">
       <img alt="重塑雕像的权利2021上海专场纪录片" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/qqvideo_ori/0/w3311yj4noa_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        30:42
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_ych:title:重塑雕像的权利2021上海专场纪录片" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/w3311yj4noa.html" target="_blank" title="重塑雕像的权利2021上海专场纪录片">
        重塑雕像的权利2021上海专场纪录片
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_ych:img:陈奕迅献唱英雄联盟动画中文主题曲《孤勇者》" class="figure" data-float="a0041xz6q7o" data-quickopen="true" href="https://v.qq.com/x/page/a0041xz6q7o.html" tabindex="-1" target="_blank">
       <img alt="陈奕迅献唱英雄联盟动画中文主题曲《孤勇者》" class="figure_pic" loading="lazy" lz_src="//vc.qpic.cn/tpic/mtviusj63pJzo/tviusj63AtZb.jpeg/250" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        04:32
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_ych:title:陈奕迅献唱英雄联盟动画中文主题曲《孤勇者》" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/a0041xz6q7o.html" target="_blank" title="陈奕迅献唱英雄联盟动画中文主题曲《孤勇者》">
        陈奕迅献唱英雄联盟动画中文主题曲《孤勇者》
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_ych:img:蔡依林、Steve Aoki，MAX《都没差(Equal In The Darkness)》" class="figure" data-float="o0041zx1gye" data-quickopen="true" href="https://v.qq.com/x/page/o0041zx1gye.html" tabindex="-1" target="_blank">
       <img alt="蔡依林、Steve Aoki，MAX《都没差(Equal In The Darkness)》" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/qqvideo_ori/0/o0041zx1gye_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        03:32
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_ych:title:蔡依林、Steve Aoki，MAX《都没差(Equal In The Darkness)》" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/o0041zx1gye.html" target="_blank" title="蔡依林、Steve Aoki，MAX《都没差(Equal In The Darkness)》">
        蔡依林、Steve Aoki，MAX《都没差(Equal In The Darkness)》
       </a>
       <div class="figure_desc" title="蔡依林、Steve Aoki，MAX新歌《都没差(Equal In The Darkness)》MV首播，以音乐为纽带，打破一切偏见和声音">
        蔡依林、Steve Aoki，MAX新歌《都没差(Equal In The Darkness)》MV首播，以音乐为纽带，打破一切偏见和声音
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_ych:img:交响音诗画·亿万职工心向党" class="figure" data-float="mzc00200rev8kmx" href="https://v.qq.com/x/cover/mzc00200rev8kmx.html" tabindex="-1" target="_blank">
       <img alt="交响音诗画·亿万职工心向党" class="figure_pic" loading="lazy" lz_src="//vc.qpic.cn/tpic/mtviupd3J55xS/tviupd3JfPXE.jpeg/250" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_ych:title:交响音诗画·亿万职工心向党" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200rev8kmx.html" target="_blank" title="交响音诗画·亿万职工心向党">
        交响音诗画·亿万职工心向党
       </a>
       <div class="figure_desc" title="陈思思阎维文致敬劳动者">
        陈思思阎维文致敬劳动者
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_ych:img:孙燕姿《匿名万岁》" class="figure" data-float="z004044em98" data-quickopen="true" href="https://v.qq.com/x/page/z004044em98.html" tabindex="-1" target="_blank">
       <img alt="孙燕姿《匿名万岁》" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/qqvideo_ori/0/z004044em98_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        03:04
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_ych:title:孙燕姿《匿名万岁》" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/page/z004044em98.html" target="_blank" title="孙燕姿《匿名万岁》">
        孙燕姿《匿名万岁》
       </a>
       <div class="figure_desc" title="戏剧化影像折射现实">
        戏剧化影像折射现实
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_ych:img:张杰《安忍》MV" class="figure" data-float="x0040l6bdqz" data-quickopen="true" href="https://v.qq.com/x/page/x0040l6bdqz.html" tabindex="-1" target="_blank">
       <img alt="张杰《安忍》MV" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/qqvideo_ori/0/x0040l6bdqz_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        04:01
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_ych:title:张杰《安忍》MV" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/page/x0040l6bdqz.html" target="_blank" title="张杰《安忍》MV">
        张杰《安忍》MV
       </a>
       <div class="figure_desc" title="传递安忍、追求本心的态度">
        传递安忍、追求本心的态度
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_ych:img:INTO1《风暴眼》首唱会" class="figure" data-float="mzc00200v3drchq" href="https://v.qq.com/x/cover/mzc00200v3drchq.html" tabindex="-1" target="_blank">
       <img alt="INTO1《风暴眼》首唱会" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/vcover_hz_pic/0/mzc00200v3drchq1634282107572/332" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
       <img alt="云首发" class="mark_v mark_v_云首发" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20210121/tag_nor_vip_released_x1_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20210121/tag_nor_vip_released_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_ych:title:INTO1《风暴眼》首唱会" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc00200v3drchq.html" target="_blank" title="INTO1《风暴眼》首唱会">
        INTO1《风暴眼》首唱会
       </a>
       <div class="figure_desc" title="成团首张EP">
        成团首张EP
       </div>
      </div>
     </div>
    </div>
   </div>
  </div>
  <div _expose="new_vs_hot_ent" _wind="columnname=精选_娱乐热点&amp;controlname=new_vs_hot_ent" class="mod_row_box" cur-page-num="0" data-context="10" data-istyle="4" has-next-page="false" id="new_vs_hot_ent">
   <div class="mod_hd">
    <h2 class="mod_title">
     <a _stat="new_vs_hot_ent:通栏功能区:通栏标题" class="title_link" data-target="_blank" href="https://v.qq.com/channel/ent">
      娱乐热点
     </a>
    </h2>
    <div class="mod_page_small none">
     <button _stat="new_vs_hot_ent:通栏功能区:上一页" class="btn_prev disabled" title="上一页" wind-click="100">
      <svg class="svg_icon svg_icon_prev" height="10" viewbox="0 0 6 10" width="6">
       <path d="M1.4 4.7L5 1M1.3 5.3L5 9" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="1.4">
       </path>
      </svg>
     </button>
     <span class="page_num" data-count="1" data-info="8 7" data-page="1">
      1/1
     </span>
     <button _stat="new_vs_hot_ent:通栏功能区:下一页" class="btn_next" title="下一页" wind-click="100">
      <svg class="svg_icon svg_icon_next" height="10" viewbox="0 0 6 10" width="6">
       <path d="M4.6 4.7L1 1M4.7 5.3L1 9" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="1.4">
       </path>
      </svg>
     </button>
    </div>
   </div>
   <div class="mod_bd cf _quickopen _quickopen_duration">
    <div class="mod_figure mod_figure_h_default mod_figure_h_default_1row mod_figure_h_default mod_figure_scroll" data-rowcount="8" data-rowlen="1">
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_ent:img:杨颖：每个年龄段都值得被爱" class="figure" data-float="u3311huzsdj" data-quickopen="true" href="https://v.qq.com/x/page/u3311huzsdj.html" tabindex="-1" target="_blank">
       <img alt="杨颖：每个年龄段都值得被爱" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/qqvideo_ori/0/u3311huzsdj_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        02:30
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_ent:title:杨颖：每个年龄段都值得被爱" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/u3311huzsdj.html" target="_blank" title="杨颖：每个年龄段都值得被爱">
        杨颖：每个年龄段都值得被爱
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_ent:img:国风话剧《鱼玄机》惊艳开演 雨澜熙身兼多职直言挑战多多" class="figure" data-float="o3311gcmg1r" data-quickopen="true" href="https://v.qq.com/x/page/o3311gcmg1r.html" tabindex="-1" target="_blank">
       <img alt="国风话剧《鱼玄机》惊艳开演 雨澜熙身兼多职直言挑战多多" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/qqvideo_ori/0/o3311gcmg1r_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        03:23
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_ent:title:国风话剧《鱼玄机》惊艳开演 雨澜熙身兼多职直言挑战多多" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/o3311gcmg1r.html" target="_blank" title="国风话剧《鱼玄机》惊艳开演 雨澜熙身兼多职直言挑战多多">
        国风话剧《鱼玄机》惊艳开演 雨澜熙身兼多职直言挑战多多
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_ent:img:【腾讯视频娱乐X戏客】祖鹅化身速滑少女，“运动系”女主够燃够热血！" class="figure" data-float="m3310uwd9wp" data-quickopen="true" href="https://v.qq.com/x/page/m3310uwd9wp.html" tabindex="-1" target="_blank">
       <img alt="【腾讯视频娱乐X戏客】祖鹅化身速滑少女，“运动系”女主够燃够热血！" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/qqvideo_ori/0/m3310uwd9wp_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        05:07
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_ent:title:【腾讯视频娱乐X戏客】祖鹅化身速滑少女，“运动系”女主够燃够热血！" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/m3310uwd9wp.html" target="_blank" title="【腾讯视频娱乐X戏客】祖鹅化身速滑少女，“运动系”女主够燃够热血！">
        【腾讯视频娱乐X戏客】祖鹅化身速滑少女，“运动系”女主够燃够热血！
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_ent:img:专访徐开骋：申请把“无趣”加入穷叉叉 自己在剧组是欢乐槽点" class="figure" data-float="l33102weg12" data-quickopen="true" href="https://v.qq.com/x/page/l33102weg12.html" tabindex="-1" target="_blank">
       <img alt="专访徐开骋：申请把“无趣”加入穷叉叉 自己在剧组是欢乐槽点" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/qqvideo_ori/0/l33102weg12_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        07:23
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_ent:title:专访徐开骋：申请把“无趣”加入穷叉叉 自己在剧组是欢乐槽点" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/l33102weg12.html" target="_blank" title="专访徐开骋：申请把“无趣”加入穷叉叉 自己在剧组是欢乐槽点">
        专访徐开骋：申请把“无趣”加入穷叉叉 自己在剧组是欢乐槽点
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_ent:img:探班《超新星运动会》！INTO1米卡对我说“牛哇”！| 桃叨叨vlog" class="figure" data-float="f3309efbsb3" data-quickopen="true" href="https://v.qq.com/x/page/f3309efbsb3.html" tabindex="-1" target="_blank">
       <img alt="探班《超新星运动会》！INTO1米卡对我说“牛哇”！| 桃叨叨vlog" class="figure_pic" loading="lazy" lz_src="//vc.qpic.cn/tpic/mtviuyZwNxbY1/im5p7747yhoq9396/250" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        08:03
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_ent:title:探班《超新星运动会》！INTO1米卡对我说“牛哇”！| 桃叨叨vlog" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/f3309efbsb3.html" target="_blank" title="探班《超新星运动会》！INTO1米卡对我说“牛哇”！| 桃叨叨vlog">
        探班《超新星运动会》！INTO1米卡对我说“牛哇”！| 桃叨叨vlog
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_ent:img:【专访魏晨】和俞灏明二搭？这就是神仙友情吗？" class="figure" data-float="g3310pfeesm" data-quickopen="true" href="https://v.qq.com/x/page/g3310pfeesm.html" tabindex="-1" target="_blank">
       <img alt="【专访魏晨】和俞灏明二搭？这就是神仙友情吗？" class="figure_pic" loading="lazy" lz_src="//vc.qpic.cn/tpic/mtviuy62tjjAL/.jpeg/250" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        08:06
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_ent:title:【专访魏晨】和俞灏明二搭？这就是神仙友情吗？" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/g3310pfeesm.html" target="_blank" title="【专访魏晨】和俞灏明二搭？这就是神仙友情吗？">
        【专访魏晨】和俞灏明二搭？这就是神仙友情吗？
       </a>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs_hot_ent:img:部唠娱专访吴宇恒 | emoji猜成语难度up！“无语哼”叹气~" class="figure" data-float="c3309bs5ia7" data-quickopen="true" href="https://v.qq.com/x/page/c3309bs5ia7.html" tabindex="-1" target="_blank">
       <img alt="部唠娱专访吴宇恒 | emoji猜成语难度up！“无语哼”叹气~" class="figure_pic" loading="lazy" lz_src="//vc.qpic.cn/tpic/mtviuy5eqvCqy/.jpeg/250" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        07:00
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs_hot_ent:title:部唠娱专访吴宇恒 | emoji猜成语难度up！“无语哼”叹气~" class="figure_title figure_title_two_row" href="https://v.qq.com/x/page/c3309bs5ia7.html" target="_blank" title="部唠娱专访吴宇恒 | emoji猜成语难度up！“无语哼”叹气~">
        部唠娱专访吴宇恒 | emoji猜成语难度up！“无语哼”叹气~
       </a>
      </div>
     </div>
    </div>
   </div>
  </div>
  <div _expose="new_vs3_baby" _wind="columnname=精选_母婴常识&amp;controlname=new_vs3_baby" class="mod_row_box" cur-page-num="0" data-context="10" data-istyle="4" has-next-page="false" id="new_vs3_baby">
   <div class="mod_hd">
    <h2 class="mod_title">
     <a _stat="new_vs3_baby:通栏功能区:通栏标题" class="title_link" data-target="_blank" href="https://v.qq.com/channel/baby">
      母婴常识
     </a>
    </h2>
    <div class="mod_page_small">
     <button _stat="new_vs3_baby:通栏功能区:上一页" class="btn_prev disabled" title="上一页" wind-click="100">
      <svg class="svg_icon svg_icon_prev" height="10" viewbox="0 0 6 10" width="6">
       <path d="M1.4 4.7L5 1M1.3 5.3L5 9" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="1.4">
       </path>
      </svg>
     </button>
     <span class="page_num" data-count="2" data-info="8 9" data-page="1">
      1/2
     </span>
     <button _stat="new_vs3_baby:通栏功能区:下一页" class="btn_next" title="下一页" wind-click="100">
      <svg class="svg_icon svg_icon_next" height="10" viewbox="0 0 6 10" width="6">
       <path d="M4.6 4.7L1 1M4.7 5.3L1 9" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="1.4">
       </path>
      </svg>
     </button>
    </div>
   </div>
   <div class="mod_bd cf _quickopen _quickopen_duration">
    <div class="mod_figure mod_figure_h_default mod_figure_h_default_1row mod_figure_h_default mod_figure_scroll" data-rowcount="8" data-rowlen="1">
     <div __wind="" class="list_item">
      <a _stat="new_vs3_baby:img:孩子在幼儿园被孤立" class="figure" data-float="u331107iiik" data-quickopen="true" href="https://v.qq.com/x/page/u331107iiik.html" tabindex="-1" target="_blank">
       <img alt="孩子在幼儿园被孤立" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/qqvideo_ori/0/u331107iiik_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        01:39
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_baby:title:孩子在幼儿园被孤立" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/page/u331107iiik.html" target="_blank" title="孩子在幼儿园被孤立">
        孩子在幼儿园被孤立
       </a>
       <div class="figure_desc" title="妈妈的做法很关键">
        妈妈的做法很关键
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_baby:img:当妈不想听的话" class="figure" data-float="f3311rn5708" data-quickopen="true" href="https://v.qq.com/x/page/f3311rn5708.html" tabindex="-1" target="_blank">
       <img alt="当妈不想听的话" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/qqvideo_ori/0/f3311rn5708_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        06:30
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_baby:title:当妈不想听的话" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/page/f3311rn5708.html" target="_blank" title="当妈不想听的话">
        当妈不想听的话
       </a>
       <div class="figure_desc" title="孩子睡了你就睡❗️">
        孩子睡了你就睡❗️
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_baby:img:老酸奶比普通酸奶更有营养？" class="figure" data-float="e33112jbncg" data-quickopen="true" href="https://v.qq.com/x/page/e33112jbncg.html" tabindex="-1" target="_blank">
       <img alt="老酸奶比普通酸奶更有营养？" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/qqvideo_ori/0/e33112jbncg_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        00:43
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_baby:title:老酸奶比普通酸奶更有营养？" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/page/e33112jbncg.html" target="_blank" title="老酸奶比普通酸奶更有营养？">
        老酸奶比普通酸奶更有营养？
       </a>
       <div class="figure_desc" title="宝妈们怎么看？">
        宝妈们怎么看？
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_baby:img:孩子每次玩玩具都不收拾？" class="figure" data-float="s3311dp9yq3" data-quickopen="true" href="https://v.qq.com/x/page/s3311dp9yq3.html" tabindex="-1" target="_blank">
       <img alt="孩子每次玩玩具都不收拾？" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/qqvideo_ori/0/s3311dp9yq3_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        00:43
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_baby:title:孩子每次玩玩具都不收拾？" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/page/s3311dp9yq3.html" target="_blank" title="孩子每次玩玩具都不收拾？">
        孩子每次玩玩具都不收拾？
       </a>
       <div class="figure_desc" title="教你一招搞定孩子不爱收拾的“坏毛病”！">
        教你一招搞定孩子不爱收拾的“坏毛病”！
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_baby:img:冰雪故事绘本《期待冬奥会》" class="figure" data-float="g3311nwfvu2" data-quickopen="true" href="https://v.qq.com/x/page/g3311nwfvu2.html" tabindex="-1" target="_blank">
       <img alt="冰雪故事绘本《期待冬奥会》" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/qqvideo_ori/0/g3311nwfvu2_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        00:39
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_baby:title:冰雪故事绘本《期待冬奥会》" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/page/g3311nwfvu2.html" target="_blank" title="冰雪故事绘本《期待冬奥会》">
        冰雪故事绘本《期待冬奥会》
       </a>
       <div class="figure_desc" title="一起为北京2022冬奥加油！">
        一起为北京2022冬奥加油！
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_baby:img:5款益智又好玩的玩具已选好" class="figure" data-float="s3310edgg0l" href="https://v.qq.com/x/page/s3310edgg0l.html" tabindex="-1" target="_blank">
       <img alt="5款益智又好玩的玩具已选好" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/qqvideo_ori/0/s3310edgg0l_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_baby:title:5款益智又好玩的玩具已选好" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/page/s3310edgg0l.html" target="_blank" title="5款益智又好玩的玩具已选好">
        5款益智又好玩的玩具已选好
       </a>
       <div class="figure_desc" title="【好物清单】get同款吧！">
        【好物清单】get同款吧！
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_baby:img:给孩子取个一生受益的名字" class="figure" data-float="f3311x5oqe0" data-quickopen="true" href="https://v.qq.com/x/page/f3311x5oqe0.html" tabindex="-1" target="_blank">
       <img alt="给孩子取个一生受益的名字" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/qqvideo_ori/0/f3311x5oqe0_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        03:34
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_baby:title:给孩子取个一生受益的名字" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/page/f3311x5oqe0.html" target="_blank" title="给孩子取个一生受益的名字">
        给孩子取个一生受益的名字
       </a>
       <div class="figure_desc" title="4个技巧【必看】">
        4个技巧【必看】
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_baby:img:魔术玩具开箱！" class="figure" data-float="m3311nfmyth" data-quickopen="true" href="https://v.qq.com/x/page/m3311nfmyth.html" tabindex="-1" target="_blank">
       <img alt="魔术玩具开箱！" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/qqvideo_ori/0/m3311nfmyth_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        03:06
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_baby:title:魔术玩具开箱！" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/page/m3311nfmyth.html" target="_blank" title="魔术玩具开箱！">
        魔术玩具开箱！
       </a>
       <div class="figure_desc" title="亲戚朋友面前就可以露一手！">
        亲戚朋友面前就可以露一手！
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_baby:img:孕吐很正常？" class="figure" data-float="c3311dod9sh" data-quickopen="true" href="https://v.qq.com/x/page/c3311dod9sh.html" tabindex="-1" target="_blank">
       <img alt="孕吐很正常？" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo_ori/0/c3311dod9sh_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        04:25
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_baby:title:孕吐很正常？" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/page/c3311dod9sh.html" target="_blank" title="孕吐很正常？">
        孕吐很正常？
       </a>
       <div class="figure_desc" title="别把孕吐不当回事！">
        别把孕吐不当回事！
       </div>
      </div>
     </div>
    </div>
   </div>
  </div>
  <div _expose="new_vs3_star" _wind="columnname=精选_星座聚焦&amp;controlname=new_vs3_star" class="mod_row_box" cur-page-num="0" data-context="11" data-istyle="4" has-next-page="false" id="new_vs3_star">
   <div class="mod_hd">
    <h2 class="mod_title">
     <a _stat="new_vs3_star:通栏功能区:通栏标题" class="title_link" data-target="_blank" href="http://v.qq.com/x/channel/astro">
      星座聚焦
     </a>
    </h2>
    <div class="mod_page_small">
     <button _stat="new_vs3_star:通栏功能区:上一页" class="btn_prev disabled" title="上一页" wind-click="100">
      <svg class="svg_icon svg_icon_prev" height="10" viewbox="0 0 6 10" width="6">
       <path d="M1.4 4.7L5 1M1.3 5.3L5 9" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="1.4">
       </path>
      </svg>
     </button>
     <span class="page_num" data-count="2" data-info="8 11" data-page="1">
      1/2
     </span>
     <button _stat="new_vs3_star:通栏功能区:下一页" class="btn_next" title="下一页" wind-click="100">
      <svg class="svg_icon svg_icon_next" height="10" viewbox="0 0 6 10" width="6">
       <path d="M4.6 4.7L1 1M4.7 5.3L1 9" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="1.4">
       </path>
      </svg>
     </button>
    </div>
   </div>
   <div class="mod_bd cf _quickopen _quickopen_duration">
    <div class="mod_figure mod_figure_h_default mod_figure_h_default_1row mod_figure_h_default mod_figure_scroll" data-rowcount="8" data-rowlen="1">
     <div __wind="" class="list_item">
      <a _stat="new_vs3_star:img:虎虎生威大师季-滴天居士" class="figure" data-float="e0041mzocfy" href="https://v.qq.com/x/page/e0041mzocfy.html" tabindex="-1" target="_blank">
       <img alt="虎虎生威大师季-滴天居士" class="figure_pic" loading="lazy" lz_src="//vc.qpic.cn/tpic/mtviuCevoMKo1/sjjv8429ffuks844/250" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        25:46
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_star:title:虎虎生威大师季-滴天居士" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/page/e0041mzocfy.html" target="_blank" title="虎虎生威大师季-滴天居士">
        虎虎生威大师季-滴天居士
       </a>
       <div class="figure_desc" title="虎年生肖财富运">
        虎年生肖财富运
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_star:img:呦呦说星相" class="figure" data-float="j0041ixp1bq" data-quickopen="true" href="https://v.qq.com/x/page/j0041ixp1bq.html" tabindex="-1" target="_blank">
       <img alt="呦呦说星相" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/qqvideo_ori/0/j0041ixp1bq_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        02:49
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_star:title:呦呦说星相" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/page/j0041ixp1bq.html" target="_blank" title="呦呦说星相">
        呦呦说星相
       </a>
       <div class="figure_desc" title="12月4日射手座日食">
        12月4日射手座日食
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_star:img:星座呦呦秀" class="figure" data-float="o331070ui8g" data-quickopen="true" href="https://v.qq.com/x/page/o331070ui8g.html" tabindex="-1" target="_blank">
       <img alt="星座呦呦秀" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/qqvideo_ori/0/o331070ui8g_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        12:20
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_star:title:星座呦呦秀" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/page/o331070ui8g.html" target="_blank" title="星座呦呦秀">
        星座呦呦秀
       </a>
       <div class="figure_desc" title="星座高质量伴侣之“心动的恋爱”">
        星座高质量伴侣之“心动的恋爱”
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_star:img:虎虎生威大师季-方杖" class="figure" data-float="mzc002002c209d7" href="https://v.qq.com/x/cover/mzc002002c209d7.html" tabindex="-1" target="_blank">
       <img alt="虎虎生威大师季-方杖" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/vcover_hz_pic/0/gu4b63v2hvzms6m/332" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
       </div>
       <img alt="VIP" class="mark_v mark_v_VIP" loading="lazy" onerror="picerr(this)" src="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x1.png" srcset="//vfiles-raw.gtimg.cn/vupload/20201015/tag_vip_x2.png 2x"/>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_star:title:虎虎生威大师季-方杖" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/cover/mzc002002c209d7.html" target="_blank" title="虎虎生威大师季-方杖">
        虎虎生威大师季-方杖
       </a>
       <div class="figure_desc" title="四象法则解析2022十二星座整体运势">
        四象法则解析2022十二星座整体运势
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_star:img:星座狗联盟" class="figure" data-float="h33119o0qtg" data-quickopen="true" href="https://v.qq.com/x/page/h33119o0qtg.html" tabindex="-1" target="_blank">
       <img alt="星座狗联盟" class="figure_pic" loading="lazy" lz_src="//vc.qpic.cn/tpic/mtviuCeHcrUsC/rn8584309xfnb907/250" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        00:32
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_star:title:星座狗联盟" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/page/h33119o0qtg.html" target="_blank" title="星座狗联盟">
        星座狗联盟
       </a>
       <div class="figure_desc" title="男生和女生看电视的区别">
        男生和女生看电视的区别
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_star:img:南翌说风水" class="figure" data-float="w33084193w6" data-quickopen="true" href="https://v.qq.com/x/page/w33084193w6.html" tabindex="-1" target="_blank">
       <img alt="南翌说风水" class="figure_pic" loading="lazy" lz_src="//vc.qpic.cn/tpic/mtviuBHaNqpgN/k67j8319jya73702/250" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        02:29
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_star:title:南翌说风水" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/page/w33084193w6.html" target="_blank" title="南翌说风水">
        南翌说风水
       </a>
       <div class="figure_desc" title="风水大师最怕的7种“风水绝地”">
        风水大师最怕的7种“风水绝地”
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_star:img:星座蛙" class="figure" data-float="f3311xb9m78" data-quickopen="true" href="https://v.qq.com/x/page/f3311xb9m78.html" tabindex="-1" target="_blank">
       <img alt="星座蛙" class="figure_pic" loading="lazy" lz_src="//vc.qpic.cn/tpic/mtviuyyFrRFmL/2z8o8171c4rm6995/250" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        01:47
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_star:title:星座蛙" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/page/f3311xb9m78.html" target="_blank" title="星座蛙">
        星座蛙
       </a>
       <div class="figure_desc" title="蛙叔讲本周十二星座周运势">
        蛙叔讲本周十二星座周运势
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_star:img:陈茂源" class="figure" data-float="y33099ygach" data-quickopen="true" href="https://v.qq.com/x/page/y33099ygach.html" tabindex="-1" target="_blank">
       <img alt="陈茂源" class="figure_pic" loading="lazy" lz_src="//vc.qpic.cn/tpic/mtviuAVRG5Bt7/843c8155q8ago286/250" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        07:02
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_star:title:陈茂源" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/page/y33099ygach.html" target="_blank" title="陈茂源">
        陈茂源
       </a>
       <div class="figure_desc" title="白羊座有哪些怪癖？">
        白羊座有哪些怪癖？
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_star:img:语漫天" class="figure" data-float="i3309iyot54" data-quickopen="true" href="https://v.qq.com/x/page/i3309iyot54.html" tabindex="-1" target="_blank">
       <img alt="语漫天" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo_ori/0/i3309iyot54_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        00:24
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_star:title:语漫天" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/page/i3309iyot54.html" target="_blank" title="语漫天">
        语漫天
       </a>
       <div class="figure_desc" title="拉黑一个人毁掉一段情的水瓶">
        拉黑一个人毁掉一段情的水瓶
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_star:img:星座不求人" class="figure" data-float="a33069hw58d" data-quickopen="true" href="https://v.qq.com/x/page/a33069hw58d.html" tabindex="-1" target="_blank">
       <img alt="星座不求人" class="figure_pic" loading="lazy" lz_next="//vc.qpic.cn/tpic/mtviuqGVykB8N/tviuqGVywmxA.jpeg/250" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        02:16
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_star:title:星座不求人" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/page/a33069hw58d.html" target="_blank" title="星座不求人">
        星座不求人
       </a>
       <div class="figure_desc" title="分手后如何确定天秤座是否想复合">
        分手后如何确定天秤座是否想复合
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_star:img:凤影焰" class="figure" data-float="d3306l47ynp" href="https://v.qq.com/x/page/d3306l47ynp.html" tabindex="-1" target="_blank">
       <img alt="凤影焰" class="figure_pic" loading="lazy" lz_next="//vc.qpic.cn/tpic/mtviurVEYuMaj/tviurVEYA9Sd.jpeg/250" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        31:44
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_star:title:凤影焰" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/page/d3306l47ynp.html" target="_blank" title="凤影焰">
        凤影焰
       </a>
       <div class="figure_desc" title="2021年11月十二星座运势">
        2021年11月十二星座运势
       </div>
      </div>
     </div>
    </div>
   </div>
  </div>
  <div _expose="new_vs3_auto" _wind="columnname=精选_汽车资讯&amp;controlname=new_vs3_auto" class="mod_row_box" cur-page-num="0" data-context="11" data-istyle="4" has-next-page="false" id="new_vs3_auto">
   <div class="mod_hd">
    <h2 class="mod_title">
     <a _stat="new_vs3_auto:通栏功能区:通栏标题" class="title_link" data-target="_blank" href="https://v.qq.com/channel/auto">
      汽车资讯
     </a>
    </h2>
    <div class="mod_page_small">
     <button _stat="new_vs3_auto:通栏功能区:上一页" class="btn_prev disabled" title="上一页" wind-click="100">
      <svg class="svg_icon svg_icon_prev" height="10" viewbox="0 0 6 10" width="6">
       <path d="M1.4 4.7L5 1M1.3 5.3L5 9" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="1.4">
       </path>
      </svg>
     </button>
     <span class="page_num" data-count="2" data-info="8 9" data-page="1">
      1/2
     </span>
     <button _stat="new_vs3_auto:通栏功能区:下一页" class="btn_next" title="下一页" wind-click="100">
      <svg class="svg_icon svg_icon_next" height="10" viewbox="0 0 6 10" width="6">
       <path d="M4.6 4.7L1 1M4.7 5.3L1 9" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="1.4">
       </path>
      </svg>
     </button>
    </div>
   </div>
   <div class="mod_bd cf _quickopen _quickopen_duration">
    <div class="mod_figure mod_figure_h_default mod_figure_h_default_1row mod_figure_h_default mod_figure_scroll" data-rowcount="8" data-rowlen="1">
     <div __wind="" class="list_item">
      <a _stat="new_vs3_auto:img:试驾一汽丰田-亚洲狮" class="figure" data-float="t3244ly7kdr" data-quickopen="true" href="https://v.qq.com/x/page/t3244ly7kdr.html" tabindex="-1" target="_blank">
       <img alt="试驾一汽丰田-亚洲狮" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/qqvideo_ori/0/t3244ly7kdr_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        06:14
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_auto:title:试驾一汽丰田-亚洲狮" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/page/t3244ly7kdr.html" target="_blank" title="试驾一汽丰田-亚洲狮">
        试驾一汽丰田-亚洲狮
       </a>
       <div class="figure_desc" title="搭2.0L+CVT">
        搭2.0L+CVT
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_auto:img:体验ARCFOX极狐阿尔法T" class="figure" data-float="z3244n22fll" data-quickopen="true" href="https://v.qq.com/x/page/z3244n22fll.html" tabindex="-1" target="_blank">
       <img alt="体验ARCFOX极狐阿尔法T" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/qqvideo_ori/0/z3244n22fll_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        05:58
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_auto:title:体验ARCFOX极狐阿尔法T" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/page/z3244n22fll.html" target="_blank" title="体验ARCFOX极狐阿尔法T">
        体验ARCFOX极狐阿尔法T
       </a>
       <div class="figure_desc" title="逃离城市体验高品质生活">
        逃离城市体验高品质生活
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_auto:img:169马力+全时四驱30万出头？" class="figure" data-float="z32442ne73d" data-quickopen="true" href="https://v.qq.com/x/page/z32442ne73d.html" tabindex="-1" target="_blank">
       <img alt="169马力+全时四驱30万出头？" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/qqvideo_ori/0/z32442ne73d_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        12:12
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_auto:title:169马力+全时四驱30万出头？" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/page/z32442ne73d.html" target="_blank" title="169马力+全时四驱30万出头？">
        169马力+全时四驱30万出头？
       </a>
       <div class="figure_desc" title="这台SUV不一般！">
        这台SUV不一般！
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_auto:img:觉得特斯拉Model 3无敌？" class="figure" data-float="a3244o34iix" data-quickopen="true" href="https://v.qq.com/x/page/a3244o34iix.html" tabindex="-1" target="_blank">
       <img alt="觉得特斯拉Model 3无敌？" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/qqvideo_ori/0/a3244o34iix_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        12:05
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_auto:title:觉得特斯拉Model 3无敌？" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/page/a3244o34iix.html" target="_blank" title="觉得特斯拉Model 3无敌？">
        觉得特斯拉Model 3无敌？
       </a>
       <div class="figure_desc" title="来看看什么才叫性能车！">
        来看看什么才叫性能车！
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_auto:img:第七代伊兰特要啥有啥" class="figure" data-float="s3244lqysqd" data-quickopen="true" href="https://v.qq.com/x/page/s3244lqysqd.html" tabindex="-1" target="_blank">
       <img alt="第七代伊兰特要啥有啥" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/qqvideo_ori/0/s3244lqysqd_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        10:08
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_auto:title:第七代伊兰特要啥有啥" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/page/s3244lqysqd.html" target="_blank" title="第七代伊兰特要啥有啥">
        第七代伊兰特要啥有啥
       </a>
       <div class="figure_desc" title="10万家轿别只看轩逸卡罗拉">
        10万家轿别只看轩逸卡罗拉
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_auto:img:抢先试驾优雅运动家" class="figure" data-float="c324346wymw" href="https://v.qq.com/x/page/c324346wymw.html" tabindex="-1" target="_blank">
       <img alt="抢先试驾优雅运动家" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/qqvideo_ori/0/c324346wymw_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        23:25
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_auto:title:抢先试驾优雅运动家" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/page/c324346wymw.html" target="_blank" title="抢先试驾优雅运动家">
        抢先试驾优雅运动家
       </a>
       <div class="figure_desc" title="捷尼赛思G80与捷尼赛思GV80">
        捷尼赛思G80与捷尼赛思GV80
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_auto:img:揭秘美国最大的“汽车坟场”" class="figure" data-float="u3243czliey" data-quickopen="true" href="https://v.qq.com/x/page/u3243czliey.html" tabindex="-1" target="_blank">
       <img alt="揭秘美国最大的“汽车坟场”" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/qqvideo_ori/0/u3243czliey_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        08:19
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_auto:title:揭秘美国最大的“汽车坟场”" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/page/u3243czliey.html" target="_blank" title="揭秘美国最大的“汽车坟场”">
        揭秘美国最大的“汽车坟场”
       </a>
       <div class="figure_desc" title="一千买奔驰，两千买玛莎">
        一千买奔驰，两千买玛莎
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_auto:img:试驾奥迪RS7" class="figure" data-float="v3243xnujux" href="https://v.qq.com/x/page/v3243xnujux.html" tabindex="-1" target="_blank">
       <img alt="试驾奥迪RS7" class="figure_pic" loading="lazy" lz_src="//puui.qpic.cn/qqvideo_ori/0/v3243xnujux_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        19:49
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_auto:title:试驾奥迪RS7" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/page/v3243xnujux.html" target="_blank" title="试驾奥迪RS7">
        试驾奥迪RS7
       </a>
       <div class="figure_desc" title="性能玩家的最终归宿？">
        性能玩家的最终归宿？
       </div>
      </div>
     </div>
     <div __wind="" class="list_item">
      <a _stat="new_vs3_auto:img:宝马7系耀影特别版上市" class="figure" data-float="r3240wvltqf" data-quickopen="true" href="https://v.qq.com/x/page/r3240wvltqf.html" tabindex="-1" target="_blank">
       <img alt="宝马7系耀影特别版上市" class="figure_pic" loading="lazy" lz_next="//puui.qpic.cn/qqvideo_ori/0/r3240wvltqf_360_204/0" onerror="picerr(this,'h')" src="//puui.qpic.cn/vupload/0/common_pic_h.png/0"/>
       <div class="figure_caption">
        01:35
       </div>
      </a>
      <div class="figure_detail figure_detail_two_row">
       <a _stat="new_vs3_auto:title:宝马7系耀影特别版上市" class="figure_title figure_title_two_row bold" href="https://v.qq.com/x/page/r3240wvltqf.html" target="_blank" title="宝马7系耀影特别版上市">
        宝马7系耀影特别版上市
       </a>
       <div class="figure_desc" title="全球限量25台">
        全球限量25台
       </div>
      </div>
     </div>
    </div>
   </div>
  </div>
  <div _expose="ad_qll_width3" class="mod_row_box mod_row_box_special mod_row_box_ad" data-context="11" data-istyle="11" id="ad_qll_width3">
   <div _stat="ad_qll_width3:ad_l" class="mod_ad_main">
    <!--$loc$_div AD begin...."l=$loc$&log=off"-->
    <div class="l_qq_com" data-index="3" data-loc="QQlive_SP_QLL_Width" id="QQlive_SP_QLL_Width:3" style="width:960px;height:90px;">
    </div>
    <!--$loc$ AD end -->
    <!--[if !IE]>|xGv00|251758c0dec2c53d7bd30780b2b6da5b<![endif]-->
   </div>
   <div _stat="ad_qll_width3:ad_r" class="mod_ad_side">
    <a class="ad1" href="https://v.qq.com/x/cover/vbb35hm6m6da1wc.html" target="_blank">
     <img loading="lazy" lz_src="//puui.qpic.cn/tv/0/151620538_73090/0" src="//puui.qpic.cn/vupload/0/common_blank.png/0"/>
    </a>
    <a class="ad2" href="https://v.qq.com/x/cover/vbb35hm6m6da1wc.html" target="_blank">
     <img loading="lazy" lz_src="//puui.qpic.cn/tv/0/151620545/0" src="//puui.qpic.cn/vupload/0/common_blank.png/0"/>
    </a>
    <a class="ad3" href="https://v.qq.com/x/cover/vbb35hm6m6da1wc.html" target="_blank">
     <img loading="lazy" lz_src="//puui.qpic.cn/tv/0/151620541/0" src="//puui.qpic.cn/vupload/0/common_blank.png/0"/>
    </a>
   </div>
  </div>
  <meta charset="utf-8"/>
  <link href="//vm.gtimg.cn/tencentvideo/vstyle/web/v6/style/css/footer.css" rel="stylesheet"/>
  <!--[if lte IE 9 ]>
<link rel="stylesheet" href="//vm.gtimg.cn/tencentvideo/vstyle/web/v6/style/css/footer.ie.css" />
<![endif]-->
  <div class="site_footer">
   <div class="mod_footer_contentinfo cf __lite_hide__">
    <div class="contentinfo_column contentinfo_channel">
     <div class="contentinfo_title">
      热门频道
     </div>
     <div class="contentinfo_ul">
      <div class="foot_item">
       <a _stat="page_footer:channel_1" class="foot_link" href="https://v.qq.com/tv" target="_blank" title="电视剧">
        电视剧
       </a>
      </div>
      <div class="foot_item">
       <a _stat="page_footer:channel_2" class="foot_link" href="https://v.qq.com/variety" target="_blank" title="综艺">
        综艺
       </a>
      </div>
      <div class="foot_item">
       <a _stat="page_footer:channel_3" class="foot_link" href="https://v.qq.com/movie" target="_blank" title="电影">
        电影
       </a>
      </div>
      <div class="foot_item">
       <a _stat="page_footer:channel_4" class="foot_link" href="https://v.qq.com/channel/nba" target="_blank" title="NBA">
        NBA
       </a>
      </div>
      <div class="foot_item">
       <a _stat="page_footer:channel_5" class="foot_link" href="https://v.qq.com/fun" target="_blank" title="搞笑">
        搞笑
       </a>
      </div>
      <div class="foot_item">
       <a _stat="page_footer:channel_6" class="foot_link" href="https://v.qq.com/channel/music" target="_blank" title="音乐">
        音乐
       </a>
      </div>
      <div class="foot_item">
       <a _stat="page_footer:channel_7" class="foot_link" href="https://v.qq.com/ent" target="_blank" title="娱乐">
        娱乐
       </a>
      </div>
      <div class="foot_item">
       <a _stat="page_footer:channel_8" class="foot_link" href="https://v.qq.com/cartoon" target="_blank" title="动漫">
        动漫
       </a>
      </div>
      <div class="foot_item">
       <a _stat="page_footer:channel_9" class="foot_link" href="http://v.qq.com/games/" target="_blank" title="游戏">
        游戏
       </a>
      </div>
      <div class="foot_item">
       <a _stat="page_footer:channel_10" class="foot_link" href="https://film.qq.com" target="_blank" title="VIP影院">
        VIP影院
       </a>
      </div>
      <div class="foot_item">
       <a _stat="page_footer:channel_11" class="foot_link" href="https://v.qq.com/channel/usuk" target="_blank" title="海外剧">
        海外剧
       </a>
      </div>
      <div class="foot_item">
       <a _stat="page_footer:channel_12" class="foot_link" href="https://v.qq.com/channel/doco" target="_blank" title="纪录片">
        纪录片
       </a>
      </div>
      <div class="foot_item">
       <a _stat="page_footer:channel_13" class="foot_link" href="https://v.qq.com/news" target="_blank" title="新闻">
        新闻
       </a>
      </div>
      <div class="foot_item">
       <a _stat="page_footer:channel_14" class="foot_link" href="https://v.qq.com/life" target="_blank" title="生活">
        生活
       </a>
      </div>
      <div class="foot_item">
       <a _stat="page_footer:channel_15" class="foot_link" href="https://v.qq.com/channel/sports_new" target="_blank" title="体育">
        体育
       </a>
      </div>
     </div>
    </div>
    <div class="contentinfo_column contentinfo_feature">
     <div class="contentinfo_title">
      特色推荐
     </div>
     <div class="contentinfo_ul">
      <div class="foot_item">
       <a _stat="page_footer:rec_1" class="foot_link" href="https://v.qq.com/channel/dv" target="_blank" title="自制电影">
        自制电影
       </a>
      </div>
      <div class="foot_item">
       <a _stat="page_footer:rec_2" class="foot_link" href="https://guanjia.qq.com/?ADTAG=media.buy.sogo.SEO8&amp;type=1" target="_blank" title="杀毒软件">
        杀毒软件
       </a>
      </div>
     </div>
    </div>
    <div class="contentinfo_column contentinfo_download">
     <div class="contentinfo_title">
      软件下载
     </div>
     <div class="dl_list">
      <a _stat="page_footer:download_1" class="item" href="https://v.qq.com/biu/download#iPhone" target="_blank">
       <svg class="svg_icon svg_icon_iphone" height="50" viewbox="0 0 50 50" width="50">
        <path d="M34 3h-18c-1.657 0-3 1.343-3 3v38c0 1.657 1.343 3 3 3h18c1.657 0 3-1.343 3-3v-38c0-1.657-1.343-3-3-3zm1 38h-20v-32h20v32z">
        </path>
        <!--[if lte IE 8 ]><image src="//puui.qpic.cn/vupload/0/20190105_svg_icon_iphone.png/0" xlink:href="" /><![endif]-->
       </svg>
       <span class="text_icon">
        手机版
       </span>
      </a>
      <a _stat="page_footer:download_2" class="item" href="https://v.qq.com/biu/download#Windows" target="_blank">
       <svg class="svg_icon svg_icon_win" height="50" viewbox="0 0 50 50" width="50">
        <path d="M7 23.977l13.282-.176v-14.384l-13.282 2.286v12.274zm15.953-15.02v14.809l20.047-.266v-17.993l-20.047 3.45zm-15.953 29.339l13.282 2.286v-14.383l-13.282-.176v12.273zm15.953 2.746l20.047 3.451v-17.994l-20.047-.265v14.808z">
        </path>
        <!--[if lte IE 8 ]><image src="//puui.qpic.cn/vupload/0/20190105_svg_icon_win.png/0" xlink:href="" /><![endif]-->
       </svg>
       <span class="text_icon">
        Windows版
       </span>
      </a>
      <a _stat="page_footer:download_3" class="item" href="https://v.qq.com/biu/download#Mac" target="_blank">
       <svg class="svg_icon svg_icon_mac" height="50" viewbox="0 0 50 50" width="50">
        <path d="M42.705 17.437c-2.28-2.958-5.474-4.671-8.49-4.671-3.99 0-5.675 1.976-8.454 1.976-2.85 0-5.022-1.964-8.478-1.964-3.384 0-6.993 2.143-9.285 5.796-3.218 5.15-2.672 14.85 2.541 23.114 1.864 2.958 4.358 6.275 7.623 6.312h.06c2.838 0 3.681-1.928 7.587-1.952h.06c3.847 0 4.619 1.94 7.445 1.94h.059c3.265-.036 5.889-3.713 7.753-6.659 1.342-2.12 1.84-3.185 2.873-5.581-7.54-2.97-8.751-14.059-1.294-18.311zm-18.155-4.371c2.529 0 5.118-1.581 6.625-3.605 1.461-1.928 2.565-4.658 2.162-7.461-2.375.168-5.141 1.736-6.768 3.784-1.472 1.856-2.683 4.611-2.208 7.282h.189z">
        </path>
        <!--[if lte IE 8 ]><image src="//puui.qpic.cn/vupload/0/20190105_svg_icon_mac.png/0" xlink:href="" /><![endif]-->
       </svg>
       <span class="text_icon">
        Mac版
       </span>
      </a>
      <a _stat="page_footer:download_4" class="item" href="https://v.qq.com/biu/download#Pad" target="_blank">
       <svg class="svg_icon svg_icon_ipad" height="50" viewbox="0 0 50 50" width="50">
        <path d="M46 8h-42c-1.657 0-3 1.343-3 3v28c0 1.657 1.343 3 3 3h42c1.657 0 3-1.343 3-3v-28c0-1.657-1.343-3-3-3zm-2 32h-38v-30h38v30z">
        </path>
        <!--[if lte IE 8 ]><image src="//puui.qpic.cn/vupload/0/20190105_svg_icon_ipad.png/0" xlink:href="" /><![endif]-->
       </svg>
       <span class="text_icon">
        iPad版
       </span>
      </a>
      <a _stat="page_footer:download_5" class="item" href="https://v.qq.com/biu/download#TV" target="_blank">
       <svg class="svg_icon svg_icon_tv" height="50" viewbox="0 0 50 50" width="50">
        <path d="M2 11h44v10h2v-11c0-.552-.448-1-1-1h-46c-.552 0-1 .448-1 1v27c0 .552.448 1 1 1h11v2c0 .552.448 1 1 1h22c.552 0 1-.448 1-1v-2h4v-2h-38v-25zm46 12h-4c-1.105 0-2 .895-2 2v14c0 1.105.895 2 2 2h4c1.105 0 2-.895 2-2v-14c0-1.105-.895-2-2-2zm-2 13c-1.657 0-3-1.343-3-3s1.343-3 3-3 3 1.343 3 3-1.343 3-3 3zm0-5c-1.105 0-2 .895-2 2s.895 2 2 2 2-.895 2-2-.895-2-2-2z">
        </path>
        <!--[if lte IE 8 ]><image src="//puui.qpic.cn/vupload/0/20190105_svg_icon_tv.png/0" xlink:href="" /><![endif]-->
       </svg>
       <span class="text_icon">
        TV版
       </span>
      </a>
     </div>
    </div>
    <div class="contentinfo_column contentinfo_service">
     <div class="contentinfo_title">
      服务
     </div>
     <div class="service-content">
      <div class="contentinfo_ul left">
       <div class="foot_item">
        <a _stat="page_footer:service_1" class="foot_link" data-query="undefined" href="http://kf.qq.com/product/QQlive.html" target="_blank" title="客服">
         客服
        </a>
       </div>
       <div class="foot_item">
        <a _stat="page_footer:service_2" class="foot_link" data-query="data=NHSl1WvfqEi%2BdmRYiwgwJOsLD%2F1x7stUBmO2vO9239NG%2BhmriCxlu3v4l2%2FiBr0J24kWGBFUPo6YkIH6QX9HYw7ibxWrGGLx9fq%2FFHSk0nAFVrMXY7rPjYLeuTZ5t2CC0ZOg%2FlmIlt5RYvCT%2Bob%2FfJntbMDr6Fh6NPEwuKU1twl8N0FI9q0qZa%2B4SbWTNIPtUVODRHclewGGunqawIC9pAi%2ByUU2Dq2QRcia3VmBFX%2BkLO4cwyDrJItz0EXSVexEOf721gm49uw7ZOVo2ci8Edc6NuEtCoiNFb3a96jnjeqb7jJ6UvmaaE5kOGVYYTDouMBA3VRT11n2jcc69pDxgg%3D%3D&amp;appid=843a3ae2a1&amp;pid=1" href="javascript:toast();" target="" title="反馈">
         反馈
        </a>
       </div>
       <div class="foot_item">
        <a _stat="page_footer:service_3" class="foot_link" data-query="undefined" href="https://v.qq.com/biu/tort" target="_blank" title="侵权投诉">
         侵权投诉
        </a>
       </div>
       <div class="foot_item">
        <a _stat="page_footer:service_4" class="foot_link" data-query="undefined" href="https://v.qq.com/open/" target="_blank" title="免广告合作">
         免广告合作
        </a>
       </div>
       <div class="foot_item">
        <a _stat="page_footer:service_5" class="foot_link" data-query="undefined" href="https://dcm.qq.com/txsp.html#/" target="_blank" title="VIP采购">
         VIP采购
        </a>
       </div>
       <div class="foot_item">
        <a class="foot_link" href="https://privacy.qq.com/document/preview/3fab9c7fc1424ebda42c3ce488322c8a" target="_blank" title="腾讯视频隐私保护指引">
         腾讯视频隐私保护指引
        </a>
       </div>
      </div>
      <div class="contentinfo_ul right">
       <div class="foot_item">
        <a class="foot_link" href="https://privacy.qq.com/document/priview/7900b34b6f8248e08313cf3f1899ea37/8.3.00.21753" target="_blank" title="腾讯视频第三方SDK目录">
         腾讯视频第三方SDK目录
        </a>
       </div>
       <div class="foot_item">
        <a class="foot_link" href="https://privacy.qq.com/document/preview/ba4294dc9d4a45a89f3d682eb07a489b" target="_blank" title="腾讯视频第三方信息共享清单">
         腾讯视频第三方信息共享清单
        </a>
       </div>
       <div class="foot_item">
        <a class="foot_link" href="https://privacy.qq.com/document/preview/18f3ac8cb4364ed8b2ba596a9bfe3111" target="_blank" title="腾讯视频已收集个人信息清单">
         腾讯视频已收集个人信息清单
        </a>
       </div>
       <div class="foot_item">
        <a class="foot_link" href="https://privacy.qq.com/policy/kids-privacypolicy" target="_blank" title="腾讯儿童隐私保护声明">
         腾讯儿童隐私保护声明
        </a>
       </div>
       <div class="foot_item">
        <a class="foot_link" href="https://film.qq.com/support/term.html" target="_blank" title="腾讯视频VIP会员服务协议">
         腾讯视频VIP会员服务协议
        </a>
       </div>
       <div class="foot_item">
        <a class="foot_link" href="https://film.qq.com/support/term.html?type=svip" target="_blank" title="腾讯视频超级影视VIP会员服务协议">
         腾讯视频超级影视VIP会员服务协议
        </a>
       </div>
      </div>
     </div>
    </div>
   </div>
   <div class="mod_footer">
    <div class="copyright_zheng">
     <a href="https://www.qq.com/culture.shtml" rel="nofollow" target="_blank">
      粤网文[2017]6138-1456号
     </a>
     |
     <a href="https://www.qq.com/cbst.shtml" rel="nofollow" target="_blank">
      网络视听许可证1904073号
     </a>
     | 增值电信业务经营许可证：
     <a href="https://beian.miit.gov.cn/" rel="nofollow" target="_blank">
      粤B2-20090059
     </a>
     |
     <a href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=44030002000001" rel="nofollow" target="_blank">
      粤公网安备 44030002000001号
     </a>
    </div>
    <div class="footermenu">
     <a href="https://www.tencent.com/" rel="nofollow" target="_blank">
      关于腾讯
     </a>
     |
     <a href="https://www.tencent.com/en-us/" rel="nofollow" target="_blank">
      About Tencent
     </a>
     |
     <a href="https://www.qq.com/contract.shtml" rel="nofollow" target="_blank">
      服务条款
     </a>
     |
     <a href="https://ads.privacy.qq.com/ads/adoptout.html?media_source=113001" rel="nofollow" target="_blank">
      广告服务
     </a>
     |
     <a href="https://careers.tencent.com/" rel="nofollow" target="_blank">
      腾讯招聘
     </a>
     |
     <a href="https://kf.qq.com/product/QQlive.html" rel="nofollow" target="_blank">
      客服中心
     </a>
     |
     <a href="https://www.qq.com/map/" rel="nofollow" target="_blank">
      网站导航
     </a>
    </div>
    <div class="copyrighten">
     Copyright © 1998 - 2021 Tencent.
     <a href="https://www.tencent.com/en-us/statement.html" rel="nofollow" target="_blank">
      All Rights Reserved.
     </a>
    </div>
    <div class="copyrightzh">
     腾讯公司
     <a href="https://www.tencent.com/zh-cn/statement.html" rel="nofollow" target="_blank">
      版权所有
     </a>
    </div>
   </div>
   <div class="mod_footer_supervision">
    <a class="supervision_logo" href="https://szcert.ebs.org.cn/1efd63b4-7863-490a-839f-53968220109f" rel="nofollow" target="_blank">
     <img alt="深圳市市场监督管理局企业主体身份公示" class="supervision_pic" src="https://vfiles.gtimg.cn/vupload/202005/1f68341597825237110.png"/>
    </a>
   </div>
   <!-- 反馈toast弹窗 -->
   <div class="toast_wrap" id="aisee" style="display:none; height:570px; width: 40vw; border: 1px solid #eee;">
    <div class="title_wrap" style="height:50px; padding: 0 10px; box-sizing: border-box; border-bottom: 2px solid #e0e0e0; text-align: center; line-height:50px; background-color: #fff;">
     <span style="font-size:20px">
      反馈
     </span>
     <a href="javascript:closeToast();" style="position: absolute; right: 11px; top: -8px; text-decoration: none; font-size: 20px; color: #999898;">
      x
     </a>
    </div>
    <div class="ifream_wrap" style="background-color: #fff;">
     <iframe frameborder="0" height="520px" id="Aiframe" scrolling="auto" width="100%">
     </iframe>
    </div>
   </div>
   <div class="mask_wrap" id="mask" style="display: none; width: 100vw; height: 100vh; background-color: rgba(0, 0, 0, .2);">
   </div>
   <script type="text/javascript">
    function toast() {
			var aStyle = document.getElementById("aisee").style;
			var mStyle = document.getElementById("mask").style;
			var Aiframe = document.getElementById("Aiframe"); // 获取反馈标签链接上的data-query

			var aTags = [].slice.call(document.getElementsByClassName("foot_link"));
			var feedback_a = aTags.filter(function (item) {
			return item.title === "反馈";
			})[0];
			var query = feedback_a.getAttribute("data-query"); // 给iframe拼接正确的src

			Aiframe.src = "https://h5.aisee.qq.com/pc/submit?" + query; // 设置样式

			mStyle.display = "";
			mStyle.position = "fixed";
			mStyle.top = "0";
			mStyle.left = "0";
			mStyle.zIndex = "9";
			aStyle.display = "";
			aStyle.position = "fixed";
			aStyle.top = "50%";
			aStyle.left = "50%";
			aStyle.transform = "translate(-50%,-50%)";
			aStyle.zIndex = "99"; // 提交成功自动关闭弹窗

			window.addEventListener('message', function (event) {
			var origin = event.origin || event.originalEvent.origin;

			if (origin !== 'https://h5.aisee.qq.com') {
				return;
			}

			setTimeout(function () {
				aStyle.display = "none";
				mStyle.display = "none";
			}, 2150);
			});
		}
		function closeToast(){
			var aStyle = document.getElementById("aisee").style;
			var mStyle = document.getElementById("mask").style;
			var Aiframe = document.getElementById("Aiframe");
			aStyle.display = "none";
			mStyle.display = "none";
		}
   </script>
  </div>
  <script type="text/javascript">
   window.V_PAGE_INFO = {
        page: 'choice',
        adType: 'index',
        channel: 'choice'
    }
    var doc_el = document.compatMode == 'BackCompat' ? document.body : document.documentElement;
    typeof txv !== 'undefined' && txv.common.initPage({
        boss: {
            app: '频道页',
            page: '精选频道',
            isRecalc: true
        },
        lazyload: {
            getScreenShowHeight: (function (doc) {
                return function () {
                    var scrollTop = window.pageYOffset || doc_el.scrollTop;
                    return doc.clientHeight + scrollTop + 600;
                }
            })(doc_el)
        }
    });
  </script>
  <script crossorigin="anonymous" src="//vm.gtimg.cn/tencentvideo/script/vchannel/index.3a28.js">
  </script>
  <script async="" defer="" src="//js.aq.qq.com/js/aq_common.js" tpye="text/javascript">
  </script>
  <script arguments="{'mo_page_ratio':0.02,'mo_ping_ratio':0.01,'mo_ping_script':'//ra.gtimg.com/sc/mo_ping-min.js'}" id="l_qq_com" src="//ra.gtimg.com/sc/vqq/crystal-min.js">
  </script>
  <script src="//vm.gtimg.cn/c/=/tencentvideo/script/index2017/public_comps/shortcut.min.js,/tencentvideo/script/module/floatpanel.js" tpye="text/javascript">
  </script>
  <script async="" crossorigin="anonymous" defer="" src="//vm.gtimg.cn/tencentvideo/script/quick-open/quick_open.min.js" type="text/javascript">
  </script>
 </body>
 <script type="text/javascript">
  window.floatPanel({
        page: window.channelName,
        channel: function (t) {
            return t && t.el && t.el.parents(".mod_row_box").attr("id");
        },
    });
    window.guangping_crystal && window.guangping_crystal();
    window.shortcut && window.shortcut.init({
        download: true, // 下载
        top: true, // 回到顶部
        usersign: true, // 签到
        feedback: true // 意见反馈
    })
 </script>
 <script src="//cdn-go.cn/aegis/aegis-sdk/latest/aegis.min.js">
 </script>
 <script>
  document.domain = 'qq.com';
  (function () {
    function getCookie(name) {
      var arr,
        reg = new RegExp('(^| )' + name + '=([^;]*)(;|$)');
      return (arr = document.cookie.match(reg)) ? unescape(arr[2]) : null;
    }
    window.aegis = new Aegis({
      id: 'pZvtOYxcQufEvoqUJe',
      uin: getCookie('vqq_vuserid') || getCookie('vuserid'),
      reportApiSpeed: true, // 接口测速
      reportAssetSpeed: true, // 静态资源测速
      beforeReportSpeed(msg) {
        // 上报屏蔽
        if (msg && msg.url && msg.url.indexOf('btrace.qq.com') !== -1) {
            return false;
        }

        if (msg && msg.url && msg.url.indexOf('node.video.qq.com/x/api/wuji_cache/object') !== -1) {
            return false;
        }

        if (msg && msg.url && msg.url.indexOf('dp3.qq.com/stdlog') !== -1) {
            return false;
        }

        return msg;
      },

      beforeReport: function(log){
            if(log && log.msg){
                if(log.msg.indexOf('btrace.qq.com')!== -1){
                    return false
                }
                if(log.msg.indexOf('Script error')!== -1){
                    return false
                }
                if (log.msg.indexOf('Uncaught TypeError') !== -1) {
                    return false;
                }

                if (log.msg.indexOf('Error.message') !== -1) {
                    return false;
                }

                if(log.msg.indexOf('type: error') !== -1){
                    return false;
                }

                if(log.msg.indexOf('Uncaught ReferenceError') !== -1){
                    return false;
                }

                if(log.msg.indexOf('Uncaught Error') !== -1){
                    return false;
                }
          }

        return log;
      },
    });
  })();
'''
# response = requests.get(url=url,headers=headers)                           # 发送请求
#当当居然用gbk编码，牛气
# response.encoding='gbk'
# response.encoding='utf-8'
soup=BeautifulSoup(resopnseStr,'lxml')
#打印出整齐有排面的样式
print(soup.prettify())
print('========================================')
##########################################################################

#找到包含整个元素的最小单元unit
unit = soup.find_all(name='h2',class_='mod_title')
for i in unit:
    # print(i)
    print(i.text.strip())
    print('--------')

print('=================================================')
unit = soup.find_all(name='div', class_='mod_row_box')
c=0

for i in unit:
    c+=1
    print('--- '+str(c)+' ---')
    if i.find(name='h2',class_='mod_title') != None:
        print('>>> ：',i.find(name='h2',class_='mod_title').text.strip())
        detail = i.find_all(name='a',class_='figure_title figure_title_two_row')
        # detail = i.find_all(class_='figure_title figure_title_two_row')
        if len(detail)==0 :
            detail = i.find_all(class_='figure_title figure_title_two_row bold')

        # print(detail)
        for j in detail:
             # print('二级标题：',j.text)

             y = j.contents

             printContent = '>>>>>> ：';

             for k in range(0,len(y)):
                 x =y[k].string.strip()
                 printContent = printContent+x
             print(printContent)

    print('--------')

print('=================================================')
print('=================================================')
