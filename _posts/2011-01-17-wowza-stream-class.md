---
layout: post
title: Using the Wowza Stream Class
date: 2011-01-17 16:43:07.000000000 -06:00
type: post
parent_id: '0'
published: true
password: ''
status: publish
categories:
- Internet Campus
- streaming
- Wowza
tags:
- playlists
- SMIL
- stream class
meta:
  dsq_thread_id: '218055152'
  _wp_old_slug: ''
  _edit_last: '2'
  s2mail: 'yes'
  _googl_shortlink: http://goo.gl/gPy1B
  _oembed_34ecd288be0b6759e6db0362878554cd: "{{unknown}}"
  _oembed_5895943b2bd038c50d33e21ab72a8ad6: "{{unknown}}"
  _oembed_9b0e24a9d37db500414bbc46c9922921: "{{unknown}}"
  _oembed_e059da45c594a3d8ad225630b0ed4544: "{{unknown}}"
  _oembed_4ff3539d9d2648030cad39eae7b319fe: "{{unknown}}"
  _oembed_fb62dde521738c4928a9b8a20416e4f1: "{{unknown}}"
  _oembed_02ce231f81ef1018aeb3cce5465a703d: "{{unknown}}"
  _oembed_681877c3f85700867c1df156c1efb2b0: "{{unknown}}"
  _oembed_cf3334a6952cc23f10f5a82cc45bf984: "{{unknown}}"
author:
  login: ianbeyer
  email: ian.beyer@gmail.com
  display_name: Ian Beyer
  first_name: Ian
  last_name: Beyer
permalink: "/2011/01/17/wowza-stream-class/"
---

