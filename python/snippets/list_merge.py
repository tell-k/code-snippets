#!/usr/bin/env python
#-*- coding:utf8 -*-

alist = [
        (3,),
        (1,),
        (5,),
]

blist = [
        (4,),
        (2,),
        (6,),
]
ret = [a[0] for a in alist+blist]

for r in ret:
    print r
