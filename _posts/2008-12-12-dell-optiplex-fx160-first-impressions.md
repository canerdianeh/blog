---
layout: post
title: Dell Optiplex FX160 - first impressions!
date: 2008-12-12 09:45:29.000000000 -06:00
type: post
parent_id: '0'
published: true
password: ''
status: publish
categories:
- Hardware
tags:
- dell
- FX160
- HPSucks
- Shiny
- thin clients
- XPe
meta:
  dsq_thread_id: '217880055'
  _googl_shortlink: http://goo.gl/jnUGO
author:
  login: ianbeyer
  email: ian.beyer@gmail.com
  display_name: Ian Beyer
  first_name: Ian
  last_name: Beyer
permalink: "/2008/12/12/dell-optiplex-fx160-first-impressions/"
---

(Edited at 4:45pm to add some additional information about power supplies)
[![]({{site.baseurl}}/assets/2008/12/desktop-optiplex-fx160-overview1.jpg)](http://nerdian.ca/files/2008/12/desktop-optiplex-fx160-overview1.jpg)Today, I got the [FX160](http://www.dell.com/content/topics/global.aspx/sitelets/solutions/virtualization/fcs\_optiplex\_fx160?c=us&cs=555&l=en&s=biz) demo unit from [Dell](http://www.dell.com) that I've been salivating over for several weeks now. We're looking at buying a number of XPe thin clients next year, and, while I like the HP thin clients, HP support alone is worth making the jump to Dell. Despite being pretty sure that this was our next thin-client platform, I still wanted to try one out, and our Dell rep was able to get approval for a seed unit to help solidify the decision to buy the Dells. These hit the market at the beginning of December, and they fit in a number of niches in Dell's desktop product offering. Our particular niche is light-duty computing and kiosks.
Here are my first impressions of the unit. I haven't had a chance to do extensive testing yet, but I'll be sure to let you know.
The Unboxing: Like most Dell packaging, the box is nothing special like it is from Apple. Dell shipped the unit with one the optional desk mount bracket. This is a good-looking unit, and the first thing you notice when you look at the connections is the dual displays (one VGA, one DVI), followed quickly by the IEC power connector, telling me this thing doesn't have a line lump power supply like my HP thin clients. (It should be noted here that the HP 12V power supply has the exact same mechanical interface as the 20V power supply for a Zebra label printer. When you hook up the wrong one, magic smoke comes out and the unit has to be sent to HP, taking it out of service for 2 weeks). Also visible is the spot for the antenna for the optional built-in wireless (which this one didn't have - I wonder how easy it is to retrofit? it's mini-PCI)
Dell also was nice enough to send me a 22" UltraSharp display (which Clif called dibs on). Mysteriously, though, it shipped without a stand. I stole one from one of the 19" displays on my desk and hooked it all up, casting a 5720 used for Arena Check-in development onto a nearby shelf.
I hit the power button and the smooth face starts blinking. Ooo, blue LEDs. Nice touch. They turn orange if something is amiss, though, just like you'd expect them to on a Dell. The usual set of Dell 1/2/3/4 diagnostic LEDs is present, as is the network link indicator for the gigabit ethernet port.
The system boots up to a user desktop that blessedly allows me to right-click and change the display settings. I adjust to match the big shiny monitor and fire up a browser and cruise over to Hulu, where I am pleased to discover that the stock load on this beast includes a recent version of Flash. Sadly, this thing just doesn't have the horsepower to run the Simpsons in full-screen, and definitely not the HD version of The Office. After trying its performance on video (it does just fine on lower-bandwidth stuff, but if you buy one of these hoping for good graphics performance, you'll probably be disappointed).
I decide to log out of the user account and go poke around under the admin account so I can see more of what's under the hood. I do the usual holding down of the shift key while I log out, so that it doesn't auto login back under the user account (configured as "User1").
This is where I run into problems. Dell hasn't documented the default password anywhere with the system, so I head over to Google, which doesn't help me much either. HP was at least up-front about its default passwords. Dell, this is highly annoying. Please correct this. I'm cutting you some slack because this is a new product for you guys.
So, the thing's been out of the box for less than an hour, and It's already generated a support call. Fortunately, Dell's support on these is up to their usual standard, and I'm able to get a hold of someone at ProSupport on their support chat system.
HP, are you paying attention here? This alone is enough to make me buy these. This beats the socks off of your process of having to slog through your pathetic IVR system that doesn't know what "Thin Client" means, picking a random support group, and then having them tell me in a thick Indian accent, "let me transfer you to the correct support group," followed by at least one (and frequently more) heavily-accented techs who can't figure out the process of getting me Altiris support without me explaining it in detail. Especially since your chat system doesn't know what a thin client is either, and when I tell it it's a desktop system, it tells me the serial number is invalid. 
Another huge advantage of the Dell unit and the associated support is that if the system board is relieved of its magic smoke (much harder to do than the HP), I'll get a part in my hands the following day, rather than paying to ship it in for depot repair and waiting a few weeks to get it back in service.
The Dell tech on the chat finally gave me the default passwords, after insisting on verifying ownership of the unit (??? I just want the default password, not the keys to NORAD). For those who don't want to go through the trouble of contacting support to gain access to the box they just purchased, the administrator password is the ever-so-creative "dell" (all lowercase) and the User1 password is equally original: "password". Apparently there's also an "Admin1" account that also uses "dell". I ask about the monitor, telling him it doesn't have a leg to stand on. I'm told it was ordered without one. Huh???? Gonna have to get on my rep about that.
On gaining administrative access, I see that this unit shipped with the single-core [Atom 230](http://processorfinder.intel.com/details.aspx?sSpec=SLB6Z), as well as 1GB each of RAM and flash (which Dell calls NVRAM). The performance tab on the Task Manager tells me this proc is hyperthreaded and presents it as 2 cores to the OS (confirmed by Intel - this proc also supports EM64T).
The [XPe](http://www.microsoft.com/windowsembedded/en-us/products/wexpe/default.mspx)-based FX160 comes with the same [Altiris](http://www.altiris.com)-based  [remote management](http://www.dell.com/downloads/global/solutions/Tranquility\_Whitepaper\_Ver\_1\_3.pdf) that the HP thins do, but I did notice that, while it detected my existing Altiris install, it didn't connect to it due to a licensing issue. I hope I can simply add the Dell licenses to my existing Altiris install rather than do a whole separate one. I suspect this is going to generate a call to support as well, so we'll see how that process compares to getting Altiris support from HP. My guess is it will be a whole lot less painful, simply because it would be extremely difficult to make the process worse than HP has)
That's about as far as I got yesterday, and I'm taking today off. I'll report back in soon on what the factory load contains, and how well it does with some of our applications. Hopefully, [Clif](http://clifguy.com "Clif Guy ALL THE TIME!") won't have stolen the monitor by then.
I think Dell's got a winner here, barring some unforeseen discovery of a major showstopper problem with the OS load. The FX160 comes with a wide enough range of options to fit a lot of business needs (the dual-core unit with a hard drive could be a good low-end desktop). The @DellServerGeeks have also been helpful and tweeted a few links about desktop streaming and the FX160.
Stay tuned. I suspect we're going to be buying some over the course of the coming year.
