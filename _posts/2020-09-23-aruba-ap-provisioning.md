---
layout: post
title: Aruba AP Provisioning
date: 2020-09-23 16:25:32.000000000 -05:00
type: post
parent_id: '0'
published: true
password: ''
status: publish
categories:
- Aruba
- networking
- Wireless
tags: []
meta:
  _publicize_twitter_user: "@CaNerdIan"
  _wpas_skip_19898087: '1'
  _wpas_done_all: '1'
  _thumbnail_id: '1792'
  _edit_last: '2'
  _last_editor_used_jetpack: block-editor
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
permalink: "/2020/09/23/aruba-ap-provisioning/"
image: "/assets/images/2020/09/AdobeStock_330987132-scaled.jpeg"
---

As part of trying to wrap my own head around the various profile dependencies in actually provisioning an Aruba AP , I've mapped it out. This is the  that goes into this process:
`provision-ap`
`read-bootinfo {wired-mac|ip-addr|ap-name} `
``
`reprovision {serial|wired-mac|ip-addr|ap-name} `
As you go to provision an AP, start on the outside of this map and work your way in. This will make sure that all the various profiles you need are in place. The web UI hides some of this stuff from you and doesn't organize it as logically as one might expect.
When doing this on the CLI in Mobility ~~Master~~ Conductor, make sure you're in the right corner of your hierarchy (namely, \*/md\* or \*/md/GROUP\*). And remember that on ~~MM~~MCR, \*\*\*show run\*\*\* is not nearly as useful as \*\*\*show config effective\*\*\*... And \*\*\*config purge-pending\*\*\* sure comes in handy when you goof something up.
You can also do \*\*\*show profile-hierarchy\*\*\* but that only shows the profile entries and it doesn't fit neatly in a terminal window.
Lastly, don't forget about \*\*show references\*\* to see what other profiles reference the one you're interested in.
\*Caveat: This is not comprehensive by any stretch. There are dozens more options, these are just the more common ones. If I goofed, let me know. All the gory details can be found in the ArubaOS User Guide.\*
[![]({{site.baseurl}}/assets/2020/09/Aruba-AP-Provisioning-1-645x1024.png)](https://nerdian.ca/files/2020/09/Aruba-AP-Provisioning-1.png)
