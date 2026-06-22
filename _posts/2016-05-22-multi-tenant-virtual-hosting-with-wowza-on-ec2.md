---
layout: post
title: Multi-tenant Virtual Hosting with Wowza on EC2
date: 2016-05-22 13:01:59.000000000 -05:00
type: post
parent_id: '0'
published: true
password: ''
status: publish
categories:
- Cloud Computing
- networking
- streaming
tags:
- ec2
- VPC
- wowza
meta:
  _edit_last: '2'
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
permalink: "/2016/05/22/multi-tenant-virtual-hosting-with-wowza-on-ec2/"
---

That's a mouthful, isn't it?

I recently needed to migrate a couple of Wowza Streaming Engine tenants on a baremetal server that was getting long in the tooth, and was getting rather expensive. These tenants were low-volume DVR or HTTP transmuxing customers, with one transcoding customer that required some more CPU power. But this box was idle most of the time. So I decided to move it over to AWS and fire up the box only when necessary. Doing this used to be a cumbersome process with the AWS command-line tools that were Java-based. The current incarnation of tools is quite intuitive and runs in Python, so there's not a lot of insane configuration and scripting to do.

You may recall my [post from a few years back about multi-tenant virtual hosting](http://nerdian.ca/2014/04/16/multi-tenant-hosting-for-wowza/). I'm going to expand on this and describe how to do it within the Amazon EC2 environment, which has historically limited you to  a single IP address on a system.

The first step to getting multiple network interfaces on EC2 is to create a Virtual Private Cloud (VPC) and start your EC2 instances within your VPC. "Classic" EC2 does not support multiple network interfaces.

Once you've started your Wowza instance within your VPC (for purposes of transcoding a single stream, I'm using a c4.2xlarge instance), you then go to the EC2 console, and on the left-hand toolbar, under "network and security" is a link labeled "Network Interfaces". When you click on that, you have a page listing all your active interfaces.

To add an interface to an instance, simply create a network interface, select the VPC subnet it's on, and optionally set its IP (the VPC subnet is all yours, in dedicated RFC1918 space, so you can select your IP). Once it's created, you can then assign that interface to any running instance. It shows up immediately within the instance without needing to reboot.

Since this interface is within the VPC, it doesn't get an external IP address by default, so you'll want to assign an ElasticIP to it if you wish to have it available externally (in most cases, that's the whole point of this exercise)

Once you have the new interface assigned, simply configure the VHosts.xml and associated VHost.xml files to listen to those specific internal IP addresses, and you're in business.  
As for scheduling the instance? On another machine that IS running 24/7 (if you want to stick to the AWS universe, you can do this in a free tier micro instance), [set up the AWS command line tools](http://docs.aws.amazon.com/cli/latest/userguide/installing.html) and then make a crontab entry like this:

```

30 12 * * 1-5 aws ec2 start-instances --instance-ids i-XXXXXXXX
35 12 * * 1-5 aws ec2 associate-address --network-interface-id eni-XXXXXXXX --allocation-id eipalloc-XXXXXXXX
35 12 * * 1-5 aws ec2 associate-address --network-interface-id eni-XXXXXXXX --allocation-id eipalloc-XXXXXXXX
30 15 * * 1-5 aws ec2 stop-instances --instance-ids i-XXXXXXXX
```

This fires up the instance at 12:30pm on weekdays, assigns the elastic IPs to the interfaces, and then shuts it all down 3 hours later (because this is an EBS-backed instance in a VPC, stopping the instance doesn't nuke it like terminating does, so any configuration you make on the system is persistent)

Another way you can use this is to put multiple interfaces on an instance with high networking performance and gain the additional bandwidth of the multiple interfaces (due to Java limitations, there's no point in going past 4 interfaces in this use case), and then put the IP addresses in either a round-robin DNS or a load balancer, and simply have Wowza bind to all IPs (which it does by default).
