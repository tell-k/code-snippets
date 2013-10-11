#!/usr/bin/env python
#-*- coding:utf8 -*-

def lets_take_tea_break(m, e, n, c):
    if pow(m, e) % n == c: return str(m)
    return ""

if __name__ == "__main__":
    import sys

#    for i in range(100000):
#        r = lets_take_tea_break(*[int(i) for i in (i, 17, 3569, 915)])
#        if r:
#            print r

    print("http://cp1.nintendo.co.jp/" + lets_take_tea_break(*[int(i) for i in (sys.argv[1], 17, 3569, 915)]))

