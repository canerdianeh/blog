---
layout: post
title: Amazon EC2 and DNS
date: 2011-02-05 16:53:50.000000000 -06:00
type: post
parent_id: '0'
published: true
password: ''
status: publish
categories:
- Cloud Computing
tags:
- Cloud
- dns
- wowza
meta:
  _wp_old_slug: ''
  dsq_thread_id: '223504341'
  _edit_last: '1'
  _googl_shortlink: http://goo.gl/ixtQq
author:
  login: ianbeyer
  email: ian.beyer@gmail.com
  display_name: Ian Beyer
  first_name: Ian
  last_name: Beyer
permalink: "/2011/02/05/amazon-ec2-and-dns/"
---

Just discovered an interesting little tidbit about using DNS from within Amazon's EC2:

When resolving the public DNS name of an EC2 instance, from another EC2 instance, you will get the internal IP address of that instance.This is useful if you have multiple EC2 instances talking to each other.

For example, if you have a Wowza edge/origin setup, you have your origin set up on an elastic IP for consistency in your configuration, and point your edge servers to that IP.

Now this may seem insignificant until you remember that any traffic between EC2 instances via the public IP (elastic IP or not) is going to incur a charge of 1 cent per gigabyte. If you've got a large streaming setup, that can add up.

If you want to use your own domain name for your server, be sure to use a CNAME record to the public IP instead of an A record. The A record will always return the public IP. The CNAME will tell the nameserver what the public DNS name is for that instance, which EC2's nameservers will then return as the internal address.

With an A record to the public (elastic) IP:

```

ubuntu@ip-10-245-bar-baz:~$ nslookup wms.domain.org.
Non-authoritative answer:
Name:   wms.domain.org
Address: 50.16.XXX.YYY
```

With a CNAME record to the public DNS name:

```

ubuntu@ip-10-245-bar-baz:~$ nslookup wms.domain.org.
Non-authoritative answer:
wms2.domain.org      canonical name = ec2-50-16-XXX-YYY.compute-1.amazonaws.com.
Name:   ec2-50-16-XXX-YYY.compute-1.amazonaws.com
Address: 10.114.AAA.BBB
```
