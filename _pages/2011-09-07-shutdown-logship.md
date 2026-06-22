---
layout: page
title: Shutdown with log shipping (bash)
date: 2011-09-07 19:11:39.000000000 -05:00
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
  dsq_thread_id: '417465722'
  _googl_shortlink: http://goo.gl/lUCbV
  _syntaxhighlighter_encoded: '1'
author:
  login: admin
  email: ian@nerdherd.net
  display_name: Site Administrator
  first_name: Site
  last_name: Administrator
permalink: "/code/ec2/shutdown-logship/"
---

Shuts down an instance and ships the Wowza logs.  

```

bash
  
#!/bin/bash

export JAVA\_HOME=/usr  
export EC2\_HOME=/opt/ec2/tools

export date=`date +%m-%d-%y`  
export var\_loc = $HOME/var  
export count=`cat ${var\_loc}/repcount.txt`  
export start=0  
export end=`expr $count - 1`  
echo terminating ${count} repeaters from ${start} to ${end}  
echo setting shutdown flag...  
touch ~/var/shutdown.sem

# instantiate a loop to shut down each repeater

for (( i=0;i&lt;=${end};i++))  
do  
export index=${i}  
echo Terminating Repeater ${index}  
if [ -f ~/var/repeater-${index}.iid ]  
then

# Capture the instance ID  
export iid=`cat ~/var/repeater-${index}.iid`

# Capture the instance IP address  
export ip=`${EC2\_HOME}/bin/ec2-describe-instances ${iid} | grep INSTANCE | cut -f17`

echo Terminating Repeater ${index} at AMI ${iid} on IP address ${ip}  
echo Shutting down services...

# Shut down Wowza service, so that the load balancer is notified of the server being stopped  
ssh -o StrictHostKeyChecking=no -i ~/.ssh/gsg-keypair.priv.txt root@${ip} service WowzaMediaServer stop

# zip up the logs  
echo Archiving logs...  
ssh -o StrictHostKeyChecking=no -i ~/.ssh/gsg-keypair.priv.txt root@${ip} gzip /usr/local/WowzaMediaServer/logs/\*.log

# ship the logs to a local directory, organized by date and instance ID.  
echo Shipping logs...  
mkdir -p ${var\_loc}/logs/repeaters/${date}/${iid}  
scp -o StrictHostKeyChecking=no -i ~/.ssh/gsg-keypair.priv.txt root@${ip}:/usr/local/WowzaMediaServer/logs/\*.gz ~/var/logs/repeaters/${date}/${index}

# Now we can actually shut it off.  
echo Terminating instance...  
${EC2\_HOME}/bin/ec2-terminate-instances ${iid}  
if [ $? != 0 ]; then  
echo Error terminating instance for image ${iid}  
exit 1  
fi

# Clean up temp files from startup script.

echo Removing temporary data files...  
rm ~/var/repeater-${index}.\*  
rm ~/var/wowza\_current\_instance\_${ip}

echo Instance ${iid} has been terminated.  
fi

done

## End of loop

# check to see if there's anything left over  
if [ `ls -l ${var\_loc}/repeater-\*.iid | wc -l` -gt 0 ]  
then  
echo Some AMI ID files still exist. Please manually shut down those instances if necessary  
fi

# reset the repeater counter  
echo 0 &gt; ${var\_loc}/repcount.txt

# remove the shutdown semaphore  
rm ${var\_loc}/shutdown.sem  
```
