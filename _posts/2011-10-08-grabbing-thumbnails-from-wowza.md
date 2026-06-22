---
layout: post
title: Grabbing thumbnails from Wowza
date: 2011-10-08 22:45:36.000000000 -05:00
type: post
parent_id: '0'
published: true
password: ''
status: publish
categories:
- streaming
- Wowza
tags:
- thumbnails
meta:
  _edit_last: '2'
  wp_plus_one_redirect: ''
  dsq_thread_id: ''
  _googl_shortlink: http://goo.gl/1NFMJ
author:
  login: ianbeyer
  email: ian.beyer@gmail.com
  display_name: Ian Beyer
  first_name: Ian
  last_name: Beyer
permalink: "/2011/10/08/grabbing-thumbnails-from-wowza/"
---

Here's a quick and dirty way to grab a thumbnail from a Wowza application:

```

rtmpdump -v -B 0.01 -r rtmp://wowza.server/application/stream -o temp.flv
ffmpeg -i temp.flv -vframes 1 -s qvga /var/www/frame.jpg
```

There's also a way to [do it with a Wowza module](http://www.wowza.com/forums/showthread.php?577-Custom-module-to-create-single-frame-snapshots-of-live-and-VOD-stream "Single-frame snapshots"), but it's considerably more complex and not for the faint of Java.

Caveat: This likely won't work if you have hotlink denial turned on on your stream.
