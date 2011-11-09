#!/usr/bin/env python
#-*- coding:utf8 -*-


from datetime import date
from calendar import monthrange

def get_month_last_date(year, month):
    """ 月末日を取得 """
    youbi, day = monthrange(year, month)
    return date(year, month, day)


print get_month_last_date(2011, 1)
print get_month_last_date(2011, 2)
print get_month_last_date(2011, 3)
print get_month_last_date(2011, 4)
print get_month_last_date(2011, 5)
print get_month_last_date(2011, 6)
print get_month_last_date(2011, 7)
print get_month_last_date(2011, 8)
print get_month_last_date(2011, 9)
print get_month_last_date(2011, 10)
print get_month_last_date(2011, 11)
print get_month_last_date(2011, 12)
