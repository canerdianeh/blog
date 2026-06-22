---
layout: post
title: Live Streaming on a Budget (Part 4) - How it works
date: 2009-07-05 13:43:18.000000000 -05:00
type: post
parent_id: '0'
published: true
password: ''
status: publish
categories:
- Internet Campus
- streaming
tags:
- A/V
- ec2
- production
- VT5
meta:
  _edit_last: '2'
  dsq_thread_id: '219350018'
  _googl_shortlink: http://goo.gl/ofAlp
author:
  login: ianbeyer
  email: ian.beyer@gmail.com
  display_name: Ian Beyer
  first_name: Ian
  last_name: Beyer
permalink: "/2009/07/05/live-streaming-on-a-budget-part-4/"
---

We started streaming to iPhones today. Huge success, way easier than it ought to be, now that the iPhone does HTTP streaming and Wowza's V2 software supports everything needed to stream to the FruitFone. All we had to do was shell out $250 to MainConcept for their [AAC encoder plugin](http://www.mainconcept.com/site/prosumer-products-4/aac-encoder-21580/information-21891.html) for Flash Media Live Encoder. (Although we subsequently discovered that there is a bug with the MainConcept encoder that cause audio sync problems on iPhone, so we've moved iPhone encoding off to a separate machine)

There are a lot of layers to this onion, so I put together a [block diagram](http://nerdian.ca/streaming/workflow) that links everything from the cameras to client.
