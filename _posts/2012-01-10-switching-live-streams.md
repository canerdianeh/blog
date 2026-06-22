---
layout: post
title: Switching Live Streams
date: 2012-01-10 04:00:21.000000000 -06:00
type: post
parent_id: '0'
published: true
password: ''
status: publish
categories:
- Web 2.0
tags:
- CSS
- javascript
meta:
  _edit_last: '2'
  _syntaxhighlighter_encoded: '1'
  dsq_thread_id: '533346318'
author:
  login: ianbeyer
  email: ian.beyer@gmail.com
  display_name: Ian Beyer
  first_name: Ian
  last_name: Beyer
permalink: "/2012/01/10/switching-live-streams/"
image: "http://blog.ianbeyer.com/files/2012/01/rackmonitorscreencap.png"
---

Continuing on the rack theme mentioned yesterday, I got to wondering about a stream monitor that could be switched to any of a number of live streams, without reloading the page. Fortunately, JW Player makes this easy. I threw together a player embedded inside some CSS and then added a button panel. Each button is a DIV with an *onclick()* action that calls *jwplayer().load()*. While it's well known that you can use this to switch files simply by passing the filename to the *file* flashvar, we need to also pass the *streamer* value. Fortunately, the *load()* method has the ability to pass on not only files as a string value, but also objects, which are nothing more than an array of flashvars (it can also take playlist items, but that's beyond the scope of this post). So, all you need to do in order to switch streams with JW Player is call the following JavaScript method:

```

jwplayer().load({file: 'streamname', streamer: 'rtmp://w.streampunk.tv/live'})
```

The result I got was this:![]({{site.baseurl}}/assets/2012/01/rackmonitorscreencap.png "Rack Monitor")Clicking on each of the buttons in the bar below the screen will switch the stream. A [live example can be found here](http://v.streampunk.tv/jw/blog.html "Stream Switch Example"). If you want to see what else the JWPlayer API can do, head on over to the [API docs](http://www.longtailvideo.com/support/jw-player/jw-player-for-flash-v5/12540/javascript-api-reference "JW Player JavaScript API Documentation"). FlowPlayer appears to have something similar in the *clip.update()* method ([flowplayer API documentation](http://flowplayer.org/documentation/api/clip.html)), but I haven't tested it.

Page code:

```

[html]

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>

	<title>JW Player Switching</title>

	<style type="text/css">
		body { background-color: #fff; padding: 0 20px; color:#000; font: 13px/18px Arial, sans-serif; }
		a { color: #360; }
		h3 { padding-top: 20px; }
		ol { margin:5px 0 15px 16px; padding:0; list-style-type:square; }
	</style>

</head>
<body>
	<!-- START OF THE PLAYER EMBEDDING TO COPY-PASTE -->
	<div class="rack" style="width: 600px;">
	<div class="rackmonitor" style="width: 600px; height: 323px; background-image: url('rackmonitor.png'); position: relative">
	&nbsp;
	<div class="screen" style="width: 455px; height: 275px; position: absolute; left: 60px; top: 28px;">
	<div id="mediaplayer">Player...</div>
	<script type="text/javascript" src="/jwplayer/jwplayer.js"></script>
	<script type="text/javascript">
		jwplayer("mediaplayer").setup({
			flashplayer: "/jwplayer/player.swf",
			height: "275",
			width: "455",
			file: "commons.stream",
			streamer: "rtmp://w.streampunk.tv/live",
			autostart: true,
			controlbar: 'none',
			mute: true
		});
	</script>
	</div>
	</div>
	</div>
	<div class="panel" 
	style="width: 600px; 
	height: 57px; 
	background-image: url('blankPanel.png'); 
	position: relative
	">	
		<div class="button1" 
		style="width: 75px; 
		height: 20px; 
		position: absolute; 
		left: 50px; 
		top: 20px; 
		border-radius: 10px; 
		background-color: #009900; 
		color: #cccccc; 
		border: 1px solid black; 
		text-align: center;" 
		onclick="jwplayer().load({file: 'playlist-high', streamer: 'rtmp://wms.rezonline.org/redirect'})
		">
		RezOnline
		</div>
		<div class="button2" 
		style="width: 75px; 
		height: 20px; 
		position: absolute; 
		left: 150px; 
		top: 20px; border-radius: 10px; 
		background-color: #009900;
		color: #cccccc; 
		border: 1px solid black;text-align: center;" 
		onclick="jwplayer().load({file: 'commons.stream', streamer: 'rtmp://w.streampunk.tv/live'})
		">
		Commons
		</div>
		<div class="button3" 
		style="width: 75px; 
		height: 20px; 
		position: absolute; 
		left: 250px; 
		top: 20px; border-radius: 10px; 
		background-color: #990000;
		color: #cccccc; 
		border: 1px solid black;text-align: center;" 
		onclick="jwplayer().load({file: 'streamclass', streamer: 'rtmp://w.streampunk.tv/live'})
		">
		StreamClass
		</div>
		<div class="button4" 
		style="width: 75px; 
		height: 20px; 
		position: absolute; 
		left: 350px; 
		top: 20px; border-radius: 10px; 
		background-color: #990000;
		color: #cccccc; 
		border: 1px solid black;text-align: center;" 
		onclick="jwplayer().load({file: 'aircam.stream', streamer: 'rtmp://w.streampunk.tv/live'})
		">
		AirCam
		</div>
	</div>
</body>
</html>
[/html]
```
