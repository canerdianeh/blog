---
layout: page
title: Wowza Origin Server Startup (bash)
date: 2011-09-07 18:48:34.000000000 -05:00
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
  dsq_thread_id: '407769231'
  _googl_shortlink: http://goo.gl/mXJiK
  _syntaxhighlighter_encoded: '1'
author:
  login: admin
  email: ian@nerdherd.net
  display_name: Site Administrator
  first_name: Site
  last_name: Administrator
permalink: "/code/ec2/wowza-origin-startup-bash/"
---

```bash
#!/bin/bash
export JAVA\\_HOME=/usr
export EC2\\_HOME=/opt/ec2/tools
export amiid="ami-5a649833"
export config\\_loc="$HOME/amazon"
export config="origin"
export var\\_loc="$HOME/var"
export key="keypair"
export zone="us-east-1c"
export group="Wowza"
export ip="11.22.33.44"
#     The variables that start with the name EC2 are used by the Tools API. They are the directory where you downloaded your Tools installation and the key and cert files provided to you by Amazon when you created your instance. The other variables are used by the shell commands in this example, and include:
#
#    \\* **amiid**: Amazon Image ID
#    \\* **key**: Key name associated with this instance
#    \\* **zone**: The zone in which this instance was created
#    \\* **group**: The security group associated with this instance
#    \\* **ip**:  The Elastic IP address to associate with the instance
#  \\* **config\\_loc**: the location where your startup package config directories are located
# \\* **config:** the name of the directory containing the startup package for this instance
# \\* **var\\_loc:** the location of the directory containing temporary data for these scripts
echo Starting ${config} server
# zip up the config directory for sending to amazon as user data.
# Zip file must not exceed 16K.
if [ -f ${var\\_loc}/${config}.zip ]
then
rm ${var\\_loc}/${config}.zip
fi
cd ${config\\_loc}/${config}
zip -ru9 ${var\\_loc}/${config}.zip \\*
ls -la ${var\\_loc}/${config}.zip
#    Now it's time to start the instance, and then loop until it is running.
#
# Steps:
# 1) Start the instance
# 2) Capture the output so that we can grab the INSTANCE ID field and use it to determine when the instance is running
echo Launching AMI ${amiid}
${EC2\\_HOME}/bin/ec2-run-instances ${amiid} --user-data-file ${var\\_loc}/${config}.zip -t m1.small -k ${key} --group ${group} --monitoring > ${var\\_loc}/${config}.ec2
if [ $? != 0 ]; then
echo Error starting instance for image ${amiid}
exit 1
fi
# Now that the instance has and ID, we need to capture and save it to a file
export iid=`cat ${var\\_loc}/${config}.ec2 | grep INSTANCE | cut -f2`
echo ${iid} > ${var\\_loc}/${config}.iid
#
# Loop until the status changes to .running.
#
sleep 30
echo Starting instance ${iid}
# Define the string we're looking for from ec2-describe-instances to determine running status
export RUNNING="running"
# Set the running flag to false. As soon as it's running, we'll change the value in the while loop, causing it to exit and move on.
export done="false"
while [ $done == "false" ]
do
export status=`${EC2\\_HOME}/bin/ec2-describe-instances ${iid} | grep INSTANCE | cut -f6`
if [ $status == ${RUNNING} ]; then
export done="true"
else
echo Waiting...
sleep 10
fi
done
# Now that the instance is running, we can tag it with all kinds of stuff.
${EC2\\_HOME}/bin/ec2-create-tags ${iid} --tag user=`whoami` --tag origin=0 --tag Name=Wowza Origin
# Capturing the startup IP
export startip=`${EC2\\_HOME}/bin/ec2-describe-instances ${iid} | grep INSTANCE | cut -f17`
echo Instance ${iid} is running at ${startip}
# If you need to attach an EBS volume, this is the place to do it. Uncomment the requisite lines and be sure to define the variables.
#    Now we have the running instance ID, which we will use going forward. We next attach the EBS volume to the running instance, associating a device name. After we attach the volume, we wait until its status indicates that it is attached.
#
# Attach the volume to the running instance
#
#    echo Attaching volume ${vol\\_name}
#    ${EC2\\_HOME}/bin/ec2-attach-volume ${vol\\_name} -i ${iid} -d ${device\\_name}
#    sleep 15
#
# Loop until the volume status changes
# to "attached"
#
#    export ATTACHED="attached"
#    export done="false"
#    while [ $done == "false" ]
#    do
#    export status=`${EC2\\_HOME}/bin/ec2-describe-volumes | grep ATTACHMENT | grep ${iid} | cut -f5`
#    if [ $status == ${ATTACHED} ]; then
#    export done="true"
#    else
#    echo Waiting...
#    sleep 10
#    fi
#    done
#    echo Volume ${vol\\_name} is attached
#
## END EBS SECTION
#    Now we associate the Elastic IP address with the running instance. This capability is important in an environment where instances are being started and stopped at various points for scalability reasons, so these operations will happen with no interruption for the user.
#
# Associate the Elastic IP with the instance
# After this operation we just sleep a bit to let Amazon catch up.
#
echo Associating elastic IP address ${ip}
${EC2\\_HOME}/bin/ec2-associate-address ${ip} -i ${iid}
sleep 30
echo ${iid} > ~/var/wowza\\_current\\_instance\\_${ip}
echo Image ${amiid} instance ${iid} is ready to go!
```
