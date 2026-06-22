---
layout: post
title: Fixing network priority in Windows
date: 2008-10-10 12:10:37.000000000 -05:00
type: post
parent_id: '0'
published: true
password: ''
status: publish
categories:
- networking
- Wireless
tags:
- Hardware
- networking
- Windows
meta:
  dsq_thread_id: '217876998'
  _googl_shortlink: http://goo.gl/yDgxb
  _edit_last: '2'
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
permalink: "/2008/10/10/fixing-network-priority-in-windows/"
image: "/assets/images/2008/10/networkproperties.png"
---

Recently, we made some changes to the DNS infrastructure on our public wireless networks which has had the unintended consequence of breaking things when our laptop users are plugged into the LAN and have their wireless active. Brian and I have wrangled with this in the office, but we simply turned off the wireless as a workaround.

What's happening is that when connected to both networks, the wireless has a higher priority by default, and so it resolves DNS via that interface. This is problematic when trying to access an internal resource, because our DNS is set to have a default resolution to our website for \*.cor.org. To complicate matters further, Arena behaves differently when you're on the guest network (sends to a forms-based auth portal instead of using IE integrated authentication).

After much digging, I found out how to change interface priority. Here's the process in XP screenshots (the process is similar in Vista):

1. Open your network connection properties (XP: Via control panel or right-click on Network Places, then select Properties. Vista: Go to Network and Sharing Center and select "Manage Network Connections in the links on the left)

[caption id="attachment\_77" align="aligncenter" width="500"][![XP Network Properties]({{site.baseurl}}/assets/2008/10/networkproperties.png)](http://blog.ianbeyer.com/files/2008/10/networkproperties.png) XP Network Properties[/caption]

2. On the menu bar (press Alt to show it in Vista), Select Advanced, then "Advanced Settings"

[caption id="attachment\_78" align="aligncenter" width="404"][![Advanced Network Properties Dialog (XP)]({{site.baseurl}}/assets/2008/10/advanced.png)](http://blog.ianbeyer.com/files/2008/10/advanced.png) Advanced Network Properties Dialog (XP)[/caption]

3. Move the Wired LAN Connection (By Default, "Local Area Connection") to the top, followed by the wireless connection. Make sure that any VPN virtual adapters come after these, otherwise the VPN will only use the ones above it. This tends to be problematic if you're using split tunneling, as it will kill any network connection you have.[![]({{site.baseurl}}/assets/2008/10/advanced2.png)](http://blog.ianbeyer.com/files/2008/10/advanced2.png)

4. Hit OK, and you're good to go.
