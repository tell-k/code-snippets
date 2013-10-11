# -*- coding:utf-8 -*-

# from __future__ import print_function

# fizzbuzz = (lambda branch, const, remzero, identity:
#                (lambda k : branch(k)(remzero(15), const("fizzbuzz"),
#                (lambda k : branch(k)(remzero(3), const("fizz"),
#                (lambda k : branch(k)(remzero(5), const("buzz"),
#                identity)))))))
#                ((lambda k :
#                    (lambda pred, succ, fail:
#                        (lambda n : succ(k)(n) if pred(n) else fail(k)(n)))),
#                 (lambda x: (lambda k : (lambda _: k(x)))),
#                 (lambda x : (lambda n : n % x == 0)),
#                 (lambda k : (lambda n : k(n))))

# _fizzbuzz = lambda *args: print(args[0][1]) if args[0][0] else _fizzbuzz(*args[1:])
# fizzbuzz = lambda x: _fizzbuzz(
#           ((x % 15 == 0), "fizzbuzz"),
#           ((x % 3 == 0), "fizz"),
#           ((x % 5 == 0), "buzz"),
#           (True, x),
#           )
# for i in range(1, 101):
#    fizzbuzz(i)

#import sys
#sys.stdout.write("fizz")
#
#print sys.stdout.readinto()
#['__class__', '__delattr__', '__doc__', '__enter__', '__exit__',
#'__format__', '__getattribute__', '__hash__', '__init__', '__iter__',
#'__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
#'__sizeof__', '__str__', '__subclasshook__', 'close', 'closed',
#'encoding', 'errors', 'fileno', 'flush', 'isatty', 'mode',
#'name', 'newlines', 'next', 'read', 'readinto', 'readline',
#'readlines', 'seek', 'softspace', 'tell', 'truncate',
#'write', 'writelines', 'xreadlines']

#for i in range(1, 101):
#    if i % 3 == 0:
#        sys.stdout.write("fizz")
#    if i % 5 == 0:
#        print("buzz")
#    else:
#        print "\n%d" % i if i % 3 == 0 else i
#test = {
#    "20130802": 3,
#    "20130801": 100,
#    "20130803": 5,
#    "20130800": 100,
#    "20130804": 10,
#}
#
#print test
#print sorted(test.items())

import sys
for i in range(1, 101):
    if i % 3 == 0:
        sys.stdout.write("fizz")
    if i % 5 == 0:
        print "buzz"
    else:
        print "\n%d" % i if i % 3 == 0 else i
