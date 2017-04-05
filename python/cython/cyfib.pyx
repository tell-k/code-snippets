
def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)

def fib_int(int n):
    if n < 2:
        return n
    return fib_int(n-2) + fib_int(n-1)


def fib_cdef(int n):
    return fib_in_c(n)

cdef int fib_in_c(int n):
    if n < 2:
        return n
    return fib_in_c(n-2) + fib_in_c(n-1)

cpdef int fib_cpdef(int n):
    if n < 2:
        return n
    return fib_cpdef(n-2) + fib_cpdef(n-1)

def fib2(n):
    if n < 1:
        return n
    a, b = 1, 0
    while n > 1:
        a, b = (a + b), a
        n -= 1
    return a

def fib2_int(int n):
    if n < 1:
        return n
    a, b = 1, 0
    while n > 1:
        a, b = (a + b), a
        n -= 1
    return a

def fib2_cdef(int n):
    return fib2_in_c(n)


cdef unsigned int fib2_in_c(int n):
    if n < 1:
        return n
    a, b = 1, 0
    while n > 1:
        a, b = (a + b), a
        n -= 1
    return a

cpdef unsigned int fib2_cpdef(int n):
    if n < 1:
        return n
    a, b = 1, 0
    while n > 1:
        a, b = (a + b), a
        n -= 1
    return a
