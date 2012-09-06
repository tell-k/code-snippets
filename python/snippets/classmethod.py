#-*- coding:utf8 -*-

class User(object):

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.call_san(self.name)

    @classmethod
    def call_san(cls, name):
        return "%s san" % name

hoge = User("hoge")
print hoge #=> hoge san
print User.call_san("fuga") #=> fuga san
