
import re

h = '1234567'
if not re.search(r'^[0-9]{7}$', h):
    print h

h = ' '
if h == '' or h == None:
   print "missing1"

if not h:
   print "missing2"
