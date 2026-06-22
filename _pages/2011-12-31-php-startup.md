---
layout: page
title: EC2 Startup (PHP)
date: 2011-12-31 21:01:23.000000000 -06:00
type: page
parent_id: '272'
published: true
password: ''
status: publish
categories: []
tags: []
meta:
  _edit_last: '1'
  _wp_page_template: default
  dsq_thread_id: '522475154'
  _syntaxhighlighter_encoded: '1'
author:
  login: admin
  email: ian@nerdherd.net
  display_name: Site Administrator
  first_name: Site
  last_name: Administrator
permalink: "/code/ec2/php-startup/"
---

```php
  
<?php  
require\_once '/usr/share/php/AWSSDKforPHP/sdk.class.php';

define('AWS\_KEY', 'XXXX');  
define('AWS\_SECRET\_KEY', 'YYYY');

$ec2 = new AmazonEC2();

$filename = "startup.zip";  
$userdata = base64\_encode(file\_get\_contents($filename));

if (filesize($filename) > 16383 ) { die('Startup package exceeeds 16KB. Please adjust and try again'); }

$startup\_opts = array (  
"KeyName" => 'keypair'],  
"SecurityGroup" => 'security'],  
"InstanceType" => 'm1.small',  
"UserData" => $userdata  
);

$ec2->set\_region('us-east-1');

$startup\_response = $ec2->run\_instances($ami,1,1,$startup\_opts);  
if ($startup\_response->status != "200") {  
print\_r($startup\_response);  
die('Error starting up.');  
}

# Get instance ID  
$instance\_id = $startup\_response->body->instancesSet->item->instanceId;

# Set instance tags  
# These tags are arbitrary key/value pairs  
$tags = array (  
array("Key"=>'Name', "Value" => 'Name'),  
array("Key"=>'Type', "Value" => 'Type'),  
array("Key"=>'Client', "Value" => 'Client')  
);

$tags\_response = $ec2->create\_tags($instance\_id,$tags);  
$tags\_status = $tags\_response->status;

if ($tags\_status != "200")  
{ print "Tags error : $tags\_response\n"; }

# Query every few seconds and see if the instance is running yet

print "Waiting for instance to enter running state ...";  
$running = false;  
while (! $running ) {  
$describe\_opts = array( "InstanceId" => $instance\_id);  
$response = $ec2->describe\_instances($describe\_opts);

$state = $response->body->reservationSet->item->instancesSet->item->instanceState->name;

if ($state == 'running') {  
$running = TRUE;  
#print "Complete.\n";  
}  
else {  
#print ".";  
sleep (5);  
}

}

# Optionally associate Elastic IP  
$elastic\_ip = '1.2.3.4';  
$ip\_response = $ec2->associate\_address($instance\_id,$elastic\_ip);  
if ($ip\_response->status != "200") {print "IP Address allocation error"; }  
flush();

?>  
```
