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

import re
text = "Gained"
if re.search(r'\\Ug\\Eained', text):
    print "match"
