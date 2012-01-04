#!/usr/bin/env python
#-*- coding:utf8 -*-

from itertools import imap, ifilter

test = [1, 2, 3, 4, 5]


def map_between(x, func):
    return list(imap(func, x, x[1:]))

print map_between(test, lambda x, y: x + y) #=> [3, 5, 7, 9]

def map_between2(lst, func):
    itr = iter(lst)
    x = itr.next()
    for y in itr:
        yield func(x, y)
        x = y

print list(map_between2(test, lambda x, y: x + y)) #=> [3, 5, 7, 9]

def map_between3(lst, func):
    itr = iter(lst)
    x = itr.next()
    ret = []
    for y in itr:
        ret.append(func(x, y))
        x = y
    return ret

print map_between3(test, lambda x, y: x + y) #=> [3, 5, 7, 9]

def map_between4(lst, func):
    return [func(lst[i], lst[i + 1]) for i in range(len(lst) - 1)]

print map_between4(test, lambda x, y: x + y) #=> [3, 5, 7, 9]

class List(list):

    def map_between(self, func):
        return list(imap(func, self, self[1:]))

    def map_between4(self, func):
        return [func(lst[i], lst[i + 1]) for i in range(len(lst) - 1)]

mylist = List(test)
print mylist.map_between(lambda x, y: x + y) #=> [3, 5, 7, 9]
