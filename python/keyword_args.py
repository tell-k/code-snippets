#!/usr/bin/env python
#-*- coding:utf8 -*-

def testfunc(test=None, test2=None):
    print test
    print test2

params = [
    {'test': 'hoge'},
    {'test2': 'hoge2'},
]

for param in params:
    testfunc(**param)
    print "---------"
