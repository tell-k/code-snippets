#!/usr/bin/env python
#-*- coding:utf8 -*-

import re

akey = 'total_cost_xxx'
bkey = 'total_min_cost_xxx'
print re.sub(r'^(total_(min_|))cost_', r'\1monthly_cost_', akey)
print re.sub(r'^(total_(min_|))cost_', r'\1monthly_cost_', bkey)

#key = "total_min_cost"
#newkey = re.sub(r'total_min_cost', 'total_monthly_min_cost', key)
#print newkey
#newkey = re.sub(r'total_cost', 'total_monthly_cost', newkey)
#print newkey

