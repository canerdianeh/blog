---
layout: post
title: JW Player 5.0 and Wowza Load Balancing
date: 2009-12-30 09:33:29.000000000 -06:00
type: post
parent_id: '0'
published: true
password: ''
status: publish
categories:
- Internet Campus
- streaming
- Wowza
tags:
- flash video
- JW Player
meta:
  _edit_last: '2'
  dsq_thread_id: '217880184'
  s2mail: 'yes'
  _googl_shortlink: http://goo.gl/sYA2V
author:
  login: ianbeyer
  email: ian.beyer@gmail.com
  display_name: Ian Beyer
  first_name: Ian
  last_name: Beyer
permalink: "/2009/12/30/jw-player-5-0-and-wowza-lb/"
---

[Longtail](http://www.longtailvideo.com/) recently released [JW Player 5.0](http://www.longtailvideo.com/players/jw-player-5-for-flash), but it had a bug that prevented it from being used with a [Wowza](http://wowzamedia.com) load balance setup. It would catch the redirect and show the first few frames and then start buffering without end.

I just got the new [764 build](http://developer.longtailvideo.com/svn/trunk/fl5/) and am happy to report that it works quite nicely now.
