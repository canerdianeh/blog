---
layout: post
title: Wowza/EC2 Q&A Session
date: 2013-02-10 18:36:21.000000000 -06:00
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
  _wpas_done_all: '1'
  dsq_thread_id: '1076151771'
author:
  login: ianbeyer
  email: ian.beyer@gmail.com
  display_name: Ian Beyer
  first_name: Ian
  last_name: Beyer
permalink: "/2013/02/10/wowza-ec2-qa-session/"
image: "http://blog.ianbeyer.com/files/2013/02/Screen-Shot-2013-02-10-at-6.05.01-PM-1024x482.png"
---

I'll admit, the nerd meter on here has been running past redline for a while, so I'm going to step back and answer some questions that have come in via e-mail or [twitter](http://twitter.com/ianbeyer "Ian Beyer Twitter") from those of you still trying to get started with Wowza streaming.

#### **Q: How do I find a good Wowza EC2 server to use, what should I be using?**

A: I understand your confusion. There are a lot of Wowza AMIs out there on the EC2 stack, and that's just the official ones! When starting an instance from the AWS console, simply searching for "wowza" under the community AMIs is a bit of a daunting process. Just in us-east-1, you get 68 results:

![Starting Wowza on EC2]({{site.baseurl}}/assets/2013/02/Screen-Shot-2013-02-10-at-6.05.01-PM-1024x482.png)

As a general rule, the most recent version available is the one you want to use. Wowza keeps a [list of the most recent AMIs](http://www.wowza.com/forums/content.php?23-pre-built-amis-(amazon-machine-images) "Wowza EC2 Current AMIs") on their support site, and unless you have bought a license (Plug: I'm a reseller, support your streamnerd!), you'll want to use the DevPay instances which require a $5 monthly subscription from Amazon.

If you need to run an older version, Wowza's support team can give you the AMI ID you need, as they continue to make older versions available (which is why you get such a huge list), although they're not maintained once a newer AMI has been released. With a few exceptions, startup packages designed for one version will generally work on another version.

Where it gets complicated is if you're dealing with BYO Licenses and Marketplace instances. That's probably a topic for another post.

#### Q: How do I know if I need to set up load balancing and how do I do that, in plain English?

A: Simply put, you'll need to do load balancing any time the audience on your server exceeds the network throughput that your instance size will support. Wowza has published some numbers in the past for a few of the instance sizes, but those numbers are several years old, and changes to both Amazon's infrastructure and the Wowza code base have rendered them obsolete. Since I now manage some very large Wowza servers outside the Amazon stack, I will be running some new benchmarking tests in the next few weeks. When I get the results, I'll be posting those here as well as sharing them with the Wowza team.

The best way to make your Wowza stack scalable is to configure your single server as both an origin and an edge, and make it a load balancing army of one. That way, if you get an unexpected surge in traffic, adding more repeaters is a fairly simple task. All you need to do is keep a set of startup packages with the configuration for each type on hand, and you can start them up.

The key thing to remember about Wowza load balancing is that the load balancer and the origin/edge architecture are independent of each other. In an origin/edge configuration, you publish to one application, and another application (on either the same server or a different server) pull the stream from the origin application and then distribute it out to clients.

There are many ways to determine which edge application a client goes to, but the most common one is the Wowza load balancer module. This module consists of a "sender" that lives on edge servers, and a "listener" that lives on the load balancing server (which is usually the origin server, but doesn't have to be). The sender keeps track of how many connections are on its server, and reports those back to the listener along with its address and a unique identifier. When queried, the load balancer will then provide the address of whichever server has the fewest connections (or an XML dump listing all the servers in the pool and their status).

Once you have the information of which server has the fewest connections, it's simply a matter of directing an incoming connection to that edge server. The load balancer package provides an application that will redirect RTMP clients, but that doesn't work with HTTP clients such as iOS and Android devices, so you'll need some additional steps for them.

#### Q: I can check connection counts for stats, but all other posts I read about analytics is confusing. Is there a better, easier way?

One of the most challenging things about Wowza facing new users is that it lacks all the pretty graphs - but the flip side of that is that you get access to raw data. Out of the box, there's not really anything other than the connectioncounts.xml and serverinfo.xml XML dumps. There are a number of third-party components that can massage this data into something a little more useful and "boss-friendly". On the commercial side there's CasterStats (Plug: I'm a reseller. Support your streamnerd!) which can do both live stats and post-analysis of log files, as well as Sawmill and AWStats which will analyze logs. There are probably a few others as well. And, naturaly, there are also a number of PHP scripts that I've posted on this blog before that can help with analyzing and processing the XML dumps.

One final plug: If you're interested in a web-based control system that manages your startup packages and live stats, ask me about cdnBuilder.

That's all for today, if you've got a Wowza question (EC2 or not!), drop me a line on [twitter](http://twitter.com/ianbeyer "Ian Beyer on Twitter") or leave me a comment below!
