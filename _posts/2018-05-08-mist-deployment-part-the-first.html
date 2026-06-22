---
layout: post
title: Mist Deployment (Part The First)
date: 2018-05-08 22:13:06.000000000 -05:00
type: post
parent_id: '0'
published: true
password: ''
status: publish
categories:
- Church IT
- Cloud Computing
- Hardware
- IT
- networking
- Wireless
tags:
- Mist
meta:
  _edit_last: '2'
  _publicize_twitter_user: "@CaNerdIan"
  _thumbnail_id: '1533'
  _wpas_done_all: '1'
  _wpas_skip_19898085: '1'
  _wpas_skip_19898087: '1'
  _wpas_skip_19898090: '1'
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
permalink: "/2018/05/08/mist-deployment-part-the-first/"
image: "https://nerdian.ca/files/2018/05/302569-nature-landscape-lake-mist-mountain-morning-forest-Scotland-trees-island-748x409.jpg"
---

*First in a series about our first deployment of a Mist Systems wireless network.*![Mist Systems Logo]({{site.baseurl}}/assets/2018/05/MistLogo-300x289.png)

Over the course of the past few months, I’ve been working with the IT staff at [College Park Church](//yourchurch.com) in Indianapolis to overhaul their aging Ubiquiti UniFi wireless system. They initially were looking at a Ruckus system, owing to its widespread use among other churches involved with the [Church IT Network](//churchitnetwork.com) and its national conference (where I gave a presentation on Wi-Fi last fall). We had recently signed on as a partner with industry newcomer [Mist Systems](//mistsys.com), and had prepared a few designs of similar size and scope for other churches in the Indianapolis area using the Mist system. We proposed a design with [Ruckus](//ruckusnetworks.com), and another with Mist, with the church selecting Mist for its magic sauce, which is its Bluetooth Low Energy (BLE) capability for location engagement and analytics.

Fundamentally, the AP count, coverage, and capacity were not significantly different with Ruckus vs. Mist, and Mist offered a few advantages over the Ruckus in terms of the ability to add external antennas for creating smaller cells in the sanctuary from the APs mounted on the catwalks, as floor mounting was not an option.

## About Mist

Mist is a young company that’s been around for about two or three years, and they have developed a couple of cool things in their platform - The first is what they call their AI cloud, the second is their BLE subsystem, and the last is their API.

Their AI component is a cloud management dashboard (similar to what you would see with Ruckus Cloud or Meraki — many of the engineers that started with Mist came over from Meraki), where the APs are constantly analyzing AP and client performance through frame capture and analysis, and reporting it back to the cloud controller. The philosophy here is that a large majority of the issues that users have with Wi-Fi performance is actually related to performance on the wired side of the network ("It's always DNS." Not always, but DNS -- and DHCP -- are major sources of Wi-Fi pain). The machine learning AI backend is looking at the stream of frames to detect problems, and then using that to generate Wi-Fi SLA metrics that can help determine where problems lie within the infrastructure, and doing some analysis of root causes. An example of this is monitoring the entire Station/AP conversation during and shortly following the association process. It looks at how long association took. How long DHCP took (and if it was successful), whether 4-way handshakes completed, and so on. It will also keep a frame capture of that conversation for further manual troubleshooting. It also keeps a log of AP-level events such as reboots and code changes so that client errors can be correlated on a timeline to those events. There’s a lot more it can do, and I’m just giving a brief summary here. Mist has lots of [informational material on their website](https://www.mist.com/products/) (and admittedly, there’s a goodly amount of marketing fluff in it, but that’s what you’d expect on the vendor website).

![Graphs of connection metrics from the Mist system]({{site.baseurl}}/assets/2018/05/Screenshot-2018-05-08-22.52.14-1024x509.png)

Next, we have their BLE array. This is what really sets Mist apart from the others, and is one of the more interesting pieces of tech to show up in wifi hardware since Ruckus came on the scene with their adaptive antenna technology. Each AP has not one, but \*eight\* BLE radios in it, coupled with a 16-element antenna array (8 TX, 8RX). Each antenna provides an approximately 45° beam covering a full circle. Mist is able to use this in two key ways. One is the ability to get ridiculously precise BLE location information from their mobile SDK, (and by extension, locate a BLE transponder for asset visibility/tracking) and the other is the ability to use multiple APs to place a virtual BLE beacon anywhere you want without having to go physically install a battery-powered beacon. There are myriad uses for this in retail environments, and the possibilities for engagement and asset tracking are very interesting in the church world as well.

Lastly, we have their API. According to Mist, their cloud controller’s web UI only exposes about 40% of what their system can do. The remainder is available via a REST API that will allow you do do all kinds of neat tricks with it. I haven’t had a chance to dig into this much yet, but there’s a tremendous amount of potential there. Jake Snyder has taught a 3-day boot camp on using Python in network administration to leverage the power of APIs like the one from Mist (Ruckus also has an API on their Cloud and SmartZone controllers)

Mist is also updating their feature set on a weekly basis - rather than one big update every 6 months that may or may not break stuff, small weekly releases allow them to deploy features in a more controlled manner, making it easy to track down any potential show-stopper bugs, preferably before they get released into the wild. You can select whether your APs get the early-release updates, or use a more extensively tested stable channel.

Much like Meraki, having all your AP data in the cloud is tremendously useful when contacting support, as they have access to your controller data without you having to ship it to them. They can also take database snapshots and develop/test new features based on real data from the field rather than simulated data. No actual upper-layer traffic is captured.

## The Hardware

note: all prices are US list - specific pricing will be up to your partner and geography.

There are four APs in the Mist line. The flagship 4x4 AP41 ($1385), the lower-end AP21 ($845), the outdoor AP61 ($?) , and the BLE-only BT11 ($?). The AP41 also comes in a connectorized version called the AP41E, at the same price as the AP41 with the internal antenna.

The AP41/41E is built on a cast aluminum heat sink, making the AP noticeably heavy. It offers an Ethernet output port, a USB port, a console port, and what they call an “IoT port” that provides for some analog sensor inputs, Arduino-style. It requires 802.3at (PoE+) power, or can use an external 12V supply with a standard 5.5x2.5mm coaxial connector. In addition to the 4-chain Wifi radio and the BLE array, the AP41 also has a scanning radio for reading the RF environment. On the AP41E, the antenna connectors are located on the downward face of the AP.

The AP21 is an all-plastic unit that uses the same mounting spacing as the AP41, and has an Ethernet pass-through port with PoE (presumably to power downstream BT11 units or cameras). Like the AP41, it also has the external 12V supply option.

This install didn’t make use of BT11 or AP61 units, so I don’t have much hands-on info about them.

It's also important to note that none of these APs ship with a mounting bracket, nor does the AP have any kind of integrated mounting like you would find on a Ruckus AP. Mist currently offers 3 mounting brackets: a T-Rail bracket ($25), a drywall bracket ($25) and a threaded rod bracket ($40). The AP attaches to these brackets via four T10 metric shoulder screws (Drywall, Rod), or four metric Phillips screws (T-Rail). More on these later.

### The Software

Each AP must be licensed, and there are three possibilities: Wifi-only, BLE Engagement, and BLE Asset tracking. Each subscription is nominally $150/year per AP, although there are bundles available with either two services or all three. Again, your pricing will depend on your location and your specific partner. Mist recently did away with multi-year pricing, so there’s no longer a cost advantage in pre-buying multiple years of subscriptions.

When the subscription expires, Mist won’t shut off the AP the way Meraki does, however, the APs will no longer have warranty coverage. After a subscription has been expired for two months, Mist will not reactivate an AP. The APs will continue to operate with their last configuration, however, but there will no longer be access to the cloud dashboard for that AP.

### Links:

[Mist Systems](http://mistsystems.com)

[Jake Snyder on Clear To Send podcast #114: Automate or Die](http://www.cleartosend.net/cts-114-automate-or-die/)

[Mist Product Information](https://www.mist.com/resources/?resourcelib_category=product-information)

**Up Next:** [The Design](http://blog.ianbeyer.com/2018/05/10/mist-deployment-part-2/)
