import threading
from Queue import Queue
import os, time
import urllib2
import cProfile

url_queue = Queue()
rlock = threading.RLock()

save_dir = './img'

class ImgDownload(threading.Thread):
    def run(self) :
        def get_filename(url):
            val = url.rsplit('/')
            return val[len(val)-1]

        while True:
            try:
                url = url_queue.get_nowait()
            except:
                break
            save_file = os.path.join(save_dir, get_filename(url))
            html = urllib2.urlopen(url).read()
            with open(save_file, "w") as fp:
                fp.write(html)
            with rlock: print(url)


def main():
    if False == os.path.exists(save_dir):
        os.makedirs(save_dir)
    url = 'http://blog-imgs-35.fc2.com/p/y/s/pyshu/img%d.png'
    for n in range(10):
        url_queue.put(url%n)
    MAX_THREAD = 4
    threads = []
    for n in range(MAX_THREAD):
        threads.append(ImgDownload())

    start_time = time.clock()
    for thd in threads:
        thd.start()
    for thd in threads:
        thd.join()
    finish_time = time.clock()
    print('time = %f(s)' % (finish_time-start_time))


if __name__ == '__main__':
    cProfile.run("main()")
