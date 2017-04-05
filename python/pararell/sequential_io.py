import time
import os


def _io_bound_work(fid):
    big_number = 1000000
    file_number = 10
    for i in range(file_number):
        with open("test_{}_{}.txt".format(fid, i), "w") as fw:
            for j in range(big_number):
                fw.write("line %d\n" % j)


if __name__ == '__main__':
    for fid in range(8):
        _io_bound_work(fid)
