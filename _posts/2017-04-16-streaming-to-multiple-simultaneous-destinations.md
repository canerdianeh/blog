---
layout: post
title: Streaming to multiple simultaneous destinations
date: 2017-04-16 09:24:07.000000000 -05:00
type: post
parent_id: '0'
published: true
password: ''
status: publish
categories:
- Cloud Computing
- streaming
- Wowza
tags:
- Facebook Live
- Teradek
- Youtube Live
meta:
  _edit_last: '2'
  _thumbnail_id: '1459'
  _wpas_done_all: '1'
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
permalink: "/2017/04/16/streaming-to-multiple-simultaneous-destinations/"
image: "/assets/images/2017/04/6820932624_b6ca9295c7_k.jpg"
---

Live streaming has been a "thing" for some time. I work with many churches to help them solve their streaming challenges and develop their technology strategy for streaming. One of the most frequent questions I hear is, "can I stream to Facebook Live and still keep my other stream?" Fortunately, this is a lot easier than it used to be. There are variations on this question, but they all boil down to wanting to know how to send one stream to multiple outlets to expand audience reach.

### Method 1:

**Multiple outputs from your encoder**

Several software encoder platforms support multiple outputs. The easiest among these is probably [Telestream's Wirecast](http://primary.telestream.net/wirecast/) software. (The free/open-source [Open Broadcast Studio](https://obsproject.com) does this as well, but I don't have much experience with it, and I prefer the Wirecast interface, which is much more polished.) With Wirecast, it's merely a matter of adding the additional outputs to the various streaming services that are supported. The downside to this approach is that you'll need more bandwidth, as you are sending the same stream multiple times.

[![Screenshot 2017-04-16 09.56.42]({{site.baseurl}}/assets/2017/04/Screenshot-2017-04-16-09.56.42-1024x450.png)](http://blog.ianbeyer.com/files/2017/04/Screenshot-2017-04-16-09.56.42.png)

### Method 2:

**The Cloud**

1. Teradek Core

This is a vendor-specific approach that integrates with [Teradek](http://www.teradek.com)'s pro-grade encoders (Cube, Bond, Slice, and T-Rax). It provides a single pane of glass that lets you manage your entire fleet of encoder devices (and control/configure them remotely), and then virtually patch the output of those encoders to one or more outputs. You can also use their [Live::Air apps](https://teradek.com/collections/live-air-family) for iOS as an input (stay tuned for a post about using Live::Air). If you are using a Bond product, the input is via their Sputnik server, which allows you to spread the stream across multiple connections for extra bandwidth and redundancy, and then it's reassembled before sending it on to the next step.

In this example, I'm taking an input stream from the Live::Air Solo app on my iPhone, and sending it to [Wowza Streaming Clou](http://cloud.wowza.com)d, and Facebook Live, all while recording the incoming stream:

[![Screenshot 2017-04-16 07.10.22]({{site.baseurl}}/assets/2017/04/Screenshot-2017-04-16-07.10.22-1024x554.png)](http://blog.ianbeyer.com/files/2017/04/Screenshot-2017-04-16-07.10.22.png)

This is a simple drag and drop operation: Drag a source on the left into the workspace, and then drag one or more destinations from the left - this can be:

Teradek decoders (this is great for a multisite church scenario)

Channels (which are external stream destinations):

[![Screenshot 2017-04-16 09.49.05]({{site.baseurl}}/assets/2017/04/Screenshot-2017-04-16-09.49.05-1024x510.png)](http://blog.ianbeyer.com/files/2017/04/Screenshot-2017-04-16-09.49.05.png)

Groups (a combination of the above):

[![Screenshot 2017-04-16 09.50.31]({{site.baseurl}}/assets/2017/04/Screenshot-2017-04-16-09.50.31-1024x315.png)](http://blog.ianbeyer.com/files/2017/04/Screenshot-2017-04-16-09.50.31.png)

If you click the "Auto" box on the outputs, it will start that output automatically when the stream is available from the input.

When you create stream destinations for social sites, it will authenticate you against that site and keep that authentication.

You can manage a lot of inputs and outputs this way. This example from Teradek's marketing department shows the scale:

[![core-management-platform-user-interface_e811873e-7cfb-4514-a465-1467d487d8d7]({{site.baseurl}}/assets/2017/04/core-management-platform-user-interface_e811873e-7cfb-4514-a465-1467d487d8d7-1024x527.jpg)](http://blog.ianbeyer.com/files/2017/04/core-management-platform-user-interface_e811873e-7cfb-4514-a465-1467d487d8d7.jpg)

2. Wowza Streaming Engine/Streaming Cloud

Similar to Core, but not tied to a specific vendor, Wowza Streaming Engine provides Stream Targets as of version 4.4 (although the functionality has been in the software since sometime in version 2, as the PushPublish module, Stream Targets integrates it into the UI). Facebook Live support has been an option since almost the very beginning of Facebook Live. YouTube Live support is there, but as a standard RTMP destination.

Similarly, Wowza Streaming Cloud also offers this capability under the "Advanced Menu":

[![Screenshot 2017-04-16 10.07.49]({{site.baseurl}}/assets/2017/04/Screenshot-2017-04-16-10.07.49-1024x515.png)](http://blog.ianbeyer.com/files/2017/04/Screenshot-2017-04-16-10.07.49.png)

From there, you can create a stream target:

[![Screenshot 2017-04-16 10.08.02]({{site.baseurl}}/assets/2017/04/Screenshot-2017-04-16-10.08.02-300x164.png)](http://blog.ianbeyer.com/files/2017/04/Screenshot-2017-04-16-10.08.02.png)

Once that target is created, simply go into a transcoder output and add it (you can also create a target directly from there):

[![Screenshot 2017-04-16 10.12.26]({{site.baseurl}}/assets/2017/04/Screenshot-2017-04-16-10.12.26-941x1024.png)](http://blog.ianbeyer.com/files/2017/04/Screenshot-2017-04-16-10.12.26.png)

As with Core, you can add multiple destinations to a transcoder output - Generally speaking you'll want to send your best output to places like FB Live, YouTube, etc, as they do their own internal transcoding.

[![Screenshot 2017-04-16 10.13.31]({{site.baseurl}}/assets/2017/04/Screenshot-2017-04-16-10.13.31-300x136.png)](http://blog.ianbeyer.com/files/2017/04/Screenshot-2017-04-16-10.13.31.png)

### Method 3:

Multiple Encoders

This is the obvious one, but also the least efficient both in terms of hardware and bandwidth. Each encoder goes to its own destination. This generally requires signal distribution amplifiers and other extra hardware.
