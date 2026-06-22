---
layout: post
title: FX160, Deeper look
date: 2008-12-15 12:03:42.000000000 -06:00
type: post
parent_id: '0'
published: true
password: ''
status: publish
categories:
- Hardware
tags:
- dell
- FX160
- thin clients
meta:
  dsq_thread_id: '217877171'
  _googl_shortlink: http://goo.gl/dDWvF
author:
  login: ianbeyer
  email: ian.beyer@gmail.com
  display_name: Ian Beyer
  first_name: Ian
  last_name: Beyer
permalink: "/2008/12/15/fx160-deeper-look/"
---

Now that I've had a chance to play with the FX160 a little more, here are a few things I've discovered:

When the service manual tells you to remove the two screws from the back of the unit and then *"slide* the cover toward the front and lift off", what they really meant to say is "Give the cover a good glancing whack with the palm of your hand toward the front of the unit and then lift it off." The reverse is also true when putting the cover back on. It needs more than mere sliding, it needs a good whack.

Under the cover, we find that Dell has indeed done a great job with this unit.

- Flash interface is SATA and held in place with an actual screw, compared to HP's really lame locking plastic tab that makes it a pain in the butt to swap the module on and off its PATA header pins. SATA FTW.
- There's an additional SATA port on the board, as well as a power connector for said SATA. Dell could make this even better by providing an optional eSATA port on the back (and maybe even go all Apple on us and make a matching eSATA chassis!)
- There's another power header on the board for a CPU fan. I'm guessing this is for the dual-core units.
- Despite its teeny size, this little guy uses standard desktop DIMMs. It came with one of the two slots populated with a 1GB module. The system supports up to 4GB acccording to the technical guidebook, but I've seen elsewhere that it can handle 8GB. Given that the CPU options support EM64T, this is an interesting prospect.
- Mini-PCI slot for wireless. The Technical Guidebook says Dell 1397 only (802.11g), but I've seen other mention of the Dell 1510 card (802.11abg) also being supported.
- Jumper #5. From the factory, this comes unjumpered, locking out BIOS setup. Since the lid can be locked in place with a standard cable lock or even a small padlock, Dell's done a very good job with security.
- Front USB ports (mounted on the board with all die blinkenlights , audio, and the power switch) is connected through a standard 2x5-pin system board connector, as is the audio. If your application requires a USB security key, it should be easy to mount on internally by disconnecting the front USB ports and adding a little pigtail. Props to Dell for designing it this way, rather than a single cable for the entire front panel. Dell could take this a step further by adding an internal USB port on the front panel board for mounting such a key. There's plenty of physical space for it. This would be a huge bonus for POS systems that require these keys.

On the software side:

- I can add and remove programs with... the Add/Remove programs control panel application. What a novel idea. HP, You fail at this. Having Altiris be the only mechanism to add or remove packages is... sub-optimal.
- XPe is still Service Pack 2. Microsoft does have a SP3-based version of XPe out there, and that would be a good thing.
- Administrator account has Start->Run disabled. Booo! Luckily, I can just as easily start up IE and type the command there.
- .NET Framework installed is 2.0, no service pack. In order to install 3.5, I have to install .NET 2.0 SP1 first. There's no real reason these can't ship with .NET 3.5 from the factory.
- I just checked free space on the flash... 60 MB. Yikes! I can see why Dell pushes the 2GB flash option for these. Some of that may be due to the .NET install going on.
- The system ships with a software reload DVD. This is good. I hope Dell will provide frequent OS image updates through their support site. HP does this, and it's a happy thing.
- Altiris agent on the unit isn't playing nice with my existing Altiris Deployment server set up for the HP thins. Hopefully this will be easy to resolve.

Dell support for Altiris: Doesn't exist. They flat out told me they don't handle support and that I need to call Altiris directly. I'm not sure how this is going to go. The process with HP (I've had to explain it to HP support agents enough times) is that the call to Altiris has to originate from HP. This process sucks, but it is what it is. The first thing the folks at AltirisSymantec ask you for is a contract number or customer number. Altiris has already kicked the ball back to Dell. Not looking good so far. Back to Dell support, and they really don't know what the process is.

Definitely would recommend the 2GB flash if you're buying one of these. the OS alone takes up almost 70% of the flash. This is clearly a much more substantial install of XPe than what's on the HP machines.
