
from Queue import Queue
import threading
import os
import time
import urllib2
import cProfile

url_queue = Queue()
rlock = threading.RLock()

save_dir = './img'


def get_filename(url):
    val = url.rsplit('/')
    return val[len(val) - 1]


def download(url):
    save_file = os.path.join(save_dir, get_filename(url))
    html = urllib2.urlopen(url).read()
    with open(save_file, "w") as fp:
        fp.write(html)


def main():
    if False == os.path.exists(save_dir):
        os.makedirs(save_dir)
    url = 'http://blog-imgs-35.fc2.com/p/y/s/pyshu/img%d.png'

    start_time = time.clock()
    for n in range(10):
        download(url % n)
    finish_time = time.clock()
    print('time = %f(s)' % (finish_time - start_time))


if __name__ == '__main__':
    cProfile.run("main()")
