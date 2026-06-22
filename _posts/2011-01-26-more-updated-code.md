---
layout: post
title: More Updated Code
date: 2011-01-26 13:30:44.000000000 -06:00
type: post
parent_id: '0'
published: true
password: ''
status: publish
categories:
- streaming
- Wowza
tags:
- automation
- bash
- code
meta:
  dsq_thread_id: '218062451'
  _edit_last: '1'
  s2mail: 'yes'
  _wp_old_slug: ''
  _googl_shortlink: http://goo.gl/U553D
author:
  login: ianbeyer
  email: ian.beyer@gmail.com
  display_name: Ian Beyer
  first_name: Ian
  last_name: Beyer
permalink: "/2011/01/26/more-updated-code/"
---

Updated the [Wowza Launch Script](http://blog.ianbeyer.com/code/ec2/wowza-origin-startup-bash/ "Wowza Origin Server Startup (bash)"). Changed it to be more friendly to a non-root user directory, as well as adding logic that makes the startup package on the fly, so that if you want to edit the contents, the next launch will send the current incarnation.

Stay tuned for a post soon on the anatomy of a Wowza startup package for EC2.
