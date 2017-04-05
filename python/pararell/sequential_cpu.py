def _cpu_bound_work():
    i = 0
    while i < 100000000:
        i += 1


if __name__ == '__main__':
    for _ in range(8):
        _cpu_bound_work()