I mentioned in the previous post about using [ffmpeg](http://ffmpeg.org "ffmpeg") in a cron job to create Simulated Live events via Wowza. In this post, I'll explain how to do it using the Wowza Stream Class module, which allows you to set a broadcast schedule to play a mix of recorded and live content.
Wowza has a pretty good [document](http://www.wowzamedia.com/forums/content.php?145 "Stream class example with playlists and schedules set in smil file") on how to add this module in to your server and do a test playlist.If you're setting this up on Amazon EC2, you'll need to update your startup package by putting the module in the wowza/lib directory and the playlist in the wowza/content directory
Unfortunately, the tutorial doesn't really cover playlist creation beyond the example. This is especially tricky, given that the scheduling parameters don't seem to conform to any known SMIL standard. Yes, it's XML, so theoretically, it doesn't matter, but there are extensions in [SMIL 3.0](http://www.w3.org/TR/2006/WD-SMIL3-20061220/ "SMIL 3.0") that are meant to deal with server-side playlists for automating programming.
Unless you specified a different application name in the Properties section of Server.xml, the automated playlist will publish to the \*live\* application.
The basic structure of the SMIL file body consists of  and  statements.
### Stream Element
The  element defines one or more virtual stream names that the playlists will feed into:

```

<stream name="playlist-high"></stream>
<stream name="playlist-low"></stream>
```

In this example, I have a high and low bandwidth stream. In your player, you reference the stream name, rather than the streamshedule.smil file, like this:
#### Flash RTMP:
streamer: rtmp://wowza.server.address(:port)/live
file: playlist-high
#### Flash HTTP:
http://wowza.server.address/live/playlist-high/manifest.f4m
#### HLS:
http://wowza.server.address/live/playlist-high/playlist.m3u8
#### Silverlight
http://wowza.server.address/live/playlist-high/Manifest
### Playlist element
The  element defines specific video sequences that go into the virtual stream. There are four key parameters to the playlist element:
- \*\*name\*\* : This is a unique name for that particular sequence.
- \*\*playOnStream\*\* : This tells the Stream Class module which of the previously defined streams this playlist is associated with.
- \*\*repeat\*\* : Valid values are true/false. This defines whether this playlist loops when it gets to the end.
- \*\*scheduled\*\* : When this playlist is scheduled, in the format "YYYY-MM-DD HH:MM:SS" (24-hour time)
Within the playlist element are one or more  statements that use the following parameters:
- \*\*src\*\*: the video to be played. Can either be:
- a stream within the same live application (use the stream name only)
- an MP4 video file in the Wowza content directory (use \*mp4:filename.mp4\*)
- A stream elsewhere (requires some additional modules)
- \*\*start\*\* : The number of seconds into the video to start playing. If this is a live source, use the value \*\*-2\*\*.
- \*\*length\*\* : The number of seconds to play the video. The value \*\*-1\*\* indicates to play until it ends.
Using start/length is a useful way to introduce commercial breaks or intermissions into a stream. This example would show \*\*BigBuckBunny.mp4\*\* from the start, for 60 seconds, then cut to a commercial for the duration of the \*\*advertisement-1.mp4\*\* file. After the commercial, it would resume and play for 2 more minutes, play a 30-second commercial from \*\*advertisement-2.mp4\*\* and then plays the rest of the \*\*BigBuckBunny.mp4\*\* file. If the playlist set to repeat, this will loop.

```

<video src="mp4:BigBuckBunny.m4v" start="0" length="60"/>
<video src="mp4:advertisement-1.mp4 start="0" length="-1"/>
<video src="mp4:BigBuckBunny.m4v" start="60" length="120"/>
<video src="mp4:advertisement-2.mp4 start="0" length="30"/>
<video src="mp4:BigBuckBunny.m4v" start="180" length="-1"/>
```

When a particular playlist has ended, and there are no others currently scheduled, it will default to the last playlist, even if that playlist's **repeat** is set to **false**.

Here's an example for our weekly service replays, and live sunday events:

```

<smil>
 <head>
 </head>
 <body>

  <stream name="playlist-high"></stream>
  <stream name="playlist-low"></stream>

  <playlist name="mon-l" playOnStream="playlist-low" repeat="false" scheduled="2011-01-17 07:45:00">
   <video src="mp4:traditions-l.mp4" start="0" length="-1"/>
  </playlist>

  <playlist name="mon-h" playOnStream="playlist-high" repeat="false" scheduled="2011-01-17 07:45:00">
   <video src="mp4:traditions-h.mp4" start="0" length="-1"/>
  </playlist>

  <playlist name="mon-loop-h" playOnStream="playlist-high" repeat="true" scheduled="2011-01-17 09:30:00">
   <video src="mp4:1-16-Loop-H.mp4" start="0" length="-1"/>
  </playlist>

  <playlist name="mon-loop-l" playOnStream="playlist-low" repeat="true" scheduled="2011-01-17 09:30:00">
   <video src="mp4:1-16-Loop-L.mp4" start="0" length="-1"/>
  </playlist>

  <playlist name="tue-l" playOnStream="playlist-low" repeat="false" scheduled="2011-01-18 12:45:00">
   <video src="mp4:praise-l.mp4" start="0" length="-1"/>
  </playlist>

  <playlist name="tue-h" playOnStream="playlist-high" repeat="false" scheduled="2011-01-18 12:45:00">
   <video src="mp4:praise-h.mp4" start="0" length="-1"/>
  </playlist>

  <playlist name="tue-loop-h" playOnStream="playlist-high" repeat="true" scheduled="2011-01-18 14:30:00">
   <video src="mp4:1-16-Loop-H.mp4" start="0" length="-1"/>
  </playlist>

  <playlist name="tue-loop-l" playOnStream="playlist-low" repeat="true" scheduled="2011-01-18 14:30:00">
   <video src="mp4:1-16-Loop-L.mp4" start="0" length="-1"/>
  </playlist>

  <playlist name="wed-l" playOnStream="playlist-low" repeat="false" scheduled="2011-01-19 21:45:00">
   <video src="mp4:praise-l.mp4" start="0" length="-1"/>
  </playlist>

  <playlist name="wed-h" playOnStream="playlist-high" repeat="false" scheduled="2011-01-19 21:45:00">
   <video src="mp4:praise-h.mp4" start="0" length="-1"/>
  </playlist>

  <playlist name="wed-loop-h" playOnStream="playlist-high" repeat="true" scheduled="2011-01-19 23:30:00">
   <video src="mp4:1-16-Loop-H.mp4" start="0" length="-1"/>
  </playlist>

  <playlist name="wed-loop-l" playOnStream="playlist-low" repeat="true" scheduled="2011-01-19 23:30:00">
   <video src="mp4:1-16-Loop-L.mp4" start="0" length="-1"/>
  </playlist>

  <playlist name="thu-l" playOnStream="playlist-low" repeat="false" scheduled="2011-01-20 03:15:00">
   <video src="mp4:traditions-l.mp4" start="0" length="-1"/>
  </playlist>

  <playlist name="thu-h" playOnStream="playlist-high" repeat="false" scheduled="2011-01-20 03:15:00">
   <video src="mp4:traditions-h.mp4" start="0" length="-1"/>
  </playlist>

  <playlist name="thu-loop-h" playOnStream="playlist-high" repeat="true" scheduled="2011-01-20 05:00:00">
   <video src="mp4:1-16-Loop-H.mp4" start="0" length="-1"/>
  </playlist>

  <playlist name="thu-loop-l" playOnStream="playlist-low" repeat="true" scheduled="2011-01-20 05:00:00">
   <video src="mp4:1-16-Loop-L.mp4" start="0" length="-1"/>
  </playlist>

  <playlist name="fri-l" playOnStream="playlist-low" repeat="false" scheduled="2011-01-21 07:45:00">
   <video src="mp4:traditions-l.mp4" start="0" length="-1"/>
  </playlist>

  <playlist name="fri-h" playOnStream="playlist-high" repeat="false" scheduled="2011-01-21 07:45:00">
   <video src="mp4:traditions-h.mp4" start="0" length="-1"/>
  </playlist>

  <playlist name="fri-loop-h" playOnStream="playlist-high" repeat="true" scheduled="2011-01-21 09:30:00">
   <video src="mp4:1-16-Loop-H.mp4" start="0" length="-1"/>
  </playlist>

  <playlist name="fri-loop-l" playOnStream="playlist-low" repeat="true" scheduled="2011-01-21 09:30:00">
   <video src="mp4:1-16-Loop-L.mp4" start="0" length="-1"/>
  </playlist>

  <playlist name="sat-l" playOnStream="playlist-low" repeat="false" scheduled="2011-01-22 02:45:00">
   <video src="mp4:praise-l.mp4" start="0" length="-1"/>
  </playlist>

  <playlist name="sat-h" playOnStream="playlist-high" repeat="false" scheduled="2011-01-22 02:45:00">
   <video src="mp4:praise-h.mp4" start="0" length="-1"/>
  </playlist>

  <playlist name="sat-loop-h" playOnStream="playlist-high" repeat="true" scheduled="2011-01-22 04:30:00">
   <video src="mp4:1-16-Loop-H.mp4" start="0" length="-1"/>
  </playlist>

  <playlist name="sat-loop-l" playOnStream="playlist-low" repeat="true" scheduled="2011-01-22 04:30:00">
   <video src="mp4:1-16-Loop-L.mp4" start="0" length="-1"/>
  </playlist>

  <playlist name="sun-am-high" playOnStream="playlist-high" repeat="false" scheduled="2011-01-23 11:30:00">
   <video src="mobile-2" start="-2" length="6300"/>
  </playlist>

  <playlist name="sun-am-low" playOnStream="playlist-low" repeat="false" scheduled="2011-01-23 11:30:00">
   <video src="mobile-1" start="-2" length="6300"/>
  </playlist>

  <playlist name="sun-am-loop-h" playOnStream="playlist-high" repeat="true" scheduled="2011-01-23 13:15:00">
   <video src="mp4:1-16-Loop-H.mp4" start="0" length="-1"/>
  </playlist>

  <playlist name="sun-am-loop-l" playOnStream="playlist-low" repeat="true" scheduled="2011-01-23 13:15:00">
   <video src="mp4:1-16-Loop-L.mp4" start="0" length="-1"/>
  </playlist>

  <playlist name="sun-pm-high" playOnStream="playlist-high" repeat="false" scheduled="2011-01-23 17:45:00">
   <video src="mobile-2" start="-2" length="6300"/>
  </playlist>

  <playlist name="sun-pm-low" playOnStream="playlist-low" repeat="false" scheduled="2011-01-23 17:45:00">
   <video src="mobile-1" start="-2" length="6300"/>
  </playlist>

  <playlist name="sun-pm-loop-h" playOnStream="playlist-high" repeat="true" scheduled="2011-01-23 19:30:00">
   <video src="mp4:1-16-Loop-H.mp4" start="0" length="-1"/>
  </playlist>

  <playlist name="sun-pm-loop-l" playOnStream="playlist-low" repeat="true" scheduled="2011-01-23 19:30:00">
   <video src="mp4:1-16-Loop-L.mp4" start="0" length="-1"/>
  </playlist>

  <playlist name="default-high" playOnStream="playlist-high" repeat="true" scheduled="2011-01-01 00:00:01">
   <video src="mp4:1-16-Loop-H.mp4" start="0" length="-1"/>
  </playlist>

  <playlist name="default-low" playOnStream="playlist-low" repeat="true" scheduled="2011-01-01 00:00:01">
   <video src="mp4:1-16-Loop-L.mp4" start="0" length="-1"/>
  </playlist>

 </body>
</smil>
```

Video files can either be uploaded, or recorded on the server using a live-record application type.

Once your playlist is built, you'll need to restart the Wowza service for it to read the new playlist in and schedule it internally.

Update(July 18, 2001) : I've added a post about my Excel [playlist generator](http://nerdian.ca/wowza-stream-class-playlist-generator/ "Wowza Stream Class Playlist Generator").
