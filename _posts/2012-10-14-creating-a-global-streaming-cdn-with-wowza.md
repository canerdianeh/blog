---
layout: post
title: Creating a global streaming CDN with Wowza
date: 2012-10-14 17:15:47.000000000 -05:00
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
  dsq_thread_id: '885345471'
author:
  login: ianbeyer
  email: ian.beyer@gmail.com
  display_name: Ian Beyer
  first_name: Ian
  last_name: Beyer
permalink: "/2012/10/14/creating-a-global-streaming-cdn-with-wowza/"
---

I've posted in the past about the various components involved in doing [edge](http://nerdian.ca/code/ec2/wowza-edge-startup-bash/ "Edge Server Startup Script (bash)")/[origin](http://nerdian.ca/code/ec2/ec2-wowza-origin-server-shutdown/ "Origin Server Shutdown Script") setups with Wowza, as well as [startup packages](http://nerdian.ca/2011/01/26/wowza-startup-packages/ "Inside Wowza Startup Packages") and [Route 53 DNS magic](http://nerdian.ca/2012/09/11/adding-ec2-to-route53/ "Adding EC2 instances to Route53"). In this post, I'll tie the various pieces together to put together a geographically-distributed CDN using Wowza.

For the purposes of this hypothetical CDN, we'll do it all within EC2 (although there's no reason it has to be), with three edge servers in each availability zone.

There are two ways we can do load balancing within each zone. One is to use the Wowza load balancer, and the other is to use round-robin DNS. The latter is not as evenly balanced as the former, but should work reasonably well. If you're using set-top devices like Roku, you'll likely want to use DNS as redirects aren't well supported in the Roku code.

For each zone, create the following DNS entries in Route 53. If you use your registrar's DNS, you'll probably want to create a domain name as many registrar DNS servers don't deal well with third-level domains (sub.domain.tld). For the purposes of this example, I'll use nhicdn.net, the domain I use for [Nerd Herd](http://www.nerdherd.net "Nerd Herd, Inc. ") streaming services. None of these hostnames actually exist.

We'll start with Wowza's load balancer module. Since the load balancer is not in any way tied to the origin server (although they frequently run on the same system), you can create a load balancer on one of the edge servers in that zone. Point the loadbalancertargets.txt on each edge server in that zone to that server, and point to the origin stream in the Application.xml configuration file. Once the load balancer is created, create a simple CNAME entry in Route 53 called lb-zone.nhicdn.net, pointing to the hostname of the load balancer server:

***lb-us-east.nhicdn.net CNAME ec2-10-20-30-40.compute-1.amazonaws.com***

If you opt to use DNS for load balancing, again point the Application.xml to the origin stream, and then create a weighted CNAME entry to each server in that zone, all with the same host record, each with equal weight (1 works):

***lb-us-east.nhicdn.net CNAME ec2-10-20-30-40.compute-1.amazonaws.com***  
 ***lb-us-east.nhicdn.net CNAME ec2-10-20-30-41.compute-1.amazonaws.com***  
 ***lb-us-east.nhicdn.net CNAME ec2-10-20-30-42.compute-1.amazonaws.com***

If you wish, you can also create a simple CNAME alias for each server for easier tracking - this is strictly optional:

***edge-us-east1.nhicdn.net CNAME ec2-10-20-30-40.compute-1.amazonaws.com***  
 ***edge-us-east2.nhicdn.net CNAME ec2-10-20-30-41.compute-1.amazonaws.com***  
 ***edge-us-east3.nhicdn.net CNAME ec2-10-20-30-42.compute-1.amazonaws.com***

Once you've done this in each zone where you want servers, Create a set of latency-based CNAME entries for each lb entry:

***lb.nhicdn.net CNAME lb-us-east.nhicdn.net***  
 ***lb.nhicdn.net CNAME lb-us-west.nhicdn.net***  
 ***lb.nhicdn.net CNAME lb-europe.nhicdn.net***  
 ***lb.nhicdn.net CNAME lb-brazil.nhicdn.net***  
 ***lb.nhicdn.net CNAME lb-singapore.nhicdn.net***  
 ***lb.nhicdn.net CNAME lb-japan.nhicdn.net***

Once your DNS entries are in place, point your players to lb.nhicdn.net and use either the name of the edge application (if using DNS) or the redirect application (if using Wowza load balancer), and clients will go to either the edge server or load balancer for the closest region.

One other thing to consider is to set up a load balancer on your origin, and use that for gathering stats from the various servers. You can put multiple load balancers in the loadbalancertargets.txt file, so you can have each server report in to both its regional load balancer and the global one, except the global one is not being used to redirect clients, but rather only for statistics gathering. You can also put multiple load balancers in each region for redundancy and use a weighted CNAME entry.

If you would like assistance setting up a system like this for your organization, I am available for hire for consulting and/or training.
