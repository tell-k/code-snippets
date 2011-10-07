#!/usr/bin/env python
#-*- coding:utf8 -*-

#http://www.nishiohirokazu.org/pwe2007/2007/06/post_2.html

# リスト内を順番に出力する関数
def show(data):
        for buf in data:
                if isinstance(buf, list):
                        show(buf);
                else:
                        print buf;

# リストが整数とリストのみで構成されていることを確認する関数
def isList(data):
        ret = True;
        for buf in data:
                if isinstance(buf, list):
                        ret = isList(buf);
                else:
                        if isinstance(buf, int) == False:
                                ret = False;
                                break;
        return ret;

d1 = [1, [5, 4, 4], 5, [[[6], [7, 8], 9], 10]]
d2 = [1, [2, 3, 4], 5, [[[6], [7, 8], 9], 10],"aaa"]
show(d1)
#show(d2)
#print isList(d1)
#print isList(d2)
