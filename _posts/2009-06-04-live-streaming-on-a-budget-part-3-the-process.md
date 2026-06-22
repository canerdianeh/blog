---
layout: post
title: Live Streaming On a Budget (Part 3) - The Process
date: 2009-06-04 09:56:15.000000000 -05:00
type: post
parent_id: '0'
published: true
password: ''
status: publish
categories:
- Internet Campus
- streaming
tags:
- audio
- process
- production
- video
- worship
meta:
  dsq_thread_id: '218227194'
  _googl_shortlink: http://goo.gl/NWo5m
  _edit_last: '1'
author:
  login: ianbeyer
  email: ian.beyer@gmail.com
  display_name: Ian Beyer
  first_name: Ian
  last_name: Beyer
permalink: "/2009/06/04/live-streaming-on-a-budget-part-3-the-process/"
image: "/assets/images/2009/06/11089636-300x225.jpg"
---

For background information, see [Part 1](http://blog.ianbeyer.com/2009/06/03/live-streaming-on-a-budget-part-1-genesis/ "Live Streaming On a Budget (Part 1) – Genesis") and [Part 2](http://blog.ianbeyer.com/2009/06/03/live-streaming-on-a-budget-part-2-encoding/ "Live Streaming On a Budget (Part 2) – Encoding")

**Server Infrastructure**

We currently send our Flash stream to a small EC2 instance of the Wowza AMI, configured with the liverepeater application in origin mode (using the prebundled packages), and 3 small EC2 instances running liverepeater edge mode that pull from that server. We also run a custom Windows AMI running Windows Media Services, so we have 5 instances in all. Total cost for these is 68 cents an hour.

We have a set of five Elastic IPs in reserve so that we don't have to jack with DNS every time and configure the repeaters in a round-robin DNS that is referenced by the player. The origin and Windows instances also have their own Elastic IPs in DNS. It costs us a penny for every hour each of these IPs are not mapped to an instance, but it's a small price to pay for simplifying it.

Unfortunately, the process of spinning up the servers and assigning their IP addresses is not especially attractive to someone who is nontechnical. I'm working on devising a way to do this easily from a web interface, but that's still on the drawing board. If anyone is handy with perl or PHP and wish to assist with this, let me know. Perl has a module on CPAN to access the Amazon API, I don't know about PHP. The API tools that Amazon provides are written in Java, and there's a [Firefox extension](http://developer.amazonwebservices.com/connect/entry.jspa?externalID=609) for managing the machine images.

The Windows instance is configured with WMS and a publishing point set to pull from the encoder and auto-start. The VT[5] machine has a static IP and is NATted to an external IP so all I have to do is fire it up and wait for the encoder to see the incoming connection.

**Getting it rolling**

On Sunday morning, I show up at about 9:00 and sit through the first traditional service to get a feel for how the service flows.  While I'm doing that, I'm getting VT[5] ready for the morning's services, creating the pre-service announcement loop from the slide graphics our communications department puts up on [BackPack](http://backpackit.com/). Once VT[5] is running and presenting the video device to the system, I start Flash Media Encoder and Windows Media Encoder. At around 10:00 or so, I'll spin up the Windows instance (which takes about 15 minutes to boot), and then fire up my 4 Wowza servers (which are usually ready in 1-2 minutes). After assigning the Elastic IPs to my instances, it takes about a minute or so to propagate the changes through Amazon's network. When everything is ready, I launch the slide loop and a music bed and start both encoders.

Once that's going, I turn to my laptop and fire up Outlook (to catch the feedback forms from [Wufoo](http://www.wufoo.com)), [PlanningCenter](http://www.planningcenteronline.com) (to follow the service rundown), IRC (tech chat with people involved in the stream), an RDP session to the Windows instance to watch client counts, and a small VB script that polls each of the Wowza servers for client counts and adds them all up for me so I can see how many people are watching.

Over on another screen that's at the encoding station, I launch Woopra to watch live site stats and to see where our audience is coming from, as well as keeping an eye on network traffic with WhatsUp Gold and watching the stream coming off the Wowza and Windows servers.

We're currently building out an ops console station that will offload the monitoring to staff  (that means yours truly most weeks), and a volunteer will be handling the switching. The protoype: ![11089636]({{site.baseurl}}/assets/2009/06/11089636-300x225.jpg)

This will live just around the corner from the switching workstation.It will also be equipped with a laptop dock. I'll post pics when it's all done. This will also be equipped with a backup system with WireCast in case the VT[5] [bursts into flames](http://www.facebook.com/pages/Not-being-on-fire/73570766516) or something equally catastrophic.

**The Service**

Most of the time, I'm feeding the IMAG program into the live stream, but will take a different camera shot every now and then to establish context or provide better visuals when IMAG is running a full-screen slide (such as prayer times). I have access to all 7 IMAG camera feeds as well as an additional [Sony EVI-D70 camer](http://pro.sony.com/bbsc/ssr/mkt-industrialautomation/mkt-industrialautomationrobotic/product-EVID70/)a on stage pointing out at the sanctuary seating. We're working on getting remote control of that camera so that we can get some extra shots.

On the audio side, we feed our onstage mics back to a separate console in the recording studio and mix for broadcast there. We run the output through a dbx compressor upstream of the VT[5]. We're also in the process of cabling for direct input of the FOH mix into the VT[5] in case of a failure in the broadcast mix hardware.

**The Aftermath**

Once the service is over, our video crew will shoot the postlude for the web, and then we'll run slides for a few more minutes before shutting eerything down. Then we repeat the whole process at the evening service or any special broadcasts.

See? It's just that simple!
