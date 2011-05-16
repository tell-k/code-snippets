#!/usr/bin/env python
#-*- coding:utf8 -*-

def bucho_make_love(name, lovers=[]):
    lovers.append(name)
    return lovers

print bucho_make_love('haru') #=> ['haru']
print bucho_make_love('ae35') #=> ['haru', 'ae35']
print bucho_make_love('shin') #=> ['haru', 'ae35', 'shin']

