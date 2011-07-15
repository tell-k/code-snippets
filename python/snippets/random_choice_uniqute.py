#!/usr/bin/env python
#-*- coding:utf8 -*-
import random


def random_choice_unique(lists, num=4):
    if not lists:
        return []

    if len(lists) <= num:
        return lists

    copy_lists = lists[:]
    results = []
    for i in range(num):
        t = random.choice(copy_lists)
        results.append(t)
        copy_lists.remove(t)

    return results


l = ['1', '2', '3', '4', '5']
print random_choice_unique(l)

l = [1, 2, 3, 4, 5]
print random_choice_unique(l)

l = [[0, 1], [1, 2], [3, 4], [5, 6]]
print random_choice_unique(l)

l = [{'ae': 35}, {'shin': 30}, {'haru': 860}, {'key': 3}, {'easy': 1126}]
print random_choice_unique(l)

#remove はオブジェトでも大丈夫。
class BuchoLover():

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name + " is a bucho lover"

l = [BuchoLover(name) for name in ['ae35', 'shin', 'm_432', 'haru', 'feiz']]
print random_choice_unique(l)
