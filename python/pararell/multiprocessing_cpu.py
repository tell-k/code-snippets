# multiprocessing_cpu.py
import multiprocessing


def _cpu_bound_work():
    i = 0
    while i < 100000000:
        i += 1


class TestProcess(multiprocessing.Process):
    def run(self):
        _cpu_bound_work()


if __name__ == '__main__':
    for _ in range(8):
        process = TestProcess()
        process.start()
    for process in multiprocessing.active_children():
        process.join()
