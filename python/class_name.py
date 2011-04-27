#!/usr/local/bin/python
#-*- coding:utf8 -*-


class Test:

    def __init__(self):
        pass

    def get_classname(self):
        return self.__class__.__name__

    def get_type(self):
        return self.__class__

t = Test()
print t.get_type()
