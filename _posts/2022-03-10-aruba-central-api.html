---
layout: post
title: Working With the Aruba Central API
date: 2022-03-10 11:07:47.000000000 -06:00
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
permalink: "/2022/03/10/aruba-central-api/"
image: "https://nerdian.ca/files/2022/03/Screen-Shot-2022-03-10-at-10.04.25.png"
---

Yep. Another post about code. No, I'm not a software developer, I'm just a lazy network engineer who has an allergic reaction to doing GUI-based management of large environments. And thus I code because that's a growing part of being a network engineer in the 2022.

A recent client project involving deploying a large fleet of Remote Access Points for teleworkers has required me to look at the [Aruba Central API](https://developer.arubanetworks.com/aruba-central/docs) as a way of simplifying and streamlining the deployment of these APs to ensure consistency and completeness of the deployment. If you're going to do anything more than about 5 times, it's worth trying to automate it. If you're going to do it 5000 times, you *should* automate it. I'm starting to get the hang of the [AOS8 API](https://developer.arubanetworks.com/aruba-aos/docs) and its many quirks, but Central is much more API-first than AOS8 which uses the API primarily as a frontend to the CLI.

If you have a remote workforce that depends on secure connections back to the corporate network, you should definitely check out the [Aruba RAP solution](https://blogs.arubanetworks.com/solutions/aruba-remote-access-points-experience-the-smart-workspace/). It beats the pants off software VPN clients (and at this point, how many teleworkers are even still wearing pants?). This solution has been available since almost the very beginning of Aruba nearly 2 decades ago and is mature and robust.

Like all of Aruba's platforms, Central has a REST API that allows automation. The web frontend is essentially leveraging this API to work its magic. [Aaron Scott](https://wifidownunder.com), an Aruba CSE in Australia, has even built [his own frontend to Aruba Central](https://central.wifidownunder.com/dashboard.html), because you can do that sort of thing when you have an API.

## It's got Swagger!

The Central API, like most, is documented with [Swagger](https://swagger.io/) which allows you to browse and try various API calls to see how they behave.

I won't rehash how to get access to it here, because Aruba documents the process very well in the Developer Hub page:

- [Getting Started](https://developer.arubanetworks.com/aruba-central/docs/api-getting-started)
- [Creating the Application and Token](https://developer.arubanetworks.com/aruba-central/docs/api-gateway-creating-application-token)
- [Obtaining Access Tokens](https://developer.arubanetworks.com/aruba-central/docs/api-gateway-obtaining-access-tokens)
- [Using Swagger make API calls](https://developer.arubanetworks.com/aruba-central/docs/api-swagger-documentation)

Note: once you've generated your token, make sure you download it by clicking "Download Token". It will open a new window containing the JSON text with the actual token in it. Save this to a text file which you can use with your scripts later. Note the expiration time on this: **7200 seconds**. This token is*only good for two hours**.*** You will need to use the refresh token in there to keep it alive past the 2 hour window. The refresh token is good for **15 days**. How? It's in the docs listed above (yeah, I just dropped an RTFM on you!)

[![]({{site.baseurl}}/assets/2022/03/Screen-Shot-2022-03-10-at-10.04.25-1024x504.png)](https://nerdian.ca/files/2022/03/Screen-Shot-2022-03-10-at-10.04.25.png)

## Programming with the API

##### *(and a gratuitous plug for the Aruba Developer Hub)*

If you want to access the API programmatically, you'll want to use Python, although anything capable of making HTTP calls and processing JSON responses will work. Fortunately, Aruba has provided a Python library (again, on the [Aruba Developer Hub](http://devhub.arubanetworks.com/home) - this site has a wealth of great stuff).

The [documentation on how to install the Python libraries](https://developer.arubanetworks.com/aruba-central/docs/python-using-api-sdk) can be found on the Developer Hub. At some point, you'll likely be referred to the [documentation for the library on Read The Docs](https://pycentral.readthedocs.io/en/latest/index.html). This documentation is broadly good, but in some places omits a few key points. Most notably, any time you need to send data to the API in a POST call, it's not immediately apparent that body data needs to go into the **apiData** parameter.

Plenty of examples on the Dev Hub, and what you do will depend on your workflow and what you're trying to accomplish. It may be helpful to draw yourself a mind map of what steps are needed to perform a task, and then map out what API calls and Python classes are required to make them, as well as what input data it depends on. Practice good code hygiene and don't ever put your tokens in your code lest you accidentally share it to the world when you share your code (this is partly why the tokens on Aruba Central are only good for 2 hours!). Instead refer to the token file I suggested you download earlier (which you can do simply by opening the file and doing a **json.load** to import the contents into a dict.)

It's also worth noting that the Aruba Central API does not provide you with any access to the Aruba Activate provisioning system (this is a bit of an annoyance to me, but out of my control). This has recently been given a major overhaul and has been migrated to the [HPE GreenLake Platform](https://www.hpe.com/us/en/greenlake.html) and is now under the GreenLake device management function. There is an API for many GreenLake functions (see also: the [HPE Developer Hub](https://developer.hpe.com/)), but from what I understand, the platform is presently still migrating the API. I'll update the post as soon as it's available. (and did you know that if you have HPE servers, the [ILO management subsystem also has a REST API](https://developer.hpe.com/platform/ilo-restful-api/home/)? API ALL THE THINGS!)
