---
layout: post
title: Live Streaming on a Budget (Part eleventy point one) – Metrics Revisited
date: 2009-11-18 13:58:49.000000000 -06:00
type: post
parent_id: '0'
published: true
password: ''
status: publish
categories:
- Internet Campus
- streaming
- Wowza
tags: []
meta:
  _edit_last: '1'
  dsq_thread_id: '217877522'
  s2mail: 'yes'
  _googl_shortlink: http://goo.gl/7ORgR
author:
  login: ianbeyer
  email: ian.beyer@gmail.com
  display_name: Ian Beyer
  first_name: Ian
  last_name: Beyer
permalink: "/2009/11/18/live-streaming-on-a-budget-part-eleventy-point-one-metrics-revisited/"
image: "/assets/images/2009/11/streams-200911151215.png"
---

Back in July, I made a [post about metrics](http://blog.ianbeyer.com/2009/07/12/live-streaming-on-a-budget-part-eleventy-metrics/ "Live Streaming on a Budget (Part eleventy) – Metrics") and a cheesy VB Script that got the job done, but wasn't particularly elegant. I've since improved on this due to load balancing (I [posted about that](http://blog.ianbeyer.com/2009/09/27/live-streaming-on-a-budget-wowza-load-balancing-part-um-how-many-is-it-now/ "Live Streaming on a budget: Wowza Load Balancing (Part … um.. how many is it now?)") in September).

I've since then learned a bunch about [RRDTool](http://oss.oetiker.ch/rrdtool/), and have put together a script that pulls the XML data, groks it, and then populates an RRD. The net result is that I get a graph like this:

![streams-200911151215]({{site.baseurl}}/assets/2009/11/streams-200911151215.png)

This graph gives me the following information: The iPhone stream count (with a 10:1 vertical exaggeration), the Flash stream count, and the total viewer count, which is the sum of Flash and iPhone streams, multiplied by a factor of 1.7 (which we've found reasonably reflects how many actual people are watching, versus streams. Then the vertical red line shows the time the peak occurred, and the horizontal line shows the level of that peak. The actual peak numbers are listed on the bottom. The RRD and the graph are set up to take into account Windows streams, just as soon as I find a good way to pull that data from WMI via perl.

The general operation is as follows: There's a [script](http://blog.ianbeyer.com/code/backend/wowza-metrics-perl/ "Wowza stats collector with RRD (perl)") that's started in a cron job 10 minutes after the servers are spun up, and it polls the origin server every 10 seconds for its counts and populates the RRD. There's another cron job that runs every minute to [generate a current graph](http://blog.ianbeyer.com/code/backend/rrd-graphing/ "RRD Graphing Script (bash)"), which is then displayed on a page with [some javascript](http://blog.ianbeyer.com/code/client/js-image-refresh/ "Image refresh (javascript)") that refreshes the image in realtime. Then, at 12:15 and 6:30, there's another cron job that takes a snapshot of the previous two hours, puts it into a web-accessible directory, and appends an HTML file with a link for easy access later.

All of the metrics scripts, automation scripts, and graphing tools live on a linux virtual machine that runs on our central campus.

This is big improvement over dumping a vbscript into a CSV and then graphing manually with Excel. This happens automatically, in real time, without me being there.
