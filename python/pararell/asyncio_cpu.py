import asyncio

@asyncio.coroutine
def _cpu_bound_work():
    i = 0
    while i < 100000000:
        i += 1

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [asyncio.ensure_future(_cpu_bound_work()) for _ in range(8)]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
