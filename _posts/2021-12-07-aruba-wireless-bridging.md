---
layout: post
title: Setting Up An Aruba Wireless Bridge
date: 2021-12-07 12:19:29.000000000 -06:00
type: post
parent_id: '0'
published: true
password: ''
status: publish
categories:
- Aruba
- networking
- Wireless
tags:
- Bridging
- Instant
- Mesh
- Point to Point
- Standalone
meta:
  _last_editor_used_jetpack: block-editor
  _publicize_twitter_user: "@CaNerdIan"
  _wpas_skip_19898087: '1'
  _wpas_done_all: '1'
  _thumbnail_id: '1881'
  _edit_last: '2'
  _wp_old_slug: setting-up-an-aruba-wireless-bridge
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
permalink: "/2021/12/07/aruba-wireless-bridging/"
image: "https://nerdian.ca/files/2021/12/AdobeStock_120498612-scaled.jpeg"
---

One of the most underrated features of Aruba wireless hardware is its ability to be used as a wireless bridge. Running a cable to provide power and data to an AP is always the best way, but sometimes you just can't get one there and have to go wirelessly.

With the release of Instant v 8.4, the concept of a mesh cluster name and key was introduced along with the [AP-387 5/60GHz outdoor bridge](https://www.arubanetworks.com/products/wireless/access-points/outdoor-ruggedized-access-points/387-series/). This mesh cluster mode lets the APs in the cluster establish their own mesh SSID and encryption, without the brain damage of provisioning those parameters on each device. This also introduced the concept of a standalone Instant AP, which allows you to run a point-to-point bridge or a multipoint mesh without the AP trying to join an existing Instant Virtual Cluster (VC).

Once a bridge is established, it is fully transparent at L2. Anything that shows up on the interface on the Mesh Portal AP will pop out the other side on the Mesh Point's bridged Ethernet interface. You can optionally prune VLANs if you need to.

Key Terms:

- **WIRELESS MESH** : one or more access points that connect to the network wirelessly.
- **MESH PORTAL/MESH ROOT**: an access point in a mesh network that is connected to the network via an Ethernet connection. An Aruba AP configured for mesh will determine if it is a portal by listening for traffic on the Ethernet port. a given mesh cluster can have multiple portals.
- **MESH POINT:** an access point in a mesh network that is connected to the network via one or more wireless connections to a Mesh Portal. Mesh points can also provide a wireless connection to another mesh point, but you don't want to go more than one or two hops to a root bridge. If you have to go long distances, a linear mesh topology may be more useful. An Aruba AP will determine it is a mesh point in a cluster by either not seeing traffic on the Ethernet ports, or if the Ethernet port is set to bridging mode and has devices downstream.
- **MESH CLUSTER**: A group of Aruba APs that are configured for the same mesh.

What you will need:

- two Aruba APs that support Instant 8.4 or higher. Update them to the latest 8.10 or 8.7 LTS code trains if you can. I labbed this up on a pair of AP-515s, but the APs don't necessarily have to be the same model of hardware, just the same software version. The Aruba mesh will operate on 5GHz.
- A means of powering both APs. This can be PoE, but you'll want the network on the Mesh Point side of the link to be an isolated Layer 2 segment from the one on the Mesh Portal, otherwise you'll create a loop when the bridge comes up. It's generally easiest to put a separate PoE switch on each end, making it easier to connect devices to troubleshoot. If using PoE, make sure it's sufficient to run the AP.
- Not strictly necessary, but helpful: A console cable for each AP. The 570 series APs use a standard USB Type C connection and ship with the requisite cable. Otherwise you'll need either the "Orange Cable" (**JY728A** AP-CBL-SERU) that has a Micro-B connector on the end (this isn't actually USB, so don't even bother trying to use a standard MicroUSB cable), or the older TTL pin header to DB9 cable.

To start, hook up the console cable to the AP, and power it on. When prompted, stop the boot loader. Once at the boot loader prompt, issue the following commands:

```

factory_reset
setenv standalone_mode 1
setenv uap_controller_less 1
saveenv
boot
```

This does the following:

- resets the AP to factory defaults
- sets the AP to standalone mode (ignores any incoming L2 Instant VC broadcasts and suppresses any outgoing ones)
- Sets the AP to Controllerless (Instant)
- Saves the environment variables
- Boots the AP.

You can also do this from a booted AP on the AOS CLI by issuing the following commands:

```

write erase all
swarm-mode standalone
reload
```

Once the AP is booted up into standalone mode, you'll need to log in via the GUI or the CLI (console or ssh) using the default credentials (admin/admin or admin/serial#), and set a new admin password. Once you've done this, you'll need to create an access SSID to get it out of Instant's SetMeUp mode. You can disable this later if the AP is not also being used for access (generally not a good idea on a mesh bridge, unless you're restricting it to the 2.4GHz radio which is unused by the mesh.) If you're using an AP-387, you don't need to do this.

Once you've created this dummy/temporary SSID (easiest from the Web UI), go to Configuration>System>Show Advanced Settings, **disable Extended SSID** and reboot.

On the CLI:

```

conf t
virtual-controller-country US
name Mesh-Portal (or name of your choice)
no extended-ssid
exit
commit apply
reload
```

virtual-controller-country is vital here. The AP will not do anything on RF until this is set.

Once the AP is back up, configure the mesh:

```

no mesh-disable
mesh-cluster-name &lt;cluster name&gt; (If doing multiple bridge links, each one must have a unique name)
mesh-cluster-key &lt;cluster-key&gt;
commit apply
```

If you're in a multi-VLAN environment, this is also a good time to set VLANs and such. If you're just running a flat network, skip this part.

```

uplink-vlan &lt;VLAN ID&gt; (this is the VLAN the AP listens on)

#If configuring a static IP: 
ip-address &lt;ip-address&gt; &lt;subnet-mask&gt; &lt;nexthop-ip-address&gt; &lt;dns-ip-address&gt; &lt;domain-name&gt;

conf t
wired-port-profile Mesh_Portal_Uplink-wpp
 switchport-mode trunk
 allowed-vlan &lt;list of VLANs or "all"&gt;
 native-vlan &lt;port Native VLAN&gt;
 trusted
 no shutdown
 type employee
 auth-server InternalServer
 captive-portal disable
 no dot1x
exit

enet0-port-profile Mesh_Portal_Uplink-wpp
enet1-port-profile Mesh_Portal_Uplink-wpp

exit
commit apply
```

Check the status of the mesh cluster settings with:

```

show ap mesh cluster status
```

It should look something like this:

```

Mesh cluster      :Enabled
Mesh cluster name :Mesh_Lab
Mesh role         :Mesh Portal
Mesh Split5G Band Range :full
Mesh mobility     :Disabled
```

Now you'll want to do the same process on the Mesh Point AP, plus the following to enable the bridging (you can also do this in the boot loader by doing **setenv enet0\_bridging 1** and **savenv**):

```

enet0-bridging
commit apply
reload
```

Once everything is booted back up, give it a few minutes to establish the mesh link, and then run:

```

show ap mesh link
```

Which will give you information about the link. the RSSI column is the SNR in dB. You can see from the flags that the link is running an 802.11ax/HE PHY (E), that legacy PHYs are allowed (L), and that it is connected to the mesh portal (K).

```

# show ap mesh link

Neighbor list
-------------
Radio  MAC                AP Name          Portal  Channel  Age  Hops  Cost  Relation                 Flags  RSSI  Rate Tx/Rx  A-Req  A-Resp  A-Fail  HT-Details    Cluster ID
-----  ---                -------          ------  -------  ---  ----  ----  -----------------        -----  ----  ----------  -----  ------  ------  ----------    ----------
0      aa:bb:cc:dd:ee:ff  Mesh_Lab_Portal  Yes     116E     0    0     4.00  P 22h:18m:57s            ELK    55    1531/1701   1      1       0       HE-80MHz-4ss  29c8af3dec64e7c278bfcbfab07a2a3

Total count: 1, Children: 0
Relation: P = Parent; C = Child; N = Neighbor; B = Blacklisted-neighbor
Flags: R = Recovery-mode; S = Sub-threshold link; D = Reselection backoff; F = Auth-failure; H = High Throughput; V = Very High Throughput, E= High efficient, L = Legacy allowed
        K = Connected; U = Upgrading; G = Descendant-upgrading; Z = Config pending; Y = Assoc-resp/Auth pending
        a = SAE Accepted; b = SAE Blacklisted-neighbour; e = SAE Enabled; u = portal-unreachable; o = opensystem
```

From this point, you should be able to send traffic across the link, and you're ready to go install the bridge in its permanent home. If running outdoors, don't forget to ensure a clear line of sight and unobstructed Fresnel Zone.
