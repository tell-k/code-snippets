import numpy as np
cimport numpy as np
cimport cython

cdef random_unique_numbers(num, end, start=1):
    numbers = []
    end += 1
    while len(numbers) < num:
        numbers += set(np.random.randint(start, end, num - len(numbers)))
    return list(numbers)


cdef random_unique_numbers2(num, end):
    numbers = set()
    cdef int l = 0
    end += 1
    while l < num:
        numbers = numbers.union(np.random.randint(1, end, num - l))
        l = numbers.__len__()
    return list(numbers)
