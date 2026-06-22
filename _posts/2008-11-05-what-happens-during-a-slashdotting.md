---
layout: post
title: What happens during a slashdotting?
date: 2008-11-05 23:07:56.000000000 -06:00
type: post
parent_id: '0'
published: true
password: ''
status: publish
categories:
- networking
tags:
- Consumerist
- Internet Campus
- megablog
- WUG
meta:
  dsq_thread_id: '262710005'
  _googl_shortlink: http://goo.gl/pLsS5
  _edit_last: '1'
author:
  login: ianbeyer
  email: ian.beyer@gmail.com
  display_name: Ian Beyer
  first_name: Ian
  last_name: Beyer
permalink: "/2008/11/05/what-happens-during-a-slashdotting/"
image: "/assets/images/2008/11/consumeristapache.png"
---

Well, OK, it wasn't [Slashdot](http://www.slashdot.org "Slashdot") that was the culprit this time, but rather the pro blog [Consumerist](http://www.consumerist.com "Consumerist") (if we're a megachurch, does Consumerist count as a megablog? It claims nearly 3 million unique visitors a month)

Last week, [Clif](http://www.clifguy.com "Clif Guy ALL THE TIME!") [posted about his experience at Best Buy](http://clifguy.com/2008/10/30/worst-buy/ "Worst Buy?"). Seems the folks at [Gawker Media](http://www.gawker.com "Gawker Media") got wind of the story (Best Buy is a perennial favourite target of theirs) and [posted it](http://consumerist.com/5077143/best-buy-sells-new-laptop-used-by-employee) at 10:21am Eastern, 9:21 in KC. Here's what happened to our [Wordpress server](http://mu.wordpress.org/ "Wordpress MU"):

[caption id="attachment\_88" align="aligncenter" width="500" caption="Apache Processes, November 5"][![Apache Processes, November 5]({{site.baseurl}}/assets/2008/11/consumeristapache.png)](http://nerdian.ca/files/2008/11/consumeristapache.png)[/caption]

[caption id="attachment\_89" align="aligncenter" width="500" caption="Web Datacenter traffic, November 5 (% of 10Mbps link)"][![Web Datacenter traffic, November 5 (% of 10Mbps link)]({{site.baseurl}}/assets/2008/11/consumeristtraffic.png)](http://nerdian.ca/files/2008/11/consumeristtraffic.png)[/caption]

Wow. I noticed the odd traffic behaviour (that particular server gets very little traffic most of the time) when I got in the office, and called a few folks to see if they'd done anything that would cause this. When that came up empty, I started looking at the access logs on the server and noticed a lot of referrer traffic from Consumerist. I threw [AWstats](http://awstats.sourceforge.net "AWStats") onto the server to grok the apache logs. At posting time, Clif's blog post had seen around 7000 visitors. Apache peaks out at a point due to the [MaxClients directive](http://httpd.apache.org/docs/1.3/mod/core.html#maxclients "MaxClients"), in order to keep the CPU from saturating and killing the site.

It's always fun to see new an interesting traffic patterns. It's very helpful to have active monitoring to tell us when things leap outside the bounds of normalcy.
