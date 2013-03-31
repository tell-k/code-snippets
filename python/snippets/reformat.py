# -*- coding: utf-8 -*-

import sys, codecs

str_num = 50
sys.stdout = codecs.getwriter("utf-8")(sys.stdout)

with open('tes') as f:
    for line in f:
        line = unicode(line.strip('\n'), 'utf-8')
        if len(line) > str_num:
            print line[:str_num]
            print line[str_num:]
        else:
            print line
