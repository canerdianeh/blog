---
layout: post
title: Live Streaming On a Budget (Part 2) - Encoding
date: 2009-06-03 22:11:52.000000000 -05:00
type: post
parent_id: '0'
published: true
password: ''
status: publish
categories:
- Internet Campus
- streaming
tags:
- newtek
- switchers
- video
- wirecast
meta:
  dsq_thread_id: '217877490'
  _googl_shortlink: http://goo.gl/3vXPe
  _edit_last: '1'
author:
  login: ianbeyer
  email: ian.beyer@gmail.com
  display_name: Ian Beyer
  first_name: Ian
  last_name: Beyer
permalink: "/2009/06/03/live-streaming-on-a-budget-part-2-encoding/"
---

If you missed it, [go back to Part 1](http://blog.ianbeyer.com/2009/06/03/live-streaming-on-a-budget-part-1-genesis/ "Live Streaming On a Budget (Part 1) – Genesis") to see how we got here.

As I mentioned previously, Flash video was a key functional requirement of the project due to its cross-platform ability and its near ubiquity in the browser. This was a solution that wouldn't require most of our audience to download anything extra to their machine.

In order to stream Flash, you have a couple of options:

1. use a dedicated encoder system that slurps video in one end and spits Flash out the other. From a simplicity standpoint, this is great. From a production standpoint, not so great, because more than likely what you're feeding it is your IMAG program, which doesn't lend itself very well to people outside the room. I'll cover that in a later post.
2. Use a PC with a capture card and [Flash Media Encoder](http://www.adobe.com/products/flashmediaserver/flashmediaencoder/). Cheap, simple to put together, but it suffers the same issues as option #1.
3. Do some switching in software and encode to Flash.
4. Run a dedicated switcher into an encoder. This gets expensive in a hurry.

We initially went with Option #3 using [Telestream](http://www.telestream.net/)'s [WireCast software](http://www.telestream.net/wire-cast/overview.htm). WireCast is a nice inexpensive option (it was about $300 at church/educational pricing) and does its job reasonably well.

WireCast is available both for Mac and Windows (although a license key doesn't allow you to move between platforms, a drawback). The Mac version has a slightly more polished user interface and the ability to show your program feed on a VGA output. The Windows version can't do that, but it does have the option of encoding to Windows Media. The software will take any video source presented to the OS, whether it's a USB webcam, a DV Device such as a video deck/camera/analog bridge, or a dedicated capture board such as [ViewCast'](http://viewcast.com/)s Osprey line. It's got some serious advantages for portability (a laptop and a couple of DV-capable cameras, and you're good to go!), we encountered a number of issues with this solution that eventually led us to another solution. If you're looking at using WireCast with multiple analog sources, I'd highly recommend 2 capture cards being fed by a matrix switch with 2 outputs. This makes multi-input scenes in wirecast a lot easier to configure.

We configured our WireCast system with a pair of [Osprey 210](http://www.viewcast.com/products/osprey-210) PCI cards in a quad-core Dell Optiplex 755 (I really would have liked an additional card, but the Opti mini-tower only has two PCI slots). Each Osprey card had its own audio capture which presented itself in Wirecast.

At the time, Wirecast didn't actually encode to Flash directly, but rather to H.264 QuickTime that was then converted to Flash by the Wowza software (It was the folks at [Wowza](http://www.wowzamedia.com/) that recommended WireCast to us). Wirecast has since added the capability to encode directly to Flash, although it only does [H.264](http://en.wikipedia.org/wiki/H.264). One of the problems we immediately encountered with this conversion was that the video lagged the audio by 10 or 11 frames. Initially, we had to add a hardware audio delay prior to encoding to compensate for this, which meant that any streams we recorded had the audio lagging by 10 or 11 frames. Wowza later added an option in their configuration to compensate at the server end which allowed us to record in sync and get rid of the delay unit.

By this point, the audio was in sync, but was still not the quality we expected of it. Frequent drops and "zippering" on both the stream and the recording seemed to indicate that there was a hardware bottleneck on the encoder. When we started looking at performance metrics on the Dell, we noticed that not only was CPU during the encoding up around 65%, merely firing up WireCast would consume 10-15% CPU dealing with [Deferred Procedure Calls (DPCs)](http://en.wikipedia.org/wiki/Deferred_Procedure_Call). We initially suspected the Osprey drivers as DPCs are often related to video hardware and bad drivers. However, if I fired up Flash Media Encoder and pointed it to the same cards, it wasn't a problem.

We then began suspecting that PCI might be a problem and got our hands on an Osprey 450e card which was quad encoders on a single PCIe board ([PCIe](http://en.wikipedia.org/wiki/PCI_express) has dramatically more bandwidth to work with than PCI or PCI-X, even at a single lane). This was still a problem, so we started looking at whether the PC was the problem. We got a demo of a used Precision 690 from [Stallard Technologies](http://www.stikc.com) and gave that one a try, with no success. The PC platform was not working for us.

So, we gave our friends at Apple a call and asked if we could try out a Mac Pro for 30 days and purchase it if this fixed it. This is where we discovered many flaws in the plan:

1. Wirecast Mac requires a different license key than the Win version. Added bonus: Our vendor seemed to have vanished.
2. Osprey cards don't work on Mac.
3. The video capture world for Mac consists of a bunch of consumer-grade DV bridges, or really expensive broadcast-grade HD DV bridges. PCIe hardware is pretty much limited to [DeckLink](http://www.decklink.com/products/).
4. While the DeckLink Driver supports multiple cards in one system, using them is entirely application-dependent, and WireCast doesn't do that.

This process took us several months to figure out, and we bought and returned thousands of dollars of hardware. Our vendors were very gracious to us through the process. A big thank you goes out to Apple, CDW (Osprey Cards) and B&H (Decklink) for their support. Thanks also to Matt at Stallard for letting me peruse their warehouse in search of a PC platform with sufficient PCIe slots, and then letting me return it when it didn't solve all my problems (it didn't make julienne fries, either)

At the end of it all, it became clear that while WireCast is a great application, it wasn't going to meet our needs on a weekly basis (but I can see using it either as a backup plan, or for other venues as we expand). So, we began the quest for a new solution.

Early on in the process, I'd encountered a device called the [TriCaster](http://www.newtek.com/tricaster/) from [NewTek](http://www.newtek.com). PC-based switcher in a turnkey box, with streaming capability. Looked neat, but for the inputs we'd need, we were [looking at  $10,000](http://www.newtek.com/tricaster/tricaster_studio.php), which wasn't going to work within our budget. After some conversations with Terry Storch at Lifechurch.tv, I found out that NewTek makes a PC-based version called [VT[5]](http://www.newtek.com/vt/index.php) which is a software/hardware combo where you supply the PC and OS. With an added breakout box ([SX-84](http://www.newtek.com/vt/assec.php)) that expands the number of inputs (up to 24 composite signals!!!!) beyond the initial 3, we were able to apply this combo to our Optiplex 755 for about $6000. An [SDI breakout is also available](http://www.newtek.com/vt/assec.php), but we're not using it. The package comes with an entire production studio - switcher, playback, capture, nonlinear editing, character generation, live sets, chroma key, and animation, and lots of other goodies too.

The Tricaster has a panel in the desktop that does streaming via Flash, but the default profiles max out at 480x360@30fps. I'm told you can create custom profiles, but this is not supported by NewTek. On the VT[5] side, however, it merely presents the program output as video and audio devices to the OS. Added bonus is that the driver is coded such that multiple applications can use it simultaneously. To encode Flash, I simply launch FME after the software starts. I can then configure my stream with anything FME supports. Meanwhile, I can also launch an instance of WME that can feed a Windows Media stream to a server for low-bandwidth and mobile devices. For us, this is a huge advantage of the VT[5] over Tricaster. Both have an [optional USB control surface (LC-11)](http://newtek.com/addons/livecontrol.php) that presents a mechanical user interface of buttons and T-bar that's familiar to anyone who's operated a switcher. Thanks to a donor to our technical production ministry, we were able to acquire one which should make it a lot easier on the volunteers who will be operating it.

Because the VT[5] is a hardware-software solution, a lot of the issues we encountered with WireCast aren't a factor. With WireCast, most of the magic happens in software. NewTek's product makes all the magic happen on the PCI board, and merely uses the software to control the hardware. This alleviates much of the bandwidth constraint posed by the PCI interface. Rumour has it the next generation of the NewTek hardware that is present in the [TriCaster XD300](http://www.newtek.com/tricaster/xd300.php) is a 16x PCIe device (unsurprisingly, as it supports HD).

So far, the VT[5] is looking good.

(I've also heard of some places that have used one of the M/E buses on their production switcher to feed the stream, and then using the main program out of the switcher to do IMAG. I've not tried this, so I can't tell you how well it works.

Stay tuned for the next installment, where I'll talk about our production process.
