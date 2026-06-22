---
layout: post
title: Integrating Controller Data Into Ekahau Surveys
date: 2022-02-23 17:24:51.000000000 -06:00
type: post
parent_id: '0'
published: true
password: ''
status: publish
categories:
- Aruba
- Code
- networking
- Wireless
tags: []
meta:
  _last_editor_used_jetpack: block-editor
  _publicize_twitter_user: "@CaNerdIan"
  _wpas_done_all: '1'
  _thumbnail_id: '1912'
  spay_email: ''
  _wpas_mess: 'On the #blog : How to boost your #WiFi surveys with controller data
    #WLPC #Python '
  _wpas_is_tweetstorm: ''
  _wpas_feature_enabled: '1'
  _edit_last: '2'
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
permalink: "/2022/02/23/integrating-controller-data-into-ekahau-surveys/"
excerpt: 'In which I describe how to enhance your survey data using controller data
  and a little Python. '
image: "/assets/images/2022/02/Estudio-del-Wi-Fi-Ekahau.png"
---

If you've done a few post-install validation surveys with [Ekahau](https://ekahau.com), you've probably run into the dreaded "Measured AP-a1:b6", even if your AP/ESSID were supposed to have AP name broadcast in the beacon (or you just forgot to turn it on before surveying). You have probably also encountered the problem of null SSIDs (aka "hidden" SSIDs). Those aren't really useful in a survey, but when you survey a 10-story building with hundreds of access points, you sure don't want to go through and manually rename each and every AP, or manually add data tags that you looked up in an Excel table.

It may also be handy for your survey to include information that isn't directly available through surveying the beacons, such as the AP's specific model, wired MAC, and serial number, or what AP group it's in.

Fortunately, with a [little bit of Python magic](https://github.com/canerdianeh/ekahau-data/blob/main/Update_APs.py), you can crack open the Ekahau data file and add this information to a survey. With a [little bit more Python magic](https://github.com/canerdianeh/aruba-campus), you can extract this information from your controller's [BSS table](https://github.com/canerdianeh/aruba-campus/blob/main/apbsstable.py) and [AP database](https://github.com/canerdianeh/aruba-campus/blob/main/apdb2csv.py) into a couple of CSV files.(At present, it also requires a little bit of Excel magic to generate the data to update, but I'm working on that).

The scripts linked above (on [my github](https://github.com/canerdianeh)) will pull the data from an Aruba Mobility Conductor, but I am sure that if you use a different vendor (or Aruba Central or Instant), you can get similar data from your controller. The key is to get it into CSV format. One of these days I'll adapt those scripts to Central and Instant.

## How it works

I posted a while back about the [overall structure of the Ekahau data file](https://nerdian.ca/2020/06/08/tag-youre-it/). This script opens up an ekahau data file with surveyed access points, and loads the relevant data into some dictionaries, and does some crazy iteration to update the data and write it back out to a new Ekahau file (so that if we accidentally break it, the original is untouched).

As you recall, Ekahau is using JSON data in a rather unorthodox way to form what would be considered a relational database. The BSSID from a particular measurement is a few layers deep. in the *AccessPointMeasurements.json* file, which is referenced by *MeasuredRadios.json*, which is referenced by *AccessPoints.json*, which contains the actual AP name.

## The Data

The input CSV file contains the following columns - this can be generated from the CSV scripts and some basic Excel lookups.

- From the Controller's BSS Table:
  - BSSID
  - ESSID
  - AP Name
- from the Controller's AP Table (looked up via AP Name):
  - AP Group
  - AP Model
  - AP Serial
  - AP Wired MAC
- Arbitrary:
  - Color (in the form of *Scheme/Name*)

While Ekahau has a predefined and hardcoded set of colors (which are defined in the "Ekahau" scheme in the code) the actual color information for an AP is stored as an RGB Hex value, and is properly rendered in the application, so the sky is the limit)

If you're putting the AP serial/MAC/group in as tags, make sure those tags and their UUIDs have been created within the project first so that *TagKeys.json* exists.

## Running the script

Pretty straightforward: Run the script on the CLI with the following options:

`./Update_APs.py input.csv surveyfile.esx`

What you will get in a minute or so is an updated Ekahau survey file, and now any surveyed BSSIDs that existed in your controller environment will have the correct AP name, AP model, ESSID names (even "hidden" ones), a set of tags with the MAC/Serial/Group, "My" will be selected (and APs not in the database will be deselected - this is great for APs from adjacent buildings on the campus that were seen but not placed on any maps), and optionally will be assigned a custom color.

And you now just did in about 10 minutes what would have taken you a week and copious amounts of coffee to accomplish. Now go get some coffee before you build that report.

(I'd post some screen shots, but at the moment I only have real customer data and can't show it)

Requisite disclaimer: *Data security and integrity is on you. If this blows up your file and you didn't keep a backup of the original somewhere, that's a you problem, and Ekahau probably won't help if you were fiddling with the inner workings of their data file. Don't say I didn't warn you.*

## Credits:

Huge thanks goes to Blake Krone for supplying the core code that iterates through the Ekahau data - it saved me may hours of having to reinvent the wheel and write it myself - although it turned out I was taking a similar approach.

That base code (and many other useful scripts for fiddling with Ekahau data) comes from the [Advanced Ekahau Design & Survey Fundamentals](https://wifiacademy.net/courses/aeds) lab course offered by Blake's [WifiAcademy](https://wifiacademy.net/).

Post image borrowed from [Ekahau](https://www.ekahau.com).
