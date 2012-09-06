# coding: utf-8

#http://qiita.com/items/41e1376c41d8c15e8894
from random import randint

def match(seq, r=100):
    from random import randint
    # 奇数個の時に先頭周辺の要素がボッチになるのが嫌なら、先に後ろの方の
    # 要素を取り除いて偶数にしておくこと.
    while len(seq) >= 2:
        # 引数を省略すると末尾の要素を取り出す.
        print seq
        a = seq.pop()
        # 配列の後ろから r の範囲内でランダムに選択し取り出す.

        #print r
        #print len(seq)
        #print min(r, len(seq))

        b = seq.pop(-randint(1, min(r, len(seq))))
        yield a, b

def test(n, r):
    for a, b in match(range(n), r):
        assert a - b < 4

import sys
test(20, 2)

#0 1 2 3 4
#4 | 0 1 2 3  # seq.pop
#
# r と 残ったリストのlenを min関数に掛けて、探索数を決定
#min(2, len([0, 1, 2, 3])) # => 2
#
# そのリストの末尾から探索数の範囲内でrandomで要素をpopする。
#
#b = seq.pop(-randint(1, 2))
# => 1 2 3 4 のウチ 3 4 が対象範囲でranditでどちらが選択される
# で末尾と その選択された結果がを比較してる

import cgi
#query = cgi.parse_qs("hoge=hoge&fuga=fuga")
#print query["hoge"]

import urllib
params = {
    "hoge": "fuga",
    "piyo": None,
}
#print urllib.urlencode({'key': ['value1', 'value2']})
#print urllib.urlencode({'key': ['value1', 'value2']}, doseq=True)
#print urllib.urlencode(params, True)

print urllib.urlencode([(k, v) for k, v in params.items() if v is not None])
print urllib.urlencode(filter(lambda x: x is not None, params))
