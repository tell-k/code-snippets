#!/usr/bin/env python
#-*- coding:utf8 -*-

import datetime
import time


# start
date_start = datetime.date(2011, 1, 1)

d = date_start
for x in xrange(0, 365):
    difference = datetime.timedelta(days=x)
    d = date_start + difference
#    weeknum = d.strftime("%U") # Sunday as the first day of the week
    weeknum = d.strftime("%W") # Monday as the first day of the week
    weekday = d.strftime("%w")
    dayname = d.strftime("%a")
#    weeknum = d.isocalendar()[1] # ISO week number
    print str(d) + ' weeknum ' + str(weeknum) + ' weekday ' + str(weekday) + ' dayname ' + str(dayname)
