---
layout: post
title: Another cool use of the WLANpi
date: 2019-11-08 10:41:15.000000000 -06:00
type: post
parent_id: '0'
published: true
password: ''
status: publish
categories:
- networking
- Wireless
tags:
- AirWave
- Gadgets
- WLANpi
meta:
  _publicize_twitter_user: "@CaNerdIan"
  _wpas_done_all: '1'
  _wpas_mess: Another cool use of the WLANpi...
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
permalink: "/2019/11/08/another-cool-use-of-the-wlanpi/"
image: "https://nerdian.ca/files/2019/11/IMG_7577.jpg"
---

Recently, the nice people that employ me to be a wireless network engineer for them were kind enough to add a [WLANpi](http://wlanpi.com) to my [toolkit](https://blog.ianbeyer.com/2019/10/04/whats-in-that-survey-kit-fall-2019-edition/) (as well as that of several of my co-workers), and it is indeed a very handy gizmo for network engineering work.

The other day, I found yet another useful trick I could do with it: Software repository. Sounds basic, because it is. But useful nonetheless. Necessity is the mother of invention, after all.

![]({{site.baseurl}}/assets/2019/11/IMG_7577-768x1024.jpg)  

The WLANpi, with a little [customization](https://www.semfionetworks.com/blog/customize-your-wlan-pi)...

The situation was that I needed to update [AirWave](https://www.arubanetworks.com/products/networking/management/airwave/) on a customer server, and the WLAN management network at this site is isolated from the rest of the world (and even if it wasn't, a satellite connection is not a fun thing to download a couple of gigabytes over!) Fortunately I came prepared for this and while I was at home on my gigabit fiber connection, I downloaded a whole host of software images I might need and stored them on my laptop.

AirWave's heavily locked down CLI does give you the option of uploading a file, but it does it in a strange way that is in fact initiating an SCP download from somewhere. There's not really any way to push a file to the box. No worries, Macs are Unix-ish, and this should be trivial, right? Nope, in Mojave there appears to be a strange quirk where ssh won't respond on anything but localhost. So, my plan to scp from my Mac was shot to bits. I needed a linux box, and didn't want to download an install ISO over the satellite any more than I wanted to download AirWave (after all, AirWave is itself Linux-based). Then I remembered I had my WLANpi.

Like an increasing number of gadgets these days, the WLANpi's USB port (used for power) also happens to be an [OTG port](https://en.wikipedia.org/wiki/USB_On-The-Go), and presents itself to the host system as an "[RNDIS](https://en.wikipedia.org/wiki/RNDIS) Ethernet Gadget", and sets up an Ethernet link over the USB. This allows gadgets like the WLANpi and the Ekahau Sidekick to easily communicate with the host without going through the brain damage of custom device drivers (incidentally, Aruba is taking a similar approach to IoT support on its APs). RNDIS handles the messy layer 1 and layer 2 stuff, sets up layer 3 (the WLANpi defaults to 192.168.42.1) and then the application only has to implement standard upper-layer network communications.

So all I had to do was open an ssh session to my WLANpi (I use [Emtec's ZOC](https://www.emtec.com/zoc/), which I have been using since the days of OS/2!) to see if I had enough storage space on the device to hold the 2.5GB AirWave update (Narrator: it did). Then I fired up [Transmit](https://apps.apple.com/us/app/transmit-5/id1436522307?mt=12), my go-to file transfer application on MacOS (whatever your platform, anything that supports scp will fit the bill), and sent the Airwave update over to a newly created files directory in the WLANpi user's home directory.

Once the file was on the WLANpi, I plugged the WLANpi's Ethernet port into a VLAN that was accessible to the WLAN management devices (I used the AP management VLAN since it already had a DHCP server), and then opened an ssh session to the AirWave server from my existing session on the WLANpi, essentially using it as a jump box. This served to verify port 22 connectivity, and also meant I didn't have to put my laptop on that VLAN either.

![]({{site.baseurl}}/assets/2019/11/Screen-Shot-2019-11-06-at-9.38.59-AM-1024x563.png)

Once I was able to copy the file from the AirWave server, the process was a snap to get the thing upgraded.

I think I'm going to get a bigger SD card for my WLANpi and store a full set of code and images that I may need, and also set up a tftp server on there, and maybe a file manager for the WLANpi's web interface.
