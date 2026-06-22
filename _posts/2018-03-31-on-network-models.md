---
layout: post
title: On Network Models
date: 2018-03-31 21:31:52.000000000 -05:00
type: post
parent_id: '0'
published: true
password: ''
status: publish
categories:
- nerd
- networking
- Wireless
tags: []
meta:
  _edit_last: '2'
  _thumbnail_id: '1481'
  _wpas_done_all: '1'
  _wpas_skip_19898085: '1'
  _wpas_skip_19898087: '1'
  _wpas_skip_19898090: '1'
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
permalink: "/2018/03/31/on-network-models/"
image: "https://nerdian.ca/files/2018/03/7-layer-burrito.jpg"
---

One of the most fundamental concepts underlying modern data networking is that of the network

"stack", which consists of individual "layers" that allow one to describe a network without actually getting lost in the weeds of specific underlying technologies. There are two models that are in common usage (there are several others as well but are less common):

- the seven-layer OSI Model (which is largely theoretical), published in 1984 as ISO ![]({{site.baseurl}}/assets/2018/03/layers.jpeg)standard 7498 and officially known as the "Open Systems Interconnection Reference Model" *(Kansas connection: the OSI model's designer, [Charles Bachman III](https://en.wikipedia.org/wiki/Charles_Bachman), was born in Manhattan, the son of the head football coach at K-State at the time)*
- the four-layer TCP/IP Model (which is a more practical model owing to the widespread use of the internet). The TCP/IP model predates the OSI model and can trace some of its roots to BBN's early work on internetworking in the late 1960s.

One of the key principles of the model is that each layer is carried by the layer below it. The layers each have their own methods and protocols, which are (for the most part) independent of the layers below that are carrying them from A to B. In the TCP/IP column, I've also indicated what type of system operates at that layer.

| Network Model | | | | | |
| --- | --- | --- | --- | --- | --- |
|  | OSI | TCP/IP | OSI Protocol data unit (PDU) | Function |
| Host  layers | 7. Application | Application (Computer) | Data | High-level APIs, including resource sharing, remote file access |
| 6. Presentation | Translation of data between a networking service and an application; including |
| 5. Session | Managing communication sessions, i.e. continuous exchange of information in the form of multiple back-and-forth transmissions between two nodes |
| 4. Transport | Transport (ISP) | Segment | Reliable transmission of data segments between points on a network, including segmentation, acknowledgement and multiplexing |
| Media  layers | 3. Network | Internetwork (Router) | Packet | Structuring and managing a multi-node network, including addressing, routing, and traffic control |
| 2. Data link | Link (Switch) | Frame | Reliable transmission of data frames between two nodes connected by a physical layer |
| 1. Physical | Bit | Transmission and reception of raw bit streams over a physical medium |

The importance of understanding these network models comes into play is when you are designing or troubleshooting a network. Understanding at what level your problem is happening is a major step towards solving it. I've seen and answered countless questions on Quora about "why doesn't X" work, or "can someone on the internet trace me by my MAC address?" and various other questions that can be enlightened by an understanding of the network models. As a general rule, the lower you are in the model, the more physically localised you're dealing with.

It's probably difficult to wrap your head around if you're not used to this kind of stuff. So let me offer up an example of how this same network model manifests itself in the real world, completely unrelated to computer networking. You've almost certainly seen it in action. You've benefited from it in your life. I give you: Container Shipping.

Container shipping relies on a standardized set of steel containers (also defined by the ISO) that can be used to haul goods efficiently around the world.

Here's what the Transport Layer looks like:

![]({{site.baseurl}}/assets/2018/03/Container-Boxes-300x150.jpg)

Notice that the container is itself full of smaller containers (plain cardboard boxes: The session layer) - which themselves may contain additional boxes for retail (presentation layer), which contain an actual product (application layer). When the container is closed and sealed, its contents go wherever it goes.

But how does it get there? It makes use of the Network Layer. This is where it goes through one or more shipping companies (like ISPs) that get the contents from the factory in China (server) to the buyer (client). As in computer networking, This transportation company can use multiple types of ways to get it there, such as trucks, trains, ships, and airplanes. These are Layer 2, the Link Layer, and are all capable of carrying these containers.

![]({{site.baseurl}}/assets/2018/03/Container-Ship-300x200.jpg)

![]({{site.baseurl}}/assets/2018/03/container-car-300x145.jpg)

![]({{site.baseurl}}/assets/2018/03/container-truck-300x130.jpg) ![]({{site.baseurl}}/assets/2018/03/container-747-300x261.jpg)

Each of these Layer 2 conveyances rides on a different physical medium: Roads (land), Rails (land), Shipping routes (sea), flight paths (air).

It's also worth noting that two of these physical media are bounded media (roads and rails) which constrain the path the vehicle takes. This is akin to a wire or fiber optic cable.  The other two (sea and air) are unbounded, which means the vehicles can take any path they choose. This is akin to free-space optical transmission and wireless RF transmission - it also means those are more susceptible to interception (hijacking/piracy).

I mentioned earlier that a layer 3 device is a router. Its job is to get the data from one network to another. What does this look like in container shipping? One of these giant cranes that remove the containers from one conveyance, to be loaded onto another. Sometimes, it will buffer them in a container yard before sending it on to its destination.

![]({{site.baseurl}}/assets/2018/03/container-crane-300x241.jpg)

Once the container gets to its destination, it is signed for (an ACKnowledgement in the network world), and the signature is sent back to the shipper to confirm that it arrived at its destination - this is a transport layer function, as it is the shipper's responsibility to make sure stuff gets there on time. The buyer and shipper (Layer 7) don't really care \*how\* it got there, just that it did.
