---
layout: post
title: 'Gear: Teradek VidiU - First Look'
date: 2014-08-07 19:57:50.000000000 -05:00
type: post
parent_id: '0'
published: true
password: ''
status: publish
categories: []
tags: []
meta:
  _edit_last: '2'
  _wpas_done_all: '1'
  _bpp_element: body
  _bpp_repeat-x: 'yes'
  _bpp_repeat-y: 'yes'
  _bpp_attachment: scroll
  _bpp_position: center
  _bpp_fade: 'yes'
  _bpp_fade_height: '100'
  _bpp_color: "#"
author:
  login: ianbeyer
  email: ian.beyer@gmail.com
  display_name: Ian Beyer
  first_name: Ian
  last_name: Beyer
permalink: "/2014/08/07/gear-teradek-vidiu-first-look/"
---

I recently got some Teradek gear to try out in a church setting, and I will be posting a few blog posts about it. Other than loaning the gear, Teradek is not compensating me for this. I am, however, more than happy to sell Teradek hardware to anyone that wants to buy it from me.

First up: The VidiU, Teradek's low-cost offering at $699.

When you open the box, the unit is right on top, nestled comfortably in a piece of high-density foam. Underneath is the power supply (with plugs for just about every electrical outlet in the world), a 1-meter ethernet cable, and a 50cm HDMI to mini-HDMI cable suitable for connection to a variety of small cameras. There is also a small adapter for mounting the VidiU to a camera shoe or a tripod mount.

The unit itself is a plastic case slightly larger than a deck of cards. On the front is a small OLED display with a couple of buttons. On the left is a sliding power switch (love this, very difficult to accidentally turn off by pushing a button), a USB port for connecting a 3G/4G modem, and a headphone port for monitoring audio. on the rear is a full-size HDMI port, a 1/8" jack for connecting either a microphone or line-level signal, a recessed reset button, the ethernet port, and a standard coaxial power connector for a 6-12V DC input. I did discover that the power plug can come unplugged fairly easily. Fortunately, the unit has a built-in battery, so you don't need to be tethered to power, although I'm told the battery is limited to about an hour of runtime and is best suited for keeping it running while swapping power supplies. When plugged in, the internal battery will charge (there are power and charge indicators just below the ethernet port). When charging, it draws about 10W, and about 3W when operating on a full charge. This means you could conceivably run this unit on solar power without much difficulty. More on that in a future post.

When you first power it up, it will search for a network. When it can't find one that it knows about, the display prompts you to press the Menu button. This little black button (one of only two on the device) is more than meets the eye, and is actually a tiny 4-way joystick in addition to being a button (as is the red start/stop button above it). The setup for connecting to an existing wifi network is fairly intuitive, but due to the limited number of buttons, the process of entering wifi passphrases and URLs for your publishing point is somewhat tedious. The MIMO wifi supports both 2.4Ghz and 5GHz bands.

The easiest way to set up the VidiU is to connect it to the network via a wire (the battery comes in handy here), log into the web interface and do the configuration that way. Getting the DHCP address could be a little tricky, and the recommended process is to use the iPhone app. When I tried the app on my iPad, it gave me the IP address, but most times when I tried to connect via the iPad, the entire web UI crashed on the unit requiring a power cycle. The Android app didn't fare any better on my Samsung Galaxy S4.

The VidiU comes preconfigured to use LiveStream, Youtube Live, UStream, and Twitch, as well as a manual configuration that lets you use any RTMP server such as Wowza Streaming Engine. If you're using Wowza, make sure you set the agent to FMLE, since by default, Wowza rejects publisher user-agent strings that don't look like FMLE.

Once it's configured, streaming with the VidiU is as easy as pushing the start/stop button on the front, although a quick press doesn't do it, you need to hold it for about a second for it to do anything, and if you hold it for too long, it will ask you if you want to turn off the display.

I tried it with a variety of sources, including as a mirrored display on a Mac Mini (great for screencasts), a Roku (which was temperamental at best), and a standard video camera (the easiest of all configurations). Switching HDMI cables while it's streaming is not recommended. Doing so crashed the unit once, and confused it on 2 more occasions requiring a reboot.

The built-in quality presets are as follows:

- Full HD (1920x1080, 5.2Mbps)
- HD (1280x720, 2.2Mbps)
- High (960x540, 1.4Mbps)
- Medium (736x414, 800Kbps)
- Low (480x270, 450Kbps)
- Mobile (360x200, 275Kbps)

If you're unsure about your connection, it has a built-in speed test that can check your bandwidth and make a recommendation based on the results. There is also an adaptive bitrate option which will adjust the settings to match available bandwidth.
