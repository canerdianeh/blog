---
layout: post
title: Y2K10 in JavaScript?
date: 2009-12-29 21:32:03.000000000 -06:00
type: post
parent_id: '0'
published: true
password: ''
status: publish
categories:
- Internet Campus
tags:
- bugs
- code
- javascript
meta:
  _edit_last: '1'
  dsq_thread_id: '217880167'
  _googl_shortlink: http://goo.gl/IvQQD
author:
  login: ianbeyer
  email: ian.beyer@gmail.com
  display_name: Ian Beyer
  first_name: Ian
  last_name: Beyer
permalink: "/2009/12/29/y2k10-in-javascript/"
---

On our [live stream page](http://live.cor.org), we have a nifty little [javascript counter](http://nerdian.ca/code/client/js-countdown-timer/ "JavaScript Countdown Timer") that lets you know when the next service is.

[Leo](http://leojohns.com/) noticed today that in Internet Explorer, it's counting down properly, while in [Firefox](http://firefox.com), it's saying the event is already happening. On a hunch, we changed the target date to 12/31, and it started working properly again.

So, IE's Javascript is smart enough to figure out that on December 29, the target date of January 3 is likely to be the one next week. Firefox is clinging to the past and assuming that I really meant the January 3 that happened 51 weeks ago.

How is it that the same script can be interpreted so differently within the same language on two different browser platforms? This stuff is supposed to be standard!
