---
layout: post
title: Auditorium Density/Capacity Planning for Wi-Fi
date: 2021-03-11 17:04:07.000000000 -06:00
type: post
parent_id: '0'
published: true
password: ''
status: publish
categories:
- Aruba
- Church IT
- networking
- Wireless
tags:
- LPV
meta:
  _last_editor_used_jetpack: block-editor
  _publicize_twitter_user: "@CaNerdIan"
  _edit_last: '2'
  _thumbnail_id: '1829'
  _wpas_done_all: '1'
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
permalink: "/2021/03/11/auditorium-wifi/"
image: "https://nerdian.ca/files/2021/03/AdobeStock_340419808-scaled.jpeg"
---

I was recently (March 2021) tasked to do a design for a small 450-seat auditorium and provide capacity and throughput numbers. Those who have known me for a while probably know that this type of auditorium is kind of a sweet spot for me, having done designs for a number of church sanctuaries of various sizes. In this post, I'm going to get into the nitty gritty details of making sure that not only does an auditorium have sufficient wireless capacity to meet the connectivity needs of the space, but also to have realistic expectations of what the performance will look like in order to build sufficient backend networking infrastructure without needlessly overbuilding it.

Auditorium design should be simple, right? Here's how I have seen it done, way too many times to count:

1. Count up how many seats there are, divide by some number of seats per AP (usually based on the AP data sheet), and then figure out how many APs that gets you.
2. Figure out your capacity by taking the AP throughput (again from the data sheet) and multiplying that by the number of APs. Then divide that capacity so you know how much bandwidth you get per person.
3. Try to do a predictive model using Ekahau, to place the APs in exactly the right spot, and without ever surveying the space.

