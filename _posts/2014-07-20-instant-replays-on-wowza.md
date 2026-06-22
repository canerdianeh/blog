---
layout: post
title: Instant Replays on Wowza
date: 2014-07-20 09:19:44.000000000 -05:00
type: post
parent_id: '0'
published: true
password: ''
status: publish
categories:
- Code
- streaming
- Wowza
tags:
- bash
- powershell
- replay
- VOD
meta:
  _edit_last: '2'
  _syntaxhighlighter_encoded: '1'
  _wpas_done_all: '1'
  dsq_thread_id: '2858750942'
author:
  login: ianbeyer
  email: ian.beyer@gmail.com
  display_name: Ian Beyer
  first_name: Ian
  last_name: Beyer
permalink: "/2014/07/20/instant-replays-on-wowza/"
---

One of the useful features of Wowza is its ability to record a stream to disk and then be able to use that recording for a replay. In version 3.5, it would simply take the stream name, slap an MP4 extension on the end, and version any previous ones with \_0, \_1, etc. In 3.6, the default naming scheme for these recordings was a timestamp, with a configuration option to use the legacy naming convention. In Version 4, it appears this legacy naming convention option has disappeared altogether, meaning you can't set up a player to just play back "streamname.mp4" and it would always grab the most recent one. **EDIT: It appears that this loss of functionality was unintentional and has been classified as a bug, which should be fixed very soon.**

This became a problem for one of my clients after their Wowza server got updated to V4. It wasn't practical to re-code the player every week, or to go into the server and manually rename the file. Since it's on a Windows server, PowerShell to the rescue:

[code language="powershell"]  
$basepath= "C:\Program Files (x86)\Wowza Media Systems\Wowza Streaming Engine 4.0.3\content\"  
$replayfile = gci $basepath\streamname\*.mp4 | sort LastWriteTime | select -last 1  
$link = $replayfile.Name

cmd /c del $basepath\replay.mp4  
cmd /c mklink $basepath\replay.mp4 $basepath\$link  
[/code]

I then put this into a scheduled task, with time-based triggers. Powershell is a little tricky to get into a scheduled task, but I finally got the syntax right:

**Action:** C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe  
**Arguments:** -nologo -file "C:\Program Files (x86)\Wowza Media Systems\Wowza Streaming Engine 4.0.3\content\replay.ps1"

If you're on Linux or OSX, you can do this in bash instead:

[code language="bash"]  
#!/bin/bash

basepath='/usr/local/WowzaStreamingEngine/content'  
unset -v replayfile  
for file in "$basepath"/streamname\*.mp4  
do  
[[ -z $replayfile || $file -nt $replayfile ]] && replayfile=$file  
done;  
rm -f $basepath/replay.mp4  
ln -s $replayfile $basepath/replay.mp4

[/code]

and put it in your crontab (this example is every sunday at 11:30am)

[code]  
30 11 \* \* 0 /bin/bash /usr/local/WowzaMediaServer/content/replay.sh  
[/code]
