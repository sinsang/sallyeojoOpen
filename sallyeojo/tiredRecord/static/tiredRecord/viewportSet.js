let viewportParams2 = ", initial-scale=1.0,  user-scalable=yes, maximum-scale=1.5, minimum-scale=1.0";
let metaViewport = document.querySelector("meta[name=viewport]");
let width = $(window).width();
let height = $(window).height();
let viewportParams = "width=" + width + ", height=" + height + viewportParams2;

metaViewport.setAttribute("content", viewportParams);