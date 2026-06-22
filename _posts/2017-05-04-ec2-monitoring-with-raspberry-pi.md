---
layout: post
title: EC2 Monitoring with Raspberry Pi
date: 2017-05-04 10:56:16.000000000 -05:00
type: post
parent_id: '0'
published: true
password: ''
status: publish
categories:
- Cloud Computing
- Code
- Hardware
- nerd
- networking
tags:
- AWS
- ec2
- Monitoring
- Python
- Raspberry Pi
meta:
  _edit_last: '2'
  _syntaxhighlighter_encoded: '1'
  _thumbnail_id: '1463'
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
permalink: "/2017/05/04/ec2-monitoring-with-raspberry-pi/"
image: "/assets/images/2017/05/1200px-Mission_control_center.jpg"
---

I've been doing a little Raspberry Pi hacking lately, and put together a neat way to have physical status LEDs on your desk for things like EC2 instances.

### The Hardware

In its most basic form, you can simply hook up an LED and a bias resistor between a ground line and a GPIO line on the Pi, but that doesn't scale especially well - You can run out of GPIO lines pretty quickly, especially if you're doing different colors for each status. Plus, it's not overly elegant.

The solution? Unicorns!

No, really. The fine folks at [Pimoroni](http://pimoroni.com) in Sheffield, UK have made a lovely little HAT device for the Pi called a Unicorn. Its primary purpose is lots of blinky lights to make pretty rainbows and stuff, hence the name. However, this HAT is a 4x8 (or an 8x8) array of RGB LEDs, addressable via the I2C bus, which doesn't eat up a line per LED (good thing, otherwise it would require 96 analog lines). The **unicornhat** library (python3-unicornhat) is available for Python 2 and Python 3 in the Raspbian repo. When installed onto the Pi, the Unicorn will fit within a standard Raspberry Pi case.

### The Code

This is my first foray into Python, so there was a bit of a learning curve. If you're familiar with object-oriented code concepts, this should be easy for you. Python is much more parsimonious with punctuation than PHP or perl are.

For accessing the EC2 data, we'll need Amazon's **boto3** library, also available in the Raspbian repo (python3-boto). One area where boto3 is really nice is that the data is returned directly as a *dict* object (what users of other languages would call an array), so you don't have to mess with converting JSON or XML into an object structure, and it can be manipulated as you would any other associative array (or a hash for you old-timers that use perl). AWS returns a fairly complex object, so you kind of have to dig into it via a few iterative loops to extract the data you're after.

From there, it's a matter of assigning different RGB values to the states. I chose these ones:

- stopped: red
- pending: green
- running: blue
- stopping: yellow(ish)

I also discovered that I needed to assign a specific pixel to each instance ID, otherwise they tended to move around a bit depending on what order AWS returned them on a particular request.

Here's what the second iteration looks like in action:

[code lang="python"]  
import boto3 as aws  
import unicornhat as unicorn  
import time

# Initialize the Unicorn  
unicorn.clear()  
unicorn.show()  
unicorn.brightness(0.5)

# Create an EC2 object  
ec2 = aws.client('ec2')

# Define colors and positions  
color = {}  
color['stopped']={'red':255,'green':0,'blue':0}  
color['pending']={'red':64,'green':255,'blue':0}  
color['running']={'red':32,'green':32,'blue':255}  
color['stopping']={'red':192,'green':128,'blue':32}

pixel = {}  
pixel['i-0fa4ea2560aa17ffd']={'x':0,'y':0}  
pixel['i-06b95cd864acb1a8c']={'x':0,'y':1}  
pixel['i-0661da0f50ffb604c']={'x':0,'y':2}  
pixel['i-063ec151e0f44ef9b']={'x':0,'y':3}  
pixel['i-02c514ca567d8a033']={'x':0,'y':4}

# Loop until forever  
while True:

response = ec2.describe\_instances()

statetable = {}  
resarray = response['Reservations']  
for res in resarray:  
instarray = res['Instances']  
for inst in instarray:  
iid = inst['InstanceId']  
state = inst['State']['Name']  
# print(iid)  
# print(state)  
statetable[iid] = state

for ec2inst in statetable:  
x = pixel[ec2inst]['x']  
y = pixel[ec2inst]['y']  
r = color[statetable[ec2inst]]['red']  
g = color[statetable[ec2inst]]['green']  
b = color[statetable[ec2inst]]['blue']  
# print(x,y,r,g,b)

unicorn.set\_pixel(x,y,r,g,b)  
unicorn.show()

time.sleep(1)  
[/code]

For the moment, this is just monitoring EC2 status, but I'm going to be adding checks in the near future to do things like ping tests, HTTP checks, etc. Stay tuned.
