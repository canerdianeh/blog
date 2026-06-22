---
layout: page
title: The Old Lab.
date: 2020-09-21 18:56:03.000000000 -05:00
type: page
parent_id: '0'
published: true
password: ''
status: publish
categories: []
tags: []
meta:
  _edit_last: '2'
  _cs_replacements: a:1:{s:7:"sidebar";s:7:"sidebar";}
  _thumbnail_id: '1789'
  _last_editor_used_jetpack: block-editor
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
permalink: "/the-old-lab/"
image: "/assets/images/2020/09/AdobeStock_298508606.jpeg"
---

I often get asked about what's in The Lab. It's always somewhat fluid, but I'll update this page accordingly. This is the lab as it stood prior to January 2021 when I moved.

## The Rack.

![]({{site.baseurl}}/assets/2020/09/IMG_4114-496x1024.png)

The rack itself is a [StarTech.com 25U open-frame server rack](https://amzn.to/3hN52M5). Contents (top to bottom)

**Slot 25 Front**: Brocade VDX 6740 Leaf Switch (SW-AGMAN)

- 48 SFP+ 10-gigabit ports (Ethernet/Fiberchannel)
- 4 QSFP+ 40-gigabit ports (Ethernet/Fiberchannel)
- Dual Power Supplies

*This switch is my 10-gigabit backbone. Annoyance: Brocade would ship these (at a list price of $50,000) with only 24 of the SFP+ ports licensed for 10Gbps Ethernet. So it's really a 24-port switch and the four 40Gbps ports are decorative, unless I cough up the price of a small car to turn them on. When Broadcom bought Brocade and sold it off for parts, the NetworkOS datacenter switch line went to Extreme Networks, while the FastIron campus switch line and Ruckus Wireless went to Arris, and ultimately CommScope.*

**Slot 25 Rear**: [Tripp-Lite rackmount PDU](https://amzn.to/3kuObQ6) (non-UPS)

*For plugging in random stuff like monitors.*

**Slot 24:** Panduit [CPP24WBLY Modular Patch Panel](https://amzn.to/3cnnxWC).

- Cat 6 jacks are [Panduit CJ688TGOR](https://amzn.to/2FUKHY4)
- Couplers are [Panduit PCM-F3](https://amzn.to/35UJN91)
- First 8 ports are tie lines to the structured wiring enclosure in my office (more on that later).
- 2 ports go to the wall plate by my desk.
- 2 ports go to the AP on my office ceiling.
- 2 ports go to the garage, one for the AP, and one for my FlightFeeder.

*Yes, Panduit is considerably more expensive than the cheap jacks you can get from Monoprice or amazon. But they are incredibly reliable and most of these jacks are recycled/reused from other jobs. They also take about half the time to terminate. My supplier for these for almost 20 years has been Accu-Tech in Kansas City.*

*This modular system originated at Sprint when they were building their HQ campus in Overland Park, Kansas in the late 1990s. The patch panel holds six modular furniture (cubicle) inserts that have 4 jacks each. As luck would have it, the standard data knockout for modular furniture fits perfectly 6 across in a single rack space. Sprint also needed to be able to put two UTP/Cat5e outlets and one double-wide SC fiber outlet in each cubicle. So this system was designed to fit them all together, and required considerably less tooling. The jacks are also compact enough that you can also get a 48-port modular panel that fits in 1U, which makes data center people happy.*

**Slot 23**: HPE ProCurve 3800M PoE+ switch (SW-IVEL)

- 48 PoE+ gigabit copper ethernet
- 4 10-gigabit SFP+
- Linked to SW-AGMAN via dual 10G LACP Trunk
- Aruba 10GBase-SR Optics, OM4 optical patch
- Linked to SW-AGMAN via dual 10G LACP Trunk

**Slot 21**: Vertiv Avocent LRA185 Rack Console (with Avocent SV240 KVM on the back side)

**Slot 20**: Aruba 7005 Mobility Controller (MC-NEIL)

**Slot 19**: Aruba 7005 Mobility Controller (MC-KENZIE)

**Slot 18**: Aruba 7005 Mobility Controller (MC-TAVISH)

- ArubaOS 8.7.1.0
- Clustered, controlling the home WLAN
- Managed by Mobility Master
- Linked to SW-IVEL via 2x Gigabit LACP/Port Channel.
- Powered via PoE
- RAP termination on MC-TAVISH

**Slot 17:** HP DL360 (Gen 7) server (ANGUS)

- General purpose remote desktop
- Windows 10
- 2x Intel Xeon X5660 @2.8GHz (12 cores/24 threads)
- 32GB RAM
- 8x 300GB SAS10K HDD (2 in RAID1, 6 in RAID5)
- Dual Power Supplies
- Dual-Port QLogic BCM57810 10G Ethernet
  - fs.com 10GBase-SR optical modules
  - Connected to SW-AGMAN via OM4

**Slot 16**: HP DL360 (Gen7) server (ROTO)

- Router/Gateway
- pfSense
- 2x Intel Xeon X5660 @2.8GHz (12 cores/24 threads)
- 24GB RAM
- 4x 300GB SAS10K HDD (RAID10)
- Dual Power Supplies
- Integrated 4-port 1Gbps NIC
  - Connected to Internet
- Dual-Port QLogic BCM57810 10G Ethernet
  - fs.com 10GBase-SR optical modules
  - Connected to SW-AGMAN via OM4
  - 20Gbps LACP trunk with VLANs

**Slot 15**: HP DL360 (Gen 8) server (VM-OOSE)

- Virtualization Host
- VMWare vSphere 7.0
- 2 x Intel Xeon E5-2640 @ 2.5GHz (24 Logical Processors)
- 64GB RAM
- 8 x 300GB SAS10K HDD (RAID6)
- 16GB Internal USB (OS)
- Dual Power Supplies
- Dual-Port QLogic BCM57810 10G Ethernet
  - fs.com 10GBase-SR optical modules
  - Connected to SW-AGMAN via OM4

**Slot 13/14**: HP DL380 (Gen8) server (VM-INAL)

- Virtualization Host
- VMWare vSphere 7.0
- 2 x Intel Xeon E5-2660 @ 2.2GHz (32 Logical Processors)
- 128GB RAM
- 5 x 2TB SAS7.2K HDD (RAID5)
- 16GB Internal USB (OS)
- Dual Power Supplies
- Dual-Port QLogic BCM57810 10G Ethernet
  - fs.com 10GBase-SR optical modules
  - Connected to SW-AGMAN via OM4

**Slot 8-12**: HPE ML110 (Gen 10) server (VM-PYRE)

- Virtualization Host
- VMWare vSphere 7.0
- Intel Xeon Silver 4110 @ 2.1GHz (16 Logical Processors)
- 16GB RAM
- NVidia M2090 Server GPU (512 cores)
- 2 x 6TB SAS7.2K HDD (RAID1)
- 1 x 10TB SATA HDD (JBOD)
- 1 x 14TB SATA HDD (JBOD)
- 16GB Internal USB (OS)
- Dual Power Supplies
- Dual-Port QLogic BCM57810 10G Ethernet
  - fs.com 10GBase-SR optical modules
  - Connected to SW-AGMAN via OM4
- [NavePoint Server Rails](https://amzn.to/32RYkjM)

**Slot 6**: Dell Poweredge R210 (NM-ROD)

- Network Monitoring
- Ubuntu Linux
- Intel Xeon quad core somethingorother
- 8GB
- 512GB Samsung EVO 950 SATA SSD
- InfluxDB/Grafana/Telegraf
- Dual-port integrated gigabit NIC

**Slot 4/5**: [CyberPower OR2200LCDRT2U](https://amzn.to/3mA9fGC) (UPS-CALE)

- 2200VA Backup power (Leg A/Blue)
- [RMCARD205 Remote Management/SNMP Interface](https://amzn.to/3cqEXBx)
- Dedicated 120V/20A circuit
- [NavePoint Server Rails](https://amzn.to/32RYkjM)

**Slot 1/2**: [CyberPower OR2200LCDRT2U](https://amzn.to/3mA9fGC) (HICC-UPS)

- 2200VA Backup power (Leg B/Red)
- [RMCARD205 Remote Management/SNMP Interface](https://amzn.to/3cqEXBx)
- [CyberPower ENVIROSENSOR environmental sensor](https://amzn.to/32PTWBH)
- Dedicated 120V/20A circuit
- [NavePoint Server Rails](https://amzn.to/32RYkjM)

## The Can.

![]({{site.baseurl}}/assets/2020/09/65197850-5007-451E-B1FB-5BB707A26FA9-576x1024.png)  

Lives in my office, feeds everything in the house.

The wiring "can" is a [Leviton 28" structured residential wiring enclosure](https://amzn.to/2RMJ8OC). The top two patch panels are [Leviton 476TM-624 Twist and Mount](https://amzn.to/3iMqn9T) (Cat6). Left panel goes to various places in the house. Right panel has the ties to the lab rack and to the other wiring enclosure. Why no Panduit? Because they don't make any frames for these types of enclosures. Boo!

Power is [Leviton 47605-PSC Power Supply](https://amzn.to/35WTALy), which provides surge protection on two outlets and 40W of 12V DC power. Sadly, it does not provide backup power. It is hardwired to a dedicated 120V/20A circuit. I replaced the standard lid with a hinged lid. If you're building a new one of these, get the 42". 28" gets used up way fast.

The switch is a [Ruckus ICX 7150-C12P-2X10G PoE+ switch](https://amzn.to/2G2c5Dp) (link goes to 2x1G model). 12 ports of PoE+, 2 non-PoE ports, and 2 SFP+ ports (with fs.com optics, and 20G LACP trunk to SW-AGMAN via a pair of 15m OM4 patch cables. It is attached to the enclosure by way of a [Keeper MG magnetic gun mount](https://amzn.to/2ZWUMuy), which is screwed into the enclosure, and holds the switch in place magnetically.

## The Other Can.

![]({{site.baseurl}}/assets/2020/09/DECD2F35-6430-4C7F-8E13-4C25410C997B-576x1024.png)

This wiring enclosure is a Commercial Electric 14" enclosure (Home Depot). It contains a pair of Uniprise (CommScope) 8-port patch panels that feed the bedrooms on the far end of the house. This was installed mainly to avoid having to pull 16 more cables into my office enclosure.

Switch is a HP ProCurve 1810-8G, powered by PoE from the main wiring can. Only thing on it right now is the front door camera, a Ubiquiti G3 camera. Outlet has built in surge protection.

## Around the House

**Wireless:**

- [Aruba AP-515](https://www.arubanetworks.com/products/networking/access-points/510-series/) (AP-PEAL, AP-OGEE)
- [Aruba AP-315](https://www.arubanetworks.com/products/networking/access-points/310-series/) (AP-OSTATE, AP-PLAUSE, AP-TITUDE, AP-HORISM)
- [Aruba AP-303H](https://www.arubanetworks.com/products/networking/access-points/303h/) (AP-TERYX, AP-PETIZER, AP-EX)
- [Aruba UXI Sensor](https://capenetworks.com/) (NO-CAPES)
- [Aruba Beacons](https://www.arubanetworks.com/en-au/products/location-services/aruba-beacons/) (Beaconator, CanadianBeacon, BeaconAndEggs, BeaconLettuceTomato, SmokedBeacon, CuredBeacon)

## Virtual Servers

- Aruba Mobility ~~Masters~~Conductors (MM-GOOD, MM-BOPP)
- Aruba Mobility ~~Controller~~ Members (MC-HAMMER, MC-NUGGET, MC-LAREN)
- Aruba ClearPass Policy Manager (CP-TAIN, CP-YBARA)
- Aruba AirWave Management Platform (AMP-HIBIAN)
- Aruba Analytics and Location Engine (ALE-HOUSE)
- VMWare VCenter (VC-TORY)
- [Plex Media Server](https://plex.tv) (GUERNSEY)
- Active Directory Domain Services (AD-IOS, AD-HD)
- Active Directory Certificate Services (TEARGAS)
- [T-Pot](https://northsec.tech/introduction-to-t-pot-the-all-in-one-honeypot/) (honeypot)
- HPE Integrated Management Center (IMC-OMING)
- GNS (GNS-LINGER)

![]({{site.baseurl}}/assets/2020/09/86D6E7B1-2561-49C0-871B-431D2857CF14-1024x768.jpeg)  

The Office.

## The Office.

- Desk
  - IKEA Adjustable height frame
  - 36"x72"x1U Boos solid maple butcher block top
  - Built-in Qi charger
  - Lacing Bars
  - 12 outlet Power Strip
- Mac Notebook:
  - MacBook Pro 13" (2019)
  - Intel Core i5 (quad) @ 2.4GHz
  - 16GB RAM
  - 250GB SS Storage
  - 2x LG 27UK850 4K displays (via Type C DisplayPort+USB 3.1)
- Windows Notebook:
  - Surface Book (2016)
  - Core i7 Quad
  - 16GB
  - Surface Dock
  - Windows 10
- Network:
  - Aruba 2930F-8G PoE+ switch (SW-EDEN)
  - 8 1GBase-T gigabit copper Ethernet ports
  - 2 10-gigabit SFP+ ports
  - Linked to SW-AGMAN via 2x10G
  - fs.com 10GBase-SR Optics, OM4 optical patch

- Audio-Visual:
  - iConnectivity iConnectAUDIO 4+ Audio Interface (USB)
  - Logitech c920 USB Camera
  - JBL LSR305 Studio Monitors
  - Azden SGM1000 Shotgun Mic
- Monitoring Dashboard
  - Raspberry Pi 4 with PoE Hat
  - Dual Dell 23" FHD Displays
- Software:
  - Ekahau Pro
  - Visio
  - Office 365
  - Adobe Creative Cloud
  - GNS
  - Iris
  - ZOC Terminal
  - Notepad++
  - Edge
  - Spyder Elite (display color calibration)
