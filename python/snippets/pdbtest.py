#!/usr/local/bin/python
#-*- coding:utf8 -*-

#http://docs.python.org/library/operator.html

def div(x, y):
    return x / y

def main():
    x = 6
    import pdb; pdb.set_trace()
    for i in [3, 2, 1, 0]:
        x = div(x, i)
    return x

if __name__ == '__main__':
    main()

#python -m pdb pdbtest.py

#step s    ステップ進む
#list l    現在位置確認
#p var     変数(var)の確認
#return    returnされるところまで処理実行
#continue  最後まで処理を実行
#break x   x行にbreakpoint
#break     ブレークポイントの確認
#clear x   ブレークポイントの削除
#enable x  ブレークポイントの有効
#disable x ブレークポイントの無効
#up        スタックフレームの移動
#down      スタックフレームの移動
#quit      終了
