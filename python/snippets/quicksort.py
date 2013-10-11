

hoge = [5, 14, 10, 15, 13, 4, 2, 7, 19, 12]

import random

def quicksort(seq):
    if len(seq) <= 1:
        return seq
    pivot = seq[random.randint(0, len(seq) - 1)]
    left = []
    right = []
    for s in seq:
        if s <= pivot:
            left.append(s)
        else:
            right.append(s)

    return quicksort(left) + quicksort(right)

print quicksort(hoge)
