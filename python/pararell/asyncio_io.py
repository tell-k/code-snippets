import asyncio

@asyncio.coroutine
def _io_bound_work(fid):
    big_number = 1000000
    file_number = 10
    for i in range(file_number):
        with open("test_{}_{}.txt".format(fid, i), "w") as fw:
            for j in range(big_number):
                fw.write("line %d\n" % j)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [asyncio.ensure_future(_io_bound_work(i)) for i in range(8)]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
