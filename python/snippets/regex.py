#-*- coding:utf8 -*-
#text = "http://example.com?hoge=hoge&bucho=bucho".split('?', 1)
#print text
#
#import re
#text = "testtesthogehoge"
#match = re.search(r'(.+)\((.+)\)', text)
#if match:
#    print dir(match)
#    print match.groups()[1]
#
#
#test = ['aaa', 'bbb']
#print test.index('aaa')
#
#text = 'hoge その他'
#t = re.sub(r' (その他) $', '', text)
#print t
#
#text = '〜〜〜〜〜 a 〜〜'
#t = re.sub(r'〜〜', '〜', text)
#print t

def re_search(regex, text, m):
    for i in range(len(m)):
        m.pop()
    match = re.search(regex, text)
    if match:
        m.append(match)
    return match

def i(func, m):
    for i in range(len(m)):
        m.pop()
    ret = eval(func)
    if ret:
        m.append(ret)
    return ret

import re

text = "hoge fuga piyo"
match = re.search(r'^(.+) (.+) piyo$', text)
if match:
    print match.groups()[0] # hoge
    print match.groups()[1] # fuga

match = re.search(r'^(.+) piyo$', text)
if match:
    print match.groups()[0] # hoge fuga

m = []
if re_search(r'^(.+) (.+) piyo$', text, m):
    print m[0].groups()[0] # hoge
    print m[0].groups()[1] # fuga

if re_search(r'^(.+) piyo$', text, m):
    print m[0].groups()[0] # hoge fuga

m = []
if i("re.search(r'^(.+) (.+) piyo$', text)", m):
    print m[0].groups()[0] # hoge
    print m[0].groups()[1] # fuga

if i("re.search(r'^(.+) piyo$', text)", m):
    print m[0].groups()[0] # hoge fuga

import sta
if sta.sh(x = re.search(r'^(.+) (.+) piyo$', text)):
    print sta.sh.x.groups()[0]

#if funcfunci("re.search(r'^(.+) piyo$', text)", m):
#    print m[0].groups()[0] # hoge fuga
#text = "hoge Gained"
#if re_search(r'(.+) Gained', text, m2):
#    print m2
#
#text = "hogeGained"
#if re_search(r'(.+) Gained', text, m2):
#    print m2
##    print m2.groups()[0]
