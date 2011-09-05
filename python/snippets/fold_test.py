#!/usr/bin/env python
#-*- coding:utf8 -*-

class TestClass(object):
    """ TestClass だよ 
    python_fold.vimの折りたたみの仕方を確認
    """
    _name = None

    def __init__(self, name = None):
        """ クラスの初期化 """
        if name:
            self._name = name
        
    def hello(self):
        """ 挨拶する 
        名前がセットされていなければ
        helloとだけ表示される
        """
        print 'Hey! My name is ' + self._name if self._name else 'Hello!'

def say_hello(name=None):
    """ TestClassをインスタンス化してhelloする """
    test = TestClass(name)
    test.hello()

if __name__ == '__main__':
    say_hello('hoge') #=> Hey! My name is hoge
    say_hello()       #=> Hello!

