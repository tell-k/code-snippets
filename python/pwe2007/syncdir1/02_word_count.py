#!/usr/bin/env python
#-*- coding:utf8 -*-

#http://www.nishiohirokazu.org/pwe2007/2007/06/post_1.html

import re
text = "  　   It's , fine day, 2000 isn't it? Yes, it is! it's isn't YES 　 test 2000 years is! is?"

r = re.compile('(^[^a-zA-Z]+|[^a-zA-Z]+$)')

words = [re.sub(r, '', word.lower()) for word in text.strip().split(' ') if re.sub(r, '', word) != '']
wc = {}
for k in words:
    wc.setdefault(k, 0)
    wc[k] += 1

for k, v in sorted(wc.iteritems(), key=lambda (k, v): (v, k), reverse=True):
    print k + ' => ' + str(v)
