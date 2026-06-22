---
layout: page
title: Edge Server Startup Script (bash)
date: 2011-09-07 19:02:29.000000000 -05:00
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
  dsq_thread_id: '407777410'
  _googl_shortlink: http://goo.gl/O7JPV
  _syntaxhighlighter_encoded: '1'
author:
  login: admin
  email: ian@nerdherd.net
  display_name: Site Administrator
  first_name: Site
  last_name: Administrator
permalink: "/code/ec2/wowza-edge-startup-bash/"
---

```

bash
  
#!/bin/bash

export JAVA\_HOME=/usr  
export EC2\_HOME=/opt/ec2/tools  
export amiid="ami-5a649833"  
export config\_loc="$HOME/amazon"  
export var\_loc=”$HOME/var”  
export config="repeater"  
export key="keypair"  
export zone="us-east-1c"  
export group="Wowza"

# Check to see if there's a shutdown in progress - if there is, this could really confuse things

#     The variables that start with the name .EC2. are used by the Tools API. They are the directory where you downloaded your Tools installation and the key and cert files provided to you by Amazon when you created your instance. The other variables are used by the shell commands in this example, and include:  
#  
# \* amiid: Amazon Image ID  
# \* key: Key name associated with this instance  
# \* zone: The zone in which this instance was created  
# \* group: The security group associated with this instance  
# \* config\_loc: the location where your startup package config directories are located  
# \* config: the name of the directory containing the startup package for this instance  
# \* var\_loc: the location of the directory containing temporary data for these scripts

# Initiate startup

if [ -f ~/var/shutdown.sem ]  
then  
echo Repeater shutdown in progress. Please wait until complete before starting new instances.  
exit  
fi

# Check to see how many repeaters are already running -- if the file doesn't exist, assume there are none.

if [ -f ${var\_loc}/repcount.txt ]  
then  
export index=`cat ${var\_loc}/repcount.txt`  
else  
export index=0  
fi

# increment the count by 1 and output to the counter file.  
export repcount=$(expr ${index} + 1)

echo ${repcount} &gt; ${var\_loc}/repcount.txt

echo Starting ${config} with index ${index}  
touch ${var\_loc}/repeater-${index}.iid

# zip up the config directory for sending to amazon as user data.  
# Zip file must not exceed 16K.

if [ -f ${var\_loc}/${config}.zip ]  
then  
rm ${var\_loc}/${config}.zip  
fi

cd ${config\_loc}/${config}

zip -ru9 ${var\_loc}/${config}.zip \*

ls -la ${var\_loc}/${config}.zip

#    Now it's time to start the instance, and then loop until it is running.  
#  
# Start the instance  
# Capture the output so that  
# we can grab the INSTANCE ID field  
# and use it to determine when  
# the instance is running  
#

echo Launching AMI ${amiid}  
${EC2\_HOME}/bin/ec2-run-instances ${amiid} --user-data-file ${var\_loc}/${config}.zip -t m1.small -k ${key} --group ${group} --monitoring &gt; ${var\_loc}/${config}-${index}.ec2  
if [ $? != 0 ]; then  
echo Error starting instance for image ${amiid}  
exit 1  
fi  
export iid=`cat ${var\_loc}/${config}-${index}.ec2 | grep INSTANCE | cut -f2`

echo ${iid} &gt; ${var\_loc}/${config}-${index}.iid

#  
# Loop until the status changes to .running.  
#  
sleep 30  
echo Starting instance ${iid}  
export RUNNING="running"  
export done="false"  
while [ $done == "false" ]  
do  
export status=`${EC2\_HOME}/bin/ec2-describe-instances ${iid} | grep INSTANCE | cut -f6`  
if [ $status == ${RUNNING} ]; then  
export done="true"  
else  
echo Waiting...  
sleep 10  
fi  
done  
${EC2\_HOME}/bin/ec2-create-tags ${iid} --tag user=`whoami` --tag repeater=${index} --tag Name=Wowza Repeater  
export ip=`${EC2\_HOME}/bin/ec2-describe-instances ${iid} | grep INSTANCE | cut -f17`  
echo Instance ${iid} is running at ${ip}

#    Now we have the running instance ID, which we will use going forward. We next attach the EBS volume to the running instance, associating a device name. After we attach the volume, we wait until its status indicates that it is attached.

#  
# Attach the volume to the running instance  
#  
#    echo Attaching volume ${vol\_name}  
#    ${EC2\_HOME}/bin/ec2-attach-volume ${vol\_name} -i ${iid} -d ${device\_name}  
#    sleep 15

#  
# Loop until the volume status changes  
# to "attached"  
#  
#    export ATTACHED="attached"  
#    export done="false"  
#    while [ $done == "false" ]  
#    do  
#    export status=`${EC2\_HOME}/bin/ec2-describe-volumes | grep ATTACHMENT | grep ${iid} | cut -f5`  
#    if [ $status == ${ATTACHED} ]; then  
#    export done="true"  
#    else  
#    echo Waiting...  
#    sleep 10  
#    fi  
#    done  
#    echo Volume ${vol\_name} is attached  
#  
## END EBS SECTION

echo Image ${amiid} instance ${iid} is ready to go!  
echo ${iid} &gt; ~/var/wowza\_current\_instance\_${ip}  
```
