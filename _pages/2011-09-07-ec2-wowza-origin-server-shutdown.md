---
layout: page
title: Origin Server Shutdown Script
date: 2011-09-07 19:18:35.000000000 -05:00
type: page
parent_id: '272'
published: true
password: ''
status: publish
categories: []
tags: []
meta:
  _edit_last: '1'
  wp_plus_one_redirect: ''
  _wp_page_template: default
  dsq_thread_id: '417464741'
  _googl_shortlink: http://goo.gl/2GglG
  _syntaxhighlighter_encoded: '1'
author:
  login: admin
  email: ian@nerdherd.net
  display_name: Site Administrator
  first_name: Site
  last_name: Administrator
permalink: "/code/ec2/ec2-wowza-origin-server-shutdown/"
---

```

bash
  
#!/bin/bash

export JAVA\_HOME=/usr  
export EC2\_HOME=/opt/ec2/tools

export index=$1  
export date=`date +%m-%d-%y`

# Get instance ID

if [ -f ~/var/origin.iid ]  
then  
export iid=`cat ~/var/origin.iid`  
else  
echo That instance does not exist!  
exit  
fi

# Get IP address  
export ip=`${EC2\_HOME}/bin/ec2-describe-instances ${iid} | grep INSTANCE | cut -f17`  
echo Terminating Origin server at AMI ${iid} on IP address ${ip}

# Shut down Wowza

echo Shutting down services...  
ssh -i ~/.ssh/gsg-keypair.priv.txt root@${ip} service WowzaMediaServer stop

# Back up content of archive directory to mounted S3 bucket  
echo Archiving content directory  
ssh -i ~/.ssh/gsg-keypair.priv.txt root@${ip} rm -f /usr/local/WowzaMediaServer/content/s3\*.smil  
ssh -i ~/.ssh/gsg-keypair.priv.txt root@${ip} rm -f /usr/local/WowzaMediaServer/content/s3\*.mp4  
ssh -i ~/.ssh/gsg-keypair.priv.txt root@${ip} cp /usr/local/WowzaMediaServer/content/\*.smil /usr/local/WowzaMediaServer/content/s3  
ssh -i ~/.ssh/gsg-keypair.priv.txt root@${ip} cp /usr/local/WowzaMediaServer/content/\*.mp4 /usr/local/WowzaMediaServer/content/s3

# Zip up the logs  
echo Archiving logs...  
ssh -i ~/.ssh/gsg-keypair.priv.txt root@${ip} gzip /usr/local/WowzaMediaServer/logs/\*.log

# Save the logs to a local directory  
echo Shipping logs...  
mkdir -p ~/var/logs/origin/${date}/${iid}  
scp -i ~/.ssh/gsg-keypair.priv.txt root@${ip}:/usr/local/WowzaMediaServer/logs/\*.gz ~/var/logs/origin/${date}/${index}

# Shut 'er down  
echo Terminating instance...  
${EC2\_HOME}/bin/ec2-terminate-instances ${iid}  
if [ $? != 0 ]; then  
echo Error terminating instance for image ${iid}  
exit 1  
fi

# clean up files  
echo Removing temporary data files...  
rm ~/var/origin.\*  
rm ~/var/wowza\_current\_instance\_${ip}

echo Instance ${iid} has been terminated.  
```
