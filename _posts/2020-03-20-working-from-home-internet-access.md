---
layout: post
title: 'Working From Home: Internet Access'
date: 2020-03-20 10:36:46.000000000 -05:00
type: post
parent_id: '0'
published: true
password: ''
status: publish
categories:
- Cloud Computing
- Hardware
- IT
- networking
- Working from Home
tags: []
meta:
  _publicize_twitter_user: "@CaNerdIan"
  _wpas_done_all: '1'
  _thumbnail_id: '1671'
  spay_email: ''
  _wpas_mess: 'New on the blog in my Working From Home series: Internet Access'
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
permalink: "/2020/03/20/working-from-home-internet-access/"
image: "https://nerdian.ca/files/2020/03/AdobeStock_234092604-scaled.jpeg"
---

In my [previous post](https://nerdian.ca/2020/03/18/working-from-home-the-basics/), I went over the basics of working from home. It's worth noting here that many of these concepts can also be applied to your kids who might be taking school online - they're teleworking just like you are, and face many of the same challenges. In this and future posts, I'll be dealing with the tech basics required for a successful and productive home office.

I was originally going to do a single post on all things tech, but it started getting lengthy, so I decided to break it down into a couple of parts. This post will deal specifically with external network connectivity.

## The Internet

No surprises here - a decent internet connection is pretty much a given for remote work. One thing that is becoming apparent during this quarantine period is that a whole lot of people have abysmally bad internet connections at home. I'm hearing horror stories from the trenches, from my colleagues and friends who work front-line IT support.

The word "Broadband" is thrown around a lot by ISPs intent on selling you a service package, but what does it really *mean*? In the United States, the Federal Communications Commission updated their definition of "broadband" most recently in 2015, to mean a connection speed of at least 25Mbps downstream (from ISP to your house), and 3Mbps upstream (from your house to your ISP. But what do those speeds really mean? The FCC also has a [handy guide](https://www.fcc.gov/consumers/guides/broadband-speed-guide) listing what activities require what level of speed.

So your Cable ISP touts their "SuperGigaFast" service with "gigabit" service. Sounds great, right? Not so fast. Cable-based ISPs that come into your house via a coaxial cable use a technology called DOCSIS, which has great downstream speeds, and (usually) abysmally bad upstream speeds. The cable companies originally designed this technology back in the late 1990s when internet usage consisted largely of downloading web pages and sending small bits of control data. This meant that an asymmetrical connection would work great for most users, and they would be able to leverage their existing wiring infrastructure.

Fast forward 25 years to 2020, and cloud-based data storage and teleconferencing and the like mean that you need a lot more upstream speed than you used to. But that hasn't stopped cable companies from selling "gigabit" packages with a paltry 10Mbps upstream connection. When getting an internet service package for teleworking, your upstream speed should be *at least* 10% of your downstream speed - because if you saturate your upstream link, it's going to negatively impact your downstream traffic and limit it. This lets the cable company sell you "gigabit", knowing full well that they'll never have to deliver on that promise. They also usually provide really cheap equipment which means your Wi-Fi speeds are going to be limited even more, and they still don't have to deliver on those gigabit speeds they're charging you for. If you have the option of a symmetrical connection (usually delivered over fiber optic cable), it will be a lot more functional.

Much of what applies to DOCSIS cable connections also applies to DSL connections from the local telephone company. Make sure you have enough upstream bandwidth to do what you need to do. Also beware of any service that has a data cap - working from home can blow through a data cap in a real hurry.

It's usually worth investing in your own router - the equipment provided by the ISP is, in most cases, absolute junk. AT&T is notoriously bad about this on both their U-Verse DSL and fiber-based services, and they have it configured such that it's very difficult to use a "real" router with their service.

And in some places, cable, fiber, or DSL aren't an option, and you're stuck with either a wireless ISP or cellular.

## Hardware

The typical internet connection requires a couple of devices. ISPs and telcos generally refer to this as "Customer Premises Equipment", or "CPE".

![1950s-era dial telephone using an acoustic coupler modem]({{site.baseurl}}/assets/2020/03/2979693877_5aa6ccec2e_o.jpg)

### The Modem

This is the device that interfaces your ISP's connection with your home network, usually via an Ethernet connection. The term comes from "**mod**ulation/**dem**odulation", which is the process of converting a data stream into a series of electrical signals. This operates between what us network nerds call "Layer 1" (electrical signals) and "Layer 2" (data link). I posted [on network layers in this post](https://nerdian.ca/2018/03/31/on-network-models/) from 2018, if you want to get into some of the details of those. The modem's primary function is extending your ISP's physical network to your house. Before the days of direct internet connections, the data link was established over a telephone line by modulating the data signals into electrical signals in the narrow audio range supported by the telephone system.

Modems can take many forms, and in many cases, your ISP's modem is integrated into a single device with a router. In the case of cable, you can usually supply your own. In the case of DSL or fiber service (where it's usually called an Optical Network Terminal instead of a modem) it's usually provided by the ISP and you won't get much choice in the matter, although sometimes it's possible to request a specific type or model.

Your smartphone also contains a modem that interfaces to the cellular networks - it likely uses LTE (4G), but older ones (3G) would use CDMA or GSM, and newer ones (5G) use a few different things, mostly based on LTE. If you need to interface a cellular network to your home network, either as a primary or backup link, there are dedicated cellular modem devices for that (more on that in a moment).

![GIF from "The IT Crowd" where Moss shows Jen a small black box, and tells her, "This, Jen, is the Internet"]({{site.baseurl}}/assets/2020/03/3486822e9654f3542cb64519b7d82f1e.gif)

### The Router

This is the device that connects *your* network to your ISP's network. It operates at "Layer 3", which for the vast majority of people means "the internet". The internet is nothing more than a whole bunch of **inter**connected **net**works. A protocol (known as the "Internet Protocol", or "IP") has been in place for decades, specifying how all these networks can talk to each other. Each network is connected to other networks by way of a router (also known as a "gateway"). Its job is to look at traffic that comes in, and decide where it needs to go next. If it's for another device on a network it's directly connected to, it sends it directly. For something elsewhere on the internet, it sends it to the next router down the line (usually your ISP) to deal with and eventually get it to where it needs to go. This process usually happens in a matter of milliseconds (you can use the "ping" command to see how long this takes, or "tracert" (windows)/"traceroute" (everything else) to see the path it takes. The whole idea is that you don't see what's happening under the hood.

The term "Router" is often misconstrued to mean "WiFi". This is often because the equipment provided by an ISP or purchased consists of a router, a network switch, and a Wi-Fi access point (and sometimes a modem) all in one box referred to as "the router".

Owing to a general shortage of IP addresses, your ISP will assign a single IP address (which is unique on the entire internet!) to your router's Internet-facing connection (the Wide Area Network/WAN interface), and your own network devices (on the Local Area Network/LAN interface) will occupy address space that is defined by [RFC1918](https://tools.ietf.org/html/rfc1918) as "private" address space (which can not be used directly on the internet, but can be re-used by anyone - in most cases, your network will be 192.168.*something,* the specifics vary from one devices to another). The router will then perform Network Address Translation (NAT) to move data between the two networks. Most of the time, you don't need to worry about the details of how it's set up, although when it comes to troubleshooting, having at least a general awareness of how it's set up can be useful.

![3D Illustrated representation of a firewall. ]({{site.baseurl}}/assets/2020/03/AdobeStock_137109535-1024x768.jpeg)

### The Firewall

This is a key piece of the network, as it is what decides which traffic is and isn't allowed. This is critical to providing network security. It is usually integrated into the router. It examines each packet and checks a list of rules (which can be updated multiple times a day to react to ongoing threats) to determine if the packet should be sent along its merry way, or dropped into a deep, dark hole.

![LAN Party]({{site.baseurl}}/assets/2020/03/lan-1.png)

### The Local Area Network

The router is the transition point from your network to the rest of the internet. I'm not going to get into the details of the LAN for the moment (that's for another post), but this is where you will connect all your equipment, either wirelessly via Wi-Fi, or via a wire to an Ethernet switch.

![Single car in a tunnel]({{site.baseurl}}/assets/2020/03/SJM-L-POWERDOWN-1009-13.jpg)

### Virtual Private Networking (VPNs)

This isn't really a hardware component, but is usually a key piece of any home office (it sometimes uses dedicated hardware, though). The function of a VPN is to connect you to another private LAN located elsewhere (either physically or just another part of the network.) When working from home, installing a dedicated private network connection between the main office to a home office is cost-prohibitive (although there are some interesting new technologies with 5G that will allow you to connect mobile devices directly to the corporate network, essentially making the corporate network its own cellular carrier.)

Enter the VPN - It uses the public internet to establish a connection to the corporate network, and it builds an encrypted tunnel that allows corporate traffic to pass through securely. Sometimes, this is an application that runs directly on a computer, establishing the tunnel directly to that computer, and sometimes, the tunnel is established by the network equipment you have at home, and it just presents another LAN for you to connect anything to. In most cases, in order to use bandwidth more efficiently, any traffic destined for the internet will go out directly from your router rather than through the tunnel and go out from the corporate network. This is known as a "split tunnel". Some companies, however, will choose to pass all traffic through the tunnel in order to benefit from high-power corporate firewalls to better secure traffic against malware, data leakage, or to just filter content.

As cloud-based services such as Office 365 become more prevalent, VPN connections back to the office are becoming less important.

It's worth noting that this is very different from public "VPN" services that claim to offer privacy when accessing the internet. While the underlying technology is similar, all these are doing is relocating where you hop on to the internet, sending it through the VPN service's network where they can inspect all your traffic.

![Home Network Equipment]({{site.baseurl}}/assets/2020/03/Rubber-Feet-for-Network-Equipment-1024x683.jpg)

## Equipment

A quick rundown of connectivity equipment:

#### Cellular Modems

If you need to connect to a cellular network, you can use the following:

- Your smartphone hotspot (easiest in a pinch, can also usually connect to your laptop via a USB cable if you don't want to or can't use Wi-Fi)
- A portable hotspot, sometimes called a "Mi-Fi" or a "Jetpack", both are brand names for common devices in this category. Many of these also can connect via USB.
- A USB cellular modem (check your cellular carrier for options)
- An Ethernet cellular modem or router such as a CradlePoint IBR series device

Some home routers and most enterprise routers will support a USB cellular modem as a WAN connection, either primary or as a backup.

#### Home Routers

There is a wide variety of these out there, and most of what you can get commercially will do the job better than what the ISP provides. NetGear and Asus both make devices that perform well, but these devices have limited security capabilities. TP-Link and Linksys are cheap, but tend to underperform. Plan on about $200-300 for these types of devices. I'll get into this a little more when I talk about the LAN side of things.

Many people recommend Ubiquiti equipment, but that's a lot more complex than I feel is appropriate for non-technical users. If it's what a managed service provider supplies, then it's quite adequate, but make sure they're the ones that have to deal with the technical side of it. If you're a network nerd, then you already know this stuff.

#### Enterprise Firewalls

This is where your corporate IT department or managed service provider usually comes into play, and provide you with a firewall/router device that is pre-configured for corporate networking and security standards (and will often set up a dedicated VPN connection as well). These devices come from a vendor like Fortinet, Aruba (in the form of a Remote Access Point), Palo Alto, Cisco/Meraki, and other enterprise networking vendors. These are helpful in a home office because they are generally managed by your MSP or IT department and are essentially plug and play, giving you a secure network connection that is functionally equivalent to being on the network at the office.

You can also purchase your own standalone firewall from these vendors, all of which have a home office model or two in their lineup. They usually come with an annual subscription cost which gives you frequent updates to the security profiles and rules, to adapt to the changing network threat landscape. These will typically provide much better security than a residential gateway device, but are more complex and expensive to operate.

## Summary/tl;dr

This got long (which is why I'm breaking tech up into multiple posts), but the bottom line is that your internet connection is a vital piece of the home office puzzle, and it's one where you're going to want to spend some time and money getting it right. If you have to go cheap somewhere, this is not the place to do it, but you also don't need to go overboard.

My colleague Scott Lester also posted on his blog about [temporary internet access](https://blog.theitrebel.com/2020/03/20/temporary-network-connectivity-options/).

Please share your internet access related tips and experiences in the comments.
