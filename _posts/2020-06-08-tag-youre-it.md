---
layout: post
title: Tag, You're It!
date: 2020-06-08 12:43:01.000000000 -05:00
type: post
parent_id: '0'
published: true
password: ''
status: publish
categories:
- Code
- networking
- Wireless
tags:
- APIs
- automation
- Ekahau
meta:
  _publicize_twitter_user: "@CaNerdIan"
  _edit_last: '2'
  _cs_replacements: a:1:{s:7:"sidebar";s:7:"sidebar";}
  _thumbnail_id: '1700'
  _wpas_skip_19898087: '1'
  _wpas_done_all: '1'
  _bpp_element: body
  _bpp_repeat-x: 'yes'
  _bpp_repeat-y: 'yes'
  _bpp_attachment: scroll
  _bpp_position: center
  _bpp_fade: 'yes'
  _bpp_fade_height: '100'
  _bpp_color: "#"
  _last_editor_used_jetpack: block-editor
author:
  login: ianbeyer
  email: ian.beyer@gmail.com
  display_name: Ian Beyer
  first_name: Ian
  last_name: Beyer
permalink: "/2020/06/08/tag-youre-it/"
image: "/assets/images/2020/06/unmasked.jpg"
---

*Cover Image:* [Unmasked](https://brianwallfineart.com/portfolio/unmasked/) *(detail), ([Brian Wall](https://brianwallfineart.com/), 2014)*

Just this past week, Ekahau released the latest iteration of their excellent wireless network planning software, and with this version, they've [added a few features](https://sw.ekahau.com/download/ess/Release%20Notes.html) that many of us have been wanting for quite some time. Of course, we always want more, and there's only so much the elves at Ekahau can do! So this leaves us with building our own tools to extract the data we need out of the project file. (Hey, Ekahau, you know what would be really awesome? an SDK for doing this!)

Fortunately, Ekahau has been really good about building a standards-based project file format (and not encrypting it or doing things that make it a pain to use your own data). Since the Ekahau software is built in Java (cross platform on Windows/Mac!), it's logical for the data file to be in something like XML or JSON, and they have chosen the latter, and have effectively built a relational database in JSON, and bundled the whole thing up into a convenient zip file. It's almost like they understand that their core market is made up almost entirely of customers who like to tinker with things.

![]({{site.baseurl}}/assets/2020/06/Screen-Shot-2020-06-08-at-1.21.41-PM-1024x580.png)

***Disclaimers:***

Naturally, manipulating this file is something to be done entirely at your own risk, and if you break it, don't go crying to Ekahau, because they don't support mucking with their data file outside of their application (nor should they be expected to!) Make sure you have backups, etc, etc.

Also, this post is in no way based on any inside information from Ekahau, nor is it anything official from them - this is simply an analysis of the contents of the project file that anyone could do, whose nature as a zipped file full of JSON has been known for quite some time.

## "I'm gonna get some tags... This is f'ing awesome"

Probably the coolest new feature in v 10.2 is the ability to add key:value tags to stuff. You can apply these tags to APs, either just the tag by itself, or a tag with a value associated with it. The Quick Select also lets you select any APs that have a particular tag key (although somehow they missed the ability to refine based on tag value, which I hope will be corrected in the near future).

Why is this useful? This allows you to add free-form information to access points, whether simulated or measured, that allows Ekahau to be more than just an RF simulation tool, and extends it into a full blown planning and deployment tool. Tagged information can be any kind of metadata you wish. things like:

- Mounting hardware
- Wired MAC address
- AP Group
- Serial Number
- Zone
- Switch
- Port
- Cable
- IDF
- ... and the list is nearly endless.

This is in addition to the already rich metadata that is associated with the AP that are directly relevant to the RF modeling, such as mounting height, mounting surface, antenna angles, power, channel, antenna types, and so forth.

So how does it work? Pretty simple: on an AP, simply open the sushi menu at the top right, select "Tag AP". You can also do this from the Edit AP or bulk edit screen when doing multiple APs. This will give you a list of existing tag keys already associated with the project (as well as tags you've used before on other projects), along with a free form box to enter your own, or add a value.

As of right now, there's not a whole lot you can do within the Ekahau software once you have those tags (I would LOVE a table view of my APs and all the metadata, as well as ability to import/export to CSV or Excel), nor is template-based reporting on those tags documented at this point (although I expect they're working diligently to document this). One key weakness of the template reporting system is that it all has to go through Microsoft Word (with a whole bunch of limitations imposed by that format), and that gets really hairy once you start creating data tables, especially if you want them in Excel or something else.

*Side note: Using Excel as a database is really a terrible use of a spreadsheet, but it happens all. the. time.*

Which brings me to manipulating/extracting your data by building your own tools. Several people have been doing this unofficially for years, but Ekahau doesn't offer anything for this... yet.

I mentioned earlier that Ekahau's data is stored mostly in JSON, which makes it really easy to work with using Python (or, for that matter, Java or perl if you're into self-flagellation). Every object in the data file has an ID that ties it back to other objects. And that's the key thing (literally). There are about 2 dozen separate files that track various data, and that's how they all tie together. Notes and tag keys are each kept in their own file, while the AP data file has a data object that contains a list of the note IDs, and another that keeps a list of tag IDs and the value associated with that tag:

