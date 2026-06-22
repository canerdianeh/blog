---
layout: post
title: Browser-aware player code, revisited again
date: 2012-10-29 17:46:52.000000000 -05:00
type: post
parent_id: '0'
published: true
password: ''
status: publish
categories:
- Code
- streaming
- Wowza
tags: []
meta:
  _edit_last: '2'
  _syntaxhighlighter_encoded: '1'
  dsq_thread_id: '906284334'
author:
  login: ianbeyer
  email: ian.beyer@gmail.com
  display_name: Ian Beyer
  first_name: Ian
  last_name: Beyer
permalink: "/2012/10/29/browser-aware-player-code-revisited-again/"
---

It's the code snippet that just won't go away. I've updated the code for some additional functionality. This version takes server, port, and stream parameters via the URL, parses them in javascript, and then queries a streamcheck HTTPProvider on the server to see if a stream by that name is currently published. If it is, it will load the player, otherwise load a message, and check periodically to see if the stream is published, and load the player if the state changes to true, and unload it if it changes to false, returning to the message. The player is designed to scale to fit whatever window it's in, so make an IFRAME of whatever size you want the player, and you're off and running

```html

```

![]({{site.baseurl}}/assets/2012/10/Screen-Shot-2012-10-29-at-6.38.37-PM-300x172.png "Screen Shot 2012-10-29 at 6.38.37 PM")
Without further ado, here's the code:

```javascript
The video stream is currently offline. Playback will resume as soon as a stream is available.

// Browser-aware video player for JW Player and Wowza
plwd=self.innerWidth;
plht=self.innerHeight;
// var debugwindow=document.getElementById("debug")
// debugwindow.innerHTML='<P>Dimensions: '+plwd+'x'+plht+'</P>';
var streamer=getUrlVars()["streamer"];
var app=getUrlVars()["app"];
var port=getUrlVars()["port"];
var stream=getUrlVars()["stream"];
var server=streamer+':'+port+'/'+app;
var agent=navigator.userAgent.toLowerCase();
var is\\_iphone = (agent.indexOf('iphone')!=-1);
var is\\_ipad = (agent.indexOf('ipad')!=-1);
var is\\_ipod = (agent.indexOf('ipod')!=-1);
var is\\_playstation = (agent.indexOf('playstation')!=-1);
var is\\_safari = (agent.indexOf('safari')!=-1);
var is\\_blackberry = (agent.indexOf('blackberry')!=-1);
var is\\_android = (agent.indexOf('android')!=-1);
var streamstatus = false;
var prevstatus = false;
var curstatus = false;
streamcheck();
setInterval(function(){streamcheck()},10000);
function streamcheck() {
$.ajax({
type: "GET",
url: "http://"+streamer+":8086/streamcheck?stream="+stream,
dataType: "json",
success: function(result){
curstatus = Boolean(result);
//if (result === "true") { curstatus = true;}
//if (result === "false") { curstatus = false;}
if (curstatus == prevstatus) {
} else {
if (curstatus) {
if (is\\_iphone || is\\_ipad || is\\_ipod) { iOSPlayer("videoframe",plwd,plht,server,stream);}
else if (is\\_blackberry) { rtspPlayer("videoframe",plwd,plht,server,stream);}
else { flashPlayer("videoframe",plwd,plht,server,stream); }
console.log("Changed from false to true");
} else {
var vframe=document.getElementById("videoframe")
if (is\\_iphone || is\\_ipad || is\\_ipod || is\\_blackberry) {
} else {
jwplayer("videoframe").remove();
}
vframe.innerHTML = 'The video stream is currently offline. Playback will resume as soon as a stream is available.';
console.log("Changed from true to false");
}
}
prevstatus = curstatus;
}
});
}
function getUrlVars() {
var vars = {};
var parts = window.location.href.replace(/[?&]+([^=&]+)=([^&]\\*)/gi, function(m,key,value) {
vars[key] = value;
});
return vars;
}
function iOSPlayer(container,width,height,server,stream)
{
var player=document.getElementById(container)
player.innerHTML='<VIDEO controls '+
'HEIGHT="'+height+'" '+
'WIDTH="'+width+'" '+
'title="Live Stream">'+
'<SOURCE SRC="http://'+server+'/'+stream+'/playlist.m3u8"> '+
'</video>';
}
function rtspPlayer(container,width,height,server,stream)
{
var player=document.getElementById(container)
player.innerHTML='<A HREF="rtsp://'+server+'/'+stream+'">'+
'<IMG SRC="poster-play.png" '+
'ALT="Start Mobile Video" '+
'BORDER="0" '+
'HEIGHT="'+height+'" '+
'WIDTH="'+width+'">'+
'</A>';
}
function flashPlayer(container,wide,high,server,stream)
{
jwplayer(container).setup({
height: high,
width: wide,
streamer: 'rtmp://'+server,
file: stream,
autostart: true,
stretching: 'uniform'
});
}
```

The code for the streamcheck module is as follows:

```java
package net.nerdherd.wms.http;
import java.io.\\*;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import com.wowza.wms.application.IApplicationInstance;
import com.wowza.wms.http.\\*;
import com.wowza.wms.logging.\\*;
import com.wowza.wms.vhost.\\*;
public class StreamCheck extends HTTProvider2Base {
public void onHTTPRequest(IVHost vhost, IHTTPRequest req, IHTTPResponse resp) {
StringBuffer report = new StringBuffer();
StringBuffer streamlist = new StringBuffer();
if (!doHTTPAuthentication(vhost, req, resp))
return;
Map> params = req.getParameterMap();
String stream = "";
boolean status = false;
boolean listing = false;
if (req.getMethod().equalsIgnoreCase("post")) {
req.parseBodyForParams(true);
}
if (params.containsKey("stream"))
stream = params.get("stream").get(0);
try
{
if (vhost != null)
{
List appNames = vhost.getApplicationNames();
Iterator appNameIterator = appNames.iterator();
while (appNameIterator.hasNext())
{
try {
String Name = appNameIterator.next();
IApplicationInstance NowApp = vhost.getApplication(Name).getAppInstance("\\_definst\\_");
List PublishedNames = NowApp.getPublishStreamNames();
Iterator ThisPublished = PublishedNames.iterator();
if ( PublishedNames.size()>0 )
{
while ( ThisPublished.hasNext() )
{
try {
String NowPublished = ThisPublished.next();
if (NowPublished.equals(stream)){
status = true;
}
} catch (Exception e) {}
}
}
} catch (Exception e) {report.append(e.toString()); }
}
}
}
catch (Exception e)
{
WMSLoggerFactory.getLogger(HTTPServerVersion.class).error("StreamCheck: " + e.toString());
e.printStackTrace();
}
if (!listing) {
if (status){
report.append("true");
} else {
report.append("false");
}
}
try {
resp.setHeader("Content-Type", "text/plain");
resp.setHeader("Access-Control-Allow-Origin","\\*");
OutputStream out = resp.getOutputStream();
byte[] outBytes = report.toString().getBytes();
out.write(outBytes);
} catch (Exception e) {
WMSLoggerFactory.getLogger(null).error(
"MediaCasterHTTP: " + e.toString());
}
}
}
```
