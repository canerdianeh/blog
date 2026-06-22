---
layout: post
title: Controlling Audio With ProPresenter
date: 2016-11-20 14:17:46.000000000 -06:00
type: post
parent_id: '0'
published: true
password: ''
status: publish
categories:
- Church IT
- Hardware
- Misc
tags:
- MIDI
- ProPresenter
- Tech Arts
meta:
  _edit_last: '2'
  _thumbnail_id: '1396'
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
permalink: "/2016/11/20/controlling-audio-with-propresenter/"
image: "https://nerdian.ca/files/2016/11/ProQu24.png"
---

Our church is a small one. So its not always especially easy to fully staff our tech booth, and sometimes, one must fly solo, which adds to the workload, and sometimes stuff gets forgotten, like unmuting microphones for the choir or the person reading the scripture.

Fortunately, there is some tech than can help us in this regard. We use [ProPresenter](http://www.renewedvision.com/propresenter.php) for our graphics presentation, and an [Allen & Heath QU-24 console](http://www.allen-heath.com/ahproducts/qu-24/) for our audio. The Qu-24 is connected to the Mac that runs ProPresenter via a USB cable, which shows up in the Mac as a 32 in/32 out audio device, as well as a [MIDI](https://en.wikipedia.org/wiki/MIDI) device. This is primarily to be able to use the console as a multitrack and DAW interface, but it also lets us play back audio from ProPresenter media cues without ever leaving the digital domain, and saving us a couple of inputs on the board (although there's no shortage of those). But because it's also a MIDI device, this gives us some options with ProPresenter's $99 MIDI module add-on. The Qu series boards can also do MIDI over IP (in fact, the Qu-Pad remote control app for iPad uses MIDI over IP to work its magic). If you're using MIDI over IP with a Mac, you'll need a special driver for the Mac. No driver is needed for USB.

First, a few resources we'll need:

- Allen & Heath's [Qu Mixer MIDI Protocol Reference](http://www.allen-heath.com/media/Qu-MIDI-Protocol-V1.82.pdf)
- Snoize [MIDI Monitor](https://www.snoize.com/MIDIMonitor/) (Open-Source)
- The [MIDI Module](https://www.renewedvision.com/store.php?item=midi) for ProPresenter ($99 but can be used in watermarked demo mode at no cost)

In the Qu Series, mutes and mute groups are controlled by a sequence of a Note On/Off message. The specific note determines the channel or mute group being controlled, and a the velocity value determines if it's being turned on (Muted) or off (Unmuted). Velocity values below 64 turn the mute off, and above turn it on.

Meanwhile, over in ProPresenter, since Version 6, we have the ability to add MIDI Note On/Off cues to a slide. See where this is going? Unfortunately, ProPresenter doesn't have the ability to do anything other than MIDI notes in a slide at the moment, so we can't get really crazy with starting recordings or anything else requiring non-note MIDI messages.

So how do we know what notes emulate button presses? The documentation provides this handy method:

![]({{site.baseurl}}/assets/2016/11/Screenshot-2016-11-20-13.28.35-300x177.png)

OK, this requires thinking and math. Not so helpful. This is where the MIDI monitor comes in. Download it and run it, and it shows everything coming across the MIDI interface. Push the button you're interested in, and lo, MIDI Monitor helpfully shows you what note you're interested in:

![]({{site.baseurl}}/assets/2016/11/Screen-Shot-2016-11-20-at-12.39.50-PM-300x236.png)

In this case, G#4 is the mute group for our choir. A4 is the mute group for the speaking mics on the chancel. A1 is the lectern mic.

![Screenshot 2016-11-20 13.51.30]({{site.baseurl}}/assets/2016/11/Screenshot-2016-11-20-13.51.30-300x204.png)So now, to be able to add a cue at the beginning of a song the choir is singing, I simply have to add two cues to the first slide to turn on the choir microphones:

- NOTE ON, G#4(80), 63
- NOTE OFF, G#4(80)

Then I can add a slide at the end of the playlist entry that then turns them back off, or add these to the beginning of the next playlist entry:

- NOTE ON, G#4(80), 127
- NOTE OFF, G#4(80)

Likewise, when someone is at the lectern reading scripture, I can unmute that channel automatically using the corresponding note number, and mute them again when they're done.

On the flip side, you can also use note on/off commands to control ProPresenter. So you \*could\* also use the Mute, SEL, and PAFL buttons on unused channels to trigger things in ProPresenter (you also want to make sure that you don't overlap these with the mutes and mute groups that you are actively using so as not to inadvertently advance a slide when hurriedly muting a channel). ProPresenter also conveniently tells you what the last note sent was, so you can actively push the button you want to use, make a note of its number, and put it in the action you wish.

![]({{site.baseurl}}/assets/2016/11/Screen-Shot-2016-11-20-at-12.43.10-PM.png)

Another approach you can take is to create a presentation in ProPresenter containing blank slides with the various functions you wish to use. Then you can copy these slides into presentations and add a Go To Next timer to them to automatically advance to the next slide. I would also recommend using slide labels and colors to clearly identify what each slide is doing:

[![Screenshot 2016-11-20 13.47.55]({{site.baseurl}}/assets/2016/11/Screenshot-2016-11-20-13.47.55-300x198.png)](http://blog.ianbeyer.com/files/2016/11/Screenshot-2016-11-20-13.47.55.png)

If you have controllable lighting and your lighting console also has MIDI capability, This comes in handy as well. And if you're *really* a one-man band, and like to do things like pads underneath certain worship elements, you can use this to trigger those as well. But if you get to that point, you may want to look into [QLab](https://figure53.com/qlab) to control all of them at the same time.

So there you have it: a quick and easy way to automate some of your workload with the Qu series boards. If you've got another board that you use, let me know in the comments if you do (or would like to do) something like this. Would also love to hear if anyone is using hardware MIDI controllers like the [Novation LaunchPad](https://global.novationmusic.com/launch/launchpad#) and how you have it set up.

Additional Info:

[Summary of MIDI Messages](https://www.midi.org/specifications/item/table-1-summary-of-midi-message) (midi.org)