accessPoints.json:

```

{
   "accessPoints": [
     {
       "location": {
         "floorPlanId": "b799747a-e2ed-49ad-8c5e-c9ea8c36fa61",
         "coord": {
           "x": 2475.397796817626,
           "y": 1537.8008975928194
         }
       },
       "name": "Simulated AP-1",
       "mine": true,
       "userDefinedPosition": false,
       "noteIds": [
         "37faa8ef-c5c8-4d9d-a882-916db175b935",
         "663419b4-ddb4-4ddb-b3f2-d50233743c5c"
       ],
       "vendor": "Aruba",
       "model": "AP-515",
       "tags": [
         {
           "tagKeyId": "59650f76-3e4b-4c40-b78b-2d0088f5b227",
           "value": "123456789"
         },
         {
           "tagKeyId": "5c9cb127-8ba2-4a60-84e5-75f47ce87f99",
           "value": "C-Suite"
         },
         {
           "tagKeyId": "991b12b7-dbb0-47de-9cd2-260ee064b3e3",
           "value": "aa:bb:cc:dd:ee:ff"
         }
       ],
       "id": "a0b90f2a-8b1b-4339-8362-dc51122931ed",
       "status": "CREATED"
     }
   ]
 }
```

tagKeys.json:

```

{
  "tagKeys": [
    {
      "key": "Serial",
      "id": "59650f76-3e4b-4c40-b78b-2d0088f5b227",
      "status": "CREATED"
    },
    {
      "key": "AP Group",
      "id": "5c9cb127-8ba2-4a60-84e5-75f47ce87f99",
      "status": "CREATED"
    },
    {
      "key": "MAC",
      "id": "991b12b7-dbb0-47de-9cd2-260ee064b3e3",
      "status": "CREATED"
    }
  ]
}
```

notes.json:

```

{
  "notes": [
    {
      "text": "This is another test note",
      "history": {
        "createdAt": "2020-06-08T16:25:11.868Z",
        "createdBy": "Ian Beyer"
      },
      "imageIds": [],
      "id": "663419b4-ddb4-4ddb-b3f2-d50233743c5c",
      "status": "CREATED"
    },
    {
      "text": "This is a test note",
      "history": {
        "createdAt": "2020-06-08T16:25:04.883Z",
        "createdBy": "Ian Beyer"
      },
      "imageIds": [],
      "id": "37faa8ef-c5c8-4d9d-a882-916db175b935",
      "status": "CREATED"
    }
  ]
}
```

simulatedRadios.json:

