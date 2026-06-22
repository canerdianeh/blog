---
layout: post
title: 'Wowza Stream Scheduler Hacks: Google Calendar'
date: 2016-10-16 13:13:57.000000000 -05:00
type: post
parent_id: '0'
published: true
password: ''
status: publish
categories:
- Code
- streaming
- Wowza
tags:
- iCal
- PHP
- Stream Scheduler
meta:
  _edit_last: '2'
  _syntaxhighlighter_encoded: '1'
  _wpas_done_all: '1'
  _thumbnail_id: '1384'
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
permalink: "/2016/10/16/wowza-stream-scheduler-hacks-google-calendar/"
image: "/assets/images/2016/10/CDsqQFlWAAA7A5z.png"
---

One of Wowza's most underutilized yet most powerful features is the stream scheduler. I've blogged about it extensively in the past, and I'll return from a long hiatus to do it again.
To recap some of the things you can do with this add-on:
- Create a virtual stream that plays a loop of server-side content
- Play a sequence of video content (think TV programming)
- A combination of both
- Play portions of a video file (in/out points)
- In combination with the LoopUntilLive module, do all that and then interrupt with a live stream
This gives you the ability to have a continuous 24/7 stream of programming including advertising. The output of this schedule is then treated by Wowza like any other stream, meaning it can be used as input to a transcoder, nDVR, or sent somewhere with Stream Targets.
The challenge we run into is that building the schedule in XML is not the most obvious thing in the world as there is not currently any integration of the module into the Wowza Streaming Engine Manager's GUI.
As the schedule is written as a SMIL file (a specific XML schema) in an application's content directory, It requires either logging in to the server and manipulating files with a text editor, or uploading into the content directory.
The other way is to build the schedule programmatically. Command-line PHP is an easy way to do this as PHP has some excellent PHP processing tools.
If you want to peek at the Java code for the scheduler module, [Wowza has it up on GitHub](https://github.com/WowzaMediaSystems/wse-plugin-streampublisher).
A quick recap of the structure of the stream scheduler's XML Schema:
- The entire file is wrapped in  tags to indicate that this is in fact a SMIL file.
- an empty  block - Wowza doesn't currently make use of anything in here, but it's a good place to put comments, and it makes for good XML.
- The meat of the file, a  block that contains all the good stuff.
- Within the body block, there are two key element types:
1. One or more  blocks that define the names of the virtual streams that are created by the schedule.
2. One or more  blocks that define the content and timing of what gets published. Each playlist tag specifies the following attributes:
- \*\*name\*\* : The name of the playlist. This is arbitrary but should be unique within the file
- \*\*playOnStream\*\*: specifies which of the streams created in the  block this playlist's content will go to
- \*\*repeat\*\*: a boolean (true/false) value that specifies if this playlist loops until something else happens. If it runs out of content, the virtual stream will stop.
- \*\*scheduled\*\*: The date and time (based on server timezone) this playlist will be published to the stream. This is in [ISO 8601 format](https://en.wikipedia.org/wiki/ISO\_8601#Dates) without the T delimiter (YYYY-MM-DD HH:MM:SS)
3. Within the  block are one or more  tags with the following attributes:
- \*\*src\*\*: The path and filename (relative to the application's content directory) of the video file to play. This should be prefixed with \*\*mp4:\*\*as you would any other video file within Wowza. You can also put in the name of a live stream published within the same application.
- \*\*start\*\*: The offset (in seconds) from the beginning of the file where playback is to begin.
- \*\*length\*\*: Play duration (in seconds) from the \*\*start\*\* point. A value of \*\*-1\*\* will play to the end of the file. A value of \*\*-2\*\* indicates that this is a live stream.
- Once the end of this item is reached, it will move to the next element in the playlist. If there is no more content it will either loop (if \*\*repeat\*\* is set to true) or stop. If there is nothing further on the schedule, the stream will unpublish and stop. If this is not a repeating playlist, It's generally a good idea to put a buffer video (a number of minutes of black video or a logo works just fine) at the end of it to fill any gaps to the next playlist.
So, the schedule is pretty straightforward, but it can get tedious to build. I previously posted about a [way to generate this with a spreadsheet in Excel](http://blog.ianbeyer.com/2011/07/18/wowza-stream-class-playlist-generator/). This is clunky, but can save a lot of typing, and is good for repeating events.
But this lacked a good visual interface. As I was working on a project for a client to translate a schedule generated from their video content management system into the Wowza Stream Scheduler's XML, it occurred to me that there was another structured schedule format that could be translated easily into XML: iCal. This calendar format is defined in [RFC 2445](https://www.ietf.org/rfc/rfc2445.txt) and is widely used by many calendaring systems.
Unfortunately, iCal is not XML to begin with (iCal/RFC2445 predates XML by a decade), which would be WAY too easy. Here is a sample of iCal data out of Google Calendar that contains two events (Google \*used\* to make their calendar shares available in XML but it seems that is no longer the case):
[code]
BEGIN:VCALENDAR
PRODID:-//Google Inc//Google Calendar 70.9054//EN
VERSION:2.0
CALSCALE:GREGORIAN
METHOD:PUBLISH
X-WR-CALNAME:Wowza Event Scheduler Calendar
X-WR-TIMEZONE:America/Chicago
X-WR-CALDESC:
BEGIN:VEVENT
DTSTART:20161017T160000Z
DTEND:20161017T170000Z
DTSTAMP:20161016T164145Z
UID:xxxxxx@google.com
CREATED:20161012T212924Z
DESCRIPTION:mp4:video1.mp4\,0\,-1
LAST-MODIFIED:20161016T164138Z
LOCATION:teststream
SEQUENCE:3
STATUS:CONFIRMED
SUMMARY:11am Broadcast
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART:20161017T170000Z
DTEND:20161017T180000Z
DTSTAMP:20161016T164145Z
UID:xxxxxx@google.com
CREATED:20161016T164116Z
DESCRIPTION:mp4:video2.mp4\,0\,1800\nmp4:video3.mp4\,0\,1800
LAST-MODIFIED:20161016T164118Z
LOCATION:teststream
SEQUENCE:1
STATUS:CONFIRMED
SUMMARY:Noon Broadcast
TRANSP:OPAQUE
END:VEVENT
END:VCALENDAR
[/code]
As you can see, this has some hints of XML: Opening and closing tags, attributes, and the like. Fortunately, Evert Pot wrote a [handy little PHP function](https://evertpot.com/248/) to make the conversion to XML.
One of the really nice things about JSON and XML in PHP is that the objects that contain them work just like any other nested arrays, and so extracting specific items is ridiculously easy. There's a lot of data within the VEVENT block that we just aren't interested in. We really only care about the start and stop times, and a few other fields like DESCRIPTION, LOCATION and SUMMARY, which we can hack to contain the names of the streams and content. In this example, I use DESCRIPTION to contain the names of the video files on each line (and additional comma-separated data regarding start and end points, and LOCATION to specify what stream it should be published on. SUMMARY can be used as the playlist name attribute There are a number of other iCal fields that can be used for this as well.
In order to use this data, we need to do the following:
- Use the start/end times to calculate a duration
- Make a list of the streams to publish to
- figure out what video to play when
- Convert datestamps to the local server time
For starters, we're going to need to set a few defaults:

```

php
ini\\_set("allow\\_url\\_fopen", 1);
error\\_reporting(0);
date\\_default\\_timezone\\_set("US/Central");
```

Using Evert's conversion function, we get the schedule into an XML object:

```

php
$calUrl = "https://calendar.google.com/calendar/ical/xxxxxxxxxxxxx8%40group.calendar.google.com/private-xxxxx/basic.ics";
// get your private calendar URL from the calendar settings.
$CalData=file\\_get\\_contents($calUrl);
$xmlString=iCalendarToXML($CalData);
$xmlObj = simplexml\\_load\\_string($xmlString);
```

The object now looks like this:
[code]
SimpleXMLElement Object
(
[PRODID] => -//Google Inc//Google Calendar 70.9054//EN
[VERSION] => 2.0
[CALSCALE] => GREGORIAN
[METHOD] => PUBLISH
[X-WR-CALNAME] => Wowza Event Scheduler Calendar
[X-WR-TIMEZONE] => America/Chicago
[X-WR-CALDESC] => SimpleXMLElement Object
(
)
[VEVENT] => Array
(
[0] => SimpleXMLElement Object
(
[DTSTART] => 20161017T160000Z
[DTEND] => 20161017T170000Z
[DTSTAMP] => 20161016T182755Z
[UID] => 72klt8s5ssrbjp9ofdk8ucovoo@google.com
[CREATED] => 20161012T212924Z
[DESCRIPTION] => mp4:video1.mp4\,0\,-1
[LAST-MODIFIED] => 20161016T164138Z
[LOCATION] => teststream
[SEQUENCE] => 3
[STATUS] => CONFIRMED
[SUMMARY] => 11am Broadcast
[TRANSP] => OPAQUE
)
[1] => SimpleXMLElement Object
(
[DTSTART] => 20161017T170000Z
[DTEND] => 20161017T180000Z
[DTSTAMP] => 20161016T182755Z
[UID] => ac3lgjmjmijj2910au0fnv5vig@google.com
[CREATED] => 20161016T164116Z
[DESCRIPTION] => mp4:video2.mp4\,0\,1800\nmp4:video3.mp4\,0\,1800
[LAST-MODIFIED] => 20161016T164118Z
[LOCATION] => teststream
[SEQUENCE] => 1
[STATUS] => CONFIRMED
[SUMMARY] => Noon Broadcast
[TRANSP] => OPAQUE
)
)
)
[/code]
So now we need to create another XML object for our schedule and give it the basic structure:

```

php
$smilXml = new SimpleXMLElement('');
$smilHead = $smilXml->addChild('head');
$smilBody = $smilXml->addChild('body');
```

Now we need to iterate once through the VEVENT objects to get stream names:

```

php
$playonstream = [];
foreach ($xmlObj->VEVENT as $event) {
$loc = $event->LOCATION;
$playOnStream["$loc"]=true;
// We don't really care about the value of this array element, as long as it exists.
// This way we only get one array element for each unique stream name
}
// Iterate through the list of streams and create them in the SMIL
foreach ($playOnStream as $key => $value) {
$smilStream = $smilBody->addChild('stream');
$smilStream->addAttribute('name',$key);
}
```

So now we have the beginnings of a schedule:

```

xml
xml version="1.0"?
```

We now need to iterate through the list again to add in the fallback items for each stream that starts when the stream starts (this is done as a separate loop to keep the output XML cleaner):

```

php
// Add in default fallback entries
foreach ($playOnStream as $key => $value) {
$defaultPl=$smilBody->addChild('playlist');
$defaultPl->addAttribute('name',"default-$key");
$defaultPl->addAttribute('playOnStream',$key);
$defaultPl->addAttribute('repeat','true');
$defaultPl->addAttribute('scheduled',"2016-01-01 00:00:01");
$contentItem = $defaultPl->addChild('video');
$contentItem->addAttribute('src','mp4:padding.mp4');
$contentItem->addAttribute('start','0');
$contentItem->addAttribute('length','-1');
}
```

Which then gives us these new items:

```

xml
[](mp4:padding.mp4)
```

And then we need to iterate again through the VEVENTS to create the actual schedule items:

```

php
foreach ($xmlObj->VEVENT as $event) {
//parse the times into Unix time stamps using the ever-useful strtotime() function;
$eventStart = strtotime($event->DTSTART);
$eventEnd = strtotime($event->DTEND);
//format them into the ISO 8601 format for use in the schedule
//Note that we're using H:i:s rather than h:i:s because 24-hour time is important here
$start = date("Y-m-d H:i:s", $eventStart);
$end = date("Y-m-d H:i:s", $eventEnd);
//extract summary for playlist name
$plName = $event->SUMMARY;
$plLoc = $event->LOCATION;
//extract description for content
$description = $event->DESCRIPTION;
$videos=preg\\_split('/\\\\n/',$description);
// add on a padding video at the end of this list
$videos[]="mp4:padding.mp4";
//create playlist
$playlist = $smilBody->addChild('playlist');
$playlist->addAttribute('name',$plName);
$playlist->addAttribute('playOnStream',$plLoc);
$playlist->addAttribute('repeat','false');
$playlist->addAttribute('scheduled',$start);
//iterate through playlist items
foreach($videos as $plItem) {
echo "$plItem\n";
$attrs=preg\\_split('/\\\\,/',$plItem);
// set defaults for stream start/duration if not specified
// assume start at beginning and play all the way through
if(!$attrs[1]) { $attrs[1] = 0; }
if(!$attrs[2]) { $attrs[2] = -1; }
$contentItem = $playlist->addChild('video');
$contentItem->addAttribute('src',$attrs[0]);
$contentItem->addAttribute('start',$attrs[1]);
$contentItem->addAttribute('length',$attrs[2]);
} // end of playlist loop
} // end of event loop
```

And, finally, we need to add a little bit of code to format the XML object for use with Wowza:

```

php
$dom = dom\\_import\\_simplexml($smilXml)->ownerDocument;
$dom->formatOutput = true;
$output=$dom->saveXML();
echo "$output\n"; // outputs to STDOUT
$dom->save('streamschedule.smil'); // save to file
```

For the purposes of this last section, I've created some additional events to add a secondary stream:
[![Schedule Overview]({{site.baseurl}}/assets/2016/10/Screenshot-2016-10-16-13.25.18-300x185.png)](http://blog.ianbeyer.com/files/2016/10/Screenshot-2016-10-16-13.25.18.png)
[![11am Broadcast Event]({{site.baseurl}}/assets/2016/10/Screenshot-2016-10-16-13.19.45-300x182.png)](http://blog.ianbeyer.com/files/2016/10/Screenshot-2016-10-16-13.19.45.png)
[![11am Alternate Broadcast Event]({{site.baseurl}}/assets/2016/10/Screenshot-2016-10-16-13.19.29-300x179.png)](http://blog.ianbeyer.com/files/2016/10/Screenshot-2016-10-16-13.19.29.png)
[![Noon Broadcast Event]({{site.baseurl}}/assets/2016/10/Screenshot-2016-10-16-13.19.55-300x183.png)](http://blog.ianbeyer.com/files/2016/10/Screenshot-2016-10-16-13.19.55.png)
[![Event Broadcast]({{site.baseurl}}/assets/2016/10/Screenshot-2016-10-16-13.20.08-300x181.png)](http://blog.ianbeyer.com/files/2016/10/Screenshot-2016-10-16-13.20.08.png)
The iCal looks like this:
[code]
BEGIN:VCALENDAR
PRODID:-//Google Inc//Google Calendar 70.9054//EN
VERSION:2.0
CALSCALE:GREGORIAN
METHOD:PUBLISH
X-WR-CALNAME:Wowza Event Scheduler Calendar
X-WR-TIMEZONE:America/Chicago
X-WR-CALDESC:
BEGIN:VEVENT
DTSTART:20161017T160000Z
DTEND:20161017T170000Z
DTSTAMP:20161016T182604Z
UID:8m4hcp98fmuosuoe48o20drl7k@google.com
CREATED:20161016T180813Z
DESCRIPTION:mp4:video5.mp4\nmp4:video6.mp4
LAST-MODIFIED:20161016T180813Z
LOCATION:altstream
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:11am alternate broadcast
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART:20161017T180000Z
DTEND:20161017T190000Z
DTSTAMP:20161016T182604Z
UID:c1ijl48srikc22vkkvrgvpb718@google.com
CREATED:20161016T180725Z
DESCRIPTION:mp4:video4.mp4
LAST-MODIFIED:20161016T180725Z
LOCATION:teststream
SEQUENCE:0
STATUS:CONFIRMED
SUMMARY:Event
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART:20161017T160000Z
DTEND:20161017T170000Z
DTSTAMP:20161016T182604Z
UID:72klt8s5ssrbjp9ofdk8ucovoo@google.com
CREATED:20161012T212924Z
DESCRIPTION:mp4:video1.mp4\,0\,-1
LAST-MODIFIED:20161016T164138Z
LOCATION:teststream
SEQUENCE:3
STATUS:CONFIRMED
SUMMARY:11am Broadcast
TRANSP:OPAQUE
END:VEVENT
BEGIN:VEVENT
DTSTART:20161017T170000Z
DTEND:20161017T180000Z
DTSTAMP:20161016T182604Z
UID:ac3lgjmjmijj2910au0fnv5vig@google.com
CREATED:20161016T164116Z
DESCRIPTION:mp4:video2.mp4\,0\,1800\nmp4:video3.mp4\,0\,1800
LAST-MODIFIED:20161016T164118Z
LOCATION:teststream
SEQUENCE:1
STATUS:CONFIRMED
SUMMARY:Noon Broadcast
TRANSP:OPAQUE
END:VEVENT
END:VCALENDAR
[/code]
And when we run the process, we get this spiffy code coming out:

```

xml
[](mp4:padding.mp4)

[](mp4:padding.mp4)

[](mp4:video5.mp4)
[](mp4:video6.mp4)
[](mp4:padding.mp4)

[](mp4:video4.mp4)
[](mp4:padding.mp4)

[](mp4:video1.mp4)
[](mp4:padding.mp4)

[](mp4:video2.mp4)
[](mp4:video3.mp4)
[](mp4:padding.mp4)
```

So there you have a relatively simple one-way hack to spit Google Calendar/iCal events out into a Wowza Schedule. You would still need to manually run this every time you wanted to update the broadcast schedule (and reload the Wowza server), and this does not send any confirmation back to your iCal that the event has been scheduled.
Stay tuned for a variation on this code that uses the Google Calendar API (a much more elegant approach)
