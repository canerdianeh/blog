---
layout: post
title: 'Stupid CSS Tricks: Wowza Load Graphs'
date: 2012-01-09 03:48:58.000000000 -06:00
type: post
parent_id: '0'
published: true
password: ''
status: publish
categories:
- Web 2.0
- Wowza
tags:
- CSS
meta:
  _edit_last: '2'
  _syntaxhighlighter_encoded: '1'
  dsq_thread_id: '532092293'
  _wp_old_slug: stupid-css-tricks-wowza-load-graphs
author:
  login: ianbeyer
  email: ian.beyer@gmail.com
  display_name: Ian Beyer
  first_name: Ian
  last_name: Beyer
permalink: "/2012/01/09/css-wowza-load-graphs/"
image: "/assets/images/2012/01/BigRack.png"
---

I've been experimenting with ways to generate load graphs for Wowza. The best way for doing bar graphs on a webpage is to go all crazy with CSS. It's really well suited to doing this. Here's a PHP script that will query a Wowza origin server for its repeaters, and then polls the repeaters for their load stats. This also provides buttons for launching/terminating repeaters, and visually representing them as a rack full of servers:

[![]({{site.baseurl}}/assets/2012/01/loadrack21.png "loadrack2")](http://blog.ianbeyer.com/files/2012/01/loadrack21.png)

You can get really crazy with this. For example, here's a farm of 14 servers:![]({{site.baseurl}}/assets/2012/01/BigRack.png "BigRack")

How do I do this?

The basic structure of my virtual rack is not unlike that of a real rack: The Rack Unit. In this case, it's a DIV 60 pixels high and 700 pixels wide. It then contains a rack space which is 600 pixels wide, leaving me some room on the end to put something if I want to. The rack space div then uses the server image as a background. Inside that I have the display, power button, Wowza button (all three of these are simple absolute position DIV elements - the Wowza button is simply an empty DIV with rounded corners set to make it an actual circle, and then a TITLE attribute containing the build info of that particular server), and graph, which is the larger container div (with opacity set to be slightly transparent) that then has the smaller graph div, with the width set to the calculated load percentage.

Now, the code. Note that this requires the [AWS SDK for PHP](http://aws.amazon.com/sdkforphp/) to be installed on your box (and apparently a prerequisite for that is a bowl of alphabet soup) Bear in mind that querying each server is going to take 2-3 seconds, so this doesn't scale well (the 14-server graph made use of a variant of this script that gets edge data via SQL, making it much faster). I'd love to know if it's possible to fork each of those getLoad() processes off so they can run in parallel.

syntax is:

```

loadrack.php?origin=1.2.3.4
```

loadrack.php:

```

```php
PHP
error\\_reporting(0);
require 'includes/aws-init.php';
include 'includes/capacity\\_vars.php';
require\\_once 'includes/functions.php';
header("Content-type: text/html; charset=utf-8");
$bwin = array();
$bwout = array();
$conn = array();
$cap = array();
$iid = array();
$ver = array();
if (isset($\\_GET['origin'])) { $origin\\_ip = $\\_GET['origin'];} else { die('No Origin Server Specified'); }
// Gather Data
$ip = getRepeaters($origin\\_ip);
$origin\\_ver = getVersion($origin\\_ip);
foreach ($ip as $repeater) {
list($in, $out, $count) = getLoad($repeater);
$bwin[$repeater] = $in;
$bwout[$repeater] = $out;
$conn[$repeater] = $count;
$ver[$repeater]= getVersion($repeater);
$size = "m1.small"; // can also query DB or AWS for this.
$sz[$repeater] = $size;
$iid[$repeater] = (string)$sizerow['IID'];
$cap[$repeater] = $mbps[$size];
}
} //End Repeater Foreach
// Display Summary
$total\\_cap = array\\_sum($cap);
$total\\_load = array\\_sum($bwout) / $total\\_cap \\* 100; // convert to percentage
$load\\_string = sprintf("%.2f",$total\\_load);
$bwout\\_string = sprintf("%.3f",array\\_sum($bwout));
$total['repeaters'] = sizeof($ip);
$total['conns'] = array\\_sum($conn);
$load\\_round = round($total\\_load);
switch ($total\\_load) {
case ($total\\_load 99): $color = "#000000"; break;
case ($total\\_load >= 85): $color = "#FF0000"; break;
case ($total\\_load >= 75): $color = "#FFFF00"; break;
default: $color = "#00FF00";
}
$label = 'Origin | ['. $origin\\_ip . "](http://'.$origin\_ip.':1935/loadbalancer?serverInfoXML)";
?>
=$total['conns'];? Connections (=$total['repeaters'];? Edges)
=$bwout\\_string;? Mbps (=$load\\_string;? %)
=$label;?
php
// Iterate through IP address array and display individual servers
foreach ($ip as $repeater) {
$server\\_load = $bwout[$repeater] / $cap[$addr] \\* 100; // convert to percentage
$load\\_string = sprintf("%.2f",$server\\_load);
$bwout\\_string = sprintf("%.3f",$bwout[$repeater]);
$load\\_round = round($server\\_load);
switch ($server\\_load) {
case ($server\\_load 99): $color = "#000000"; $heavy = true; break;
case ($server\\_load >= 85): $color = "#FF0000"; $heavy = true; break;
case ($server\\_load >= 75): $color = "#FFFF00"; break;
default: $color = "#00FF00";
}
$label = 'Edge | ['. $repeater . "](http://'.$repeater.':8086/serverinfo.xml)";
$lcd = $conn[$repeater]." Connections
$bwout\\_string Mbps ($load\\_string%)";
?>
=$lcd;?
=$label;?
php
if ($repeater != $origin\\_ip) {
echo '
"
style="position: absolute;
left: 23px;
top: 24px;
width: 20px;
height: 20px;
border-radius: 10px;
border: none;
">
php
} // Repeater Loop
echo "

```

```

aws-init.php:

```

```

php
<?php
require_once '/usr/share/php/AWSSDKforPHP/sdk.class.php';

define('AWS_KEY', $_SESSION['AWS_KEY']);
define('AWS_SECRET_KEY', $_SESSION['AWS_SECRET_KEY']);

        $startup_region = $_SESSION['DEFAULT_REGION'];
        
$ec2 = new AmazonEC2();

?>
```

```

functions.php:

```

```

php
function getRepeaters($origin_ip) {
		
	$addr = array();
	$lb = "http://$origin_ip:1935/loadbalancer?serverInfoXML";
	$xml = simplexml_load_file($lb);

	if ($xml === FALSE) {
		return("");
	}

	$server = $xml->LoadBalancerServer;

	// Get IP addresses of active repeaters and put them in an array.
	foreach ($server as $rep) {
		$ip = (string)$rep->redirect;
		if ($rep->status == "RUNNING" or $rep->status =="PAUSED") { 
			$addr[]=$ip;
		} // End Running If
	} // end Server foreach
	return($addr);
} // End Function

function getLoad($repeater) {

        $repurl = "http://$repeater:1935/connectioncounts.xml";
        $repxml = simplexml_load_file($repurl);
        $bwin = (string)$repxml->MessagesInBytesRate / 131072; // Convert Bps to Mbps
        $bwout = (string)$repxml->MessagesOutBytesRate / 131072; // Convert Bps to Mbps
        $conns = (string)$repxml->ConnectionsCurrent+0;

	$data = array ($bwin, $bwout, $conns);

	return($data);

} // End Function

function getVersion($server) {
        $repurl = "http://$server:1935/";
        $repxml = simplexml_load_file($repurl);
	$ver = (string)$repxml->body;

	return($ver);

} // End GetVersion Function
?>
```

```

capacity\_vars.php:

```

```

php
<?PHP 
$mbps['m1.small']=150; 
$mbps['m1.large']=250; 
$mbps['m1.xlarge']=350; 
?>
```

```
