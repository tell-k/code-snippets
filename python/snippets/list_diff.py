#!/usr/local/bin/python
#-*- coding:utf8 -*-

a = [1, 2, 3 ,4, 5]
b = [0, 1, 2, 3 ,4]

diff = list(set(a) - set(b))
print diff
diff = list(set(b) - set(a))
print diff
