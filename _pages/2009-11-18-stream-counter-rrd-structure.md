---
layout: page
title: Stream Counter RRD Structure
date: 2009-11-18 16:33:45.000000000 -06:00
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
  dsq_thread_id: '217880139'
  s2mail: 'yes'
  _googl_shortlink: http://goo.gl/b6Yi7
author:
  login: ianbeyer
  email: ian.beyer@gmail.com
  display_name: Ian Beyer
  first_name: Ian
  last_name: Beyer
permalink: "/code/backend/stream-counter-rrd-structure/"
---

Create RRD file ([can be graphed with this script](http://nerdian.ca/code/rrd-graphing "RRD Graphing Commands")):

```

rrdtool create filename.rrd
--step '10'
'DS:Low:GAUGE:30:U:U'
'DS:High:GAUGE:30:U:U'
'DS:HLS:GAUGE:30:U:U'
'DS:RTSP:GAUGE:30:U:U'
'DS:Flash:GAUGE:30:U:U'
'DS:iPad:GAUGE:30:U:U'
'DS:Roku:GAUGE:30:U:U'
'RRA:LAST:0.5:1:8640'
'RRA:MAX:0.5:6:10080'
'RRA:MAX:0.5:30:51840'
'RRA:MAX:0.5:360:8760'
```

Details:

- Step interval is 10 seconds
- 7 GAUGE datasets
- 4 Archive datasets:
  - Archive point is saved every 10 sec, archive kept for 1 day back.
  - Archive point is saved every 1 min, archive kept for 7 days back.
  - Archive point is saved every 5 min, archive kept for 6 months back.
  - Archive point is saved every 1 hour, archive is kept for 1 year back.
