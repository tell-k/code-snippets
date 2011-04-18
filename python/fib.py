#!/usr/local/bin/python
#-*- coding:utf8 -*-

num = 7

#in  0 1 2 3 4 5 6
#out 0 1 1 2 3 5 8

def fib(num):
    if (2 > num): return num
    return fib(num - 1) + fib(num - 2) 
    
def fib2(num):
    if (2 > num): return num

    a = 0
    b = 1
    loop = num - 1
    for i in range(loop):
        ret = a + b
        a, b = b, ret

    return ret 

print fib(num)
print fib2(num)