```

{
  "simulatedRadios": [
    {
      "accessPointId": "a0b90f2a-8b1b-4339-8362-dc51122931ed",
      "accessPointIndex": 2,
      "transmitPower": 0.0,
      "antennaTypeId": "bdf0702a-42be-456a-8891-4cf54940a5c2",
      "antennaDirection": 0.0,
      "antennaTilt": 0.0,
      "antennaHeight": 2.4,
      "antennaMounting": "CEILING",
      "radioTechnology": "BLUETOOTH",
      "spatialStreamCount": 1,
      "shortGuardInterval": false,
      "defaultAntennas": [
        {
          "radioTechnology": "BLUETOOTH",
          "frequencyBand": "TWO",
          "antennaTypeId": "bdf0702a-42be-456a-8891-4cf54940a5c2"
        }
      ],
      "enabled": true,
      "id": "c4f3c521-873c-40de-8076-b1f02b655993",
      "status": "CREATED"
    },
    {
      "accessPointId": "a0b90f2a-8b1b-4339-8362-dc51122931ed",
      "accessPointIndex": 0,
      "transmitPower": 8.000293592441343,
      "channel": [
        1
      ],
      "antennaTypeId": "785280d6-168c-4eab-9819-88e6010e2bef",
      "antennaDirection": 0.0,
      "antennaTilt": 0.0,
      "antennaHeight": 2.4,
      "antennaMounting": "CEILING",
      "technology": "AX",
      "radioTechnology": "IEEE802_11",
      "spatialStreamCount": 2,
      "shortGuardInterval": true,
      "greenfield": false,
      "defaultAntennas": [
        {
          "radioTechnology": "IEEE802_11",
          "frequencyBand": "TWO",
          "antennaTypeId": "785280d6-168c-4eab-9819-88e6010e2bef"
        },
        {
          "radioTechnology": "IEEE802_11",
          "frequencyBand": "FIVE",
          "antennaTypeId": "4ef1637e-06e5-415a-96fd-a97a82273242"
        }
      ],
      "enabled": true,
      "id": "bb7304d1-d564-4018-aa92-e6ca52cba37b",
      "status": "CREATED"
    },
    {
      "accessPointId": "a0b90f2a-8b1b-4339-8362-dc51122931ed",
      "accessPointIndex": 1,
      "transmitPower": 13.979400086720377,
      "channel": [
        36
      ],
      "antennaTypeId": "4ef1637e-06e5-415a-96fd-a97a82273242",
      "antennaDirection": 0.0,
      "antennaTilt": 0.0,
      "antennaHeight": 2.4,
      "antennaMounting": "CEILING",
      "technology": "AX",
      "radioTechnology": "IEEE802_11",
      "spatialStreamCount": 4,
      "shortGuardInterval": true,
      "greenfield": false,
      "defaultAntennas": [
        {
          "radioTechnology": "IEEE802_11",
          "frequencyBand": "TWO",
          "antennaTypeId": "785280d6-168c-4eab-9819-88e6010e2bef"
        },
        {
          "radioTechnology": "IEEE802_11",
          "frequencyBand": "FIVE",
          "antennaTypeId": "4ef1637e-06e5-415a-96fd-a97a82273242"
        }
      ],
      "enabled": true,
      "id": "4ab4a7e1-708d-4f18-b33e-d8891a808e9f",
      "status": "CREATED"
    }
  ]
}
```

One thing you can do with **simulatedRadios.json** is go through and adjust your antenna orientations to the nearest 5 or 15 degree increments - having decimal granularity in the antenna orientation isn't really useful unless you're doing some very long point to point shots, and it will make the maps look cleaner when your antenna is at 90° instead of 88.6367879° because you manually rotated it by dragging it with the mouse.

I'm also going to omit the antennaTypes.json here, but it's worth noting that if you have any custom APs/Antennas in your Ekahau setup, that data is included in your project file for portability, and you don't need that custom config replicated on the next machine that opens up this file, and aren't limited to the APs and antennas that Ekahau offers by default (although it would be really nice if they made it easy to add custom APs/antennas that survived a code update)

![]({{site.baseurl}}/assets/2020/06/Screen-Shot-2020-06-08-at-1.29.29-PM-917x1024.png)

So here's the basic process to report on your tags and notes:

1. bring in the list of access points from accessPoints.json. This will get you a list of notes, as well as the tag key IDs, along with that tag's values.
2. You'll need to then cross-reference the tag key IDs from **tagKeys.json** to get the key values (this approach seems a little convoluted at first, but ensures that a key value can be consistent from one file to the next based on not merely the text in the key value, which will come in to play when merging multiple data files into one. Ekahau was very smart about designing it this way.)
3. Extract any notes from **notes.json**.
4. Cross-reference any additional radio-specific data you need (including orientation) by looking for the access point ID in **simulatedRadios.json**
5. Cross-reference any antenna pattern data by looking for the access point ID in **antennaTypes.json**.
6. information such as floor number lurks in **buildingFloors.json** and **buildings.json**.
7. and so forth.

Hopefully you're starting to get the general idea of how this data is put together. It should be a fairly straightforward matter of running a little code against the data file and being able to generate not only a drop list for your installation contractor, but also a big chunk of your configuration script for deploying against your wireless controller. If you're feeling especially adventurous and saucy, you can even use your wireless system's API for this and be able to orchestrate a large chunk of your configuration from within Ekahau.

Once I build some actual code, I'll be sure to share it here.

Here is the big gnarly mind map of the Ekahau data file. It's probably still very much incomplete and I don't promise 100% accuracy of data types, but it gives a good visual reference of how the whole thing goes together:

[![]({{site.baseurl}}/assets/2020/06/EkahauFileStructure-2500-496x1024.png)](http://nerdian.ca/files/2020/06/EkahauFileStructure.png)

Resolution got smashed by Wordpress, so you can check out the [full resolution version](http://nerdian.ca/files/2020/06/EkahauFileStructure.png), or a [PDF version](http://nerdian.ca/files/2020/06/EkahauFileStructure.pdf).
