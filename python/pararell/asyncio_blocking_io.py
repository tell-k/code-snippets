import asyncio
import aiohttp

@asyncio.coroutine
def download(i, url):
    print('No.{}: Downloading: {}'.format(i, url))
    yield from aiohttp.request('GET', url)
    print('No.{}: Done: {}'.format(i, url))

@asyncio.coroutine
def download_parallel(urls):
    tasks = [asyncio.Task(download(i, url)) for i, url in enumerate(urls, 1)]
    yield from asyncio.gather(*tasks)

urls = [
    'http://python.org/',
    'http://www.pocketplaylab.com/',
    'http://github.com/'
]

loop = asyncio.get_event_loop()
loop.run_until_complete(download_parallel(urls))
