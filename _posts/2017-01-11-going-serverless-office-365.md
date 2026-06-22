---
layout: post
title: 'Going Serverless: Office 365'
date: 2017-01-11 14:02:43.000000000 -06:00
type: post
parent_id: '0'
published: true
password: ''
status: publish
categories:
- Church IT
- Cloud Computing
- IT
tags:
- Office 365
- sharepoint
- ubiquiti
- Windows
- wireless
meta:
  _edit_last: '2'
  _thumbnail_id: '1404'
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
permalink: "/2017/01/11/going-serverless-office-365/"
image: "/assets/images/2017/01/Products_ContentManagement.jpg"
---

Recently I just completed a project for a small church in Kansas. Several months ago, the senior pastor asked me for a quote on a Windows server to provide authentication as well as file and print share services. During the conversation, a few things became clear:

1. Their desktop infrastructure was completely on Windows 10. Files were being kept locally or in a shared OneDrive account.
2. The budget they had for this project was not going to allow for a proper server infrastructure with data protection, etc.
3. This church already uses a web-based Church Management System, so they're somewhat used to "the cloud" already as part of their workflows.

One of the key features provided by Windows 10 was the ability to use [Office 365](//Office365.com) as a login to your desktop (Windows 8 allowed it against a Microsoft Live account). Another is that for churches and other nonprofits, Office 365 is free of charge for the E2 plan.

I set about seeing how we could go completely serverless and provide access not only to the staff for shared documents, but also give access to key volunteer teams and church committees.

The first step was to make sure everybody was on Windows 10 Pro (we found a couple of machines running Windows 10 Home). [Tech Soup](http://www.techsoup.org) gave us inexpensive access to licenses to get everyone up to Pro.

Then we needed to make sure the internet connection and internal networking at the site was sufficient to take their data to the cloud. We bumped up the internet speed and overhauled the internal network, replacing a couple of consumer-grade unmanaged switches and access points with a [Ubiquiti UniFi](https://www.ubnt.com/enterprise/) solution for the firewall/router, network switch, and access points. This allows me and key church staff to remotely manage the network, as the UniFi controller operated on an [Amazon Web Services](//aws.amazon.com) EC2 instance (t2.micro). This new network also gave the church the ability to offer guest wifi access without compromising their office systems.

The next step was to join everyone to the Azure domain provided by Office 365. At this point, all e-mail was still on Google Apps, until we made the cutover.

Once we had login authentication in place, I set about building the file sharing infrastructure. OneDrive seemed to be the obvious solution, as they were already using a shared OneDrive For Business account.

One of OneDrive's biggest challenges is that, like FedEx, it is actually several different products trying to behave as a single, seamless product. At this, OneDrive still misses the mark. The OneDrive brand consists of the following:

- OneDrive Personal
- OneDrive for Business
- OneDrive for Business in Office 365 (a product formerly known as Groove)
- Sharepoint Online

All the OneDrive for Business stuff is Sharepoint/Groove under the hood. If you're not on Office 2016, you'll want to make the upgrade, because getting the right ODB client in previous versions of Office is a nightmare. Once you get it sorted, it generally works. If you've got to pay full price for O365, I would recommend DropBox for Business as an alternative. But it's hard to beat the price of Office 365 when you're a small business.

It is very important to understand some of the limitations of OneDrive for Business versus other products like DropBox for Business. Your "personal" OneDrive for Business files can be shared with others by sending them a link, and they can download the file, but you can't give other users permission to modify them and collaborate on a document. For this, you need to go back to the concept of shared folders, and ODB just doesn't do this. This is where Sharepoint Online comes in to play.

Naturally, this being Sharepoint, it's not the easiest thing in the world to set up. It's powerful once you get it going, but I wasn't able to simply drop all the shared files into a Sharepoint document library -- There's a 5000-file limit imposed by the software. Because the church's shared files included a photo archive, there were WAY more than 5000 files in it.

Sharepoint is very picky about getting the right information architecture (IA) set up to begin with. Some things you can't change after the fact, if you decide you got them wrong. Careful planning is a must.

What I ended up doing for this church is creating a single site collection for the whole organization, and several sites within that collection for each ministry/volunteer team. Each site in Sharepoint has 3 main security groups for objects within a site collection:

- Visitors (Read-Only)
- Members (Read/Write)
- Owners (Read/Write/Admin)

In Office 365, much as it is with on-premises, you're much better off creating your security groups outside of Sharepoint and then adding those groups to the security groups that are created within Sharepoint. So in this case, I created a "Worship Production" team, added the team members to the group, and then added that group to the Worship Site Owners group in Sharepoint. The Staff group was added to all the Owners groups, and the visitors group was left empty in most cases. This makes group membership administration substantially easier for the on-site admin who will be handling user accounts most of the time. It's tedious to set up, but once it's going, it's smooth sailing.

Once the security permissions were set up for the various team sites, I went into the existing flat document repository and began moving files to the Sharepoint document libraries. The easiest way to do this is to go to the library in Sharepoint, and click the "Sync" button, which then syncs them to a local folder on the computer, much like OneDrive (although it's listed as Sharepoint). There is no limit to how many folders you can sync to the local machine (well, there probably is, but for all practical purposes, there isn't). From there it's a matter of drag and drop. For the photos repository, I created a separate document library in the main site, and told Sharepoint it was a photo library. This gives the user some basic Digital Asset Management capabilities such as adding tags and other metadata to each picture in the library.

So far, it's going well, and the staff enjoys having access to their Sharepoint libraries as well as Microsoft Office on their mobile devices (iOS and Android). Being able to work from anywhere also gives this church some easy business continuity should a disaster befall the facility -- all they have to do is relocate to the local café that has net access, and they can continue their ministry work. Their data has now been decoupled from their facility. I have encountered dozens of churches over the years whose idea of data backup is either "what backup?" or a hard drive sitting next to the computer 24x7, which is of no use if the building burns to the ground or is spontaneously relocated to adjacent counties by a tornado. The staff doesn't have to worry about the intricacies of running Exchange or Sharepoint on Windows Small Business Server/Essentials. Everything is a web-based administrative panel, and support from Microsoft is excellent in case there's trouble.

If you're interested in how to take your church or small business serverless, contact me and I'll come up with a custom solution.
