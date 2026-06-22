---
layout: post
title: 'Live Streaming on a budget: Wowza Load Balancing (Part ... um.. how many is
  it now?)'
date: 2009-09-27 10:54:04.000000000 -05:00
type: post
parent_id: '0'
published: true
password: ''
status: publish
categories:
- Internet Campus
- streaming
tags: []
meta:
  dsq_thread_id: '218103602'
  _googl_shortlink: http://goo.gl/MRFNO
author:
  login: ianbeyer
  email: ian.beyer@gmail.com
  display_name: Ian Beyer
  first_name: Ian
  last_name: Beyer
permalink: "/2009/09/27/live-streaming-on-a-budget-wowza-load-balancing-part-um-how-many-is-it-now/"
---

This week, I discovered that the new version (4.5) of [JW Player](http://www.longtailvideo.com/players/jw-flv-player/) now supports the Wowza RTMP redirect method of load balancing. Huge props to [Richard Lanham](http://www.lakesidetechnical.com/) for making that possible. Richard is a tremendous asset to the Wowza community.

A few months back, the fine folks at Wowza added a load balancing method where the edge repeaters communicate with the origin server with information about the number of connected clients. In an RTMP redirect, the origin server has a special publishing point (an "application" in the Wowza vernacular) called /redirect that will then tell the player which of the connected edge servers has the lowest load. Charlie Good from Wowza has a [post in the Wowza](http://www.wowzamedia.com/forums/showthread.php?t=4637) forums that documents how to make this work

The basic mechanism of RTMP redirects for load balancing on Wowza lends itself very well to a dynamic scaling platform such as EC2. As you may recall, we've been using round-robin DNS to scale out our streaming, with Wowza's edge/repeater configuration.

What this means for us is that we can now spin up two repeaters and an origin, and we don't need to assign an ElasticIP to the repeaters and no longer need to keep a pool of addresses in reserve (at a penny an hour when they're not connected). If the load gets high on the existing repeaters, I can launch an additional one and the load balancing will send new connections to that server until it's reached the level of the others.

This makes scaling our streaming much more dynamic than three servers, and is theoretically limitless (within the performance limitations of the origin server). If we get a huge spike for something like the health care forum recently, we can adapt much quicker. It's also possible to round-robin a pair of origin servers and segment your repeater farms, or use the pair of origin servers for redundancy.

Another feature of the load balancing is a module on the origin server called serverInfoXML that returns statistics on each of the connected repeaters. I've hacked together some ugly [perl](http://www.perl.org/) to parse this into some meaningful stats, and it dynamically changes along with the number of servers. The only catch is that it doesn't work with less than two repeaters due to array dimensioning. If anyone with mad perl skills wants to help make this prettier, and feed the data into a graphing tool like [RRDTool](http://oss.oetiker.ch/rrdtool/), I'd love to hear from you.
