#!/usr/bin/env python

from time import sleep
from multiprocessing import Pool
from random import randint

#http://d.hatena.ne.jp/mizchi/20110520/1305837948

num = 20

def sleep_sort(n):
    sleep(n)
    print(n)

Pool(num).map(
        sleep_sort, 
        [randint(1, num) for i in xrange(num)]
        )
