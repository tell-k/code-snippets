import random
from benchmarker import Benchmarker
import numpy as np

from randutils import random_unique_numbers, random_unique_numbers2

MAX_NUM = 10000000
CHOICE_NUM = 100
LOOP = 100000


with Benchmarker(100000, cycle=1) as bench:

    @bench('random_unique_numbers')
    def _(bm):
        for _ in bm:
            random_unique_numbers(CHOICE_NUM, MAX_NUM)

    @bench('random_unique_numbers2')
    def _(bm):
        for _ in bm:
            random_unique_numbers2(CHOICE_NUM, MAX_NUM)

    @bench('random.sample')
    def _(bm):
        for _ in bm:
            random.sample(range(1, MAX_NUM + 1), CHOICE_NUM)
