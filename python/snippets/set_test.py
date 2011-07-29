#!/usr/bin/env python
#-*- coding:utf8 -*-

fb = [1, 2, 3, 4, 5]
tw = [1, 2, 3, 4, 5, 6, 8, 10, 5]

r = list(set(fb).union(set(tw)))
print r

fb = [1, 2]
tw = [1]

r = list(set(fb).intersection(set(tw)))
print r

tw = []
print tw

a = [1, 2, 3, 4, 5]
print a
a = [long(v) for v in a]
print a
