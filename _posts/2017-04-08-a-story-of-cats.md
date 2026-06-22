---
layout: post
title: A Story of Cats
date: 2017-04-08 02:46:23.000000000 -05:00
type: post
parent_id: '0'
published: true
password: ''
status: publish
categories:
- IT
- networking
- Wireless
tags:
- 8P8C
- ARCNet
- cable
- Cats
- Ethernet
- Token Ring
meta:
  _edit_last: '2'
  _thumbnail_id: '1435'
  _oembed_7aef0910673826224699b2e9c3b3a52a: "{{unknown}}"
  _oembed_764693efe1028397614d1a06b8206488: "{{unknown}}"
  _oembed_aec078a10b662f4f13a0f2262488d4d8: "{{unknown}}"
  _oembed_505e889503cba6b5c2bb9ca21b25fa54: "{{unknown}}"
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
permalink: "/2017/04/08/a-story-of-cats/"
image: "https://nerdian.ca/files/2017/04/IMG_4054-e1491636089427.jpg"
---

This is the internet, so at some point we've got to talk about cats. It's in the rule book.  The Internet runs on cats. Cat pictures, cat videos, and... cat cables.

Those of you not familiar with the intricacies of the first layer of the [OSI "7-layer Burrito"](https://web.archive.org/web/19990826193318/http://www.europa.com/%7Edogman/osi/) (Internet old-timers will remember this) are probably blissfully unaware of the gory details of the wiring that makes everything (including wireLESS) work.

[caption id="" align="aligncenter" width="900"][![Dilbert (April 24, 2010)]({{site.baseurl}}/assets/2017/04/22e412106cba01301d46001dd8b71c47)](http://dilbert.com/strip/2010-04-24) Dilbert (April 24, 2010)[/caption]

### So who are all these cats, anyway?

Simply put, it's an abbreviation for "Category". The Telecommunications Industry Association (TIA) has adopted a series of specifications over the years defining cable performance to transport various types of networks.

Here's a quick rundown. We're gonna get a tech lesson AND a history lesson all rolled into one.

#### Category 1 (pre-1980)

[caption id="attachment\_1436" align="alignright" width="150"][![An IBM "Type 1" Token-Ring connector. Known colloquially as a "Boy George Connector" due to its ambiguous gender. ]({{site.baseurl}}/assets/2017/04/500003040p-03-02-150x150.jpeg)](http://blog.ianbeyer.com/files/2017/04/500003040p-03-02.jpeg) An IBM "Type 1" Token-Ring connector. Known colloquially as a "Boy George Connector" due to its ambiguous gender. *Photo: [Computer History Museum](http://www.computerhistory.org/revolution/networking/19/381/2187)*[/caption]

This never officially existed, and was a retroactive term used to define "Level 1" cable offered by a major distributor. It is considered "voice grade copper", sufficient to run signals up to 1MHz, and not suitable for data of any sort (except telephone modems). You could probably meet category 1 requirements with a barbed wire fence. You laugh, but [it's been done. Extensively.](http://gizmodo.com/barbed-wire-fences-were-an-early-diy-telephone-network-1493157700)

#### Category 2 (mid-1980s)

Like Category 1, never officially existed, and was a name retroactively given to Level 2 cable from said same distributor. Cat2 brought voice into the digital age. It could support 4MHz of bandwidth, and was used extensively for early Token-Ring networks that operated at 4Mbps, as well as [ARCNet](https://en.wikipedia.org/wiki/ARCNET), which operated at 2.5Mbps on twisted pair (it had previously used coaxial cable).

#### Category 3 (1991)

This is the first of the cable categories officially recognized by TIA. It is capable of operating 10Mbps Ethernet over twisted pair (like ARCNet, Ethernet also ran on coaxial cable in the very early days). Category 3 wire was deployed extensively in the early 1990s as it was a much better alternative to 2Mbps ethernet over coax. This is where the now nearly ubiquitous 8P8C connector (often incorrectly referred to as "RJ45") came into usage for Ethernet, and it's still in use nearly 3 decades later. Both the connector pinout and the cable performance are defined in TIA standard 568.  Since token-ring networks still operated at 4Mbps, they ran quite happily over this new spec. In 2017, one can still occasionally find Cat3 in use for analog and digital phone lines. The 802.3af Power over Ethernet specification is compatible with this type of wire.

#### Category 4 (early 1990s)

This stuff existed only for a very brief period of time. In the late 1980s, IBM standardized a newer version of Token Ring that ran at 16Mbps, which required more cable bandwidth than what Category 3 could offer. Category 4 offered 20MHz to work with (which may sound familiar to the wifi folks, who use 20MHz channels a lot). But Category 5 came along pretty quickly, and Category 4 was relegated to history and is no longer recognized in the current TIA-568 standard.

#### Category 5 (1995)

TIA revised their 568 standard in 1995 to include a new category of cable, supporting 100MHz of bandwidth. This enabled the use of new 100Mbps ethernet (a 100Mbps version of Token Ring soon followed, which also used the same 8P8C connector as Ethernet).

[caption id="attachment\_1437" align="alignleft" width="150"]![An 8P8C connector, commonly (and incorrectly) referred to as "RJ45". The standard twisted-pair ethernet connector for the last quarter century. ]({{site.baseurl}}/assets/2017/04/rtaImage-150x150.jpeg) An 8P8C connector, commonly (but incorrectly) referred to as "RJ45". This has been the standard twisted-pair Ethernet connector for the last quarter century.[/caption]

#### Category 5e (2001)

TIA refined their spec on Category 5 to improve the performance of Category 5, to support the new gigabit ethernet standard. It is still a 100MHz cable, but new coding schemes and the use of all four pairs allowed the gigabit rate. IBM and the 802.5 working group even approved a gigabit standard for token ring in 2001, but no products ever made it to market, as Ethernet had taken over completely by that point.

#### Category 6 (2002)

Not long after Category 5e came to be, Along comes category 6, with 250MHz of bandwidth. This was accomplished partly with better cable geometry and by going from 24AWG conductors to 23AWG. This increased bandwidth allows 10Gbps ethernet to operate on cables up to 55 meters in length.

#### Category 6a (2009)

This refinement to Category 6 increased cable bandwidth to 500MHz in order to allow 10Gbps ethernet to operate at the full 100m length limit for Ethernet. Categories 6 and 6a will support the new 802.11bt Power Over Ethernet Level 3 (60W) and Level 4 (90W) standards (expected 2018) provided that cable bundles do not exceed 24 cables for thermal reasons.

#### Category 7/7a

[caption id="attachment\_1438" align="alignright" width="200"]![Category 7 cable. Who would want to terminate that? What a pain!]({{site.baseurl}}/assets/2017/04/200px-Cat7.jpg) Category 7 cable. Who would want to terminate that? What a pain![/caption]

This one never existed in the eyes of the TIA. It still lives as an ISO standard defining several different types of shielded cable whose performance is comparable to Category 6 (bandwidth up to 600MHz for Cat7, 1GHz for Cat7a). Both these specs were rendered moot by 10Gbps Ethernet operating on Category 6a with standard 8P8C connectors. This cat was so ugly, TIA left it at the shelter.

#### Category 8 (2017)

The latest and greatest, this cable exists to run 40Gbps ethernet. It comes in two flavors, unshielded as **8.1**, and shielded (supplanting the Category 7 specs) as **8.2**. This cable has a bandwidth of 1600MHz for unshielded, and 2000MHz for shielded.

So there you have it. The cats that put the WORK in "Network". And because this is the internet, I leave you with gratuitous kittens.

![Gratuitous Kittens]({{site.baseurl}}/assets/2017/04/89e8c9825ed8f4a033008a2989984a6b-300x211.jpg)
