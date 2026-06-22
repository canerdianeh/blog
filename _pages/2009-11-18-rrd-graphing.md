---
layout: page
title: RRD Graphing Script (bash)
date: 2009-11-18 16:32:20.000000000 -06:00
type: page
parent_id: '948'
published: true
password: ''
status: publish
categories: []
tags: []
meta:
  _edit_last: '1'
  _wp_page_template: default
  dsq_thread_id: '217880128'
  s2mail: 'yes'
  _googl_shortlink: http://goo.gl/1HIe4
  _syntaxhighlighter_encoded: '1'
author:
  login: ianbeyer
  email: ian.beyer@gmail.com
  display_name: Ian Beyer
  first_name: Ian
  last_name: Beyer
permalink: "/code/backend/rrd-graphing/"
---

Live Graph ([Source RRD Database is here](http://blog.ianbeyer.com/code/stream-counter-rrd-structure "RRD File Structure")):

```

bash
#!/bin/bash
rrdtool graph
'/var/www/streams.png'
--title 'Resurrection Online (Mobile)'
--vertical-label 'Streams'
--units-exponent 0
--width '720'
--height '400'
--upper-limit '10'
--lower-limit '0'
--y-grid 1:5
--start end-2h
'DEF:Flash=/var/rrd/streams-2011.rrd:Flash:LAST'
'DEF:HLS=/var/rrd/streams-2011.rrd:HLS:LAST'
'DEF:RTSP=/var/rrd/streams-2011.rrd:RTSP:LAST'
'DEF:iPad=/var/rrd/streams-2011.rrd:iPad:LAST'
'DEF:Roku=/var/rrd/streams-2011.rrd:Roku:LAST'
'CDEF:Total=HLS,RTSP,+,Flash,+'
'VDEF:Peak=Total,MAXIMUM'
'VDEF:FlashPk=Flash,MAXIMUM'
'VDEF:HLSPk=HLS,MAXIMUM'
'VDEF:RTSPPk=RTSP,MAXIMUM'
'VDEF:iPadPk=iPad,MAXIMUM'
'VDEF:RokuPk=Roku,MAXIMUM'
'AREA:Total#FFCC99:Totalt'
'GPRINT:Total:LAST:%3.0lf Currentt'
'GPRINT:Peak:%3.0lf Peakn'
'LINE1:Flash#993333:Flasht'
'GPRINT:Flash:LAST:%3.0lf Currentt'
'GPRINT:FlashPk:%3.0lf Peakn'
'LINE1:HLS#336633:HLStt'
'GPRINT:HLS:LAST:%3.0lf Currentt'
'GPRINT:HLSPk:%3.0lf Peakn'
'LINE1:RTSP#FF6600:RTSPt'
'GPRINT:RTSP:LAST:%3.0lf Currentt'
'GPRINT:RTSPPk:%3.0lf Peakn'
'LINE1:iPad#000000:iPadt'
'GPRINT:iPad:LAST:%3.0lf Currentt'
'GPRINT:iPadPk:%3.0lf Peakn'
'LINE1:Roku#330099:Rokut'
'GPRINT:Roku:LAST:%3.0lf Currentt'
'GPRINT:RokuPk:%3.0lf Peakn'
'VRULE:Peak#CC0000'
'LINE:Peak#CC0000'
```

Archive version:

```

bash
#!/bin/bash
FILE="streams-$(date +%Y%m%d%H%M).png"
DATESTAMP="$(date +%B %d, %Y)"
TIMESTAMP="$(date +%H:%M)"
rrdtool graph
"/var/www/$FILE"
--title "Resurrection Online Mobile Attendance ($DATESTAMP)"
--vertical-label 'Streams'
--units-exponent 0
--width '720'
--height '400'
--y-grid 1:5
--start end-3h
'DEF:Flash=/var/rrd/streams-2011.rrd:Flash:LAST'
'DEF:HLS=/var/rrd/streams-2011.rrd:HLS:LAST'
'DEF:RTSP=/var/rrd/streams-2011.rrd:RTSP:LAST'
'DEF:iPad=/var/rrd/streams-2011.rrd:iPad:LAST'
'DEF:Roku=/var/rrd/streams-2011.rrd:Roku:LAST'
'CDEF:Total=HLS,RTSP,+,Flash,+'
'VDEF:Peak=Total,MAXIMUM'
'VDEF:FlashPk=Flash,MAXIMUM'
'VDEF:HLSPk=HLS,MAXIMUM'
'VDEF:RTSPPk=RTSP,MAXIMUM'
'VDEF:iPadPk=iPad,MAXIMUM'
'VDEF:RokuPk=Roku,MAXIMUM'
'AREA:Total#FFCC99:Totalt'
'GPRINT:Total:LAST:%3.0lf Currentt'
'GPRINT:Peak:%3.0lf Peakn'
'LINE1:Flash#993333:Flasht'
'GPRINT:Flash:LAST:%3.0lf Currentt'
'GPRINT:FlashPk:%3.0lf Peakn'
'LINE1:HLS#336633:HLStt'
'GPRINT:HLS:LAST:%3.0lf Currentt'
'GPRINT:HLSPk:%3.0lf Peakn'
'LINE1:RTSP#FF6600:RTSPt'
'GPRINT:RTSP:LAST:%3.0lf Currentt'
'GPRINT:RTSPPk:%3.0lf Peakn'
'LINE1:iPad#000000:iPadt'
'GPRINT:iPad:LAST:%3.0lf Currentt'
'GPRINT:iPadPk:%3.0lf Peakn'
'LINE1:Roku#330099:Rokut'
'GPRINT:Roku:LAST:%3.0lf Currentt'
'GPRINT:RokuPk:%3.0lf Peakn'
echo "[$DATESTAMP $TIMESTAMP]($FILE)  
" >> /var/www/archives.html
```
