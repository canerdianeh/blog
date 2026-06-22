---
layout: post
title: Wowza EC2 Capacity Update
date: 2013-02-26 17:53:51.000000000 -06:00
type: post
parent_id: '0'
published: true
password: ''
status: publish
categories:
- Cloud Computing
- streaming
- Wowza
tags: []
meta:
  _edit_last: '2'
  _wpas_done_all: '1'
  dsq_thread_id: '1107203562'
author:
  login: ianbeyer
  email: ian.beyer@gmail.com
  display_name: Ian Beyer
  first_name: Ian
  last_name: Beyer
permalink: "/2013/02/26/wowza-ec2-capacity-update/"
image: "/assets/images/2013/02/Screen-Shot-2013-02-26-at-1.31.38-PM-1024x404.png"
---

It's been a while since Wowza has updated their EC2 performance numbers (they date back to about 2009), and both Amazon and Wowza have made great improvements to their products. Since I have access to a high-capacity system outside of Amazon's cloud, I am able to use Wowza's load test tool on a variety of instance sizes to see how they perform.

The test methodology was as follows:

- Start up a Wowza instance on EC2 with no startup packages (us-east)
- Install the server-side piece of [Willow](http://www.solid-thinking.com/products/willow-wowza-media-server-management-made-easy/ "Willow for Wowza") (from [Solid Thinking Interactive](http://www.solid-thinking.com/ "Solid Thinking Interactive"))
- Configure a 1Mbps stream in [Wirecast](http://www.nerdherd.net/wirecast "Wirecast Streaming Software")
- Monitor the stream in [JWPlayer](http://longtailvideo.com "JW Player") 5 with the [Quality Monitor Plugin](http://www.longtailvideo.com/addons/plugins/123/QualityMonitor "JW Player Quality Monitor Plugin")
- Configure the Wowza Load Test Tool on one of my [Wowza Hotrods](http://nerdian.ca/2013/01/31/supercharging-a-wowza-hotrod/ "Supercharging a Wowza Hotrod") located at Softlayer's Washington DC datacenter
  - Server is 14 hops/2ms from us-east-1
- Increase the load until:
  - the measured bandwidth on JW player drops below stream bandwidth
  - frame drops get frequent
  - Bandwidth levels out on the Willow Graphs while connection count increases
- Let it run in that condition for a few minutes

In Willow, it basically looked like this (this was from the m1.small test). You can see ramping up to 100, 150, 200, 250, 275, and 300 streams. The last 3 look very similar because the server maxed out at 250 Mbps. (Yes, the graph says MBytes, that was a bug in Willow which Graeme fixed as soon as I told him about it)

![Willow Bandwidth]({{site.baseurl}}/assets/2013/02/Screen-Shot-2013-02-26-at-1.31.38-PM-1024x404.png)

Meanwhile, this is what happens on the server.. the CPU has maxed out.

![EC2 CPU Usage]({{site.baseurl}}/assets/2013/02/Screen-Shot-2013-02-26-at-1.38.19-PM-1024x642.png)

So that's the basic methodology. Here are the results:

[table id=1 /]

There are a couple of things to note here. Naturally, if you're not expecting a huge audience, stick to m1.small. But the best bang for the buck is the c1.medium (High-CPU Medium), which is a relatively new instance type, which gives you 4x the performance of a m1.small at less than 2x the price. The big surprise here was the m2.xlarge. It performs only marginally better than an m1.small at 4x the price.  
All the instances that show 950 are effectively giving you the full benefit of the gigabit connection on that server and maxed out the interface long before the CPU maxes out. In the case of the c1.xlarge, there's lots of CPU to spare for things like transcoding and such if you're using a BYOL image. If you want to go faster, you'll need to roll your own [Cluster Quad](http://nerdian.ca/2012/02/09/streaming-on-amazons-superquad/ "Streaming on Amazon’s “SuperQuad”") or do a load-balanced set.

Disclaimers: Your mileage may vary, these are just guidelines, although I think they're pretty close. I have not tested this anywhere but us-east-1, so if you're using one of amazon's other datacenters, you may get different results. I hope to test the other zones soon and see how the results compare.
