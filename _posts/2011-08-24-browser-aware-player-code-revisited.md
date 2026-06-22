---
layout: post
title: Browser-aware player code, revisited
date: 2011-08-24 09:09:46.000000000 -05:00
type: post
parent_id: '0'
published: true
password: ''
status: publish
categories:
- streaming
- Wowza
tags:
- flash
- HTML5
- JWPlayer
meta:
  _edit_last: '1'
  wp_plus_one_redirect: ''
  dsq_thread_id: '394760834'
  _googl_shortlink: http://goo.gl/vVgrR
  _syntaxhighlighter_encoded: '1'
author:
  login: ianbeyer
  email: ian.beyer@gmail.com
  display_name: Ian Beyer
  first_name: Ian
  last_name: Beyer
permalink: "/2011/08/24/browser-aware-player-code-revisited/"
---

I posted a while back about [selecting video players based on browsers](http://nerdian.ca/code/browser-aware-player-code/ "Browser-Aware Player code")... It was an ugly javascript hack, and since then [LongTail](http://longtailvideo.com "Longtail Video") has updated their excellent [JWPlayer](http://www.longtailvideo.com/players/ "JW Player") to support multiple methods. In order to create an embed that worked best for supporting both HTML5 and Flash players, I had to dig through the documentation a little bit, and combine a couple of different sections.
Here's how to embed JWPlayer 5.7 to try flash first, with multiple bitrates, and then attempt HTML5 if Flash is not supported. This particular scenario is for iOS support.

```javascript
Loading the player ...

jwplayer("container").setup({
height: 360,
width: 480,
image: "http://server.com/images/thumbnail.jpg",
skin: "bekle.zip",
modes: [
{
type: "flash",
src: "player.swf",
config: {
levels: [
{ bitrate: 250, file: "playlist-low", width: 320 },
{ bitrate: 500, file: "playlist-high", width: 480 }
],
streamer: "rtmp://streamer.com:1935/live",
provider: "rtmp"
}
},
{
type: "html5",
config: {
file: "http://streamer.com/live/ipad.smil/playlist.m3u8"
}
} ]
}
);
```

This still doesn't support RTSP and other HTML5  fallbacks due to limitations in JWPlayer, so if you're on a BlackBerry, you'll still need to switch the player. The order that the "type" statements appear in the javascript determines the order in which they'll be tried. Generally, you'll want to try Flash first, otherwise browsers that support HTML5 but not Apple's HTTP Live Streaming (which is pretty much all of them), will default to the HTML5 player, but be unable to get the stream. You can, however, provide multiple video sources with different codecs (for on-demand content) to support the different flavors of browsers, though.
