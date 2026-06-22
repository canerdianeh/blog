---
layout: post
title: Location, Location, Location
date: 2021-08-10 10:03:55.000000000 -05:00
type: post
parent_id: '0'
published: true
password: ''
status: publish
categories:
- Aruba
- Code
- IoT
- Location Tech
- Wireless
tags:
- CWIDP
- CWIIP
- CWISA
- location services
- mapping
- Meridian
- Python
meta:
  _last_editor_used_jetpack: block-editor
  _publicize_twitter_user: "@CaNerdIan"
  _edit_last: '2'
  _wpas_skip_19898087: '1'
  _wpas_done_all: '1'
  _thumbnail_id: '1845'
  _cs_replacements: a:1:{s:7:"sidebar";s:7:"sidebar";}
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
permalink: "/2021/08/10/aruba-meridian-location/"
image: "/assets/images/2021/08/AdobeStock_310180925-scaled.jpeg"
---

It seems fitting that the week in which I became the first to pass the [CWIDP (Certified Wireless IoT Design Professional)](https://www.cwnp.com/certifications/cwidp/) certification would be one where I happened to be onsite doing a BLE location project with [Aruba Meridian](https://www.arubanetworks.com/products/location-services/app-platform/).

While the web based editor is great, it is mildly annoying that one of the things it *can't* do is copy and paste placemarks between floors, which would be really handy when you're deploying an office building that has almost the same layout on every floor. For this, you have to dig into the [Meridian API](https://docs.meridianapps.com/hc/en-us/categories/360002761313-Developers).

By using the API, you can spit out a list of placemarks in JSON (easiest way to do this is in [Postman](https://www.postman.com), with a **GET** to **{{BaseURL}}/locations/{{LocationID}}/placemarks**), grab the JSON objects for the placemarks you wish to copy from the output, update the fields in the JSON for which map ID they need to go on, and any other data, and then make a POST back to the same endpoint with a payload containing the JSON list of objects you want to create. Presto, now you've been able to clone all the placemarks from one floor to another.

*Note that point coordinates are relative to the map image - So cloning from one map to another can bite you in the rear if they're not properly aligned. (If you want to get really clever, You could manually create a placemark on every floor whose sole purpose is to align each floor in code - much like an alignment point in Ekahau, when you generate a placemark list, you can calculate any offsets between them and apply those to coordinates before sending them back to the API. But this trick could (and probably will) be a whole post of its own.*

The structure of a placemark object from a **GET**:

```javascript
       {
            "parent_pane": "",
            "child_pane_ne": "",
            "child_pane_se": "",
            "child_pane_sw": "",
            "child_pane_nw": "",
            "left": -1,
            "top": -1,
            "width": -1,
            "height": -1,
            "next_pane": null,
            "next_id": "XXXXXXXXXXXXXXXXXX",
            "modified": "2021-08-06T22:57:29",
            "created": "2021-08-06T15:28:13",
            "id": "XXXXXXXXXX_XXXXXXXXXX",
            "map": "XXXXXXXXXXXXXXXX",
            "x": 2152.0189227788246,
            "y": 499.59448403469816,
            "latitude": 41.94822,
            "longitude": -87.65552,
            "related_map": "",
            "name": "Pitch Room",
            "area": "2132.722,480.101,2228.177,480.498,2230.003,634.737,2132.412,634.722",
            "hint": null,
            "uid": null,
            "links": [],
            "type": "conference_room",
            "type_category": "Office",
            "type_name": "Conference Room",
            "color": "596c7c",
            "description": null,
            "keywords": null,
            "phone": null,
            "email": null,
            "url": null,
            "custom_1": null,
            "custom_2": null,
            "custom_3": null,
            "custom_4": null,
            "image_url": null,
            "image_layout": "widescreen",
            "is_facility": false,
            "hide_on_map": false,
            "landmark": false,
            "feed": "",
            "deep_link": null,
            "is_disabled": false,
            "category_ids": [
                "XXXXXXXXXXXXXXXX"
            ],
            "categories": [
                {
                    "id": "XXXXXXXXXXXXXXXX",
                    "name": "Conference Room"
                }
            ]
        }
```

However, when creating a new placemark, you don't need all these fields... The only objects that are absolutely *required* are **map**, **type**, **x**, and **y** (I haven't tried sending an **id** along with a POST, so I don't know if it will ignore it or reject it.) I've used Postman variables here for **map** and **name**, because then I could just change those in the environment variables and resubmit to put on multiple floors. The best part about the **POST** method is that the payload doesn't just have to be a single JSON object, it can be a list of them, by simply putting multiple objects inside a list using square brackets.

```javascript
{
            "map": "{{ActiveMapID}}",
            "x": 2152.0189227788246,
            "y": 499.59448403469816,
            "latitude": 41.94822,
            "longitude": -87.65552,
            "related_map": "",
            "name": "{{ActiveFloor}} Pitch Room",
            "area": "2132.722,480.101,2228.177,480.498,2230.003,634.737,2132.412,634.722",
            "hint": null,
            "uid": null,
            "links": [],
            "type": "conference_room",
            "type_category": "Office",
            "type_name": "Conference Room",
            "color": "596c7c",
            "description": null,
            "keywords": null,
            "phone": null,
            "email": null,
            "url": null,
            "custom_1": null,
            "custom_2": null,
            "custom_3": null,
            "custom_4": null,
            "image_url": null,
            "image_layout": "widescreen",
            "is_facility": false,
            "hide_on_map": false,
            "landmark": false,
            "feed": "",
            "deep_link": null,
            "is_disabled": false,
            "category_ids": [
                "5095323364098048"
            ],
            "categories": [
                {
                    "id": "5095323364098048",
                    "name": "Conference Room"
                }
            ]
        }
```

And if you want to update an *existing* placemark, simply make a **PATCH** call to the API with the existing placemark's ID, and whatever fields you wish to update. Like with the **POST** call, you can send a payload that is a list of objects This is a great way to batch update URLS or names.

It may also come in handy to generate a list of all the placemarks at a given location. So I threw together a handy little python script that will spit it out into a CSV (and will also look up the map ID and get the floor number for easy reference).

```python
#!/usr/bin/python3

# Aruba Meridian Placemark Export to CSV
# (c) 2021 Ian Beyer
# This code is not endorsed or supported by HPE

import json
import requests
import csv
import sys

auth_token = 'Please Insert Another Token to continue playing'
location_id = 'XXXXXXXXXXXXXXXX'

baseurl = 'https://edit.meridianapps.com/api/locations/'+location_id

header_base = {'Authorization': 'Token '+auth_token}

def api_get(endpoint,headers,payload):
	response = requests.request("GET", baseurl+endpoint, headers=headers, data=payload)
	resp_json = json.loads(response.text)
	return(resp_json)

#File name argument #1
try:
	fileName = str(sys.argv[1])
except:
	print("Exception: Enter file to use")
	exit()

maps={}

for floor in api_get('/maps',header_base,{})['results']:
	maps[floor['id']] = floor['name']

beacons=[]

# Iterate by floor for easy grouping - 
for flr in maps.keys():
	bcnlist=api_get('/beacons?map='+flr,header_base,{})
	# NOTE: If bcnlist['next'] is not null, then there are additional pages - this doesn't process those yet. 
	for bcn in bcnlist['results']:
		# Add floor name column for easier reading. 
		bcn['floor']=maps[bcn['map']]
		beacons.append(bcn)

data_file = open(fileName, 'w')
csv_writer = csv.writer(data_file)
count = 0

csv_fields = beacons[0].keys()

print(csv_fields)

csv_writer.writerow(csv_fields)

#print(placemarks)
for bcn in beacons:
	data=[]
	for col in csv_fields:
		data.append(bcn[col])
	# Writing data of CSV file
	csv_writer.writerow(data)
	count += 1
data_file.close()

print ("Exported "+str(count)+" beacons. ")
```

Once you have this list in a handy spreadsheet form, then you can make quick and easy edits, and then [run the process the other way](https://nerdian.ca/2021/08/11/meridian-api-part-2/).

[*Scripts on this page can also be found on github.*](https://github.com/canerdianeh/aruba-meridian)
