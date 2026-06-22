---
layout: page
title: Wowza stats collector with RRD (perl)
date: 2009-11-18 15:50:45.000000000 -06:00
type: page
parent_id: '948'
published: true
password: ''
status: publish
categories: []
tags: []
meta:
  dsq_thread_id: '218351026'
  _edit_last: '1'
  _wp_page_template: default
  s2mail: 'yes'
  _googl_shortlink: http://goo.gl/qVgZ3
  _syntaxhighlighter_encoded: '1'
author:
  login: ianbeyer
  email: ian.beyer@gmail.com
  display_name: Ian Beyer
  first_name: Ian
  last_name: Beyer
permalink: "/code/backend/wowza-metrics-perl/"
---

This perl script connects to a Wowza origin server and the connectioncounts.xml HTTPProvider function and extracts current connection counts at an interval specified on the command line (defaults every 10 seconds). Commandline options to write to an RRD file and silent operation. RRD file used in this example is [described over here](http://blog.ianbeyer.com/code/stream-counter-rrd-structure "RRD File Structure"). This can be graphed with [these commands](http://blog.ianbeyer.com/code/rrd-graphing "RRD Graphing Commands").

```

perl
#!/usr/bin/perl
use strict;
# use module
use XML::Simple;
use Data::Dumper;
use LWP::UserAgent;
use Getopt::Std;
use RRDs;
my $interval=0;
my $rrd\\_file="/var/rrd/streams-2011.rrd";
our($opt\\_r,$opt\\_q,$opt\\_i,$opt\\_s);
getopts('rqi:s:');
# Command-line options:
#
# -i  Specifies polling interval
# -q Silent operation (for running in a cron job)
# -r Outputs to RRD
# -s  Specifies server to poll
# Set default interval
if (!$opt\\_i) { $interval = 10; } else { $interval = $opt\\_i; }
!$opt\\_s && die('Please specify a server to query');
while (1) {
my $ua = new LWP::UserAgent;
$ua->timeout(10);
# Set up connection
my $wowza\\_url = "http://$opt\\_s:1935/connectioncounts.xml";
my $wowza\\_request = new HTTP::Request GET => $wowza\\_url;
my $wowza\\_result = $ua->request($wowza\\_request);
# create object
my $hlssum = 0;
my $rtspsum = 0;
my $flashsum = 0;
my $iphonesum = 0;
my @streamcount = 0;
my %namecount = 0;
if($wowza\\_result->is\\_success) {
my $wowza\\_xml = new XML::Simple;
my $wowza\\_data = $wowza\\_xml->XMLin($wowza\\_result->content);
my $loopindex = 0;
#Loop through all Streams
for my $stream (@{$wowza\\_data->{VHost}->{Application}->{ApplicationInstance}->{Stream}})
{
$loopindex++;
$flashsum += $stream->{SessionsFlash};
$hlssum += $stream->{SessionsCupertino};
$rtspsum += $stream->{SessionsRTSP};
$streamcount[$loopindex] = $stream->{SessionsFlash} + $stream->{SessionsCupertino} + $stream->{SessionsRTSP};
$namecount{$stream->{Name}} = $streamcount[$loopindex];
}
} else {
!$opt\\_q && print " [ERR] ";
}
# You'll need to alter the %namecount hashes here to accomodate for your own stream names.
$opt\\_r && RRDs::update("/var/rrd/streams-2011.rrd","N:$namecount{'mobile-1'}:$namecount{'mobile-2'}:$hlssum:$rtspsum:$flashsum:$namecount{'ipad.smil'}:$namecount{'mobile.smil'}");
if (!$opt\\_q) { $opt\\_r && print "[RRD] "; }
!$opt\\_q && print "[ F: $flashsum: H $hlssum : R $rtspsum ]";
!$opt\\_q && print "[ Low: $namecount{'mobile-1'} High: $namecount{'mobile-2'} ]";
!$opt\\_q && print "[ iOS: $namecount{'ipad.smil'} Roku: $namecount{'mobile.smil'} ]";
!$opt\\_q && print "[ StreamClass | High: $namecount{'playlist-high'} Low: $namecount{'playlist-low'} ]n";
sleep($interval);
}
```
