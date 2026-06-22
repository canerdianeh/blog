---
layout: post
title: Amazon and new Cloudfront Streaming
date: 2009-12-18 13:25:29.000000000 -06:00
type: post
parent_id: '0'
published: true
password: ''
status: publish
categories:
- streaming
tags: []
meta:
  dsq_thread_id: '224345559'
  _edit_last: '2'
  _googl_shortlink: http://goo.gl/Z2hDr
author:
  login: ianbeyer
  email: ian.beyer@gmail.com
  display_name: Ian Beyer
  first_name: Ian
  last_name: Beyer
permalink: "/2009/12/18/amazon-and-new-cloudfront-streaming/"
---

Earlier this week, I got an e-mail from Amazon Web Services, with some new goodies being announced.

The first was new pricing for Wowza. While the cost of each instance-hour is going up slightly, the cost of bandwidth is dropping about 15%. This makes me happy.

The second was that [Wowza has released version 2](http://www.wowzamedia.com/index.html). I've been working with preview versions of this since last summer with our iPhone streaming. They've made some very cool improvements to the product.

Lastly was an item that intrigued me. Amazon has, via Flash Media Server, added RTMP streaming capability to [Cloudfront](http://aws.amazon.com/cloudfront/), Amazon's cloud answer to CDN. Now instead of being able to widely distribute files, you have the capability of setting up a distribution that provides RTMP streaming of any supported video file in an S3 bucket. If you use S3 for on-demand video content, this is big for you. No longer do your viewers have to download the entire file (and run up the bandwidth meter in the process). They can now skip directly to the points they need and only use the bandwidth for stuff they actually watch.

This is potentially very good news for services that serve on-demand content from S3 (such as [blip.tv](http://www.blip.tv))

It's not so good news for the folks at Wowza, because I no longer have to spin up a Wowza instance to serve content stored in S3. Luckily for Wowza, the Cloudfront streaming doesn't do live video.

It'll be interesting to see how this plays out. As it currently stands, we could replace blip.tv with this functionality, but for the small cost, we get a whole lot of value from Blip.
