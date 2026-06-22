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

[php]
<?PHP
error_reporting(0);
require 'includes/aws-init.php';
include 'includes/capacity_vars.php';
require_once 'includes/functions.php';
header("Content-type: text/html; charset=utf-8");

$bwin = array();
$bwout = array();
$conn = array();
$cap = array();
$iid = array();
$ver = array();

if (isset($_GET['origin'])) { $origin_ip = $_GET['origin'];} else { die('No Origin Server Specified'); }

// Gather Data
$ip = getRepeaters($origin_ip);
$origin_ver = getVersion($origin_ip);

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

$total_cap = array_sum($cap);
$total_load = array_sum($bwout) / $total_cap * 100; // convert to percentage

$load_string = sprintf("%.2f",$total_load);
$bwout_string = sprintf("%.3f",array_sum($bwout));
$total['repeaters'] = sizeof($ip);
$total['conns'] = array_sum($conn);
$load_round = round($total_load);
switch ($total_load) {
	case ($total_load > 99): $color = "#000000"; break;
	case ($total_load >= 85): $color = "#FF0000"; break;
	case ($total_load >= 75): $color = "#FFFF00"; break;
	default: $color = "#00FF00";
	}
		$label = 'Origin | <A style="color: black;" HREF="http://'.$origin_ip.':1935/loadbalancer?serverInfoXML" target="_blank">'. $origin_ip . "</A>";

	?>
		<DIV class="rackslot" 
			style="height: 60px; 
				width: 660px; 
				position: relative; 
				border: none; 
				background: none;
				">
		<DIV class="server" 
			style="height: 60px; 
				float: left; 
				width: 600px; 
				position: relative; 
				background-image: url('images/rackserver2.jpg');
				">
			<DIV class="loadbar" 
				style="height: 10px; 
				border-radius: 3px; 
				opacity: 0.6; 
				position: absolute; 
				left: 46px; 
				top: 42px; 
				width: 500px; 
				background: none repeat scroll 0% 0% #ffffff; 
				border: 1px solid;
			">
				<DIV class="load" 
					style="height: 100%; 
					border-radius: 2px; 
					position: absolute; 
					left: 0px; 
					top: 0px; 
					background: <?=$color?>; 
					color: black; 
					width: <?=$load_round;?>%;
				"></div>
			</div>
			<DIV class="display" 
				style="height: 22px; 
					position: absolute; 
					left: 44px; 
					top: 12px; 
					width: 145px; 
					background-color: #2222FF; 
					color: #CCCCFF; 
					font-size: 8px; 
					border: 1px solid black; 
					border-radius: 3px; 
					margin: 2px;
					font-family: sans-serif; 
					padding: 1px;
			">
				<?=$total['conns'];?> Connections (<?=$total['repeaters'];?> Edges)<BR>
				<?=$bwout_string;?> Mbps  (<?=$load_string;?> %)
			</DIV>
			<DIV class="label"
				style="height: 13px; 
					position: absolute; 
					left: 350px; 
					top: 10px; 
					background-color: #eeeeee; 
					color: black; 
					text-align: center;
					font-size: 12px; 
					font-family: sans-serif; 
					padding: 2px;
			"><?=$label;?></DIV>
			<div class="powerbutton" 
				style="padding: 5px; 
					position: absolute; 
					left: 530px; 
					top:8px; 
					width: 30px; 
					float: right;
			">
<form action="startup.php" method="POST" target="_blank">
<input type="hidden" name="config" value="repeater" />
<input type="hidden" name="version" value="2" />
<input type="hidden" name="license" value="devpay" />
<input type="hidden" name="zone" value="us-east-1" />
<input type="hidden" name="elasticIP" value="Dynamic" />
<input type="hidden" name="keypair" value="Wowza-Keypair" />
<input type="hidden" name="security" value="Wowza-SecGrp" />
<input type="hidden" name="type" value="m1.small" />
<input title="Start a default repeater" type="image" width="20" height="20" src="/images/power-green.png" alt="Start Repeater" />
</form>

			</div>
			<div class="version"
				title="<?=$origin_ver;?>"
				style="position: absolute;
					left: 23px;
					top: 24px;
					width: 20px;
					height: 20px;
					border-radius: 10px;
					border: none;
			"></DIV>
					
		</div>
	</div>
<?php

// Iterate through IP address array and display individual servers

