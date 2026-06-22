---
layout: post
title: PHP Direct Upload to S3
date: 2012-01-19 10:12:05.000000000 -06:00
type: post
parent_id: '0'
published: true
password: ''
status: publish
categories:
- Code
tags:
- amazon
- AWS
- PHP
- S3
meta:
  _edit_last: '2'
  _syntaxhighlighter_encoded: '1'
  _wp_old_slug: php-direct-upload-s
  dsq_thread_id: '545408722'
author:
  login: ianbeyer
  email: ian.beyer@gmail.com
  display_name: Ian Beyer
  first_name: Ian
  last_name: Beyer
permalink: "/2012/01/19/php-direct-upload-s3/"
image: "http://blog.ianbeyer.com/files/2012/01/Screen-Shot-2012-08-29-at-11.20.00-AM.png"
---

Here's an easy way to upload directly to S3 from an HTML form. No Java, no Flash. Thanks to [@RaamDev](http://twitter.com/raamdev "@RaamDev") for his handy little bit of [code for doing HMAC signatures](http://raamdev.com/2008/amazon-s3-hmac-signatures-without-pear-or-php5/ "S3 HMAC Signatures without PEAR"). Based on the [documentation from Amazon](http://aws.amazon.com/articles/1434 "Browser Uploads to S3 using HTML POST Forms"). Makes use of the [AWS SDK for PHP](http://aws.amazon.com/sdkforphp/ "Amazon Web Services SDK for PHP") to list the buckets.
Screen shots:
[caption id="attachment\\_1158" align="alignnone" width="268"]![]({{site.baseurl}}/assets/2012/01/Screen-Shot-2012-08-29-at-11.20.00-AM.png "Bucket Select") Bucket Selection[/caption]
[caption id="attachment\\_1159" align="alignnone" width="311"]![]({{site.baseurl}}/assets/2012/01/Screen-Shot-2012-08-29-at-11.20.13-AM.png "File Selection") File Selection[/caption]
[caption id="attachment\\_1160" align="alignnone" width="317"]![]({{site.baseurl}}/assets/2012/01/Screen-Shot-2012-08-29-at-11.20.34-AM.png "File Selected") File Selected[/caption]
[caption id="attachment\\_1161" align="alignnone" width="452"]![]({{site.baseurl}}/assets/2012/01/Screen-Shot-2012-08-29-at-11.20.49-AM1.png "Upload Success") Upload Success[/caption]
code:
[php]

Upload a file to S3

# S3 File Upload

php
error\\_reporting(0);
$accesskey='XXXXXXXXXXXXXXXX';
$secretkey='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX';
require\\_once 'AWSSDKforPHP/sdk.class.php';
if (!class\\_exists('CFRuntime')) die('No direct access allowed.');
CFCredentials::set(array(
$name = array(
'key' => $accesskey,
'secret' => $secretkey,
'certificate\\_authority' => false
),
'@default' => $name
));
$s3 = new AmazonS3();
if(!isset($\\_GET['bucket'])) {
echo "

Please select a bucket:

\n";
$buckets=$s3->get\\_bucket\\_list();
echo '';
foreach ($buckets as $b) { echo ''.$b."  
\n"; }
echo '  
'."\n";
} else {
$bucket = $\\_GET['bucket'];
$policy='
{"expiration": "2012-01-31T00:00:00Z",
"conditions": [
{"bucket": "'.$bucket.'"},
["starts-with", "$key", ""],
{"acl": "public-read"},
{"success\\_action\\_redirect": "success.php"},
["starts-with", "$Content-Type", ""]
]
}';
/\\*
\\* Calculate HMAC-SHA1 according to RFC2104
\\* See http://www.faqs.org/rfcs/rfc2104.html
\\*/
function hmacsha1($key,$data) {
$blocksize=64;
$hashfunc='sha1';
if (strlen($key)>$blocksize)
$key=pack('H\\*', $hashfunc($key));
$key=str\\_pad($key,$blocksize,chr(0x00));
$ipad=str\\_repeat(chr(0x36),$blocksize);
$opad=str\\_repeat(chr(0x5c),$blocksize);
$hmac = pack(
'H\\*',$hashfunc(
($key^$opad).pack(
'H\\*',$hashfunc(
($key^$ipad).$data
)
)
)
);
return bin2hex($hmac);
}
/\\*
\\* Used to encode a field for Amazon Auth
\\* (taken from the Amazon S3 PHP example library)
\\*/
function hex2b64($str)
{
$raw = '';
for ($i=0; $i < strlen($str); $i+=2)
{
$raw .= chr(hexdec(substr($str, $i, 2)));
}
return base64\\_encode($raw);
}
/\\* Create the Amazon S3 Policy that needs to be signed \\*/
/\\*
\\* Base64 encode the Policy Document and then
\\* create HMAC SHA-1 signature of the base64 encoded policy
\\* using the secret key. Finally, encode it for Amazon Authentication.
\\*/
$base64\\_policy = base64\\_encode($policy);
$signature = hex2b64(hmacsha1($secretkey, $base64\\_policy));
?>

  

[Use a different bucket](.)

php
}
?
[/php]
success.php:
[php]

Upload Success!

# Upload Success!

php
echo "<PSuccessfully uploaded ".$\\_GET['key']." to bucket ".$\\_GET['bucket'].".\n";
$url = "https://".$\\_GET['bucket'].".s3.amazonaws.com/".$\\_GET['key'];
echo '

Direct URL to the file is ['.$url."]('.$url.')

\n";
include '../footer.php';
?>
[/php]
