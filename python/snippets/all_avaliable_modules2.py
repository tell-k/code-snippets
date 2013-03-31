#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pprint
import commands
import re
ret = commands.getoutput('python -c "help(\'modules\')"')
module_list = []
start = False
for line in ret.split('\n'):
    if re.match(r'[^ ]+[ ]+[^ ]+[ ]+[^ ]+[ ]+[^ ]+$', line):
        start = True
    if start and line == '':
        break
    if not start:
        continue

    line = re.sub(r'[ ]+',r' ', line)
    for module in line.split(' '):
        if module.strip(' ') != '':
            module_list.append(module.strip(' '))

module_list.sort()
pprint.pprint(module_list)
