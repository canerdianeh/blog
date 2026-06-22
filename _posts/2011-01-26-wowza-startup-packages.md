---
layout: post
title: Inside Wowza Startup Packages
date: 2011-01-26 14:41:17.000000000 -06:00
type: post
parent_id: '0'
published: true
password: ''
status: publish
categories:
- Internet Campus
- streaming
- Wowza
tags:
- ec2
- scripting
meta:
  dsq_thread_id: '217881153'
  _wp_old_slug: ''
  _edit_last: '2'
  s2mail: 'yes'
  _googl_shortlink: http://goo.gl/5NbcY
author:
  login: ianbeyer
  email: ian.beyer@gmail.com
  display_name: Ian Beyer
  first_name: Ian
  last_name: Beyer
permalink: "/2011/01/26/wowza-startup-packages/"
---

[![]({{site.baseurl}}/assets/2011/01/logo\_aws.gif)](http://blog.ianbeyer.com/files/2011/01/logo\_aws.gif)Startup packages are one of the more useful features of [Wowza Media Server for EC2](http://wowzamedia.com/ec2.html "Wowza for Amazon EC2") - they allow you to custom-configure a system for rapid scaling and provisioning. Wowza provides several [starter packages](http://wowzamediasystems.s3.amazonaws.com/packagelist.html "Wowza EC2 Startup Packages") to build on.
A startup package is a file (up to 16384 bytes in size) that's passed to the instance through the \*\*--user-data-file\*\* parameter on the API tools (if you're uploading it via the [AWS Web Consol](http://console.aws.amazon.com "Amazon Web Services Console")e, you'll need to [encode it to Base64](http://www.motobit.com/util/base64-decoder-encoder.asp "Base64 encoder/decoder") and paste it into the text box) . There are a few ways that the data can get into the instance, which Amazon [documents over here](http://docs.amazonwebservices.com/AmazonEC2/dg/2006-10-01/AESDG-chapter-instancedata.html "Using EC2 Instance Data"). For a generic EC2 instance, this can be anything, from text to binary data, depending on what the processing on the target instance is set up to do. In the case of Wowza, it's a zip file with a specific structure. Much of this is digested from the [Wowza for EC2 guide](http://www.wowzamedia.com/resources/WowzaMediaServerForEC2\_UsersGuide.pdf "Wowza for Amazon EC2 User's Guide").
# File Contents
A startup package for EC2 contains the following:
- startup.xml (startup manifest)
- tuning folder
- wowza folder
- Any other folders referenced in the startup manifest
A startup package is limited to a maximum of 16KB.
Startup activities are logged to \*\*/usr/local/WowzaMediaServer/logs/wowzamediaserver\\_startup.log\*\*. This is a good place to look if it's not behaving as expected. The package is unpacked to \*\*/opt/working\*\*.
## Startup Manifest
This file controls the startup processing for instantiating a Wowza server on Amazon EC2. It allows three commands: Install, Download, and RunScript.
### Download
The  command will download content from a web server and save it to the local Amazon instance. The  command includes the following elements: URL, Data, Header, Destination, and Action:

```

<Download>
<URL>[URL]</URL>
<Data>[data]</Data>
<Header><Name>[key-name]</Name><Value>[value]</Value></Header>
<Header><Name>[key-name]</Name><Value>[value]</Value></Header>
<Destination>[relative-or-absolute-file-path]</Destination>
<Action>[UNZIP, INSTALL]</Action>
</Download>
```

The only two required elements are  and . To download a file from the url http://www.mycompany.com/myfile.zip, save it to the local machine at the location /opt/myfile.zip and unzip the file after download, the command is:

```

<Download>
<URL>http://www.mycompany.com/myfile.zip</URL>
<Destination>/opt/myfile.zip</Destination>
<Action>UNZIP</ Action >
</Download>
```

When completed, the contents of the zip archive are located in \*\*/opt\*\*.
One use of the  command is to work around the 16kB startup package size limitation. For example, if you need to add several .jar files into the Wowza Server “lib” folder and these files push your startup package size over the 16kB limit, you might package these files into a separate zip archive. You can then host this zip archive on a web server and use the  command to install the files into the Wowza Server “lib” folder.
It's important to remember that the zipfile path structure is critical. If it uses no paths, you'll need your destination to be where it ultimately lives, either in the staging area, or the absolute path to the Wowza install. When creating the zipfile with relative paths, create the path tree as if you were in the Wowza installation root.
#### URL
The  is the URL of the file to be downloaded. The download can be performed over SSL by starting the url with https:// rather than http://. The url can also contain query parameters. The file will be downloaded using the GET method unless  is specified.
#### Data
The Data is text data that will be included as part of the body of the HTTP request. You can use post data to send user name and password information to your web server so you can protect your content.
#### Header:  and 
The  elements are name value pairs added to the header part of the HTTP request. An example would be:

```

<Header>
<Name>Content-type</Name>
<Value>text/plain</Value>
</Header>
```

#### Destination
The element is the path to which the file will be saved (including the filename). This path can be relative or absolute. The base directory when calculating a relative file path, is the root directory of the startup package (the folder that contains the startup.xml file).
#### Action
The  element is the action performed after the file is downloaded. The action can either be UNZIP or INSTALL. If the action is UNZIP the downloaded file will be unzipped using the unzip command. If the action is INSTALL the downloaded file will be unzipped and the contents of the folder will be installed (copied) into the Wowza Server installation folder.
### Install
The  command will copy the contents of a folder into the Wowza Server installation folder. The  command can either contain a single  element or single  element.

```

<Install>
<Package>[path-to-package]</Package>
</Install>
```

```

<Install>
```

```

<Folder>[foldername]</Folder>
```

```

</Install>
```

The Package path can reference an external URL, like http://wowzamediasystems.s3.amazonaws.com
The Folder path can reference either a relative path (relative to the root of the startup package where Startup.xml is located) or an absolute path on the local file system.
### RunScript
The  command will execute a script on a running Amazon instance.

```

<RunScript>
<Script>[relative-or-absolute-file-path]</Script>
<Param>[parameter]</Param>
<Param>[parameter]</Param>
</RunScript>
```

#### Script
The 

```

<RunScript>
<Script>scripts/copyfile.sh</Script>
<Param>filea.txt</Param>
<Param>fileb.txt</Param>
</RunScript>
```

Would be the equivalent of executing the command:

```

./scripts/copyfile.sh filea.txt fileb.txt
```

### Environment Variables

The following environment variables are available to scripts launched by the startup processor:

```

AWSEC2_METADATA_INSTANCE_ID - Amazon instance id
AWSEC2_METADATA_SECURITY_GROUPS - Security group
AWSEC2_METADATA_LOCAL_IPV4 - Local IP address
AWSEC2_METADATA_AMI_LAUNCH_INDEX - Launch index
AWSEC2_METADATA_PUBLIC_HOSTNAME - Public host name
AWSEC2_METADATA_PRODUCT_CODES - DevPay product code
AWSEC2_METADATA_INSTANCE_TYPE - instance type (m1-small, m1-large, m1-xlarge)
AWSEC2_METADATA_HOSTNAME - Public host name
AWSEC2_METADATA_LOCAL_HOSTNAME - Local host name
AWSEC2_METADATA_PUBLIC_IPV4 - Public IP address
AWSEC2_METADATA_AMI_MANIFEST_PATH - S3 manifest path
AWSEC2_METADATA_RESERVATION_ID - Instance reservation ID
AWSEC2_METADATA_AMI_ID - AMI ID
```

## Wowza Folder

The Wowza folder in the startup package is meant to mirror the Wowza installation folder on the server. When the Install command in the startup manifest is invoked with this folder, the file structure of this folder will be copied to the installation folder.

### Applications Tree

Contains folders for each Wowza application configured. There are not typically any files in this tree, just folders.

### Conf Tree

Contains the configuration files for the server (at the root of the tree) and for each application (in folders matching the applications tree

### Content Tree

Contains any content referenced by the applications. This is where SMIL files, stream schedules, and such go. Any audio/video content that goes here won’t fit in the startup package and will need to be downloaded separately.

### Lib Tree

Contains any additional modules for the server.

## Tuning Folder

This folder contains tuning scripts that tune the Wowza server.  It copies the requisite environment variables and tuning commands to a script executed as part of the Wowza startup, which happens after the startup processor is run.

# Scripting

The following useful linux tools are available on the standard EC2 build (based on [Fedora](http://fedoraproject.org/ "Fedora Linux")):

- MySQL client commands
- zip/unzip, bzip/bunzip, gzip/gunzip
- s3fs
- Compiler and build tools
- WGet
- RSync
- SSH commands
- dos2unix/unix2dos
- curl
- perl 5.8.8 (with MySQL support)
- GPG
- Shells: bash, sh
- RRDTool
- PHP5
- EC2 API tools

# Services

The following services are available on the EC2 build of Wowza, in startup order:

- SNMP
- SSH
- FTP (Anonymous access to /var/ftp/)
- MySQL (default password = “password”)
- Wowza
- Apache 2 – port 8080, content in /var/www/html
  - Cacti
- Java Console

Startup package scripts and data are invoked by the Wowza startup script. If you modify any applications started prior to that, you'll need to restart them.

# Example

Here's what my startup.xml looks like:

```

<Startup>
 <Commands>

 <!--
  Comments
  -->

 <Download>
  <URL>http://webserver/wowza/wms-plugin-collection.zip</URL>
  <Destination>wowza/lib/wms-plugin-collection.zip</Destination>
  <Action>UNZIP</Action>
 </Download>

 <RunScript>
  <Script>scripts/mount-s3.sh</Script>
 </RunScript>

 <Install>
  <Folder>wowza</Folder>
 </Install>

 <RunScript>
  <Script>tuning/tune.sh</Script>
 </RunScript>

 <RunScript>
 <Script>scripts/enable_cacti.sh</Script>
 </RunScript>
 </Commands>
</Startup>
```

How this works:

- Download the wms-plugin-collection.zip file and dump it in the staging area for wowza (/opt/working/wowza/lib)
- Unzip it (this leaves the zip file behind, but that doesn't matter)
- Run the a script that mounts some s3 buckets and copies them into the content folder:

```

#!/bin/sh
mkdir -p /usr/local/WowzaMediaServer/content/s3
mkdir -p /usr/local/WowzaMediaServer/content/archives

s3fs bucket1 -o accessKeyId=XXX -o secretAccessKey=YYY /usr/local/WowzaMediaServer/content/s3

s3fs bucket2 -o accessKeyId=XXX -o secretAccessKey=YYY /usr/local/WowzaMediaServer/content/archives/

cp /usr/local/WowzaMediaServer/content/s3/* /usr/local/WowzaMediaServer/content
```

- Install the Wowza configs from the staging area
- Run the tuning scripts
- Run a script that automatically enables Cacti (since polling the local host is disabled by default):

```

#!/bin/sh
mysql -u root -ppassword < scripts/enable_cacti.sql
```

enable\_cacti.sql contains the following statement:

```

update cacti.host set disabled='' where id='2';
```

(note that if you're using an Elastic IP, you'll need to restart the Wowza Service for Cacti to behave)

In my Wowza directories, I have:

- **applications**directory
  - **live** directory (think of this as a mount point - it's an empty directory, but has to exist)
- **conf**directory
  - **Server.xml** (general server parameters)
  - **VHost.xml** (host bindings, HTTP providers, etc.)
  - **live**directory (this is the application configuration for the live application)
    - **Application.xml** (defining the live application)
- **content**directory
  - **ipad.smil** ( multi-bitrate stream selection for [iOS devices](http://apple.com "Apple"))
  - **mobile.smil** (defining where the [Roku](http://roku.com "Roku") stream goes - this abstracts a potentially changing stream name, as well as giving me a way to track Roku traffic using [this perl stats collection script](http://blog.ianbeyer.com/code/backend/wowza-metrics-perl/ "Wowza stats collector with RRD (perl)"))
  - **streamschedule.smil** (defines the schedule for the [Stream Class module](http://blog.ianbeyer.com/2011/01/17/wowza-stream-class/ "Using the Wowza Stream Class"))
  - Additional material is pulled from S3 in the aforementioned script
- **lib** directory (empty mount point)

To start my Wowza instances, I create the startup package file and tree structure, and then call this [startup script](http://blog.ianbeyer.com/code/ec2/wowza-origin-startup-bash/ "Wowza Origin Server Startup (bash)") that packs up the zip file and fires off the instance.
