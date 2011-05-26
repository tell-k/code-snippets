#!/usr/local/bin/python
#-*- coding:utf8 -*-

num = 12345

def int_reverse(num, ret=0):
    
    if 10 > num: return ret + num 
    a = num % 10
    ret = ret + a
    remain = (num - a) / 10
    return int_reverse(remain, ret * 10) 
    
print int_reverse(num)
