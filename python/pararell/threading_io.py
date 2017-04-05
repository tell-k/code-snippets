import threading
import time

# http://ja.pymotw.com/2/threading/
def _io_bound_work(fid):
    big_number = 1000000
    file_number = 10
    for i in range(file_number):
        with open("test_{}_{}.txt".format(fid, i), "w") as fw:
            for j in range(big_number):
                fw.write("line %d\n" % j)

if __name__ == '__main__':
    mainthread = threading.currentThread()
    for fid in range(8):
        t = threading.Thread(target=_io_bound_work, args=(fid,))
        t.start()

    for thread in threading.enumerate():
        if mainthread != thread:
            thread.join()
