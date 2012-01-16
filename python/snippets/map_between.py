#!/usr/bin/env python
#-*- coding:utf8 -*-

from itertools import imap, ifilter
from benchmarker import Benchmarker
import time
import os

test = range(10000000)

def map_between1(x, func):
    return list(imap(func, x, x[1:]))

def map_between2(lst, func):
    itr = iter(lst)
    x = itr.next()
    for y in itr:
        yield func(x, y)
        x = y

def map_between3(lst, func):
    return [func(lst[i], lst[i + 1]) for i in range(len(lst) - 1)]

def map_between4(lst, func):
    return (func(lst[i], lst[i + 1]) for i in range(len(lst) - 1))

def map_between5(list, func):
    #http://chonan.blog.pid0.org/2012/01/python-2.html
    return map(func, list[:-1], list[1:])


class List(list):
    def map_between1(self, func):
        return list(imap(func, self, self[1:]))

func = lambda x, y: x + y

#ret = map_between3(test, func)
#for r in ret:
#    v = r
#print int(os.popen('/bin/ps -o rss %d' % os.getpid()).readlines()[-1])
#time.sleep(100000)

with Benchmarker() as bm:
    with bm('map_between1'):
        ret = map_between1(test, func)
        for r in ret:
            break
    with bm('map_between2'):
        ret = list(map_between2(test, func))
        for r in ret:
            break
    with bm('map_between3'):
        ret = map_between3(test, func)
        for r in ret:
            break
    with bm('map_between4'):
        ret = list(map_between4(test, func))
        for r in ret:
            break

