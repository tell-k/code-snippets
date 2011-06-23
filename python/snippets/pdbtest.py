#!/usr/local/bin/python
#-*- coding:utf8 -*-

#http://docs.python.org/library/operator.html

def div(x, y):
    return x / y

def main():
    x = 6
    for i in [3, 2, 1, 0]:
        x = div(x, i)
    return x

if __name__ == '__main__':
    main()

#python -m pdb pdbtest.python

#step s    ステップ進む
#list l    現在位置確認
#p hoge    変数確認
#return    returnされるとこまで
#continue  最後まで
#break x   x行にbreakpoint
#break     ブレーのポイントの確認
#clear x   ブレークポイントの削除
#enable x  ブレークポイントの有効
#disable x ブレークポイントの無効
#up        スタックフレームの移動
#down      スタックフレームの移動
#quit      終了
