# -*- coding:utf-8 -*-

# http://uokada.hatenablog.jp/entry/20120930/1349002988

import time
for i in range(1,11):
    time.sleep(1)
    prog = "[%s]" % ("=" * i + ">")
    if i == 10:
        print prog
    else:
        print prog + "\r",
