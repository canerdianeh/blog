---
layout: post
title: Live Streaming on a Budget (Part 5) - Automating EC2
date: 2009-07-08 13:42:36.000000000 -05:00
type: post
parent_id: '0'
published: true
password: ''
status: publish
categories:
- Internet Campus
- streaming
tags:
- ec2
- scripting
- wowza
meta:
  _edit_last: '1'
  dsq_thread_id: '217877503'
  _googl_shortlink: http://goo.gl/kv7Fu
author:
  login: ianbeyer
  email: ian.beyer@gmail.com
  display_name: Ian Beyer
  first_name: Ian
  last_name: Beyer
permalink: "/2009/07/08/live-streaming-on-a-budget-part-5-automating-ec2/"
---

I mentioned a few posts back that I was looking for a way to automate startup and shutdown of the servers. Thanks to some great sleuthing by [Justin Moore](http://www.wantmoore.com/) at [Granger Community Church](http://www.gccwired.com), I got some [scripts to start from](http://www.phurnace.com/blog/easy-steps-to-start-up-amazon-ec2-images-2.html). I had to make some modifications to suit our exact purposes, but that was relatively easy.

Ingredients:

Linux system with:

- Java Runtime (in Ubuntu, the package is sun-java6-jre)
- Amazon EC2 API Tools (installed in /opt/ec2/tools)
- Wowza Startup Packages (installed in /root/ec2)
- EC2 keys (installed in /root/ec2)

Note: Because these scripts are run from cron, you'll need to put all your environment variables to run EC2 at the beginning of each one.

I have 6 separate versions of the startup and termination scripts, one for each server I need to start. I could roll it into one big script, but putting them in their own individual ones not only lets me do an individual machine manually, I can run them all in parallel from cron, which shortens the startup time.

The [startup script](http://blog.ianbeyer.com/code/ec2/wowza-origin-startup-bash/ "Wowza Origin Server Startup (bash)") functions as follows:

1. Assign environment variables for EC2 and for the machine parameters
2. Launch machine with ec2-run-instances, redirect output to a temporary file\*
3. Parse temporary file and extract the instance ID, and put it into an environment variable
4. Write contents of instance ID environment variable to a file in /root/ec2 for use by the shutdown script
5. Wait 30 seconds
6. Start checking instance status every so we know when it's running (wait 10 seconds to check again if it's not)
7. Attach any EBS volumes (Optional - I don't currently need this, so it's commented out)
8. Assign Elastic IP
9. Execute any additional commands via ssh (Optional, I don't have any that need to run)

\* The original scripts use /tmp/a, which is fine, but I had to make each script do its own temporary file since all 6 were running simultaneously and I ran into problems with getting the right Instance IDs set.

The [shutdown script](http://blog.ianbeyer.com/code/ec2/ec2-wowza-origin-server-shutdown/ "Origin Server Shutdown Script") works like this:

1. Query AWS for all running instances
2. Issue EC2 termination call
3. ???
4. PROFIT!

Lastly, put it in your crontab:

> # m h  dom mon dow   command  
> 15 8 \* \* 0 /root/start-windows.sh  
> 25 8 \* \* 0 /root/start-origin.sh  
> 25 8 \* \* 0 /root/start-iphone.sh  
> 25 8 \* \* 0 /root/start-repeater1.sh  
> 25 8 \* \* 0 /root/start-repeater2.sh  
> 25 8 \* \* 0 /root/start-repeater3.sh
>
> 0 19 \* \* 0 /root/term-windows.sh  
> 0 19 \* \* 0 /root/term-iphone.sh  
> 0 19 \* \* 0 /root/term-origin.sh  
> 0 19 \* \* 0 /root/term-repeater1.sh  
> 0 19 \* \* 0 /root/term-repeater2.sh  
> 0 19 \* \* 0 /root/term-repeater3.sh

This starts up all of them (except the Windows instance which needs more time) at 8:25 on Sunday morning and shuts them down at 7 on Sunday evening.  (be sure that if you're using GMT on your Linux box to take that into account).

If you're using an encoder that can be started and stopped on a schedule, synchronize your times with this, and you'll be golden. The Wowza EC2 images take about 60-90 seconds to fully get up and running, and the Windows one takes about 10-15 min. Currently, the Windows server pulls from the encoder via a 1:1 NAT rule, so the WME instance can be running before the EC2 server is going. When EC2 is ready, it simply connects to the encoder and is off and running.
