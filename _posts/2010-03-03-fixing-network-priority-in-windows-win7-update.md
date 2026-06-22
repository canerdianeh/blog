---
layout: post
title: 'Fixing network Priority in Windows : Win7 Update'
date: 2010-03-03 10:21:37.000000000 -06:00
type: post
parent_id: '0'
published: true
password: ''
status: publish
categories:
- IT
- networking
- Wireless
tags:
- Hardware
- networking
- Windows
meta:
  dsq_thread_id: '217880308'
  _edit_last: '2'
  _googl_shortlink: http://goo.gl/vxuPy
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
permalink: "/2010/03/03/fixing-network-priority-in-windows-win7-update/"
image: "http://blog.ianbeyer.com/files/2010/03/NetworkAdvanced.png"
---

A long time ago, I made a post about [fixing network priority in Windows](http://blog.ianbeyer.com/2008/10/10/fixing-network-priority-in-windows/ "Fixing network priority in Windows"), and I found myself having to do the same task again on my new Windows 7 system. The process isn't quite as easy to find under Windows 7/Vista. Here's the updated version:

Right-click on your network icon and go to the "Network and Sharing center" (if the "Network" icon is on your desktop, you can also get there by right-clicking and going to properties)

Click on "Change Adapter Settings"

![Network Advanced]({{site.baseurl}}/assets/2010/03/NetworkAdvanced.png)

Press the "Alt" Key to show the menu, and click on "Advanced", then "Advanced Settings".

(from here, the process is unchanged)

Move the Wired LAN Connection (By Default, “Local Area Connection”) to the top, followed by the wireless connection. Make sure that any VPN virtual adapters come after these, otherwise the VPN will only use the ones above it. This tends to be problematic if you’re using split tunneling, as it will kill any network connection you have.

Once you've applied the settings, open a command prompt and run "nslookup" - it should default to the DNS server for your wired network.
