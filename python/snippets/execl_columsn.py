from string import ascii_uppercase
from operator import add
from itertools import product, count, izip
from string import ascii_uppercase

def number_to_columname(number):
    string = ''
    while True:
        number -= 1
        string = ascii_uppercase[number % 26] + string
        number /= 26
        if not number:
            return string

def cycle(string):
    for i in count(1):
        for s in product(string, repeat=i):
            yield reduce(add, s)


def number_to_columname2(n, string=ascii_uppercase):
    return [c + str(r) for r, c in izip(range(1, n + 1), cycle(string))]

print([number_to_columname(i) for i in range(1, 100)])
print([number_to_columname(i) for i in range(1, 100)])
