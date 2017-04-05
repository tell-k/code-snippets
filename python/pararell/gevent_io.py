import time
import gevent
from gevent import monkey
monkey.patch_all() # 諸々の標準ライブラリにパッチを当てる

def _io_bound_work(fid):
    big_number = 1000000
    file_number = 10
    for i in range(file_number):
        with open("test_{}_{}.txt".format(fid, i), "w") as fw:
            for j in range(big_number):
                fw.write("line %d\n" % j)

if __name__ == '__main__':
    jobs = [gevent.spawn(_io_bound_work, fid) for fid in range(8)]
    gevent.joinall(jobs)
