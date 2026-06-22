---
layout: post
title: Converting EC2 S3/instance-store image to EBS
date: 2012-05-10 19:16:01.000000000 -05:00
type: post
parent_id: '0'
published: true
password: ''
status: publish
categories:
- Cloud Computing
- Wowza
tags: []
meta:
  _edit_last: '2'
  dsq_thread_id: '684860004'
author:
  login: ianbeyer
  email: ian.beyer@gmail.com
  display_name: Ian Beyer
  first_name: Ian
  last_name: Beyer
permalink: "/2012/05/10/converting-ec2-s3instance-store-image-to-ebs/"
---

Amazon's instance-store images are convenient, but ephemeral in nature. Once you shut them down, they're history. If you want persistence of data, you want to use an EBS instance that can be stopped and started at will without losing your info. Here's the process I went through to convert a Wowza image to EBS for a client to use with a reserved instance. I'm going to assume no configuration changes for [Wowza Media Server](http://www.wowza.com/ec2 "Wowza Media Server on EC2"), as the default startup package is fairly full-featured. This process works for any other instance-store AMI, just ignore the Wowza bits if that's your situation.

Boot up a 64-bit Wowza lickey instance. I was working in us-east-1, so I used ami-e6e4418f, which was the latest as of this blog post.

Once it's booted up, log in.

Elevate yourself to root. You deserve it:

```

sudo su -
```

Stop the Wowza service:

```

service WowzaMediaServer stop
```

delete the Server.guid file. This will cause new instances to regenerate their GUID.

```

rm /usr/local/WowzaMediaServer/conf/Server.guid
```

Go into the AWS management console and create a blank EBS volume in the same zone as your instance.

Attach that volume to your instance (I'm going to assume /dev/sdf here)

Create a filesystem on it (note: while the console refers to it as /dev/sdf, Amazon Linux uses the Xen virtual disk notation /dev/xvdf):

```

mkfs.ext4 /dev/xvdf
```

Create a mount point for it, and mount the volume:

```

mkdir /mnt/ebs
mount /dev/xvdf /mnt/ebs
```

Sync the root and dev filesystems to the EBS disk:

```

rsync -avHx / /mnt/ebs
rsync -avHx /dev /mnt/ebs
```

Label the disk:

```

tune2fs -L '/' /dev/xvdf
```

Flush all writes and unmount the disk:

```

sync;sync;sync;sync && umount /mnt/ebs
```

Using the web console, create a snapshot of the EBS volume. Make a note of the snapshot ID.

Still in the web console, go to the instances and make a note of the kernel ID your instance is using. This will be aki-something. In this case, it was aki-88aa75e1.

For the next step, you’ll need an EC2 X.509 certificate and private key. You get these through the web console’s “Security Credentials” area. This is NOT the private key you use to SSH into an instance. You can have as many as you want, just keep track of the private key because Amazon doesn’t keep it for you. If you lose it, it’s gone for good. Download both the private key and certificate. You can either upload them to the instance or open them in a text editor and copy the text, and paste it into a file. Best place to do this is in /root. Once you have the files, set some environment variables to make it easy:

```

export EC2_CERT=`pwd`/cert-*.pem
export EC2_PRIVATE_KEY=`pwd`/pk-*.pem
```

once this is done, you'll need to register the snapshot as an AMI. It's important here to specify the root device name as well as map out the ephemeral storage as Wowza uses those for content and logs. Ephemeral storage will persist through a reboot, but not a termination. If you have data that needs to persist through termination, use an additional EBS volume.

```

ec2-register --snapshot [snapshot ID] --description "Descriptive Text" --name "Unique-Name" --kernel [kernel ID] --block-device-mapping /dev/sdb=ephemeral0 --block-device-mapping /dev/sdc=ephemeral1 --block-device-mapping /dev/sdd=ephemeral2 --block-device-mapping /dev/sde=ephemeral3 --architecture x86_64 --root-device-name /dev/sda1
```

Once it's registered, you should be able to boot it up and customize to your heart's content. Once you have a configuration you like, right-click on the instance in the AWS web console and select "Create Image (EBS AMI)" to save to a new AMI.

*Note: As of right now, I don't think startup packages are working with the EBS AMI. I don't know if they're supposed to or not.*
