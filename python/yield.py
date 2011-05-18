#!/usr/bin/env python
#-*- coding:utf8 -*-

#http://fujishinko.exblog.jp/7688121/

def test():
    for i in range(10):
        yield i * 10

for g in test():
    print g
    print "---"
