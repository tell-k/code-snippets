#!/usr/bin/env python
#-*- coding:utf8 -*-

lists = range(0, 120)
num = 12

idx, end = 0, 0
while (True):
    slice = lists[idx * num: end + num]
    if not slice:
        break;
    end += num
    idx += 1
    print "exec process" + str(idx)

print '-' * 15

lists = range(0, 120)
idx = 0 #実際の処理にはいらない
while (True):
    slice = lists[0: num]
    lists = list(set(lists) - set(slice))
    if not slice:
        break;
    idx += 1
    print "exec process" + str(idx)

print '-' * 15

lists = range(0, 120)
idx = 0 #実際の処理にはいらない
while (True):
    slice = lists[0: num]
    lists[0: num] = []
    if not slice:
        break;
    idx += 1
    print "exec process" + str(idx)

print '-' * 15

lists = range(0, 120)
idx = 0 #実際の処理にはいらない
while (True):
    slice = lists[0: num]
    del lists[0: num]
    if not slice:
        break;
    idx += 1
    print "exec process" + str(idx)
