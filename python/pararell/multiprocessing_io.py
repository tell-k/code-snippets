
import multiprocessing
import time


# http://stackoverflow.com/questions/1559125/string-arguments-in-python-multiprocessing
def _io_bound_work(fid):
    big_number = 1000000
    file_number = 10
    for i in range(file_number):
        with open("test_{}_{}.txt".format(fid, i), "w") as fw:
            for j in range(big_number):
                fw.write("line %d\n" % j)

if __name__ == '__main__':
    for fid in range(8):
        p = multiprocessing.Process(target=_io_bound_work, args=(fid,))
        p.start()
    for process in multiprocessing.active_children():
        process.join()
