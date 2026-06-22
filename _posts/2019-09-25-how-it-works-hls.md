---
layout: post
title: 'How It Works: HTTP Live Streaming'
date: 2019-09-25 09:39:42.000000000 -05:00
type: post
parent_id: '0'
published: true
password: ''
status: publish
categories:
- networking
- streaming
- Wireless
- Wowza
tags:
- HLS
- WiFi
meta:
  _publicize_twitter_user: "@CaNerdIan"
  _wpas_done_all: '1'
  _thumbnail_id: '1628'
  _edit_last: '2'
  _wp_old_slug: how-it-works-http-live-streaming
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
permalink: "/2019/09/25/how-it-works-hls/"
image: "/assets/images/2019/09/Aadaptive-Bitrate-Streaming-Graphic-700x313.png"
---

For those of us that work on wireless systems with a strong guest access component, the fine folks at Wowza Media Systems posted earlier this month about the inner workings of HTTP Live Streaming (Apple's proprietary streaming protocol, or HLS) which accounts for about 45% of all streaming traffic - which tracks pretty closely to Apple's market share of mobile devices.
Prior to getting hot and heavy with wireless networks, I did a lot of streaming infrastructure implementation for Wowza's customers (as many of this blog's readers are well aware - just go look into the archives!) HLS, which was released with the iPhone 3Gs, is designed from the ground up to handle the highly variable bandwidth and delay conditions inherent to mobile connections on Wi-Fi and cellular, while delivering a good streaming experience to the end user. It also allows streaming providers to leverage existing HTTP-based content delivery infrastructure.
Older streaming protocols like RTMP and RTSP are particularly unfriendly to wireless networks as they require a constant data stream at the stream bandwidth. For a video stream, much like a VOIP call, this requires consistent and timely medium access, which is definitely not a sure thing on Wi-Fi the way it is on Ethernet. The tradeoff is that the delay from live on HLS (a minute or two) is much higher than it is on RTSP (a few frames/milliseconds) or RTMP (a few seconds).
When working down at Layer 2, it's usually helpful to understand what's going on up the stack, especially with regards to what kind of unholy things are being done inside HTTP (which we may or may not have visibility into because of encrypted packet and segment payloads). In terms of the ISO model, HLS is probably best described as Layer 5 (the HTTP segmentation) and Layer 6 (the video data).
My good friend Jim Palmer (Not the baseball player) [spoke at the Wireless LAN Pros Conference](https://www.wlanpros.com/resources/the-netflix-effect-on-guest-wi-fi-jim-palmer-wlpc-phoenix-2019/) last year about the effects of user bandwidth throttling in a guest wireless environment with heavy streaming usage (predominantly Netflix). Understanding how HLS works in this context is key to understanding why the network behaves the way it does when you do that throttling. His talk is well worth ten minutes of your time. He's also had some informative appearances on the Clear To Send Podcast ([Episode #136, on antennas and filters](https://www.cleartosend.net/rf-filtering-isolation/)), the Wireless LAN Pros podcast ([Episode 116 on Captive Portals](https://www.wlanpros.com/resources/podcast116/)), and WiFi Ninjas Podcast ([Episodes 19 and 20 on Airport Wireless Design](http://wifininjas.libsyn.com/wn-podcast-019-airport-wifi-design-with-jim-palmer-part-1)).
So, here's the link to Wowza's post on the subject. I hope they post one about MPEG-DASH soon (from an HTTP standpoint, DASH works in a similar fashion).
