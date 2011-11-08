#!/usr/bin/env python
#-*- coding:utf8 -*-

from itertools import izip

def invert_dict(d):
    return dict([(v, k) for k, v in d.iteritems()])

def invert_dict_fast(d):
    return dict(izip(d.itervalues(), d.iterkeys()))

sample = {1: 'test', 2: 'test2', 3: 'test3', 4: 'test4', 5: 'test5'}

print invert_dict(sample)
print invert_dict_fast(sample)
