import gevent
from gevent import monkey
monkey.patch_all() # 諸々の標準ライブラリにパッチを当てる


def _cpu_bound_work():
    i = 0
    while i < 100000000:
        i += 1


if __name__ == '__main__':
    jobs = [gevent.spawn(_cpu_bound_work) for _ in range(8)]
    gevent.joinall(jobs)
