---
layout: post
title: Browser-Aware Player
date: 2010-05-16 18:21:53.000000000 -05:00
type: post
parent_id: '0'
published: true
password: ''
status: publish
categories:
- Internet Campus
- streaming
- Web 2.0
tags:
- flash video
- HTML5
- javascript
- mobile
meta:
  dsq_thread_id: '217880326'
  _edit_last: '1'
  _googl_shortlink: http://goo.gl/0JhzV
author:
  login: ianbeyer
  email: ian.beyer@gmail.com
  display_name: Ian Beyer
  first_name: Ian
  last_name: Beyer
permalink: "/2010/05/16/browser-aware-player/"
---

One of the big challenges of streaming to the web is the sheer diversity of devices out there.
This past week, I pushed out some modifications to the player code on our [live page](http://live.cor.org) that switches the player code based on what the user is connecting with. The genesis of this change was a problem with our change to [JW Player](http://www.longtailvideo.com/players/jw-flv-player) Version 5 causing our PlayStation users to no longer be able to watch our video since JW v5 requires Flash 10 and Sony apparently doesn't care about its customers. After a successful test with the Playstation, I extended the code to provide an [HTML5](http://www.w3schools.com/html5/html5\_reference.asp)  tag for our iPhone users (allowing us to clear up some the clutter on the sidebar), as well as MMS and RTSP links around a graphic mimicking the Flash-based player in order to provide a consistent user experience for our Android/WebOS/BlackBerry/WinMo users.
EDIT: The main reason I'm not doing straight HTML5 with Flash fallback (a much more elegant solution) is that we're sending out VP6 for our flash users and a lower-bandwidth h.264 stream for our mobile users. We're not currently using h.264 for our flash users because of the poor quality of the h.264 encoder in Flash Media Live Encoder. Once we get a "[real encoder](http://kulabyte.com)", we'll send out a single set of h.264 streams and use HTML5 with fallback.
The [code is here](http://blog.ianbeyer.com/code/browser-aware-player-code).
