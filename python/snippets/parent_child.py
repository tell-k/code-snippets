# -*- coding: utf-8 -*-

class Parent(object):

    def __init__(self):
        print "parent"

class Mother(object):

    def __init__(self):
        print "mother"

class Father(object):

    def __init__(self):
        print "mother"

class Child1(Parent):
    """ 親の__init__しか呼ばない = マザコン or ファザコン """
    pass

class Child2(Parent):
    """ 自分の__init__しか呼ばない = ナルシスト """

    def __init__(self):
        print "child2"

class Child3(Mother, Father, Parent):
    """ 親の__init__を読んだ後、自分の__init__を呼ぶ = 全うな子 """

    def __init__(self):
        super(self.__class__, self).__init__()
        super(self.__class__, self).__init__()
        print "child3"

Child1()
print "-" * 10
Child2()
print "-" * 10
Child3()
