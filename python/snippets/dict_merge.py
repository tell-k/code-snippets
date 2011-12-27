#!/usr/bin/env python
#-*- coding:utf8 -*-

t = {'test1': 1, 'test2': 2, 'test3': 3, 'test5': 5}
t2 = {'test1': 2,  'test3': 4, 'test2': 3, 'test4': 4}
#t2.update(dict(map(lambda x: (x, t[x] + t2[x]) if x in t2 else (x, t[x]), t)))
#print sorted(t2.items(), reverse=True)

def merge_dict(d1, d2, merge=lambda x, y: y):
    d1 = d1.copy()
    d2 = d2.copy()
    for k, v in d2.iteritems():
        if k in d1:
            d1[k] = merge(d1[k], v)
        else:
            d1[k] = v
    d2.update(d1)
    return d2

print merge_dict(t, t2)   #=> {'test1': 2, 'test3': 4, 'test2': 3, 'test5': 5, 'test4': 4}
print merge_dict(t2, t)   #=> {'test1': 1, 'test3': 3, 'test2': 2, 'test5': 5, 'test4': 4}
print merge_dict(t, t2, lambda x, y: x + y) #=>{'test1': 3, 'test3': 7, 'test2': 5, 'test5': 5, 'test4': 4}
print merge_dict(t2, t, lambda x, y: x + y) #=>{'test1': 3, 'test3': 7, 'test2': 5, 'test5': 5, 'test4': 4}
