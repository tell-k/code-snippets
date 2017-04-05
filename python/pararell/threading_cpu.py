# threading_cpu.py
import threading

def _cpu_bound_work():
    i = 0
    while i < 100000000:
        i += 1

class TestThread(threading.Thread):
    def run(self):
        _cpu_bound_work()

if __name__ == '__main__':
    mainthread = threading.currentThread()
    for _ in range(8):
        thread = TestThread()
        thread.start()
    for thread in threading.enumerate():
        if mainthread != thread:
            thread.join()