So let's say you have a 1000-seat sanctuary where you want to use a Ubiquiti Unifi HD access point because that's what your colleagues on social media recommended. The [vendor data sheet](https://store.ui.com/collections/unifi-network-access-points/products/unifi-hd) says that you can do 500 concurrent clients per AP, so that means two APs (let's say three just for redundancy), and each AP can do 2533 Mbps . So you should be able to get 7.6 Gbps, divided by a thousand seats, which gives you 7.6 Mbps per client, and you'll need a 10 Gbps switch. Easy job, under a thousand bucks for the gear. And then when you fill the room up, the whole thing collapses, everyone is complaining about how it doesn't work, and you're left wondering why.

*Because that's not how any of this works.*

For starters, ***never believe the data sheet***. That's marketing, not engineering. There is no amount of marketing copy that can ever overcome the fundamental laws of physics. So let's pick this design apart, piece by piece... (yes, I'm gonna pick on Ubiquiti for a bit here, because their UniFi brand is often thrown about as a solution to all your wireless problems by people who don't actually understand how wifi works - but these principles apply to any vendor - *no* vendor has a magic bullet, you *still have to do the engineering*)

***Caution: Math (or at least some basic arithmetic and some elementary statistics) ahead. Don't say I didn't warn you. Hope you paid attention in school. (If you're still in school, pay attention: you will use this stuff in real life!)***

## The Engineering

### Winging it: Ur doin it rong.

[![]({{site.baseurl}}/assets/2021/03/AdobeStock_418615328-edited-scaled.jpeg)](https://nerdian.ca/files/2021/03/AdobeStock_418615328-scaled.jpeg)

#### Error #1: AP Throughput

This is probably one of the most egregious attempts by the marketing department to ignore reality. This number published on the data sheet (and also frequently wielded by consumer AP marketing) is completely bogus, but marketing loves to show off big numbers. It is typically created by taking the maximum possibly PHY rate (more on that in a second) on each radio, and adding them together. (why? you can't aggregate client radios like that!). The number "2533 Mbps" comes from adding the max PHY on 5GHz (1733 Mbps) with the max PHY on 2.4 GHz (800 Mbps)

###### What is the PHY rate?

It is the speed at which an individual wireless frame is transmitted over the air. It can vary from one frame to the next, one client to the next, and is highly dependent on RF conditions. What goes into the PHY:

- Channel Width
- Number of MIMO Spatial Streams
- Guard Interval
- Modulation and Coding Scheme (MCS)
- Resource Unit Size (in 802.11ax)

A table of all possible PHY rates (and the math behind them) can be found at the ever-handy [mcsindex.com](http://mcsindex.com).

And here's where this speed number comes flying apart. In order to achieve this maximum PHY, you need to use an 80 MHz channel (40MHz on 2.4 GHz, which is a monumentally bad idea), a short guard interval, 256QAM with 5/6 coding (which typically requires signal:noise ratio of over 40dB to achieve), and FOUR spatial streams. Given that the vast majority of devices in the wild only support two spatial streams (and the only 4SS client device is a desktop card), it's safe to say that you're never going to even come close to that maximum PHY rate. And even then, wireless is a half-duplex shared medium where only one device can talk on a channel at a given time. So even if you were to somehow get that max PHY, your throughput for a single device might be about half that at best. And as you add more clients, it gets even lower. Remember: Every TCP segment results in FOUR transmissions on the wireless: The segment itself, the layer 2 acknowledgement of that frame, then the TCP acknowledgement, and then the layer 2 ACK of the Layer 3 ACK.

To illustrate this, I will refer you to [Aruba's throughput test of the new AP-635](https://blogs.arubanetworks.com/industries/how-wi-fi-6e-performs-in-action-with-the-aruba-ap-635/), an access point that supports the 6GHz band. If marketing were to tell you the throughput of this AP, it would sound something like "3.9 Gbps" (and, in fact, the data sheet will tell you exactly that, as this is a 2x2:2 access point). But in the real world, running the widest channels on all bands, actual throughput was a bit over 2.3Gbps, and 2/3 of that was on 6GHz... Still impressive, but it also shows why you don't actually need a 10Gbps link to it.

#### Error #2: Constrained Resources

The most important thing to remember when doing dense Wi-Fi deployments is that your most constrained resource is not bandwidth, it's *airtime* (the amount of time a given device gets to send data). In order to maximize airtime sharing, you want devices to get on, say their piece as fast as possible, and get off. This also means you want them to use as little spectrum as possible to do so. The key to supporting more client devices is to minimize their use of spectrum and maximize spectrum reuse (where multiple access points use the same frequency in a way that they don't interfere with each other, which is a lot harder than it sounds)

Ultimately, the only way you can **add capacity** to a space is to **add spectrum**. I'll demonstrate in a minute how channel width matters a lot less than one might expect.

And let's not forget that while this AP advertises throughput of 2533Mbps, it only has a 1Gbps port to connect to the switch...

#### Error #3: Assumptions

We've probably all heard the old saw about what happens when you assume something. It still holds true in wireless engineering. An auditorium may have a thousand seats, but it's also vitally important to understand how that space is used, what kinds of devices there are, how many people, etc. Broadly speaking, an auditorium will "feel" packed and completely full when there are about two thirds of the seats occupied. But if you're selling reserved tickets, it's entirely possible to fill every one of those seats. And what devices are those people bringing? There's a big difference between a 1000-seat auditorium that has 700 people in it for weekly worship and when that same space has 500 people in it attending a conference, or when 1000 people are there watching a film or a performance. Ultimately you want to plan around the most likely intensive usage scenario, which is going to typically be a conference (although I've done plans that assume the most intensive scenario is something completely insane like an Apple product launch).

[![]({{site.baseurl}}/assets/2021/03/AdobeStock_95776267-1024x614.jpeg)](https://nerdian.ca/files/2021/03/AdobeStock_95776267-scaled.jpeg)

### Planning (Doing it right)

So let's run the numbers for this fictitious auditorium that seats a thousand people. broadly speaking, this room is going to be of such a size that no matter where you place the AP, it's going to light up the whole room. At this size, you're not going to get any frequency reuse, even with directional antennas. If you were hoping to use the crowd to attenuate the signals and get reuse that way while putting your access points under the seats, stop now - Aruba (who have tested and deployed a whole lot of venues of all sizes) do not recommend going under the seat in any venues under about 10,000 seats unless you simply don't have a means to go overhead.

Since we're not getting any channel reuse, this gives us a grand total of 500 MHz of spectrum to work with, plus another 60 MHz in the 2.4GHz band - but it's probably best to simply forget about 2.4 GHz in an auditorium because a bunch of A/V stuff is using it (and likely ill behaved stuff at that), not to mention the hundreds of wearables the people in the seats have, which will light up the entire Bluetooth channel space. So let's go with 5 GHz for now. I'll talk about 6GHz later.

In the 5 GHz band, we have:

- 25 channels at 20 MHz (500 MHz)
- 12 channels at 40 MHz (480 MHz)
- 6 channels at 80 MHz (480 MHz)
- 2 channels at 160 MHz (320 MHz)

[![]({{site.baseurl}}/assets/2021/03/graphic-80211-acChannels-all-1024x461.png)](https://nerdian.ca/files/2021/03/graphic-80211-acChannels-all.png)  

5 GHz Channel Allocation *(Credit: Jennifer Minella, [SecurityUncorked.com](https://securityuncorked.com))*

I'm gonna go ahead and say it: Don't waste your time with 160MHz. Sure, you get some sick PHY rates with it, but device support is limited. And don't forget that weather radar can remove 3 channels at 20 MHz, 2 channels at 40 MHz, and 1 channel at both 80 and 160 MHz - but unless you're very near a radar site, and the radar is penetrating from outside, you can use these channels without any issue. I've even seen these used inside airport terminals within view of the TDWR. Use these channels right up until you can't.

So how do you choose what channel width to use? The only difference is whether you have more devices talking at once, at lower speeds, or fewer talking at once, but doing so at higher speeds. In the end, it doesn't make that much of a difference to your throughput, and then it becomes a decision of how many APs you can physically put in the space (and their specific placement in a small auditorium is not too picky, since every AP lights up the entire space). 12 APs is a good flexible middle ground here, because you can do 12x40MHz channels. or 24x20MHz if the AP supports dual 5GHz radios (such as the Aruba AP-340 or AP-550 series access points), or 6x80MHz and leave the other 6 as spectrum monitors. Or adapt as needed.

Let's now plan on a full conference load of 500 people, who each brought a laptop, a smartphone, and a tablet. and will be evenly distributed throughout the room (because elbow room and personal space). The tablet and the phone will be doing typical low-usage background stuff while the laptop will be doing much heavier usage, let's say 1 gigabyte per hour (which is roughly equivalent to a 2Mbps video stream - I'm thinking this is something like the [Church IT Network](https://churchitnetwork.com) conference or the [Wireless LAN Pros Conference](https://wlanprofessionals.com/) and they're all geeks doing geek stuff during the conference, and that about 3/4 of them are active, the rest have shut their devices off to minimize distraction. I'm also going to plan on these being 2SS MIMO devices, since that's the overwhelming majority of what's out there.

So here's the breakdown, assuming most clients link up at MCS7 with a standard Gaussian distribution on either side. We're also assuming a 50% net ratio of usable throughput (goodput) to PHY speed. Duty cycle is how much of the available airtime is used for this load - you want to try and stay under about 60% to accommodate for neighbor interference, etc. Much above that and performance really starts to suffer. These calculations are based on an Excel sheet that I have, but it's a little rough around the edges, so I haven't shared it here. Hit me up and I can send it to you.

|  |  |  |  |
| --- | --- | --- | --- |
|  | 24x20MHz | 12x40MHz | 6x80MHz |
| Devices | 1130 | 1130 | 1130 |
| GB/Hour | 400 | 400 | 400 |
| Available Throughput | 1560 | 1620 | 1755 |
| Duty Cycle | 57% | 55% | 50% |
| Average Throughput per client | 1.38 Mbps | 1.43 Mbps | 1.55 Mbps |

And this is where things get a bit counterintuitive (as they often do with Wi-Fi): You're slightly better off here going with fewer APs at 80 MHz than you are with more APs at 20 MHz - but if you lose an AP or a channel due to failure or radar hit, you lose a lot more capacity when using the wider channels. In any case, you can see that all you actually need for this room is a gigabit switch with a 10G uplink, and a decently fat pipe to the internet. You also need at *least* a /21 IP address space (but probably a good idea to go to /20 or even /19 to accommodate for [MAC randomization](https://www.mist.com/get-to-know-mac-address-randomization-in-2020/)). You also want to plan on sufficient AP capacity outside the space for devices to transition to during breaks and whatnot, but they won't need nearly as much airtime capacity as those devices are not going to be using it as heavily as the laptops.

[![]({{site.baseurl}}/assets/2021/03/AdobeStock_368841862-edited-scaled.jpeg)](https://nerdian.ca/files/2021/03/AdobeStock_368841862-scaled.jpeg)

#### The Math (I warned you!)

##### Input data:

- Infrastructure:
  - Area Population (Head Count) - the number of people in the room.
  - Distribution Curve: Normal/Gaussian
  - Number of access points (self-explanatory)
  - Channel Width (2.4GHz, 5 GHz) (Not directly used in calculations, only in determining link speed input)
- Client Devices:
  - Wifi Devices per person (Distribution: triangular)
  - Gross Take Rate/how many people using wifi (Distribution: Gaussian)
  - % Devices on 5GHz (if using both bands)
- Client Activity Modes: (activity per hour, in MB)
  - High/Medium/Low (Gaussian)
- Activity Distribution (percentage of traffic in each mode, Gaussian)
- Link Parameters (I shoot for the MCS7 values on 2SS - but what you can realistically expect will also be a function of how far the AP is from the seats, which is a factor in tall rooms):
  - 2.4 GHz Link Speed (Mbps, median speed, triangular)
  - 5 GHz Link Speed (Mbps, median speed, triangular)
  - TCP Net ratio (Goodput/Link speed, triangular)

[![]({{site.baseurl}}/assets/2021/03/distribution-curves.png)](https://nerdian.ca/files/2021/03/distribution-curves.png)  

[Distribution Curves](https://www.isobudgets.com/probability-distributions-for-measurement-uncertainty/): a) Normal/Gaussian, b)Rectangular/Uniform, c) Triangular/Continuous, d) U-shaped/quadratic

##### Output Data:

- **Connected Devices:** Headcount \* Devices per person \* Take Rate
- **Client Demand (MB/hr)**: (Sum of: (activity mode \* activity percentage)) \* headcount
- **Available Throughput (Mb/sec)**: AP count \* Link Speed \* Goodput Ratio
- **Duty Cycle**: ((Client Demand \* 8)/3600) / Available Throughput

You'll also want to apply the distribution curves to all those values to establish your 95% confidence ranges. Hit me up if you want details..

You can also improve your airtime efficiency by narrowing the range of PHY speeds so as to keep extra slow clients from connecting and chewing up your airtime - This is accomplished by setting your basic and available data rates to a higher value such as 12 Mbps or 24 Mbps. Also, don't forget that because any slice of airtime is at a premium, don't go crazy with your SSIDs, to keep your beacon overhead under control even at the higher basic rates. You also don't want to "hide" any SSIDs in order to keep your unassociated clients from chewing up airtime with probe requests that are trying to figure out if the hidden SSID is one they know about. You want as many devices in the room as you can get to associate to something, anything and shut up with the probes already. Even if it's an open SSID that goes nowhere.

#### Caveats

It is worth noting here that artificially throttling client speeds will do more harm than good - the additional traffic overhead that comes with that eats up airtime like crazy. So don't see this and think you should limit your client devices to 2Mbps in order to make sure the system doesn't get overwhelmed - see Jim Palmer's presentation "[The Netflix Effect on Guest Wi-Fi](https://wlanprofessionals.com/the-netflix-effect-on-guest-wi-fi-jim-palmer-wlpc-phoenix-2019/)" for why throttling client speeds doesn't work the way you think it does. Then show it to your boss to dissuade them from insisting on meddling in the affairs of dragons.

These calculations also don't factor in any airtime overhead from adjacent APs outside the space, which is one reason why you want to keep your airtime duty cycle under 60% and your goodput ratio to 50%. Once the system is deployed, you'll want to validate in the field what they actually look like, which will give you a good idea of actual usage and how well the model predicted your capacity.

And, of course, all this assumes that your client devices are going to be bashing away at the network constantly, which is a fairly unusual occurrence. But you're planning for the worst case, right? If actual usage is lower, then each client will get more throughput.

#### What about placement and directional antennas?

In an auditorium this size (or any size, unless it's an arena or a stadium, that seats thousands), **it really *doesn't matter***. Because no matter where the AP is or what antenna it has on it, it will light up the entire room, even at a low power setting like 10dBm. Don't get me wrong, I'm a huge fan of using directional antennas to sculpt the RF footprint. But unless you're dealing with a small stadium, you're not going to get frequency reuse out of directional antennas anyway (and a directional antenna can actually cause you more trouble - if the hot spot of the signal is too narrow, even way off-axis you'll still be above the -82dBm contention backoff threshold in most of the room due to reflections and how focused your antenna is). If you want a good visual of this, go find one of the lighting people and ask them to aim a lighting fixture with a narrow beam at a seating area, turn on only that light, and vary the brightness... You'll get enough scattered light in most of the room to see where you're going. Light is, after all, still electromagnetic energy, so your RF is going to behave in similar ways.

Because the APs light up the whole room, you can literally put them anywhere that's convenient for installation or maintenance access (just don't put them too close to each other). There are however some cases where you can (and probably should) use a directional antenna in an auditorium space:

**Tall ceilings** - if you're stuck with mounting the APs on a ceiling that's much more than about 10m from the seating area, use a directional - at that height, 90° is still going to cover the entire floor, and 60° likely will too (remember that antenna beam width is considered to be between the -3dB points on the antenna plot, and in a space like an auditorium, your functional beam width is going to be closer to between the -10dB points, and you're going to get a lot of scatter from the back lobes of the antenna as well, something that Ekahau doesn't model - but this multipath environment can ultimately help with MIMO.

**Keeping the signal inside and the noise outside** - this is another place where you might consider directional antennas - if your APs are near the perimeter of the space and there's space outside that also has Wi-Fi, a directional antenna can keep the outside signals from causing contention, as well as keep the signal from spilling into the area outside and causing contention with the APs external to the room. It's also probably a good idea when you're building a new auditorium to build the shell of the room such that it has high attenuation between the outside and inside (tilt-up precast concrete panels are great for this, but there's a case to be made for intentionally designing RF shielding into the walls. It probably doesn't hurt to set the room to a different BSS color if you're using 802.11ax - but I haven't yet encountered this in the wild. Last year, I was working from someone else's design in a cruise ship where there were no fewer than 40 APs in the ship's theatre, which seated 750. These APs were not only using a 60° directional antenna, it was placed immediately behind an expanded metal mesh used to support acoustic treatment fabric. And yet even at the lowest power I thought I could get away with, that one AP was still lighting up the seats below (about 6m away) at -60dBm... The back lobe of these antennas was bouncing off the steel structure of the ship, and the *weakest* spot in the room was directly on the center axis of the directional antenna. I ended up putting most of those APs in spectrum monitoring mode, and making notes for the next ship auditorium. Upside is that a steel ship gets GREAT frequency reuse elsewhere.

**Aesthetics** - Sometimes you just want to hide the APs - and in that situation, an external antenna can be easier to hide than a whole AP.

**Note:** *most APs now also have BLE functionality, and because of the power levels involved, the BLE antennas are still inside the APs even if the Wi-Fi antennas are external. So if BLE is a design consideration, keep that in mind*.

You can also hide APs (or antennas) by skinning them (printable automotive vinyl wrap is great for this), painting them (if the manufacturer allows this, just make sure you use nonmetallic paint), a paintable cover (Aruba offers matching paintable covers for almost all of its indoor APs) - I haven't tried it, but I wouldn't be surprised if you could also hydro-dip the covers or the radomes. You can also hide APs in an enclosure such as the [Oberon 1019-RM](https://oberoninc.com/products/1019-rm/) or otherwise camouflage them (See previous post: [Hiding In Plain Sight](https://nerdian.ca/2019/09/06/hiding-in-plain-sight/)). But one thing you don't want to do is put them all being the acoustic panels where they all have line of sight to each other, as this will screw with 802.11k as well as automatic channel/power algorithms like AirMatch. This is functionally the same as [putting your APs above the ceiling](https://wlanprofessionals.com/do-not-place-aps-above-ceiling/) tiles.

#### Too Much of a Good Thing?

If you're dealing with a larger space where an AP doesn't cover the entire space, check your predictive model or your survey for the number of APs visible on the band at any given location - if that number exceeds the available spectrum divided by your channel width, then you've got too many APs in the space (conversely, you can plan your AP coverage such that you never exceed that number (for example, 12 APs if you're using 40MHz channels on 5GHz), you'll maximize your spectrum reuse. You can always double up if you're big on redundancy, but you're not going to get any additional throughput or airtime out of it, and there are better ways to do that.

#### What about 802.11ax?

802.11ax ("WiFi 6") brings a few airtime efficiencies to the table, but that will mostly manifest itself with the low traffic clients that don't need to use the full data payload of a frame. High traffic clients will typically use all the RUs available in a single transmission, so our airtime usage calculations should not assume any OFDMA gains. BSS coloring (see above) may also be useful.

#### What about MU-MIMO?

Even if you have devices that support it (rare in 802.11ac, required for 802.11ax), MU-MIMO frames [don't really happen all that often in the real world](https://www.cleartosend.net/state-of-wifi-6-wlpc/), so planning your capacity around being able to use it is not a great idea. If you can somehow get MU-MIMO, then you'll see some more efficient airtime usage. Again, we can't count on this, so our capacity calculations should assume it isn't happening. Once deployed, monitoring is important to see how the throughput and MU-MIMO usage actually behaves in your environment and so you can refine your calculations and models.

#### What about 6 GHz?

6 GHz is pretty simple - you get to add more lots more spectrum (about 3x what 5GHz offers), which directly translates to more capacity/throughput. Vendors have begun releasing tri-radio/tri-band access points (Such as the Aruba [AP-630](https://www.arubanetworks.com/products/wireless/access-points/indoor-access-points/630-series/) and [AP-650](https://www.arubanetworks.com/products/wireless/access-points/indoor-access-points/650-series/) series) that add the ability to run a 6 GHz radio, so you would simply calculate the additional capacity as additional APs and swap them out when the APs become available.

But also consider that client support may not be fully available for a few years, so when you run your calculations, do them for 5GHz only and then treat 6GHz as a supplemental capability. If you're running a dozen 5 GHz APs with 40 MHz channels, you can use those same 12 APs with 80 MHz channels on 6 GHz and the higher throughput alone should encourage any 6 GHz capable client device to choose the 6 GHz connection. Band steering without the band steering.

[![]({{site.baseurl}}/assets/2021/03/6GHz-Unlicensed-Spectrum-1024x544.png)](https://nerdian.ca/files/2021/03/6GHz-Unlicensed-Spectrum.png)  

6GHz Wi-Fi Spectrum *(Image Credit: [Wireless LAN Professionals](https://wlanpros.com))*

#### What about 2.4 GHz?

Leave it. Pretend it doesn't exist. An auditorium full of people is going to be chock full of Bluetooth signals from wearables and wireless earphones (not to mention an increasing number of hearing aids). There's also a lot of A/V stuff that lives in 2.4 that you just don't want to worry about either. If you're unable to convince the theatrical engineers to integrate with your existing infrastructure, you may also want to leave one 20MHz channel on 5GHz for them (165 is easy). And you only gain 60 MHz of spectrum, at the expense of a lot of headache.

## tl;dr

Planning your auditorium capacity isn't just a matter of taking the vendor specs and multiplying it by a certain number of APs per seat. There's much more detailed engineering and calculation involved, and if it's not something you're comfortable doing or you don't understand the numbers, hire a pro who can do the engineering for you - it's going to be a lot cheaper than buying the wrong thing several times over...

### Additional Resources

- [Aruba Very High Density Validated Reference Design (VHD-VRD)](https://community.arubanetworks.com/browse/articles/blogviewer?blogkey=7bc8710b-bc01-4229-a170-41f8f5a5e6f8) (Airheads)
- Hire a Pro (such as yours truly): [Aruba Professional Services](https://www.arubanetworks.com/assets/ds/DS_Quick-Start-and-Proactive-Engineering-Services.pdf) (Aruba)
- [Jim Palmer - The Netflix Effect on Guest WiFi](https://www.wlanpros.com/resources/the-netflix-effect-on-guest-wi-fi-jim-palmer-wlpc-phoenix-2019/) (Wireless LAN Pros)
- [Enhancing the public Wi-Fi experience](https://nerdian.ca/2017/03/30/enhancing-the-public-wi-fi-experience/) (This blog)
- [Hiding In Plain Sight](https://nerdian.ca/2019/09/06/hiding-in-plain-sight/) (this blog)
- [Designing Wi-Fi for Lecture Halls](https://www.cleartosend.net/designing-wifi-lecture-halls/) (cleartosend.net)

## Props and Shout-Outs

Thanks to the following people who contributed their expertise and knowledge to this post:

- Aruba People:
  - [Clark Vitek](https://www.linkedin.com/in/clarkvitek/)
  - [Jeffrey Weaver](https://www.linkedin.com/in/jeffrey-weaver-4251835/)
  - [Oguzhan Ehren](https://www.linkedin.com/in/oguzhaneren/)
  - [Chuck Lukaszewski](https://www.linkedin.com/in/chucklukaszewski/)
  - [Scott Lester](https://wirednot.wordpress.com/)
- Wireless Nerds:
  - [Jim Palmer](https://jimswirelessworld.wordpress.com/), CommScope/Ruckus
  - [Keith Parsons](https://wlanpros.com), Wireless LAN Pros
  - [Jennifer Minella](https://securityUncorked.com), Carolina Advanced Digital
  - [François Vergès](https://www.semfionetworks.com/), Semfio Networks
  - [Peter Mackenzie](http://mackenziewifi.com/), the WiFi Magician
