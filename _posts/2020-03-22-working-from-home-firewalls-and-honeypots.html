---
layout: post
title: 'Working From Home: Firewalls and Honeypots'
date: 2020-03-22 12:55:32.000000000 -05:00
type: post
parent_id: '0'
published: true
password: ''
status: publish
categories:
- networking
- Working from Home
tags:
- Honeypot
- Security
meta:
  _publicize_twitter_user: "@CaNerdIan"
  _wpas_done_all: '1'
  _thumbnail_id: '1688'
  spay_email: ''
  _wpas_mess: 'Blogged: Working From Home: Firewalls and Honeypots'
  _edit_last: '2'
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
permalink: "/2020/03/22/working-from-home-firewalls-and-honeypots/"
image: "https://nerdian.ca/files/2020/03/Screen-Shot-2020-03-22-at-1.24.27-PM.png"
---

Yesterday, I saw a social media post from my friend Thorsten, who is an engineer for a large network security company, in which he shared some nifty dashboard graphics from his installation of a nifty little Linux distribution known as [T-Pot](https://github.com/dtag-dev-sec/tpotce) (I'm a total sucker for great dashboards!).

T-Pot is a collection of various [network honeypots](https://en.wikipedia.org/wiki/Honeypot_(computing)) with a very nice reporting backend. The project is maintained by Deutsche Telekom, who use it extensively within their own networks. (*disclosure: If you run it, it will send back anonymized collected information about the threats seen to their data lake*)

So I'm going to veer off a little bit from my regularly scheduled Working From Home series and talk about the importance of securing your networks. T-Pot won't actually *secure* your network, it will merely report on the threat actors (most of them automated) that are attacking your network every second of the day. And to a small extent, time they spend "attacking" your honeypot is time they're not spending attacking real targets (like Pooh up there at the top)

T-Pot takes about 30 minutes to install on a virtual machine (put it in a VLAN that is isolated from everything else!) and then all you do is add a firewall rule to port forward all TCP/UDP (I also did ICMP) to that machine (after any rules to forward to actual stuff), and let it do its thing.

Results will start coming in almost instantly. In a matter of minutes, I'd collected literally hundreds of attacks. After a couple of hours, the numbers were a little disturbing. About 90 minutes after going live, I saw a sharp uptick in one type of attack, as it seems the attackers had found a new target and relayed that information to other attackers.

![]({{site.baseurl}}/assets/2020/03/Screen-Shot-2020-03-22-at-1.24.27-PM-1024x562.png)  

2.5 hours worth of data.

![]({{site.baseurl}}/assets/2020/03/Screen-Shot-2020-03-22-at-1.24.39-PM-1024x531.png)  

China, Russia, and.. Canada?

![]({{site.baseurl}}/assets/2020/03/Screen-Shot-2020-03-22-at-1.25.14-PM-1024x511.png)  

the T-Pot dashboard will show you what usernames and passwords are being used against your honeypot, as well as which known vulnerabilities were being exploited.

If you're a business hastily trying to get people to work from home, did you just open up a port forward on your Layer 3 firewall to allow Remote Desktop? That probably wasn't a great idea. As you can see, threat actors are constantly scanning each and every IP address on the internet, probing for vulnerabilities. All it takes is one successful entry into your network, and you're toast. That can come through your homebound workers as well, if their networks aren't secure.

Do you still think you don't need a Layer 7 firewall?
