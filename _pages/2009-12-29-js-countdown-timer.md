---
layout: page
title: JavaScript Countdown Timer
date: 2009-12-29 21:22:20.000000000 -06:00
type: page
parent_id: '940'
published: true
password: ''
status: publish
categories: []
tags: []
meta:
  _edit_last: '1'
  _wp_page_template: default
  dsq_thread_id: '217880176'
  _googl_shortlink: http://goo.gl/GCzFr
  _syntaxhighlighter_encoded: '1'
author:
  login: ianbeyer
  email: ian.beyer@gmail.com
  display_name: Ian Beyer
  first_name: Ian
  last_name: Beyer
permalink: "/code/client/js-countdown-timer/"
---

I don't know who wrote the original script this is based on. I've modified it some.
\*\*Usage:\*\*
[js]
// \\*\\*\\*\\* Time Zone Count Down Javascript \\*\\*\\*\\* //
////////// CONFIGURE THE COUNT DOWN SCRIPT //////////////////
var month = '1'; // use '\\*' for next month; '0' for this month; or 1 thru 12 for the month
var day = '3'; // insert a number 1-31 for the day of month
var hour = '10'; // insert 0 thru 23 for the hour of the day the service starts
var min = 45; // set to 0 if the service starts on the hour. Set to 30 (or 45, etc.) if the service begins at xx:30.
var tz = '-6'; // Offset for Resurrection's timezone in hours from UTC - CST is -6; CDT is -5
var event = 'Our next worship service'; // What is displayed in the message
var onair = 'ON AIR!'; // On Air message

Code:
var lab = 'tzcdtimer'; // The id of the page entry that shows the timezone countdown
function start() {displayTZCountDown(setTZCountDown(month,day,hour,min,tz,event,onair),lab);}
// \\*\\* The start function can be changed if required \\*\\*
window.onload = start;
////////// DON'T EDIT PAST THIS LINE //////////////////
function setTZCountDown(month,day,hour,min,tz)
{
var toDate = new Date();
if (month == '\\*')toDate.setMonth(toDate.getMonth() + 1);
else if (month > 0)
{
if (month <= toDate.getMonth())toDate.setYear(toDate.getYear() + 1);
toDate.setMonth(month-1);
}
if (day.substr(0,1) == '+')
{var day1 = parseInt(day.substr(1));
toDate.setDate(toDate.getDate()+day1);
}
else{toDate.setDate(day);
}
toDate.setHours(hour);
toDate.setMinutes(0-(tz\\*60-min));
toDate.setSeconds(0);
var fromDate = new Date();
fromDate.setMinutes(fromDate.getMinutes() + fromDate.getTimezoneOffset());
var diffDate = new Date(0);
diffDate.setMilliseconds(toDate - fromDate);
return Math.floor(diffDate.valueOf()/1000);
}
function displayTZCountDown(countdown,tzcd)
{
// if (countdown < 0) document.getElementById(tzcd).innerHTML = "ON AIR!";
if (countdown < 0) document.getElementById(tzcd).innerHTML = onair;
else {var secs = countdown % 60;
if (secs < 10) secs = '0'+secs;
var countdown1 = (countdown - secs) / 60;
var mins = countdown1 % 60;
if (mins < 10) mins = '0'+mins;
countdown1 = (countdown1 - mins) / 60;
var hours = countdown1 % 24;
var days = (countdown1 - hours) / 24;
// document.getElementById(tzcd).innerHTML = '' + days + ' day' + (days == 1 ? '' : 's') + ', ' +hours+ ' hours, ' +mins+ ' minutes, and '+secs+' seconds.';
if (days > 0 ) {
document.getElementById(tzcd).innerHTML = event + ' begins in ' + days + ' day' + (days == 1 ? '' : 's') + ', ' +hours+ ' hour' + (hours == 1 ? '' : 's') +', ' +mins+ ' minute'+ (mins == 1 ? '' : 's') + ', and '+secs+' second' + (secs == 1 ? '' : 's');
}
else {
if (hours >0) {
document.getElementById(tzcd).innerHTML = event + ' begins in ' +hours+ ' hour' + (hours == 1 ? '' : 's') +', ' +mins+ ' minute'+ (mins == 1 ? '' : 's') + ', and '+secs+' second' + (secs == 1 ? '' : 's');
}
else {
document.getElementById(tzcd).innerHTML = event + ' begins in ' +mins+ ' minute'+ (mins == 1 ? '' : 's') + ' and '+secs+' second' + (secs == 1 ? '' : 's');
}
}
setTimeout('displayTZCountDown('+(countdown-1)+',''+tzcd+'');',999);
}
}
[/js]
