---
layout: post
title: High-Availability firewall on the cheap!
date: 2008-06-17 16:23:27.000000000 -05:00
type: post
parent_id: '0'
published: true
password: ''
status: publish
categories:
- networking
tags:
- BSD
- firewall
- pfSense
meta:
  dsq_thread_id: '217877551'
  _googl_shortlink: http://goo.gl/pOjSj
author:
  login: ianbeyer
  email: ian.beyer@gmail.com
  display_name: Ian Beyer
  first_name: Ian
  last_name: Beyer
permalink: "/2008/06/17/high-availability-firewall-on-the-cheap/"
---

I now have a profound appreciation for [BSD](http://www.bsd.org/).

Yesterday, our [pfSense](http://www.pfsense.org) firewall at [1102 Grand](http://www.1102grand.com) suddenly went silent and the panel on [WhatsUp](http://www.whatsupgold.com/) for that site went all red. Not good. I went down to the cage after small group last night and found the machine to have just simply locked up cold. I suspect hardware, since pfSense/BSD didn't log a thing about it going dark.

It became quite clear that this setup was... suboptimal. [Clif](http://www.clifguy.com "Clif Guy ALL THE TIME!")'s shooting for 99.99% on this new setup. I can't be racing off to the datacenter every time the firewall machine decides to take a holiday from reality. [Brian](http://officecurmudgeon.com/) and I quickly determined that we needed not only a [remote power control unit](http://www.corpsys.com/store/prodinfo.asp?number=EPCR2), but some sort of high-availability solution that wasn't going to [empty our wallet](http://www.barackobama.com) like a pair of [NSA 4500](http://sonicwall.com/us/products/NSA_4500.html)s would. (sorry [Mark](http://christsitguy.spaces.live.com/ "Mark Moreno"), we simply don't have that kind of money) We already had a spare, identical machine at the datacenter doing duty as a hardware spare and development server, and another one just like it in inventory at the Central Campus. I grabbed the extra machine and went back 1102 Grand for the second time in 12 hours, with a quick stop at [Micro Center](http://www.microcenter.com) for some [cheap NICs](http://www.linksys.com/servlet/Satellite?c=L_Product_C2&childpagename=US%2FLayout&cid=1129151689795&pagename=Linksys%2FCommon%2FVisitorWrapper&lid=8979522279B11 "Linksys!") and a red [crossover cable](http://en.wikipedia.org/wiki/Ethernet_crossover_cable).

Fortunately, pfSense has high availability capability built in, thanks to BSD's CARP and pfSync. CARP allows me to set up virtual IPs on both firewalls and synchronize between them with pfSync. The extra NICs were for a dedicated sync/heartbeat link between the two boxes. I'm still a little fuzzy on the technical details of how this works, but it works... Convergence/Failover time is 3 seconds or less, and everything is synchronized between the two machines, including state and session information. I had it all set up, and hit the reset button on the primary firewall... and nary a ping was dropped.  
The setup involves giving each machine its own LAN and WAN addresses (and a unique address on the other zones as well) and then creating a CARP virtual IP on that interface. The virtual IP is the one used as the gateway and as the NAT address. All rules and configs (including IPSEC Tunnels!) is mirrored on the second box.

Reference material:

[Excellent documentation](http://www.countersiege.com/doc/pfsync-carp/ "pfSync/CARP") on the process from the folks at [Countersiege](http://www.countersiege.com/).

Some [background](http://www.openbsd.org/faq/pf/carp.html) from the [OpenBSD](http://www.openbsd.org) folks.

A few good [tips](http://devwiki.pfsense.org/CARPConfigurationSyncTroubleShooting?show_comments=1#comments) here. These proved to be crucial.
