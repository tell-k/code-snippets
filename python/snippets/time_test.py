#!/usr/bin/env python
#-*- coding:utf8 -*-

import time
#from dateutil.parse import parse
from datetime import datetime

str = '2011-06-20'
print datetime.strptime(str, '%Y-%m-%d')

