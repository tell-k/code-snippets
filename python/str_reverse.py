#!/usr/local/bin/python
#-*- coding:utf8 -*-

str = u'あいうえお'

def str_reverse(str):
    li = list(str)
    l = len(str)
    for i in range(len(li) / 2):
        l = l - 1
        li[i], li[l] = li[l], li[i]
    return ''.join(li)

print str_reverse(str)

