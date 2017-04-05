import requests

urls = [
    'http://python.org/',
    'http://www.pocketplaylab.com/',
    'http://github.com/'
]

for i, url in enumerate(urls, 1):
    print('No.{}: Downloading: {}'.format(i, url))
    requests.get(url)
    print('No.{}: Done: {}'.format(i, url))
