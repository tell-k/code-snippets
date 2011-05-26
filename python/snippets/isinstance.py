usr/bin/env python
#-*- coding:utf8 -*-

class BaseClass:
    def __init__(self):
        pass

class TestClass(BaseClass):
    def __init__(self):
        pass

class TestClass2(BaseClass):
    def __init__(self):
        pass

a = TestClass()
print isinstance(a, TestClass)
print isinstance(a, BaseClass)
print isinstance(a, TestClass2)


