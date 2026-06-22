---
layout: post
title: 'Working with the ArubaOS API: Reading Data'
date: 2021-10-19 16:10:29.000000000 -05:00
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
  _wpas_skip_19898087: '1'
  _wpas_done_all: '1'
  _edit_last: '2'
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
permalink: "/2021/10/19/working-with-the-arubaos-api-reading-data/"
---

Another quick bit today - this is the basic framework for using the [REST API in ArubaOS](https://developer.arubanetworks.com/aruba-aos/docs/getting-started-aos8-restapi). Lots of info at the [Aruba Developer Hub](https://developer.arubanetworks.com/). This is primarily for executing \*\*show\*\* commands and getting the data back in a structured JSON format.
However, be aware that not all \*\*show\*\* commands return structured JSON - some will return something vaguely XMLish, and some will return the regular text output inside a JSON wrapper (originally the \*\*showcommand\*\* API endpoint was just a wrapper for the actual commands and would just return the CLI output, as it still does for several commands)
You can always go to \*\*https://:4343/api\*\* (after logging in) and get a Swagger doc for all the available API calls - although owing to system limitations, the description of those endpoints isn't generally there, but it can be found in the full [AOS8 API reference](https://developer.arubanetworks.com/aruba-aos/reference).
This blog entry does not deal with sending data \*to\* the ArubaOS device.

```

python
#!/usr/bin/python3

import requests
import json
import warnings
import sys
import xmltodict

aosDevice = "1.2.3.4"
username = "admin"
password = "password"
httpsVerify = False

#Set things up

if httpsVerify == False :
	warnings.filterwarnings('ignore', message='Unverified HTTPS request')

baseurl = "https://"+aosDevice+":4343/v1/"

headers = {}
payload = ""
cookies = ""

session=requests.Session()
## Log in and get session token

loginparams = {'username': username, 'password' : password}
response = session.get(baseurl+"api/login", params = loginparams, headers=headers, data=payload, verify = httpsVerify)
jsonData = response.json()['_global_result']

if response.status_code == 200 :

	#print(jsonData['status_str'])
	sessionToken = jsonData['UIDARUBA']

#	print(sessionToken)
else :
	sys.exit("Login Failed")

reqParams = {'UIDARUBA':sessionToken}

def showCmd(command, datatype):
	showParams = {
		'command' : 'show '+command,
		'UIDARUBA':sessionToken
			}
	response = session.get(baseurl+"configuration/showcommand", params = showParams, headers=headers, data=payload, verify = httpsVerify)
	#print(response.url)
	#print(response.text)
	if datatype == 'JSON' :
		#Returns JSON
		returnData=response.json()
	elif datatype == 'XML' :
		# Returns XML as a dict
		print(response.content)
		returnData = xmltodict.parse(response.content)['my_xml_tag3xxx']
	elif datatype == 'Text' :
		# Returns an array
		returnData =response.json()['_data']
	return returnData

print(showCmd('clock', 'Text')[0])

print(json.dumps(showCmd('dds debug peers', 'JSON'),indent=2, sort_keys=False))

## Log out and remove session

response = session.get(baseurl+"api/logout", verify=False)
jsonData = response.json()['_global_result']

if response.status_code == 200 :

	#remove 
	token = jsonData['UIDARUBA']
	del sessionToken
	#print("Logout successful. Token deleted.")
else :
	del sessionToken
	sys.exit("Logout failed:")
```

If you prefer, I have shared a [Postman collection for working with the basics.](https://www.getpostman.com/collections/21a541cccc8f4d24e970)
