---
layout: post
title: Sony VISCA RS-422 Control
date: 2010-12-20 10:56:42.000000000 -06:00
type: post
parent_id: '0'
published: true
password: ''
status: publish
categories:
- Hardware
- Internet Campus
- streaming
tags:
- Cameras
- RS-232
- RS-422
- Sony
- VISCA
- Wiring
meta:
  dsq_thread_id: '217880371'
  _edit_last: '2'
  s2mail: 'yes'
  _wp_old_slug: ''
  wp_plus_one_redirect: ''
  _googl_shortlink: http://goo.gl/IwBNO
  _last_editor_used_jetpack: block-editor
  _publicize_twitter_user: "@CaNerdIan"
  _cs_replacements: a:1:{s:7:"sidebar";s:7:"sidebar";}
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
permalink: "/2010/12/20/sony-visca-rs-422-control/"
image: "/assets/images/2010/12/visca-rj45-breakout.png"
---

**Update - January 2014:**Wow, 3 years later this is still one of the most popular posts on this blog! I've had some questions about using this with the EVI-HD1, which has only RS-232 DIN ports. Theoretically, it should work, but you might need to alter some pinouts in the breakout box, and I would highly recommend using shielded/grounded cable, as RS-232 is an unbalanced signal. A reader is going to give it a try, and if it's successful, I'll update the post with some pictures.

**Update - October 2021:** It blows my mind that nearly 11 years later, this is *still* one of the most frequently visited posts on the site...

Now, back to our regularly scheduled blog post!

We recently acquired a few more of Sony's excellent [EVI-D70](http://pro.sony.com/bbsc/ssr/mkt-industrialautomation/mkt-industrialautomationrobotic/product-EVID70/ "Sony EVI-D70") cameras for use in our chapel for streaming weddings, funerals, and other events in our smaller worship space.

