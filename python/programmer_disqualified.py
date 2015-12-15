# -*- coding: utf-8 -*-

# 1時間以内に解けなければプログラマ失格となってしまう5つの問題が話題に
# http://www.softantenna.com/wp/software/5-programming-problems/

# 問題1
# forループ、whileループ、および再帰を使用して、リスト内の数字の合計を計算する3つの関数を記述せよ。


def sum_for(nums):
    r = 0
    for n in nums:
        r += n
    return r


def sum_while(nums):
    r = 0
    while(nums):
        r += nums.pop()
    return r


def sum_reqursive(nums):
    if not nums:
        return 0
    return nums.pop() + sum_reqursive(nums)

assert sum_for(range(1, 11)) == 55
assert sum_while(range(1, 11)) == 55
assert sum_reqursive(range(1, 11)) == 55


# 問題2
# 交互に要素を取ることで、2つのリストを結合する関数を記述せよ。
# 例えば [a, b, c]と[1, 2, 3]という2つのリストを与えると、関数は [a, 1, b, 2, c, 3]を返す。

def merge_list(lst1, lst2):
    return [e for sublst in zip(lst1, lst2) for e in sublst]

assert merge_list(['a', 'b', 'c'], [1, 2, 3]) == ['a', 1, 'b', 2, 'c', 3]

# 問題3
# 最初の100個のフィボナッチ数のリストを計算する関数を記述せよ。
# 定義では、フィボナッチ数列の最初の2つの数字は0と1で、次の数は前の2つの合計となる。
# 例えば最初の10個のフィボナッチ数列は、0, 1, 1, 2, 3, 5, 8, 13, 21, 34となる。


def fib(num):
    ret = [0, 1]
    a, b = ret[0], ret[1]
    for i in range(num - 2):
        a, b = b, b + a
        ret.append(b)
    return ret

assert fib(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
assert len(fib(100)) == 100

# 問題4
# 正の整数のリストを与えられたとき、数を並び替えて可能な最大数を返す関数を記述せよ。
# 例えば、[50, 2, 1, 9]が与えられた時、95021が答えとなる(解答例)。
# https://blog.svpino.com/2015/05/08/solution-to-problem-4


def max_combi(nums, ret=[]):
    if not nums:
        return int(''.join(map(str, ret)))
    r = 0
    for n in nums:
        m = max_combi(list(set(nums) - set([n])), ret + [n])
        if r <= m:
            r = m
    return r

assert max_combi([50, 2, 1, 9]) == 95021

# 問題5
# 1,2,…,9の数をこの順序で、”+”、”-“、またはななにもせず結果が100となるあら
# ゆる組合せを出力するプログラムを記述せよ。
# 例えば、1 + 2 + 34 – 5 + 67 – 8 + 9 = 100となる(解答例)
#
# (適切な関数名が思い浮かばない...)


def q5(nums, index=0, lst=[]):
    if index == len(nums):
        evl = eval(''.join(lst))
        if evl == 100:
            return [''.join(lst)]
        return []
    ret = []
    num = nums[index]
    ret += q5(nums, index + 1, lst + [str(num)])
    if index != 0:
        ret += q5(nums, index + 1, lst + [' + {}'.format(num)])
        ret += q5(nums, index + 1, lst + [' - {}'.format(num)])
    return ret

answer = [
    '123 + 45 - 67 + 8 - 9',
    '123 + 4 - 5 + 67 - 89',
    '123 - 45 - 67 + 89',
    '123 - 4 - 5 - 6 - 7 + 8 - 9',
    '12 + 3 + 4 + 5 - 6 - 7 + 89',
    '12 + 3 - 4 + 5 + 67 + 8 + 9',
    '12 - 3 - 4 + 5 - 6 + 7 + 89',
    '1 + 23 - 4 + 56 + 7 + 8 + 9',
    '1 + 23 - 4 + 5 + 6 + 78 - 9',
    '1 + 2 + 34 - 5 + 67 - 8 + 9',
    '1 + 2 + 3 - 4 + 5 + 6 + 78 + 9',
]

for result in q5([1, 2, 3, 4, 5, 6, 7, 8, 9]):
    assert result in answer

# 参考

# http://shogon.hatenablog.com/entry/2015/05/14/215432
# http://mattn.kaoriya.net/software/vim/20150527121332.htm
# http://blog.kazuhooku.com/2015/05/c155.html
# http://pythoniclife.hatenablog.com/entry/2015/05/12/041634
# http://d.hatena.ne.jp/xef/20121027/p2
