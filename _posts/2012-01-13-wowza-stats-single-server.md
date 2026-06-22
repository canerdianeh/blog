---
layout: post
title: Wowza Stats - Single Server
date: 2012-01-13 19:24:53.000000000 -06:00
type: post
parent_id: '0'
published: true
password: ''
status: publish
categories: []
tags: []
meta:
  _edit_last: '2'
  _syntaxhighlighter_encoded: '1'
  dsq_thread_id: '537838247'
author:
  login: ianbeyer
  email: ian.beyer@gmail.com
  display_name: Ian Beyer
  first_name: Ian
  last_name: Beyer
permalink: "/2012/01/13/wowza-stats-single-server/"
---

Here's the code for gathering Wowza Stats from a single server. This assumes that you've enabled the stats on Wowza (serverinfo, connectioncounts in VHost.xml HTTPProviders), with authentication turned off). You'll also get better detailed stats if you use [Andrew Kennedy's CasterStats module](http://www.shamrock.org.uk/WowzaModules/CasterStats/ "Andrew Kennedy CasterStats") for the serverinfo.

```

```

xml
com.wowza.wms.plugin.test.HTTPServerInfo
serverinfo\*
none

com.wowza.wms.http.HTTPConnectionInfo
connectioninfo\*
none

com.wowza.wms.http.HTTPConnectionCountsXML
connectioncounts\*
none

```

```

PHP code:

```

```

php
PHP
error\_reporting(0);
header("Content-type: text/html; charset=utf-8");
$detailed = false;
$graph\_load = false;
$simple\_load = false;
$simple\_count = false;
$stream\_count = false;
$geo\_count = false;
$count = false;
$load = false;
$form = true;
if (isset($\_GET['server'])) { $repeater = $\_GET['server']; $form = false;}
if (isset($\_GET['mode'])) {
switch ($\_GET['mode']) {
case "detailed": $detailed = true; $count=true; break;
case "graph\_load" : $graph\_load = true; $load = true; break;
case "simple\_load" : $simple\_load = true; $load = true; break;
case "simple\_count" : $simple\_count = true; $load = true; break;
case "geo\_count" : $geo\_count = true; $count = true; break;
case "stream\_count" : $stream\_count = true; $count = true; break;
}
$form = false;
} else { $form = true; }
if (isset($\_GET['port'])) { $adminport = $\_GET['port'];} else { $adminport='8086'; }
if ($form) {
?

Single-Server Metrics

### Single-Server Stats Gathering

Server Address:

Admin Port

Data to display:   
Detailed Count  
Load Graph  
Load in Mbps  
Simple Count  
Geographical Count  
Stream Count

php
} else {
// Iterate through IP address array
// initialize counters
$agent['iPhone']=0;
$agent['iPad']=0;
$agent['iPod']=0;
$agent['stagefright']=0;
$agent['Roku']=0;
$agent['Flash']=0;
$proto['RTMP']=0;
$proto['RTSP']=0;
$proto['HLS']=0;
$proto['2']=0;
$proto['3']=0;
$proto['4']=0;
$server\_bwin = 0;
$server\_bwout = 0;
$server\_conns = 0;
if ($graph\_load) { echo "<H3Server Load"; }
$filter = array(
"Name" => 'ip-address',
"Value" => $repeater
);
$opts = array (
"Filter" => $filter
);
if($load) { // compute load per server
$repeaterurl = "http://$repeater:$adminport/connectioncounts";
$repeaterxml = simplexml\_load\_file($repeaterurl);
foreach ($repeaterxml->VHost as $vhost) {
foreach ($vhost->Application as $app) { // parse bandwidth usage by app in case we want it.
$appname = (string)$app->Name;
if ($app->Status == "Loaded") {
$inbytes = (string)$app->MessagesInBytesRate;
$outbytes = (string)$app->MessagesOutBytesRate;
$bwin[$appname] = $inbytes / 131072; // Convert Bps to Mbps
$bwout[$appname] = $outbytes / 131027; // Convert Bps to Mbps
}
} // End App Loop
} // End VHost Loop
$server\_bwin = (string)$repeaterxml->MessagesInBytesRate / 131072; // Convert Bps to Mbps
$server\_bwout = (string)$repeaterxml->MessagesOutBytesRate / 131072; // Convert Bps to Mbps
$server\_conns = $repeaterxml->ConnectionsCurrent;
if ($graph\_load) {
$server\_load = $server\_bwout / 1024 \* 100; // convert to percentage
$load\_string = sprintf("%.2f",$server\_load);
$bwout\_string = sprintf("%.3f",$server\_bwout);
$load\_round = round($server\_load);
switch ($server\_load) {
case ($server\_load > 99): $color = "black"; $heavy = true; break;
case ($server\_load >= 85): $color = "red"; $heavy = true; break;
case ($server\_load >= 75): $color = "yellow"; break;
default: $color = "green";
}
$info = '['.$repeater.'](http://'.$repeater.':$adminport/serverinfo.xml): **'. $load\_string ."%** with ". $server\_conns . " connections (". $bwout\_string ." Mbps out)";
print "

" . $info . "

";
?>php
} // End Load Graph
} // End Bandwidth Loop
if($count) {
$repeaterurl = "http://$repeater:$adminport/serverinfo";
$repeaterxml = simplexml\_load\_file($repeaterurl);
foreach ($repeaterxml-VHost as $vhost) {
foreach ($vhost->Application as $app) {
foreach ($app->ApplicationInstance as $instance) {
foreach ($instance->Client as $client) {
// Skip repeaters and encoders - FMS is already filtered out by the HTTPProvider
$skip = false; // Init variable
if (preg\_match('(Repeater)',$client->Referrer)) { $skip = true; }
if (preg\_match('(Kulabyte)',$client->Referrer)) { $skip = true; }
if (!$skip) {
$protocol = (string)$client->Protocol;
$proto[$protocol]++;
$streamnames = (string)$client->StreamNames;
$streamarray=explode("/",$streamnames);
$str\_array\_len=sizeof($streamarray);
$str\_end\_index = $str\_array\_len -1;
$strname = $streamarray[$str\_end\_index];
if ($streamarray[0] == "amazons3") {
$vod[$strname]++;
} else {
$live[$strname]++;
}
$client\_list[] = (string)$client->IpAddress;
if ($detailed) {
if ($client->UserAgent) // HTML clients will have a useragent defined
{
echo $client->IpAddress.": ".$client->UserAgent ."  
\n";
if (preg\_match('(Roku)',$client->UserAgent)) { $agent['Roku']++; }
if (preg\_match('(iPhone)',$client->UserAgent)) { $agent['iPhone']++; }
if (preg\_match('(iPad)',$client->UserAgent)) { $agent['iPad']++; }
if (preg\_match('(iPod)',$client->UserAgent)) { $agent['iPod']++; }
if (preg\_match('(stagefright)',$client->UserAgent)) { $agent['Android']++; }
}
if ($client->FlashVersion) // Flash clients will have a different string.
{
echo $client->IpAddress.": Flash version " . $client->FlashVersion ."  
\n";
$agent['Flash']++;
}
} //Client Details
} // Detailed Loop
} //Client Loop
} //Instance Loop
} // App Loop
} //VHost Loop
} // Count Loop
if ($geo\_count) {
print "

### Client Connections

\n";
echo "Last Refresh: ";
echo $date = date("Y-m-d H:i:s");
echo "\n";
foreach($client\_list as $client\_ip) {
$geo\_record = geoip\_record\_by\_name($client\_ip);
$cn = $geo\_record['country\_name'];
$cc = strtolower($geo\_record['country\_code']);
if ($cc == "us") {
$sn = $geo\_record['region'];
$state\_total[$sn]++;
}
$country\_name[$cc]=$cn;
$country\_total[$cc]++;
} //End Client iteration
arsort($country\_total);
print '

'."\n";
print '

#### Countries

'."\n";
foreach (array\_keys($country\_total) as $ccode) {
print '![](images/flags/'.$ccode.'.png) ';
print "$country\_name[$ccode] : ".$country\_total[$ccode]."  
\n";
} // End Country iteration
print '

';
arsort($state\_total);
print '

'."\n";
print '

#### States

'."\n";
foreach (array\_keys($state\_total) as $state) {
print "$state : ".$state\_total[$state]."  
\n";
} // End State iteration
print '

';
} // End Geo Loop
if ($detailed) {
$agent['iOS'] = $agent['iPhone'] + $agent ['iPad'] + $agent['iPod'];
echo "  
\n";
echo "Total HLS Clients: ". $proto['HLS']."  
\n";
echo "Total Roku clients: ". $agent['Roku']."  
\n";
echo "Total iOS clients: ". $agent['iOS'] ." (".$agent['iPhone']." iPhone,". $agent['iPad']." iPad,". $agent['iPod']." iPod)  
\n";
echo "Total RTMP clients: ". $proto['RTMP']." (". $agent['Flash'] ." Flash)  
\n";
} // Detailed Loop
if ($simple\_load) { printf("%.3f", $server\_bwout); }
if ($simple\_count) { print $server\_conns; }
if ($stream\_count) {
print "

### Stream Connections

\n";
arsort($live);
arsort($vod);
print "

#### Live

\n";
foreach (array\_keys($live) as $lstr) { print strtoupper($lstr)." : ".$live[$lstr]."  
\n"; }
print "

#### On-Demand

\n";
foreach (array\_keys($vod) as $vstr) { print strtoupper($vstr)." : ".$vod[$vstr]."  
\n"; }
print "

";
}
}
?>

```

```
