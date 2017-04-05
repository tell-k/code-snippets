

def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)


def fib2(n):
    if n < 1:
        return n
    a, b = 1, 0
    while n > 1:
        a, b = (a + b), a
        n -= 1
    return a
