---
layout: post
title: Windows Updates, To Go!
date: 2011-07-07 15:53:46.000000000 -05:00
type: post
parent_id: '0'
published: true
password: ''
status: publish
categories:
- Haiti
- Hardware
- IT
tags:
- FX160
- Windows 2003
- WSUS
meta:
  dsq_thread_id: '352464797'
  _edit_last: '1'
  _googl_shortlink: http://goo.gl/12XbK
author:
  login: ianbeyer
  email: ian.beyer@gmail.com
  display_name: Ian Beyer
  first_name: Ian
  last_name: Beyer
permalink: "/2011/07/07/windows-updates-to-go/"
---

When I leave for my trip to Haiti in a few weeks, one of the things I'll be doing is bringing multiple computers up to current patches. There are a few ways to do that:

One is to bring some sort of removable media (optical or flash stick) down and apply them manually. The problem with this is that once I leave, the machines stay in their current state until the next geek can come down and apply the next batch of patches. Downloading patches for multiple machines over developing-world internet connections can easily run into daily bandwidth caps, and Windows Update doesn't cache very well through a normal proxy server such as [Squid](http://www.squid-cache.org/ "Squid Web Proxy").

Another is to use [Windows Server Update Services (WSUS)](http://technet.microsoft.com/en-us/windowsserver/bb332157 "Windows Server Update Services (WSUS)"). I initially considered setting up a Windows Server VM on my laptop, syncing up the updates stateside and temporarily configuring the machines down there to pull from my impromptu update server. Then I got the idea that a lightweight appliance-type server that lived down there permanently would be a useful solution that would download the patches once and distribute them over the LAN. Since we're planning on using [Microsoft Security Essentials](http://www.microsoft.com/en-us/security_essentials/default.aspx "Microsoft Security Essentials") for anti-malware, this solves the problem of definition updates. Daily patch sync would happen in the wee hours of the morning when the oversubscribed connections in Haiti are generally pretty clear.

I rummaged around the office and found a Dell FX160 thin client that we got as a demo unit from Dell (I have a [number of blog posts](http://nerdian.ca/tag/fx160/ "Dell FX160 Thin Client") on the topic of this device). It has been gathering dust for some time as it's hobbled with a 1GB SATA flash disk and limited RAM. After checking on hardware requirements for both Windows Server and WSUS, I went out and picked up a 120GB SSD and a pair of 2GB RAM sticks and put them in. The choice of an SSD wasn't so much for performance reasons (although it can't hurt), but for the machine to be entirely solid-state. It's going to live in a fairly harsh environment where mechanical failures are likely.

Once I got the hardware put together, I hooked up a USB optical drive and loaded Windows Server 2003 R2, and then installed WSUS and performed an update sync. The whole process went mostly smoothly.

Here are a few of the gotchas in installing Windows 2003 on an FX160 thin client, a job it was NEVER meant to do:

- SATA controller needs to be in ATA mode. If it's in AHCI mode, Windows 2003 will not recognize the disk.
- When using a storage device that the BIOS recognizes as a hard drive, it expects to see a fan plugged into the motherboard. This fan is part of the hard drive bracket kit (Dell P/N H224H). When a fan is not detected, each boot will require a manual intervention during POST to press F1.
- Stock Windows 2003 media does not include video drivers or network drivers for the FX160 (Broadcom NetXTreme 57XX).
- Dell's support site doesn't have the most recent drivers for the Broadcom.
- It's virtually impossible to find a 6" SATA extension connector, either for data, power, or both. I was finally able to find a power extension, but used a standard SATA cable to connect to the other SATA port on the motherboard.

The SSD I used for this is an [OCZ Agility 3](http://www.ocztechnology.com/ocz-agility-3-sata-iii-2-5-ssd.html "OCZ Agility 3"), 120GB. Disk performance on large writes is almost 100MB/sec, which is about twice as fast as my 7200RPM spindle drive in my laptop. Windows performs very well with 4GB, a SSD, and a 1.6GHz Atom processor.

The next step was to configure the clients to update from the server for testing. I still have one of the Asus netbooks that we deployed to Haiti in a previous trip. This is where I discovered that Windows Home and Windows Starter don't include the policy editor (gpedit.msc) that I'm used to finding on Pro/Enterprise/Ultimate versions of windows. This is understandable, your average home user doesn't (and shouldn't) normally jack with system policy. Fortunately, all the policy editor does is manipulate registry keys, and the process of configuring Windows Update via the registry is [well documented](http://support.microsoft.com/kb/328010 "How to configure automatic updates by using Group Policy or registry settings"). This actually simplifies things, since all I have to do is create a .reg file that I can import on all the target machines.

Next post: Installing [Squid](http://www.squid-cache.org/ "Squid Web Proxy"). Not content to use this box for mere update caching, we're gonna have it be our web proxy as well.
