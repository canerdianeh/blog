---
layout: post
title: Making Sense of Mobile Streaming
date: 2010-01-06 10:03:22.000000000 -06:00
type: post
parent_id: '0'
published: true
password: ''
status: publish
categories:
- streaming
tags:
- AAC
- android
- BlackBerry
- H.264
- HTC Hero
- iPhone
- Media
- MMS
- mobile
- PalmOS
- Pre
- RTSP
- streaming
- windows mobile
meta:
  dsq_thread_id: '217880192'
  _edit_last: '1'
  _googl_shortlink: http://goo.gl/0e8br
author:
  login: ianbeyer
  email: ian.beyer@gmail.com
  display_name: Ian Beyer
  first_name: Ian
  last_name: Beyer
permalink: "/2010/01/06/making-sense-of-mobile-streaming/"
---

Now that we've gotten streaming to computers down pat, I've set my sights on delivering a good experience for mobile users. Unfortunately, with the wide variety of mobile platforms out there, this is not an especially easy task. The Mac/PC/Linux issues are complicated enough, and it gets really tricky when the platform ecosystem has half a dozen major players (and a truckload of minor ones)

Since July or so, we've been using a preview version of the recently released Wowza V2 server software to deliver our video content to iPhone/iPod devices that support Apple's new HTTP Streaming format. With minimal changes, Wowza V2 can also rebroadcast the same H.264/AAC stream over RTSP, which reaches a lot more devices. But this is where it gets complicated. BlackBerry has been supporting RTSP for some time, but it's only recently that they've supported h.264/AAC media. According to their [KB article on the subject](http://www.blackberry.com/btsc/viewContent.do?externalId=KB05482 "BlackBerry Supported Media Types"), you can do H.264 on the following:

- Bold 9000/9700
- Tour 9630
- Storm 9500/9520/9530/9550
- Curve 8900/8520

Most HTC phones have a streaming media app that supports RTSP, but only recent versions seem support H.264. For example, my Mogul has the app, but I can only hear the audio. [Brian](http://officecurmudgeon.com/ "Brian Slezak")'s Touch Pro 2 gets both (and on the TP2's WVGA screen, it looks amazing!).

Windows Media Player supports RTSP, but doesn't come with an H.264 codec (even in Windows 7!!!! BOOO!!!!). I have yet to get the RTSP stream to work on Windows Media Player. The mobile player doesn't support RTSP at all, just MMS and HTTP (but not the same HTTP as Apple! Grr!), and with the 9.5 generation of Windows Media Services (2008), [MMS has gone away](http://www.microsoft.com/windows/windowsmedia/forpros/server/faq.aspx "Microsoft Media Streaming FAQ") in favor of HTTP (which Microsoft calls Smooth Streaming, also not supported on WiMo).

The Palm Pre is supposedly able to do RTSP and H.264, but I'm waiting to hear back from one of our pre-wielding pastors to see if this is actually the case.

Thanks to [Daryl Hunter](http://www.darylhunter.me/ "Daryl Hunter") at lifechurch.tv for letting me know that it works on his HTC Hero (Android 1.5). It seems that on Android you can't manually enter an RTSP URL into the browser bar, but a web link or tinyurl redirect that goes to an RTSP URL does work.

Meanwhile, [VLC player](http://www.videolan.org/vlc/ "VLC Player") will play just about anything you throw at it, including the RTMP flash stream. Pity it's not available in a mobile version.

So, as it stands now, in order to deliver a mobile experience to as many people as possible, I'm still going to need to run a separate Windows Media server for our Windows Mobile clients, But everyone else should be able to pull from the "iPhone" stream (which I'm probably going to need to rename), as long as the device supports H.264/AAC and RTSP.
