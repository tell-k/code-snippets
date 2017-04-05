#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://d.hatena.ne.jp/norio515/20111103/1320327714

import sys
from threading import Thread
import cProfile

def spin_for_a_while(number):
    i = 0
    while i < number:
        i += 1

def main_for_cpu(cpu_number):
    big_number = 10000000
    thread_list = []
    if cpu_number == 1:
        spin_for_a_while(big_number)
    else:
        for i in xrange(cpu_number):
            thread = Thread(target=spin_for_a_while, args=(big_number/cpu_number,))
            thread_list.append(thread)
            thread.daemon = True
            thread.start()
    for thread in thread_list:
        thread.join()

if __name__ == "__main__":
    cProfile.run("main_for_cpu(int(sys.argv[1]))")