When we remodeled the space a few years back, it was originally designed with these cameras in mind.  The original intent was to provide some additional angles for videographers to use, but the idea never really took off. Due to lack of use, the cameras originally installed were re-purposed for [Resurrection Online](http://rezonline.org "Resurrection Online") in the main sanctuary. Things have come full circle now, and the ability to stream services and events from this space is being requested. As a result, we acquired some more cameras, and are in the process of updating the camera system in that room.

The original design used an AMX touchscreen/joystick controller and a custom integration over [RS-232](http://en.wikipedia.org/wiki/RS-232 "RS-232"), with each camera homerun to the control rack. There were numerous difficulties with the cameras randomly freezing up and not responding to controls, requiring someone to get on a ladder and power-cycle the unit.

As part of the updated system, we've ditched the AMX controller and are using Sony's [RM-BR300](http://pro.sony.com/bbsc/ssr/product-RMBR300/ "Sony RM-BR300") control unit which is designed for this particular camera. We also have user familiarity, since we already have one of these controllers in our main sanctuary for the [BRC-H700](http://pro.sony.com/bbsc/ssr/product-BRCH700/ "BRC-H700") remote camera mounted on the catwalks (aka, the "SkyCam"). The controller can do Sony's [VISCA protocol](http://www.chuktech.net/video/ViscaProtocol.pdf "VISCA Protocol") over RS-232 (via a Mini-DIN) or [RS-422](http://en.wikipedia.org/wiki/RS-422 "RS-422") (via a Phoenix connector).

This is where it got sticky. We have an 8-conductor homerun cable from each camera position, but the Sony controller is designed to daisy-chain the VISCA ports. Each camera has two RS-232 Mini-DIN ports (one in, one out). Fortunately, both RS-422 and RS-232 in this application only require four wires, so we can loop out and back on the same cable.

Due to the annoyance factor of having to re-terminate Mini-DIN connectors, I opted for the RS-422 port which uses a [Phoenix](http://www.phoenixcontact.com/ "Phoenix Contact") screw terminal (Part # 1840434 in case you need to order one - Sony wants an obscene amount of money for them, they're dramatically cheaper at an electronics supplier like [Mouser](http://mouser.com "Mouser Electronics")). RS-422 also has the advantage of much longer signal path due to its balanced signal. Since we're also adding a new location, I wanted to be able to wire it up with standard Category 6 twisted-pair cabling. This cable also has eight conductors, making it ideal for the task. In terms of flexibility, RJ-45 is king in the twisted-pair world, so I had do design a means of daisy-chaining my VISCA ports via ordinary patch cords.

At first, I was a little baffled by the wiring of VISCA, since the RM-BR300 connector pinout is exactly backwards from that of the one on the cameras, and the documentation provided is a little confusing. Fortunately, the Sony POSC was quick to help and they e-mailed me a [wiring diagram for this specific application](http://nerdian.ca/files/2010/12/EVI-D70.jpg "wiring EVI-D70 RS-422 to RM-BR300") (and were kind enough to allow me to post it. I translated that into two main components, a breakout box and a standard cable, that would work on either the controller or the cameras.

To make the cable, I simply took a patch cord off the shelf, lopped one end off, and terminated it on the Phoenix connector:

[![]({{site.baseurl}}/assets/2010/12/Cable-300x179.jpg)](http://nerdian.ca/files/2010/12/Cable.jpg)

The wiring is as follows:

[![]({{site.baseurl}}/assets/2010/12/VISCA-RJ45.png)](http://nerdian.ca/files/2010/12/VISCA-RJ45.png)

Now, you'll notice my wiring diagram shows the orange pair on the first two, and the picture shows green. This is because I found out (after much frustration of tracing signals) that the patch cord I grabbed happened to be wired for 568A rather than the more common 568B. Simply swap orange and green if this is the case.

Once I got the cables sorted out, I then replicated Sony's wiring diagram with a handful of data jacks. The connections go like this:

[![]({{site.baseurl}}/assets/2010/12/visca-rj45-breakout.png)](http://nerdian.ca/files/2010/12/visca-rj45-breakout.png)

I used bits I had on the shelf, but I would recommend using a different jack color for the control input so you don't get it confused. Once I got it wired up, this is what I had (I colored the control jack black with a Sharpie):

[![]({{site.baseurl}}/assets/2010/12/Jacks-300x179.jpg)](http://nerdian.ca/files/2010/12/Jacks.jpg)

Even if this install only has three cameras, I wired it up for five, to fill a six-way biscuit box that I had on the shelf (these are Lucent/Avaya components):

[![]({{site.baseurl}}/assets/2010/12/OpenBox-300x179.jpg)](http://nerdian.ca/files/2010/12/OpenBox.jpg)

.. and put the lid on it with some labels:

[![]({{site.baseurl}}/assets/2010/12/ClosedBox-300x179.jpg)](http://nerdian.ca/files/2010/12/ClosedBox.jpg)

As for the hookup, set the DIP switches on the bottom of the controller and the cameras to use RS-422 and either 9600 or 38400 bps, and hook them up. Note that they must be in sequence, or the whole chain will be broken if you skip a slot. Plug a camera into #1, it will be #1 on the controller after they self-enumerate on startup, in order of closest to farthest on the chain. Connecting a camera will cause the controller to re-initialize.

Action Shot:

[![]({{site.baseurl}}/assets/2010/12/Operational-300x179.jpg)](http://nerdian.ca/files/2010/12/Operational.jpg)

I used a biscuit box, but you could also use a modular patch panel to do the same thing. I hope to use a second category 6 run with an [S-Video termination](http://www.panduit.com/Products/ProductOverviews/ProductSearch/index.htm?Nao=10&Ns=P_ItemSortOrder&Ne=4000008&R=CJSVIW&sid=128713C94B32&lastNodeId=ss_prod_coppersolutions&N=5000001%201876%203000136 "Panduit CJSVIW") on it (2 pairs) and power (other 2 pairs) so that the whole system can run off a standard 2-cable pull.
