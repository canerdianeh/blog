---
layout: page
title: Edge-Origin Stats Collector (perl)
date: 2011-09-07 19:25:55.000000000 -05:00
type: page
parent_id: '948'
published: true
password: ''
status: publish
categories: []
tags: []
meta:
  _edit_last: '1'
  wp_plus_one_redirect: ''
  _wp_page_template: default
  dsq_thread_id: '411102441'
  _googl_shortlink: http://goo.gl/PNGPJ
  _syntaxhighlighter_encoded: '1'
author:
  login: admin
  email: ian@nerdherd.net
  display_name: Site Administrator
  first_name: Site
  last_name: Administrator
permalink: "/code/backend/edge-origin-stats-collector-perl/"
---

```perl
  
#!/usr/bin/perl  
use strict;

# use module  
use XML::Simple;  
use Data::Dumper;  
use LWP::UserAgent;  
use Getopt::Std;  
use RRDs;  
use Scalar::Util 'reftype';

# Parse Commandline options:  
# q: quiet  
# r: write to RRD  
# i: specify refresh interval (default 10s)

my $interval;

our($opt\_r,$opt\_q,$opt\_i);  
getopts('rqi:');

if (!$opt\_i) { $interval = 10; } else { $interval = $opt\_i; }

while (1) { #establish forever loop

# Poll Origin server for list of active edge servers

my $lb\_ua = new LWP::UserAgent;  
my $lb\_url = "http://wms.rezonline.org:1935/loadbalancer?serverInfoXML";  
my $lb\_req = new HTTP::Request GET => $lb\_url;  
my $lb\_res = $lb\_ua->request($lb\_req);  
my @lb\_ip;

if($lb\_res->is\_success) {

my $lb\_xml = new XML::Simple;  
my $lb\_data = $lb\_xml->XMLin($lb\_res->content);

# Dump raw XML (for debugging)  
# print Dumper($lb\_data);

# check reference type:  
# if HASH, only single server is running, and XML returns without an array wrapping single element  
# if ARRAY, multiple servers, each one inside an array element.

my $reference = reftype $lb\_data->{LoadBalancerServer}; # Check to see how to handle this...

if ( $reference eq 'ARRAY' )  
{  
for my $lb\_server (@{$lb\_data->{LoadBalancerServer}})  
{  
if ($lb\_server->{status} eq "RUNNING")  
{  
#print "ID: $lb\_server->{serverId} at $lb\_server->{redirect}n";  
push @lb\_ip, $lb\_server->{redirect};  
}  
}  
}

elsif ( $reference eq 'HASH' )  
{  
if ($lb\_data->{LoadBalancerServer}->{status} eq "RUNNING")  
{  
push @lb\_ip, $lb\_data->{LoadBalancerServer}->{redirect};  
}  
}

else {  
print "unknown reference type - abortingn";  
}

} # End is\_success loop

my $arraysize = @lb\_ip;

#print "Array size: $arraysize elements: n";

# Step through the returned array of edge IPs and gather stats

# Scope total variables  
my %streamTotal = 0;

foreach (@lb\_ip) {

# print "Gathering stats for edge server at $\_n";  
my $ua = new LWP::UserAgent;  
$ua->timeout(10);

my $edgeurl = "http://$\_:1935/connectioncounts.xml?flat"; # Make sure you use FLAT mode here, otherwise the XML is a pain to parse when there are multiple server applications  
my $edgereq = new HTTP::Request GET => $edgeurl;  
my $edgeres = $ua->request($edgereq);

# create object

my $cupertinosum = 0; #Apple HLS  
my $rtspsum = 0; #RTSP  
my $flashsum = 0; #RTMP  
my $sanjosesum = 0; #Flash HTTP  
my $smoothsum = 0; #Silverlight Smooth Streaming

my $streamcount = 0; #Total Streams  
my %namecount = 0; #Streams per published stream

if($edgeres->is\_success) {  
my $edgexml = new XML::Simple;  
my $edgedata = $edgexml->XMLin($edgeres->content, ForceArray => 1);

my $loopindex = 0;  
for my $stream (@{$edgedata->{Stream}})  
{  
# At some point we're going to want to filter out the publishing points and only look at the edge application  
# in which case, check for applicationName and ignore based on that

$loopindex++;  
$flashsum += $stream->{sessionsFlash};  
$rtspsum += $stream->{sessionsRTSP};  
$cupertinosum += $stream->{sessionsCupertino};  
$sanjosesum += $stream->{sessionsSanJose};  
$smoothsum += $stream->{sessionsSmooth};  
$streamcount += $stream->{sessionsTotal};  
$namecount{$stream->{streamName}} = $streamcount;

} # End of FOR loop

} else {  
print " X "; # Indicate that server poll was not successful  
} # End of if loop

my $rokusum = $namecount{'roku.smil'} + $namecount {'mobile.smil'};

#$start60 = $circbuf[-6];  
#$start90 = $circbuf[-9];  
#  
#shift (@circbuf);  
#  
#push (@circbuf,$flashsum);  
#$delta60=$flashsum-$start60;  
#$delta90=$flashsum-$start90;

!$opt\_q && print "$\_ : $streamcount ";  
!$opt\_q && print "[ F: $flashsum: H $cupertinosum : R $rtspsum ]";  
!$opt\_q && print "[ Low: $namecount{'mobile-1'} High: $namecount{'mobile-2'} ]";  
!$opt\_q && print "[ iOS: $namecount{'ipad.smil'} Roku: $namecount{'roku.smil'},$namecount{'mobile.smil'} ]n";  
#!$opt\_q && print "[ StreamClass | High: $namecount{'playlist-high'} Low: $namecount{'playlist-low'} ]n";

$streamTotal{'Cupertino'} += $cupertinosum;  
$streamTotal{'Flash'} += $flashsum;  
$streamTotal{'SanJose'} += $sanjosesum;  
$streamTotal{'Smooth'} += $smoothsum;  
$streamTotal{'RTSP'} += $rtspsum;  
$streamTotal{'Roku'} += $namecount{'roku.smil'};  
$streamTotal{'iOS'} += $namecount{'ipad.smil'};  
$streamTotal{'Total'} += $streamcount;

} # End stats gathering loop per server

!$opt\_q && print "Total: $streamTotal{'Total'} [F: $streamTotal{'Flash'} H: $streamTotal{'Cupertino'}(iOS: $streamTotal{'iOS'} Roku: $streamTotal{'Roku'}) SJ: $streamTotal{'SanJose'} SL: $streamTotal{'Smooth'}]";

$opt\_r && RRDs::update("/var/rrd/streams-2011.rrd","N:$streamTotal{'Smooth'}:$streamTotal{'SanJose'}:$streamTotal{'Cupertino'}:$streamTotal{'RTSP'}:$streamTotal{'Flash'}:$streamTotal{'iOS'}:$streamTotal{'Roku'}");  
if (!$opt\_q) { $opt\_r && print "[RRD] "; }

!$opt\_q && print "n";

sleep($interval);  
} # End of Forever Loop  
```
