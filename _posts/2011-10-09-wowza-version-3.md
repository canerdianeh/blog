---
layout: post
title: 'Hot off the presses: Wowza Media Server Version 3'
date: 2011-10-09 11:34:10.000000000 -05:00
type: post
parent_id: '0'
published: true
password: ''
status: publish
categories:
- streaming
- Wowza
tags: []
meta:
  _edit_last: '2'
  wp_plus_one_redirect: ''
  dsq_thread_id: '438448424'
  _googl_shortlink: http://goo.gl/9POJi
  image: ''
  quote-author: Unknown
  quote-url: http://
  quote-copy: Unknown
  audio: http://
  link-url: http://
author:
  login: ianbeyer
  email: ian.beyer@gmail.com
  display_name: Ian Beyer
  first_name: Ian
  last_name: Beyer
permalink: "/2011/10/09/wowza-version-3/"
---

**[\*\* UPDATED INFORMATION : 6 November 2011 \*\*](http://nerdian.ca/wowza-v3-for-ec2/ "Wowza Media Server V3 for Amazon EC2")**

After many months of hard work, the team at Wowza put the finishing touches on the latest major release of Wowza Media Server. The new version adds a couple of key features in the form of licensed add-ons:

- Network DVR:

- *Wowza nDVR AddOn (Beta release) is an innovative live stream cache that stores content in a normalized format accessible to Wowza Media Server 3 for any-screen HTTP playout. Compared to client-specific nDVR implementations, Wowza nDVR significantly reduces cost by minimizing network storage requirements and simplifying the delivery workflow for all screens. Wowza nDVR enables Wowza licensees to increase revenues and viewer engagement by delivering live linear streams as time-shifted services with features like live pause, rewind, and resume.*

- Live Transcoding:

- *Wowza Transcoder AddOn takes advantage of the same hardware as the server to transform incoming live streams from encoders, IP cameras, IPTV headends, and other live sources into multiple stream sets 'done right' for H.264-everywhere adaptive bitrate delivery. Adaptive bitrate streaming is supported for Flash RTMP and HTTP Dynamic Streaming, Apple HLS, and Silverlight Smooth Streaming. Wowza Transcoder also delivers non-adaptive streams over any transport protocol supported by Wowza Media Server 3, including RTMP, RTSP/RTP, MPEG-TS, and HTTP.*

- DRM Integration

- *Wowza DRM AddOn provides simultaneous secure key exchange with multiple DRM platforms such as Verimatrix VCAS and Microsoft PlayReady. Individual live or on-demand content is encrypted on-the-fly for HLS and Silverlight delivery to viewers on a wide range of devices including set-top boxes (STBs), connected TVs, smartphones and tablets. Wowza DRM AddOn can help users up-sell content for OTT premium services, and cross-sell content for multi-device distribution.*

The other key feature is a change in the subscription license model, adding a daily license in addition to the monthly license. The subscription licenses are allowed to be used on Amazon's EC2 cloud. The monthly subscription license has also seen a price reduction (there are also tiered price breaks on the monthly subscription). The subscription license is based on the number of instances you start during a given day or month. This is likely to be the new licensing model for EC2, moving away from Amazon's DevPay model which required a monthly subscription as well as limiting instances to S3-backed images that couldn't take advantage of Amazon's reserved instances. By using a subscription license, you still get the scalability of the Amazon cloud, but the flexibility of using an instance type and OS that works for you. As of the release this week, there are no pre-built EC2 images for Wowza V3, but they're coming soon. [Wowza Media Server V3 Overview (PDF)](http://www.wowza.com/resources/WowzaMediaServer3_Overview.pdf "Wowza V3 Overview") [Wowza Media Server V3 User's Guide (PDF)](http://www.wowza.com/resources/WowzaMediaServer3_Overview.pdf "Wowza V3 User's Guide") [Wowza Media Server V3 Pricing](http://www.wowza.com/pricing.html#monthly "Wowza Pricing") [Wowza Media Server V3 Add-Ons](http://www.wowza.com/video-streaming-server.html#a "Wowza V3 Add-Ons")
