#!/usr/bin/env python
#-*- coding:utf8 -*-

import re

func = lambda x: [ int(friend_id) for friend_id in x.split(",") ] if re.compile('^([0-9]|[1-9][0-9, ]*[0-9])$').match(x) else None
#print func('hogeg , 1hogege,12312')
#print func('10212, , ')
#print func('10212, 11, 90')
#print func('10212, 11, 90,')
#print func('0')
#print func('9')


def _get_friend_ids_filter():
    return lambda x: [ int(friend_id) for friend_id in x.split(",") ] \
        if (type(x) == str and re.compile('^([0-9]|[1-9][0-9, ]*[0-9])$').match(x)) else None

func2 = _get_friend_ids_filter()
print func2(None)
print func2("1231,232")
