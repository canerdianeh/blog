---
layout: post
title: Turn the radio on!
date: 2008-02-18 08:11:00.000000000 -06:00
type: post
parent_id: '0'
published: true
password: ''
status: publish
categories:
- IT
- networking
- Wireless
tags:
- 80GHz
- bridgewave
- engineering
- snow
- southcreek
- wireless
meta:
  blogger_blog: netplumber.blogspot.com
  blogger_author: The Cybernetic Entomologisthttp://www.blogger.com/profile/00786962432410897055noreply@blogger.com
  blogger_permalink: "/2008/02/turn-radio-on.html"
  _edit_last: '2'
  dsq_thread_id: '217876642'
  _googl_shortlink: http://goo.gl/b74eJ
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
permalink: "/2008/02/18/turn-the-radio-on/"
---

(apologies to [Randy Travis for lifting a title](http://www.lyricsfreak.com/r/randy+travis/turn+your+radio+on_20327652.html))

On Friday, our [vendor](http://www.proximitywireless.com/) came out to replace the radio on the Southcreek end of our wireless link. (More on that at [Clif's Blog](http://appianway.blogspot.com/2008/02/trying-again-on-wireless-lan-bridge.html)). Long story short, we improved the income side of the link budget by about 16dB.

Got this done just in time for a big rainstorm on Saturday, followed by sloppy wet driving snow on Sunday (attendance was way down, partly due to the weather. Some churches even canceled service. [Well, sort of](http://appianway.blogspot.com/2008/02/should-you-ever-cancel-church-due-to.html).) Even Kansas City International Airport [had its longest closure in history](http://www.msnbc.msn.com/id/23210769/) because they couldn't keep the runways clear long enough. We Canadians are amused by this notion.

Since we had just gotten a shiny new radio and antenna on the Southcreek end, I was curious to see how the link was performing in the snow. I fired up [WhatsUp](http://www.whatsupgold.com/) and checked my wireless status page. Both bridges showed more or less the same thing:

[![]({{site.baseurl}}/assets/2008/02/Southcreek+Snow.png)](http://bp2.blogger.com/_yY8-F4b4zEk/R7mFugjxXKI/AAAAAAAAAEQ/wts7427Hj74/s1600-h/Southcreek+Snow.png)  
(Time of day is along the X-axis, and the Y-axis is received signal level (RSL) in hundredths of a dB, so -3100 is -31dB - due to a firmware update, it only reports in whole dB now, probably because the fractional numbers weren't nearly as accurate as they were precise )

The pattern struck me as intriguing, because precipitation generally looks a little different, as demonstrated by Saturday's rainstorm (you can also see the beginning of the snow on the far right):

[![]({{site.baseurl}}/assets/2008/02/southcreek+rain.png)](http://bp3.blogger.com/_yY8-F4b4zEk/R7mGawjxXLI/AAAAAAAAAEY/2DN9QEsJ2A0/s1600-h/southcreek+rain.png)

After checking a few weather sites, I discovered that the downward slope at 6:00 correlated to the beginning of the snow. I was beginning to suspect that at least one of the radomes was plastered in snow. We'd just gotten back from church, where the wind was blowing pretty hard from the northwest, and the Central Campus end was facing almost directly into the wind at the top of the building. I asked my wife if I could run back and do a little weekend science. After realizing that this sort of thing was part of what she signed up for when she married a geek, she sent me on my way with the camera (thank you honey, I love you! \*smooch\*)

I stopped by the Southcreek office first, and realized that the blue Bridgewave logo on the radomes was going to be very helpful at determining accumulation. This is what Southcreek looked like:

[![]({{site.baseurl}}/assets/2008/02/Copy+of+Southcreek.JPG)](http://bp1.blogger.com/_yY8-F4b4zEk/R7mH7QjxXMI/AAAAAAAAAEg/PIuKgb8eiO4/s1600-h/Copy+of+Southcreek.JPG)

(apologies for the grainy picture, it was taken from about 100 feet away at max digital zoom and then cropped):

Unsurprisingly, there was no significant accumulation on the Southcreek radio, as the radome was facing downwind. This is what the weather looked like towards the other end of the link:

[![]({{site.baseurl}}/assets/2008/02/Copy+of+Southcreek+Lot.JPG)](http://bp0.blogger.com/_yY8-F4b4zEk/R7mIUAjxXNI/AAAAAAAAAEo/dxgPpkndd_I/s1600-h/Copy+of+Southcreek+Lot.JPG)

I drove over to the church, where the conditions looked like this:

[![]({{site.baseurl}}/assets/2008/02/Copy+of+Central+Campus+Trees.JPG)](http://bp2.blogger.com/_yY8-F4b4zEk/R7mItgjxXOI/AAAAAAAAAEw/3SeqM89cbws/s1600-h/Copy+of+Central+Campus+Trees.JPG)

Notice that the snow is plastered on one side of the trees. The CC radio is facing that direction.

I found a radio and got a hold of George (on the facilities team, also does desktop support for us one day a week) to let me onto the roof. George looked at me funny and wondered why I wanted up on the roof in this craptacular weather. After a brief explanation, he joined me (and wanted to see for himself, too - George is a geek at heart). I get up on the roof, and do a little skating (roofing membrane is nice and slick when wet, never mind when covered in a few inches of sloppy wet snow!)

Sure enough, here's what the radome looked like:

[![]({{site.baseurl}}/assets/2008/02/Copy+of+Central+Campus+Accumulation+3.JPG)](http://bp1.blogger.com/_yY8-F4b4zEk/R7mKjQjxXPI/AAAAAAAAAE4/OUQnS9qFMY0/s1600-h/Copy+of+Central+Campus+Accumulation+3.JPG)

It was pretty clear what was causing our 30dB signal loss (the link was still up, with about 10dB to go). George went off to find something to clean off the snow (it's about 15' from where we were standing, and we didn't have a ladder). While George was off playing MacGyver, I got to thinking that the snow probably wasn't stuck on very well, and that some sort of jarring impact might knock it off. If only I had something to throw at it... Like, say, a snowball. My concern was that the snowball would stick to the radome and REALLY attenuate the signal, but I figured this stuff was wet and slushy enough to form into a ball, but was too wet to actually stick to anything (it was above freezing the whole time). So I started chucking snowballs at a piece of gear that costs about the same as a decent new car (I love my job!). On the third try, I made solid contact just below the logo, and the sheet of snow came sliding right off (look below the right loop of the logo for the point of impact):

[![]({{site.baseurl}}/assets/2008/02/Copy+of+Central+Campus+Post-Snowball.JPG)](http://bp0.blogger.com/_yY8-F4b4zEk/R7mLxAjxXQI/AAAAAAAAAFA/U6eqz7pHLJo/s1600-h/Copy+of+Central+Campus+Post-Snowball.JPG)  
(by the time I actually got the picture taken, some more snow had accumulated on the radome. Did I mention it was snowing hard?)  
  
I went down to a computer to check on the signal level. Sure enough, the link improved a bunch. (I'll repost the image here so you don't have to scroll all the way to the start of the post.) The snowball caused the sharp vertical spike on the right side of the graph. The picture was taken about the spot where it dropped back down a few DB:

[![]({{site.baseurl}}/assets/2008/02/Southcreek+Snow.png)](http://bp2.blogger.com/_yY8-F4b4zEk/R7mFugjxXKI/AAAAAAAAAEQ/wts7427Hj74/s1600-h/Southcreek+Snow.png)

I headed back for the roof and found George had MacGyvered a pole from an extendable dusting wand and a wooden broom handle, held together with packing tape. I climbed back up onto the roof and was able to reach the radome with George MacGyver's snow brush. Cleaning it off gained me a few more dB (second, smaller vertical spike on the graph):

[![]({{site.baseurl}}/assets/2008/02/Copy+of+Central+Campus+Post-Scrub.JPG)](http://bp2.blogger.com/_yY8-F4b4zEk/R7mM8gjxXRI/AAAAAAAAAFI/Rer5IvZoZtQ/s1600-h/Copy+of+Central+Campus+Post-Scrub.JPG)

As you can see on the graph, some more snow started accumulating, and then the snow stopped and started melting off. By mid-afternoon, the sun had come out we were back up to our normal signal levels, and there was little evidence left around town that we'd even had a snowstorm. We went from this, where it's snowing sideways...

[![]({{site.baseurl}}/assets/2008/02/Copy+of+Central+Campus+Conditions+%25282%2529.JPG)](http://bp3.blogger.com/_yY8-F4b4zEk/R7mOcwjxXSI/AAAAAAAAAFQ/NakM-QwcAL4/s1600-h/Copy+of+Central+Campus+Conditions+%282%29.JPG)

...to a beautiful sunny day in a matter of hours. I'm glad I didn't bother shoveling my driveway, as it had melted clear by the time my wife and I got back from the movies (we went to see [Jumper](http://imdb.com/title/tt0489099/). Good flick, but left a lot of unanswered questions -- sequel, anyone? -- as well as leaving me with lingering nausea from the jumpy camera work)

I haven't heard what the attendance was like at the 5:00 service. Morning services were sparse due to weather, but Rev. Junius Dotson from Saint Mark UMC in Wichita was our guest preacher this week and preached a great sermon (Adam is off in Colorado enjoying the *real* snow with the high schoolers). I hope a bunch of folks got to experience Rev. Dotson at the evening service. The man just has *style*.

And now, for the ADD folks that lost me about 6 paragraphs ago, here's a nice little summary:

[![]({{site.baseurl}}/assets/2008/02/Snow%2521.jpg)](http://bp1.blogger.com/_yY8-F4b4zEk/R7mSAQjxXVI/AAAAAAAAAFo/RTmhmmy3Uw0/s1600-h/Snow%21.jpg)