foreach ($ip as $repeater) { 
		$server_load = $bwout[$repeater] / $cap[$addr] * 100; // convert to percentage

		$load_string = sprintf("%.2f",$server_load);
		$bwout_string = sprintf("%.3f",$bwout[$repeater]);
		$load_round = round($server_load);
	
		switch ($server_load) {
			case ($server_load > 99): $color = "#000000"; $heavy = true; break;
			case ($server_load >= 85): $color = "#FF0000"; $heavy = true; break;
			case ($server_load >= 75): $color = "#FFFF00"; break;
			default: $color = "#00FF00";
			}
		$label = 'Edge | <A style="color: black;" HREF="http://'.$repeater.':8086/serverinfo.xml" target="_blank">'. $repeater . "</A>";
		$lcd = $conn[$repeater]." Connections <BR>$bwout_string Mbps ($load_string%)";
		?>
		<DIV class="rackslot" 
			style="height: 60px; 
				width: 660px; 
				position: relative; 
				border: none; 
				background: none;
		">
		<DIV class="server" 
			style="height: 60px; 
				width: 600px; 
				float: left; 
				position: relative; 
				border: none; 
				background-image: url('images/rackserver2.jpg');
		">
			<DIV class="loadbar" 
				style="height: 10px; 
					border-radius: 3px; 
					opacity: 0.6; 
					position: absolute; 
					left: 46px; 
					top: 42px; 
					width: 500px; 
					background: none repeat scroll 0% 0% #ffffff; 
					border: 1px solid;
			">
				<DIV class="load" 
					style="height: 100%; 
						border-radius: 2px; 
						position: absolute; 
						left: 0px; 
						top: 0px; 
						background: <?=$color?>; 
						width: <?=$load_round;?>%;
				">
				</div> 
			</div>
			<DIV class="display" 
				style="height: 22px; 
				border-radius: 3px; 
				position: absolute; 
				left: 46px; 
				top: 14px; 
				width: 145px; 
				background-color: #2222FF; 
				color: #CCCCFF; 
				font-size: 8px; 
				border: 1px solid black; 
				font-family: sans-serif; 
				padding: 1px;
			"><?=$lcd;?></DIV>
			<DIV class="label" 
				style="height: 13px; 
					position: absolute; 
					left: 350px; 
					top: 10px; 
					background-color: #eeeeee; 
					color: black; 
					text-align: center;
					font-size: 12px; 
					font-family: sans-serif; 
					padding: 2px;
			"><?=$label;?></DIV>
			<div class="powerbutton" 
				style="padding: 5px;
				 	position: absolute; 
					left: 530px; 
					top:8px; 
					width: 30px; 
					float: right;
			">
				<?php 
					if ($repeater != $origin_ip) {
        				echo '<FORM action="terminate.php" method="POST" target="_blank">';
					echo '<INPUT type="hidden" name="instances[]" value="'.$iid[$repeater].'">';
					echo '<INPUT type="image" height="20" width ="20" src="images/power-red.png" TITLE="Terminate this server">';
					echo '</FORM>';
					}
					else 
					{
					echo '<FORM action="">';
					echo '<IMG SRC="images/power-gray.png" height="20" TITLE="Power control disabled on origin">';
					echo '</FORM>';
					}
				?>
			</div>

			<div class="version"
				title="<?php echo $ver[$repeater]." ".$sz[$repeater]." ".$iid[$repeater];?>"
				style="position: absolute;
					left: 23px;
					top: 24px;
					width: 20px;
					height: 20px;
					border-radius: 10px;
					border: none;
			"></DIV>
		</div>
	</DIV>
<?php

} // Repeater Loop
			echo "<SMALL>Last Refresh: ";
			echo $date = date("Y-m-d H:i:s");
			echo "</SMALL>\n";

?>

[/php]
```

aws-init.php:

```

[php]
<?php
require_once '/usr/share/php/AWSSDKforPHP/sdk.class.php';

define('AWS_KEY', $_SESSION['AWS_KEY']);
define('AWS_SECRET_KEY', $_SESSION['AWS_SECRET_KEY']);

        $startup_region = $_SESSION['DEFAULT_REGION'];
        
$ec2 = new AmazonEC2();

?>
[/php]
```

functions.php:

```

[php]
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
[/php]
```

capacity\_vars.php:

```

[php]
<?PHP 
$mbps['m1.small']=150; 
$mbps['m1.large']=250; 
$mbps['m1.xlarge']=350; 
?>
[/php]
```
