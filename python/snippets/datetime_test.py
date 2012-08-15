#!/usr/bin/env python
#-*- coding:utf8 -*-

import re
from datetime import date,datetime,timedelta

test = "2012-08-01 00:00:03"
if not re.search(r'^[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}$', test):
    print "not match"
    exit()

dt1 = datetime.strptime(test, "%Y-%m-%d %H:%M:%S")

test = "2012-02-29 00:00:03"
dt2 = datetime.strptime(test, "%Y-%m-%d %H:%M:%S")

if dt1 > dt2:
    print "success"

now = datetime.now()
test = "2012-07-24 13:00:03"
dt2 = datetime.strptime(test, "%Y-%m-%d %H:%M:%S")

if now > dt2:
    print "now is greater"

today = date.today()
today += timedelta(30)

print today.year
print today.month
print today.day

todatetime = datetime(today.year, today.month, today.day, 0, 0, 0)
print todatetime
