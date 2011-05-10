#!/usr/bin/env python
#-*- coding:utf8 -*-

lists = range(0, 120)

num = 1000

idx = 0
end = 0
while (True):
    slice = lists[idx * num: end + num]
    print len(slice)
    if not slice:
        break;
    end += num
    idx += 1
