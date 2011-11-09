#!/usr/bin/env python
#-*- coding:utf8 -*-

from time import time, ctime, strptime, strftime

start = time() + 3600
end = time()

print start - end

print strftime("%Y-%m-%d %H:%M:%S", strptime(ctime(start)))
print strftime("%Y-%m-%d %H:%M:%S", strptime(ctime(end)))
