

tmp = [0, 1, 2, 3, 4, 5]

def f0(xs):
   return sum(tmp[1::2])

#def f1(xs):
#   return sum([x for x in xs if x % 2 != 0])
#
#def f2(xs):
#   return sum(filter(lambda x: x % 2 != 0, xs))

print f0(tmp)
#print f1(tmp)
#print f2(tmp)
