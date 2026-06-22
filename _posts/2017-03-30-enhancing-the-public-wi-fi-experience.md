---
layout: post
title: Enhancing the public Wi-Fi experience
date: 2017-03-30 13:24:28.000000000 -05:00
type: post
parent_id: '0'
published: true
password: ''
status: publish
categories:
- Church IT
- Hardware
- IT
- networking
- Wireless
tags:
- Apple
- Caching
- CDN
- iOS
- MacOS
- netflix
- Ruckus
- Server
meta:
  _edit_last: '2'
  _thumbnail_id: '1420'
  _wpas_done_all: '1'
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
permalink: "/2017/03/30/enhancing-the-public-wi-fi-experience/"
image: "/assets/images/2017/03/Mac-OSX-Server.png"
---

Recently, there was an excellent blog post from [WLAN Pros](http://wlanpros.com) about "[Rules for successful hotel wi-fi](http://www.wlanpros.com/rules-successful-hotel-wi-fi-3)". While it is aimed primarily at Wi-Fi in the hotel business (where there is an overabundance of [Bad-Fi](https://badfi.com/bad-fi/)), many of the tips presented also apply to a wide variety of large-scale public venue wifi installations. Lots of great information in the post, and well worth a read.

At the 2016 WLPC there was an interesting TENTalk from [Mike Liebovitz](https://twitter.com/mikeleibovitz "Mike Liebovitz on Twitter") at Extreme Networks about the [pop-up wifi at Super Bowl City](https://vimeo.com/album/3831972/video/157332821) in San Francisco, where analytics pointed to a significant portion of the traffic being headed to Apple.

Meanwhile, a few months later at the 2016 National Church IT Network conference, I heard a TENTalk about Apple's MacOS Server, where I first heard about this incredibly useful feature (sadly, it wasn't recorded, that I know of, so I can't give credit...)

With most of the LPV installations I've worked on, I've found the typical client mix includes about 60% Apple devices (mostly iOS). For example, this is at a large church whose wireless network I installed. (Note that Windows machines make up **less than 10%** of the client mix on wifi!)

![Client mix from Ruckus ZoneDirector]({{site.baseurl}}/assets/2017/03/Screenshot-2017-03-31-13.56.14.png)

### OK, So what?

This provides an opportunity to make the wifi experience even better for your (Apple-toting) guests. Whenever possible, as part of the “WiFi System” I will install an Apple Mac Mini loaded with MacOS Server. This allows me to turn on [caching](https://help.apple.com/serverapp/mac/5.3/#/apd74DDE89F-08D2-4E0A-A5CD-155E345EFB83). This is not just plain old web caching like you would get with a proxy server such as [Squid](http://www.squid-cache.org), but rather a cache for all things Apple. What does this do for your fruited guests? It speeds up the download of software distributed by Apple through the Internet. It caches all software and app updates, App Store purchases, iBook downloads, iTunes U downloads (apps and books purchases only), and Internet Recovery software that local Mac and iOS devices download.

Why is this of interest and importance? Let me give you an example: A few years ago, we were hosting a national [Church IT Round Table](http://churchitnetwork.com) conference at [Resurrection](http://www.cor.org) on a day when Apple released major updates to MacOS, iOS, and their iWork suite. In addition to the 50 or so staff Mac machines on the network, there were another hundred or two Mac laptops and iThings among the conference attendees. The 200MB internet pipe melted almost instantly under the load of 250 devices each requesting 3-5GB of updates. That would have melted even a gigabit pipe, and probably given a 10Gbps pipe a solid run for its money (not to mention bogging down some of the uplinks on the internal network!. Having a caching server would have mitigated this. It didn't do great things to the access points in the conference venue either, all of which were not only struggling for airtime, but also for backhaul.

Just by way of an example, Facebook updates their app every two weeks and its current incarnation (86.0, March 30, 2017) weighs in at 320MB (the previous one was about half that!), and its close pal Messenger clocked in at 261MB. Almost everyone has those to apps, so they're going to find itself in your cache almost instantly, along with numerous other popular apps. Apple's iWork suite apps and Microsoft Office apps all weigh in around 300-500MB apiece as well. This has potential to murder your network when you least expect it. (A few years back, the church where I was working hosted the national Church IT conference that happened to coincide with Apple's release of OSX Mavericks, and a major iWork update for both iOS and MacOS. The conference Wi-Fi and the church's 200Mbps WAN pipe melted under the onslaught of a couple hundred Apple devices belonging to the guest nerds and media staff dutifully downloading the updates.)

In any case, check out the network usage analytics from either your wireless controller or your firewall. If Apple.com is anywhere near the top of the list (or on it at all), you owe it to yourself and your guests to implement this type of solution.![Network Statistics from Ubiquiti UniFi]({{site.baseurl}}/assets/2017/03/Screenshot-2017-03-30-14.07.38-1024x515.png "Network Statistics from Ubiquiti UniFi")

## **The Technical Mumbo-Jumbo**

### Hardware

As mentioned previously, a Mac Mini will do the job nicely. If you're looking to do this on the cheap, it will happily run on a 2011-vintage Mini (you can find used Mac Minis on Craigslist or eBay all day long for cheap), just make sure you add some extra RAM and a storage drive that doesn't suck (the stock 5400rpm spinning disks on the pre-2012 era Mac Mini and iMacs were *terrible.*) Fortunately, 2.5" SSDs are pretty cheap these days. Newer Minis will have SSD baked in already.

If you're wanting to put the Mac Mini in the datacenter, you might want to consider using a [Sonnet RackMac Mini](http://www.sonnettech.com/product/rackmacmini.html) (which is [available on Amazon for about $139](http://amzn.to/2nPS3B0)) and can hold one or two machines.

![Sonnet RackMac Mini]({{site.baseurl}}/assets/2017/03/hdr_rackmacmini.jpg "Sonnet RackMac Mini")

You can also happily run this off of one of the 2008-era "cheese grater" Mac Pros that has beefier processing and storage (and also fits in a rack, albeit not in the svelte 1U space the Sonnet box uses). If you have money to burn, then by all means use the "trash can" Mac Pro (Sonnet also makes a rack chassis for that model!).

This is a great opportunity to re-purpose some of those Macs sitting on the shelf after your users have upgraded to something faster and shinier.

Naturally, if you're running a REALLY big guest network, you'll want to look at something beefy, or a small farm of them Minis with SSD storage (the MacOS Server caching system makes it quite easy to deploy multiple machines to support the caching.)

### The Software

[MacOS Server](https://itunes.apple.com/us/app/macos-server/id883878097?mt=12) (Mac App Store, $19.99)

Since most of your iOS guests will have updates turned on, one of the first things an iOS device does when it sees a big fat internet pipe that isn't from a cell tower is check for app updates. If you have lots of guests, you will need to fortify your network against the onslaught of app update requests that will inevitably hit whenever you have lots of guests in the building.

The way it works is this: When an Apple device makes a request to the CDN, Apple looks at the IP you’re coming from and says, “You have a local server on your LAN, get your content from there, here’s its IP.” The result being that your Apple users will get their updates and whatnot at LAN speeds without thrashing your WAN pipe every time anyone pushes out a fat update to an app or the OS, which is then consumed by several hundred people using your guest wifi over the course of a week. You've effectively just added an edge node to Apple's CDN within your network.

Content will get cached the first time a client requests it, and it does not need to completely download to the cache before starting to send it to the client. For that first request, it will perform just as if they were downloading it directly from Apple's servers. If your server starts running low on disk space, the cache server will purge older content that hasn't been used recently in order to maintain at least 25GB of free disk space.

![MacOS Caching Server Configuration]({{site.baseurl}}/assets/2017/03/Screenshot-2017-03-30-13.57.49-1024x676.png "MacOS Caching Server Configuration")

### The configuration

If you have multiple subnets and multiple external IPs that you want to do this for, you can either do multiple caching servers (they can share cache between them), or you can configure the Mini to listen on multiple VLANs:

![Mac OS network preferences panel]({{site.baseurl}}/assets/2017/03/Screenshot-2017-03-31-13.04.50.png "Mac OS network preferences panel")

Once you have the machine listening on multiple VLANs, you can tell the caching server which ones to pay attention to, and which public IPs. The Mac itself only needs Internet access from one of those subnets.

![MacOS Server Caching Preferences]({{site.baseurl}}/assets/2017/03/Screenshot-2017-03-31-13.02.29-1.png "MacOS Server Caching Preferences")

The first dropdown will give you the option of "All Networks", "Only Local Subnets", and "Only Some Networks". Choosing the last one opens an additional properties box that allows you to define those networks:

![Mac OS Server Cache Network Settings]({{site.baseurl}}/assets/2017/03/Screenshot-2017-03-31-13.14.52.png "Mac OS Server Cache Network Settings")

The second one gives you the options of "Matching this server's network" or "On other networks". As with the first options, an additional properties box is displayed.

In both cases, hit the plus sign to create a network object:

![Mac OS Server Create a New Network]({{site.baseurl}}/assets/2017/03/Screenshot-2017-03-31-13.04.04.png)

It should be noted here that this only tells the server about existing networks, but it won't actually create them on the network interface. You'll still need to do that through the system network preferences mentioned previously. If you don't want to have the server listen on multiple VLANs, you can just make sure its address is routable from the subnets you wish to have the cache server available, define the external and internal networks it provides service to, and you should be off to the races. This will provide caching for subnet A that NATs to the internet via public IP A, and B to B, and so on. Defining a range of external IPs also has you covered if you use NAT pooling.

There's also some DNS SRV trickery that may need to happen depending on your environment. There are some additional caveats if your DNS servers are Active Directory read-only domain controllers. [This post elaborates](https://themacwrangler.wordpress.com/2016/06/14/when-apple-caching-server-just-cant-even-right-now/) on it.

### **Is it working?**

Click the stats link near the top left of the server management window. At the bottom is a dropdown where you can see your cache stats. The red bar shows bytes served from the origin, and green shows from the cache. If you only have one server doing this, you won't see any blue bars, which are for cache from peer servers. Downside is that you can only go back 7 days.

On this graph, 3/28 was when there were both a major MacOS and iOS update released, hence the huge spike from the origin servers on Apple's CDN. Nobody has updated from the network yet... But guest traffic at this site is pretty light during the week. I'll update the image early next week.

![MacOS Server Cache Stats]({{site.baseurl}}/assets/2017/03/Screenshot-2017-03-31-13.51.11.png "MacOS Server Cache Stats")

### **Other useful features**

A side benefit of this is that you can also use this to provide a network recovery boot image on the network, in case someone's OS install ate itself - on the newer Macs with no optical drive, this boots a recovery image from the internet by default. This requires some additional configuration, and the instructions to set up NetInstall are readily available with a quick Google search.

If you want, you can also make this machine the DHCP and local DNS server for your guest network. With some third-party applications, you can also serve up AirPrint to your wireless guests if they need it.

## **Conclusion**

From a guest experience perspective, your guests see their updates downloading really fast and think your WiFi is awesome, and it’s shockingly easy to set up (the longest and most difficult part is probably the actual acquisition of the Mac Mini) It will even cache iCloud data (and encrypts it in the cache storage so nobody's data is exposed). Even if you have a fat internet pipe, you should really consider doing this, as the transfers at LAN speed will reduce the amount of airtime consumed on the wireless and the overall load on your wireless network. (Side note, if you're a Wireless ISP, this sort of setup is just the sort of thing you ought to put between your customer edge network and your IP transit)

Of course, you could also firewall off Apple iCloud and Updates instead, but why would you do that to your guests? Are you punishing them for something?

Android/Windows users: So sad, Google and Microsoft don’t give you this option (Although Microsoft sort of does in a corporate environment with WSUS, but it’s not nearly as easy to pull off, nor is it set up for casual and transient users). I would love it if Google would set up something like this for play store, Chromebook, etc, as about half of the client mix that *isn't* from Apple is running on Android. You can sort of do it by installing a transparent proxy like [squid](http://www.squid-cache.org/).

Now, if only we could do the same for Netflix's CDN. The bandwidth savings would be immense.

## Update

###### *(Added November 16, 2017)*

As of the release of MacOS High Sierra and MacOS Server 5.4 ([release notes](https://support.apple.com/en-us/HT208041)), the caching service is now integrated into the core of MacOS, so any Mac on the network can do it, without even needing to install Server. The new settings are under System Preferences > Sharing:

![]({{site.baseurl}}/assets/2017/03/Screenshot-2017-11-16-08.04.28.png)
