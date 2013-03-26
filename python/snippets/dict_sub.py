#!/usr/bin/env python
#-*- coding:utf8 -*-

adict = {"a":"a", "b":"b"}
bdict = {"a":"a", "b":"a", "c": "a"}

hoge = dict((k, v) for (k, v) in bdict.iteritems() if k not in adict or v != adict[k])
print hoge
