---
layout: page
title: Load Balancer Server Monitor (perl/CGI)
date: 2011-09-07 19:27:27.000000000 -05:00
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
  dsq_thread_id: '407791612'
  _googl_shortlink: http://goo.gl/a8bvS
  _syntaxhighlighter_encoded: '1'
author:
  login: admin
  email: ian@nerdherd.net
  display_name: Site Administrator
  first_name: Site
  last_name: Administrator
permalink: "/code/backend/load-balancer-server-monitor/"
---

```perl
#!/usr/bin/perl
use strict;
print "Content-type: text/htmlnn";
print "nLoad Balancer Statusnnn";
print " np.normal {color: white; background-color: green;} np.warning {color: black; background-color: yellow;} np.danger {color: white; background-color: red;}np#total {font:bold;}n";
# use module
use XML::Simple;
use Data::Dumper;
use LWP::UserAgent;
use Scalar::Util 'reftype';
# Poll Origin server for list of active edge servers
my $lb\\_ua = new LWP::UserAgent;
my $lb\\_url = "http://wms.rezonline.org:1935/loadbalancer?serverInfoXML";
my $lb\\_req = new HTTP::Request GET => $lb\\_url;
my $lb\\_res = $lb\\_ua->request($lb\\_req);
my $lb\\_xml = new XML::Simple;
my $lb\\_data = $lb\\_xml->XMLin($lb\\_res->content);
my @lb\\_ip;
my %connections;
my %status;
my $total=0;
my $running=0;
my $capacity=250;
# Dump raw XML (for debugging)
# print Dumper($lb\\_data);
# check reference type:
# if HASH, only single server is running, and XML returns without an array wrapping single element
# if ARRAY, multiple servers, each one inside an array element.
my $reference = reftype $lb\\_data->{LoadBalancerServer}; # Check to see how to handle this...
if ( $reference eq 'ARRAY' )
{
for my $lb\\_server (@{$lb\\_data->{LoadBalancerServer}})
{
push @lb\\_ip, $lb\\_server->{redirect};
$connections{$lb\\_server->{redirect}} = $lb\\_server->{connectCount};
$status{$lb\\_server->{redirect}} = $lb\\_server->{status};
}
}
elsif ( $reference eq 'HASH' )
{
if ($lb\\_data->{LoadBalancerServer}->{status} eq "RUNNING")
{
push @lb\\_ip, $lb\\_data->{LoadBalancerServer}->{redirect};
$connections{$lb\\_data->{LoadBalancerServer}->{redirect}} = $lb\\_data->{LoadBalancerServer}->{connectCount};
$status{$lb\\_data->{LoadBalancerServer}->{redirect}} = $lb\\_data->{LoadBalancerServer}->{status};
}
}
else {
print "unknown reference type - abortingn";
}
my $arraysize = @lb\\_ip;
my $style;
foreach (@lb\\_ip) {
my $load = ($connections{$\\_} / $capacity)\\*100;
if ($load > 85) {
$style = "danger";
}
elsif ( $load >75) {
$style = "warning";
}
else {
$style = "normal";
}
if ($status{$\\_} eq "RUNNING") {
if ($\\_ eq "50.19.92.63") { print "*"; }
print "

Repeater $\\_ is $status{$\\_} with $connections{$\\_} connections ($load %)

n";
if ($\\_ eq "50.19.92.63") { print "*"; }
$total += $connections{$\\_};
$running ++;
}
}
my $load = ($total / ($running \\* $capacity)) \\* 100;
if ($load > 85) {
$style = "danger";
}
elsif ( $load >75) {
$style = "warning";
}
else {
$style = "normal";
}
print "

Total of $total connections on $running active servers ($load %)

n";
print "n";
```
