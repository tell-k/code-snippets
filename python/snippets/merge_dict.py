#!/usr/bin/env python
#-*- coding:utf8 -*-
from collections import Counter

def merge_dict(d1, d2, func=lambda x, y: y):
    """ 辞書の結合
    >>> d1
    {'a': 1, 'c': 3, 'b': 2}
    >>> merge_dict(d1, d1)
    {'a': 1, 'c': 3, 'b': 2}
    >>> merge_dict(d1, d1, lambda x, y: x + y)
    {'a': 2, 'c': 6, 'b': 4}
    """
    d1 = d1.copy()
    d2 = d2.copy()
    for k, v in d2.iteritems():
        d1[k] = func(d1[k], v) if k in d1 else v
    d2.update(d1)
    return d2

dict_1 = {'a': 1, 'c': 3, 'b': 2}
dict_2 = {'c': 1, 'd': 3, 'e': 2}
print merge_dict(dict_1, dict_2) #=>
d1 = {'a': 1, 'c': 3, 'b': 2}
d2 = {'a': 1, 'c': -3, 'b': -3}

def merge_dict_add_values(d1, d2):
    return dict(Counter(d1) + Counter(d2))

def merge_dict(d1, d2, func=lambda x, y: y):
    d1 = d1.copy()
    d2 = d2.copy()
    for k, v in d2.iteritems():
        d1[k] = func(d1[k], v) if k in d1 else v
    d2.update(d1)
    return d2

print merge_dict_add_values(d1, d2) #=> {'a': 2}
print merge_dict(d1, d2, lambda x, y: x + y) #=> {'a': 2, 'c': 0, 'b': -1}

dict_1.update(dict_2)
print dict_1 #=>
