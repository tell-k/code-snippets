#!/usr/bin/env python
#-*- coding:utf8 -*-

test = [1, 2, 3, 4, 5]

def map_between1(lst, func):
    return [func(lst[i], lst[i + 1]) for i in range(len(lst) - 1)]

def map_between2(lst, func):
    return (func(lst[i], lst[i + 1]) for i in range(len(lst) - 1))

print map_between1(test, lambda x, y: x + y) #=> [3, 5, 7, 9]
print list(map_between2(test, lambda x, y: x + y)) #=> [3, 5, 7, 9]

