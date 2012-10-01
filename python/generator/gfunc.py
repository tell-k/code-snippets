# -*- coding: utf-8 -*-

# http://www.slideshare.net/kwatch/php55

def gfunc():
   i = 0
   yield i
   i += 1
   yield i
   i += 1
   yield i

g = gfunc()
for x in g:
    print x

print "-" * 10
#------------

def toggle(odd, even):
    while True:
        yield odd
        yield even

for t in toggle("red", "blue"):
    print t
    break

print "-" * 10
#------------

def fib():
    x = 0
    y = 1
    while True:
        yield x
        (x, y) = (y, x+y)

for x in fib():
    if x >= 100:
        break
    print x

print "-" * 10
#------------
# 0 1 2 3 4 5 6
# 0 1 1 2 3 5 8

def fib2(a):
    x = 0
    y = 1

    if a < 1:
        return 0

    for i in range(a - 1):
        r = x + y
        (x, y) = (y, x + y)

    return r

#print fib2(0)
#print fib2(1)
print fib2(11)

print "-" * 10
#------------

def each_line(filename):
    with open(filename) as f:
        for line in f:
            yield line

def each_field(g):
    for line in g:
        hoge = line.replace("\n", "").replace("hoge", "")
        yield  hoge

g = each_line("sample.txt")
g = each_field(g)

for line in g:
    print line

print "-" * 10
def gfunc2():
    arg = yield
    while True:
        arg = arg * 100
        yield arg

g2 = gfunc2()
print g2.next()
print g2.send(5)
print g2.send(1)
print g2.send(4)
