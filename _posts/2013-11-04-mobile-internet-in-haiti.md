---
layout: post
title: Mobile Internet in Haiti
date: 2013-11-04 21:11:24.000000000 -06:00
type: post
parent_id: '0'
published: true
password: ''
status: publish
categories:
- Haiti
- Hardware
- IT
- networking
- Wireless
tags: []
meta:
  _edit_last: '2'
  _wpas_done_all: '1'
  dsq_thread_id: '1937166257'
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
permalink: "/2013/11/04/mobile-internet-in-haiti/"
image: "/assets/images/2013/11/Screen-Shot-2013-11-05-at-8.03.55-AM-300x200.png"
---

**Note: Be sure to read my [March 2015 update](http://blog.ianbeyer.com/2015/03/03/mobile-internet-in-haiti-part-2/ "Mobile Internet In Haiti, Part 2") about this...**

I'm back down in Haiti, as some of you already know, working on some of the wireless networks linking the different sites of the Église Méthodiste d'Haïti (EMH), which is the Haitian Methodist Church. Knowing that I was coming into an environment where the internet connection was not functioning properly, and that I was likely going to need internet access for troubleshooting, I armed myself with a 3G GSM hotspot that I picked up on eBay.

After parting with about 50 bucks (plus another 15 for a charger and 2 spare batteries), the [Huawei E583C](http://www.huaweidevice.com/worldwide/productFeatures.do?pinfoId=2619&directoryId=2462&treeId=462&tab=0 "Huawei E583C") unit showed up via USPS on my doorstep 4 days later bearing a postmark from Hong Kong (color me impressed, I can't even get postcards from Toronto that quickly!)

[![20131125_150332]({{site.baseurl}}/assets/2013/11/20131125_150332-300x152.jpg)](http://blog.ianbeyer.com/files/2013/11/20131125_150332.jpg)I opened it up and inside was a "[T-Mobile Wireless Pointer](http://www.t-mobile.co.uk/shop/mobile-broadband/wireless-pointer/ "T-Mobile UK Wireless Pointer")" from the UK division of T-Mobile. I popped on down to the local T-Mobile store and get a SIM for testing, and fired it up. After much futzing around trying to get it to speak 3G to the network without any success, I go back to T-Mobile and pick a tech's brains. Turns out this one operates on the 800/1800/1900 band, which T-Mobile has phased out 3G on to make room for more LTE. Meanwhile, Jay was in Haiti, so I asked him to pick up a NatCom SIM and bring it home with him.

I'll pause briefly here to talk a bit about mobile in Haiti. There are two major players, [Digicel](http://en.wikipedia.org/wiki/Digicel "Digicel") (which has a thing for island nations all over the world) and NatCom, which is formed out of what was left of the national telephone company (Teleco) and the Vietnamese national telecom (VietTel) that bought up a 70% interest in Teleco not long after the earthquake. What little copper telecom infrastructure existed in the country has long since been destroyed by a number of different [![Screen Shot 2013-11-25 at 3.20.19 PM]({{site.baseurl}}/assets/2013/11/Screen-Shot-2013-11-25-at-3.20.19-PM-300x172.png)](http://www.columbus-networks.com/)means, both natural and human. Since the earthquake, NatCom has been building out a LOT of fiber. Digicel operates the only direct fiber link out of the country to [Columbus Networks](http://www.columbus-networks.com/ "Columbus Networks")' Fibralink fiber network that links the Caribbean up to the rest of the world. The other way out of Haiti to the internet is via microwave backhaul to the Dominican Republic which has 2 landings of the [ARCOS](http://en.wikipedia.org/wiki/ARCOS "ARCOS Fiber Network") fiber ring.

In the nearly 4 years since the quake, mobile internet in Haiti has gone nuts. It's now quite reliable, and surprisingly cheap if you know how to do it. Monthly postpaid plans for data cost about a quarter what they do in the US - a 10GB plan on digicel will set you back 1000 HTG (about 25 bucks). The same plan on Verizon in the US by comparison is about $100! Digicel offers current-generation Android phones like the S4 (but be prepared to part with full unsubsidized price for it), and Apple recently started [making unlocked SIM-less iPhones available on its own store](http://www.geeky-gadgets.com/apple-offering-unlocked-iphone-5s-in-the-us-25-11-2013/ "Unlocked iPhones"). The smartphone revolution is coming to Haiti, and it's going to be interesting to watch. There was someone at church on sunday using an iPad, and it wasn't someone from our team.

[![]({{site.baseurl}}/assets/2013/11/Screen-Shot-2013-11-25-at-3.14.05-PM-300x193.png)](http://blog.ianbeyer.com/files/2013/11/Screen-Shot-2013-11-25-at-3.14.05-PM.png)When I got down to Haiti and put the SIM Jay obtained for me into the hotspot (erm, "Pointer"... can any Brits enlighten me as to the origin of that term?), and getting no joy. Realizing that the zillion config changes I'd made to try and get it to work on T-Mobile's network were probably interfering, I hit the factory reset button, and as soon as it rebooted, it was speaking 3G on Natcom's network. It was that easy.

Next step was to load up some funds on the card, since it was a basic card that came empty of funds. Normally you can do this from the phone, but since this was a hotspot, I didn't have the ability to dial numbers (although the Huawei firmware does allow you to SMS, which turned out to be a critical component). Natcom partners with a third party called [EzeTop](http://ezetop.com "EzeTop") which allows you to reload phone cards online (yours or anyone else's). So I dropped 10 bucks onto it (which translates to 392 HTG, a fairly lousy exchange rate) plus a penny per 10 Goudes as a transaction fee, and off I go. No sign anywhere of what the per-MB cost is. NatCom's website isn't particularly helpful in that regard (I later find out that it's 1.9HTG/MB, about 4 cents.)

Now that I had mobile internet, I fired up the iPad and did some testing on the drive to Petit-Goave, and was getting quite reasonable speeds around 1.5-2Mbps in both directions, very much capable of posting pictures to facebook and whatnot.

Once we got to the guest house where we were staying, we discovered that the wifi there was indeed out of service. I put the hotspot to good use downloading information I was going to need to fix it. In very short order, net access ceases, and I get a screen from NatCom saying that my card is empty, and provides a helpful list of plans and how to activate them. I then go find our hostess and borrow her laptop and internet access to load up some more funds on the card, and then try to activate one of the listed plans. It tells me I can't do that because I have the wrong type of card.

[![]({{site.baseurl}}/assets/2013/11/Screen-Shot-2013-11-05-at-8.03.02-AM-300x173.png)](http://blog.ianbeyer.com/files/2013/11/Screen-Shot-2013-11-05-at-8.03.02-AM.png)Then, disaster. Within a matter of little more than an hour, 20 bucks worth of data on the card had vanished. After some digging, I discovered that my good buddy CrashPlan had stabbed me in the back and decided to start a big backup. I killed CrashPlan and reloaded the card (this is getting expensive, and I'm still not entirely sure how much data I'm burning through, especially now that the team is sharing in the internet joy -- and the cost!)

Now that I'm back online, I start digging around the NatCom site again to figure out what plans I can access through the SIM I already have. Turns out that they have slightly different SIMs and [plans for laptop/USB modems](http://natcom.com.ht/3g/d-com-3g.html "Natcom Mobile Laptop Plans") and for [mobile phones](http://natcom.com.ht/mobile/plan-prepaye.html "Natcom Mobile Prepaid Plans"). I had the latter, a "Nat-Mango" card, which can be had from any street vendor for 25 HTG. I finally found the list of mobile internet plans for the phones, and the correct number to SMS the plan change to. So I send off the text, only to get back "You don't

![Screen Shot 2013-11-05 at 8.03.55 AM]({{site.baseurl}}/assets/2013/11/Screen-Shot-2013-11-05-at-8.03.55-AM-300x200.png)

have enough funds for this plan". I keep moving down the list until even the cheapest one kicks back the message... Uh-oh, I'm running on fumes again. Just as I go to top it up again, it shuts off. Fortunately, one of our Haitian team members had data on his Digicel phone, and I was able to get the account charged up, and switched over to the "Unlimited" plan. Unlimited in this case means 3.5GB at max HSPA+ speeds, then you're rate-limited to 3.5 Mbps after that. Given that I never saw 3Mbps anywhere, this isn't really a huge hindrance (that may be a factor of the device more than the network, too). By the time the week was out, our team had gobbled up nearly 25 gigabytes of data through the device.

So, in short, mobile internet from local carriers in Haiti is reliable and cheap (if you know the trick to not paying out the nose per MB), and can be done on a fairly inexpensive piece of hardware. If you're so inclined, you can also get USB sticks from NatCom for about 1500 HTG. My next step is going to be to see if a device from [Cradlepoint](http://cradlepoint.com "Cradlepoint") can handle the Natcom USB sticks, since they don't have such a tight limitation on clients.
