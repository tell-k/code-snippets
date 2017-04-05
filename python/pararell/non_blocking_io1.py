from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from benchmarker import Benchmarker
import requests

loop = 10
cycle = 1

urls = [
 'http://python.org/',
 'http://www.pocketplaylab.com/',
 'http://github.com/'
]

def download(i, url):
    print('No.{}: Downloading: {}'.format(i, url))
    requests.get(url)
    print('No.{}: Done: {}'.format(i, url))

with ProcessPoolExecutor(max_workers=3) as executer:
    for i, url in enumerate(urls, 1):
        executer.submit(download, i, url)

#with Benchmarker(loop, cycle=cycle) as bench:
#
#    @bench('thread pool')
#    def _(bm):
#        for _ in bm:
#            with ThreadPoolExecutor(max_workers=3) as thread_pool:
#                for i, url in enumerate(urls, 1):
#                    thread_pool.submit(download, i, url)
