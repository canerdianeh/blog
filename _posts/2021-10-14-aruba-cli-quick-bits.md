---
layout: post
title: Aruba CLI Quick Bits!
date: 2021-10-14 13:39:44.000000000 -05:00
type: post
parent_id: '0'
published: true
password: ''
status: publish
categories:
- Aruba
- IT
- networking
- Wireless
tags: []
meta:
  _last_editor_used_jetpack: block-editor
  _publicize_twitter_user: "@CaNerdIan"
  _wpas_skip_19898087: '1'
  _wpas_done_all: '1'
  _edit_last: '2'
  _cs_replacements: a:1:{s:7:"sidebar";s:7:"sidebar";}
  _bpp_element: body
  _bpp_repeat-x: 'yes'
  _bpp_repeat-y: 'yes'
  _bpp_attachment: scroll
  _bpp_position: center
  _bpp_fade: 'yes'
  _bpp_fade_height: '100'
  _bpp_color: "#"
author:
  login: ianbeyer
  email: ian.beyer@gmail.com
  display_name: Ian Beyer
  first_name: Ian
  last_name: Beyer
permalink: "/2021/10/14/aruba-cli-quick-bits/"
---

Just a quick post today to highlight a couple of my favorite ArubaOS v8 CLI commands of the week.
The first is \*\*[show configuration diff  ](https://www.arubanetworks.com/techdocs/CLI-Bank/Content/aos8/sh-conf.htm?Highlight=diff)\*\*. This handy tool lets you compare what's different between two different hierarchy containers. Great for chasing down obscure config items.
The second is \*\*[show references](https://www.arubanetworks.com/techdocs/CLI-Bank/Content/landing-pages/aos8-home.htm#S)\*\*, followed by a profile type and name - it will tell you all the profiles that reference the one provided. Very handy if you're trying to clean up cruft and want to find profiles that are abandoned and no longer useful, or if it won't let you delete a profile because it is still in use (where it will annoyingly not actually tell you where)
That's all for today!
