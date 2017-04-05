# -*- coding: utf-8 -*-

# http://d.hatena.ne.jp/norio515/20111103/1320327714
import sys
from threading import Thread
import cProfile


def spin_for_a_while(number):
    i = 0
    while i < number:
        i += 1


def write_heavy_data():
    big_number = 100000
    file_number = 10
    for i in xrange(file_number):
        with open("dummy/dummy%d.txt" % i, "w") as fw:
            for j in xrange(big_number):
                fw.write("line %d\n" % j)


def main_for_io(cpu_number):
    big_number = 10000000
    thread_list = []
    if cpu_number == 1:
        spin_for_a_while(big_number)
        write_heavy_data()
    else:
        for i in xrange(cpu_number):
            thread = Thread(target=spin_for_a_while, args=(big_number/cpu_number,))
            thread_list.append(thread)
            thread.daemon = True
            thread.start()

        thread_for_io = Thread(target=write_heavy_data)
        thread_list.append(thread_for_io)
        thread_for_io.daemon = True
        thread_for_io.start()

    for thread in thread_list:
        thread.join()

if __name__ == "__main__":
    cProfile.run("main_for_io(int(sys.argv[1]))")
