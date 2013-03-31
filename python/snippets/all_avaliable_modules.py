#!/usr/bin/env python
# -*- coding: utf-8 -*-

#http://www.ibm.com/developerworks/jp/linux/library/l-pyint/
#http://stackoverflow.com/questions/739993/unable-to-get-a-list-of-installed-python-modules
#http://blife.dip.jp/e85.html

from pprint import pprint
import sys
#print sys.builtin_module_names
#print "--" * 100
#print sys.modules.keys()

from pydoc import ModuleScanner
from string import find
import sys

#modules = {}
#def callback(path, modname, desc, modules=modules):
#    if modname and modname[-9:] == '.__init__':
#        modname = modname[:-9] + ' (package)'
#    if find(modname, '.') < 0:
#        modules[modname] = 1
#def onerror(modname):
#    print modname
#    callback(None, modname, None)
#ModuleScanner().run(callback, onerror=onerror)

modules = []
def callback(path, modname, desc, modules=modules):
    if modname and modname[-9:] == '.__init__':
        modname = modname[:-9]
    if modname not in modules:
        modules.append(modname)
def onerror(modname):
    callback(None, modname, None)
ModuleScanner().run(callback, onerror=onerror)



#modules = []
#def callback(path, modname, desc, modules=modules):
#    modules.append(modname)
##    if find(modname, '.') < 0:
##        modules.append(modname)
#def onerror(modname):
#    callback(None, modname, None)
#ModuleScanner().run(callback, onerror=onerror)
#modules.sort()

#print modules
#import pprint
#pprint.pprint(modules)
