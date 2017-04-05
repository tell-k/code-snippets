from gevent import monkey
monkey.patch_all()
from gevent.pool import Pool

import requests

urls = [
    'http://python.org/',
    'http://www.pocketplaylab.com/',
    'http://github.com/'
]


def download(i, url):
    print('No.{}: Downloading: {}'.format(i, url))
    requests.get(url)
    print('No.{}: Done: {}'.format(i, url))

pool = Pool(size=3)
for i, url in enumerate(urls, 1):
    pool.apply_async(download, args=[i, url])
pool.join()
