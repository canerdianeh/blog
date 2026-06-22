---
layout: post
title: Anatomy of an online worship service
date: 2010-02-21 16:41:37.000000000 -06:00
type: post
parent_id: '0'
published: true
password: ''
status: publish
categories:
- Internet Campus
- streaming
- Wowza
tags:
- Cloud
- Cloudwatch
- ec2
- Load Balancing
- Scaling
- Woopra
meta:
  dsq_thread_id: '217880265'
  _edit_last: '1'
  s2mail: 'yes'
  _googl_shortlink: http://goo.gl/wRGd4
author:
  login: ianbeyer
  email: ian.beyer@gmail.com
  display_name: Ian Beyer
  first_name: Ian
  last_name: Beyer
permalink: "/2010/02/21/anatomy-of-an-online-worship-service/"
image: "/assets/images/2010/02/02-21-10-AM-Network-300x201.png"
---

(or, How Amazon Cloudwatch helps manage Wowza server load)[![02-21-10-AM-AWS]({{site.baseurl}}/assets/2010/02/02-21-10-AM-AWS-300x159.png)](http://blog.ianbeyer.com/files/2010/02/02-21-10-AM-AWS.png)

This morning I woke up to two things: Beautiful Kansas City February weather (aka, an ice storm), and a voicemail from the Senior Pastor, asking if we had sufficient online capacity to support a larger-than-usual stream audience. Online worship streaming is a great option for these weather events that have been so common this winter (and not just in the KC area - we see increased online attendance when the weather gets foul elsewhere, like the DC storms of a few weeks ago).

My first indication that this was going to be a big event was [Woopra](http://woopra.com) showing 30 people on the web page half an hour before we start sending any kind of video (which is itself 75 minutes before we actually start the morning service). Usually there are two or three. Fifteen minutes after we started sending video, we were already cranking out 20-30 streams (again, we usually only have a small handful at this point).

[caption id="attachment\_368" align="alignleft" width="300" caption="AWS CPU Usage"][![02-21-10-AM-CPU]({{site.baseurl}}/assets/2010/02/02-21-10-AM-CPU-300x189.png)](http://blog.ianbeyer.com/files/2010/02/02-21-10-AM-CPU.png)[/caption]

Most weeks, we run two [Wowza](http://wowzamedia.com) repeaters pulling from a single origin server, which gives us plenty of capacity. I had to spin up a third repeater by the beginning of the pre-service music, a fourth about 10 minutes later, and a fifth after five more minutes. I set my threshold for spinning a new server at 75% CPU on the repeaters, as indicated by the AWS CloudWatch monitors. In the case of a heavy influx of viewers, this gives the new instance enough time to get up and running before the other repeaters hit 100% CPU.  Wowza tells me this is at about 180Mbit/sec on a small instance, which for us means around 300 streams. The CPU threshold of 75% works out to about 260 streams.

Unfortunately for our online worshipers, our web server was bogging down pretty hard at

[caption id="attachment\_370" align="alignright" width="300" caption="Web Server CPU usage"][![Web Server CPU usage]({{site.baseurl}}/assets/2010/02/web-cpu-300x152.png)](http://blog.ianbeyer.com/files/2010/02/web-cpu.png)[/caption]

the beginning of the service, where the two CPU cores were maxed out for about 15-20 minutes, which translated into slower page loads. The database server wasn't sweating too hard, so I suspect this could have been helped with better PHP caching. Fortunately for me, this had the effect of slowing down the rate of incoming streams, which allowed me to get new repeaters going before the existing ones started choking.

You can see in the graph where we added new repeaters, and how fast they ramped up. It also shows how incredibly well Wowza's built-in load balancing works. We eventually leveled out at a little over 1100 streams, which meant our EC2 instances were cranking out 600-700 Mbps for nearly an hour:

[caption id="attachment\_369" align="aligncenter" width="300" caption="AWS Network Usage"][![AWS Network Usage]({{site.baseurl}}/assets/2010/02/02-21-10-AM-Network-300x201.png)](http://blog.ianbeyer.com/files/2010/02/02-21-10-AM-Network.png)[/caption]

Meanwhile, this is what we were seeing on Woopra (note the fortunate souls escaping the ice storm in Aruba and the Cayman Islands!):

[![2-21-10-AM]({{site.baseurl}}/assets/2010/02/2-21-10-AM-300x187.png)](http://blog.ianbeyer.com/files/2010/02/2-21-10-AM.png)

Next step is to define rules in Cloudwatch for automatically scaling. For that to work, I'm going to need to build my own Wowza AMI, since the current method of starting repeaters involves sending the instance a startup package from the client. I'll need to build this configuration into the server for CloudWatch scaling to work properly.
