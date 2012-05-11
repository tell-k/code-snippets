#!/usr/bin/env python
#-*- coding:utf8 -*-

# create instance

class HogeHoge(object):
    fuga = "fugaaaaa!!!"
    hoge = None
    def __init__(self, hoge):
        self.hoge = hoge

    def shout(self):
        print str(self.hoge) + ' ' + self.fuga

# normal
hoge = HogeHoge("hogedayo!")
hoge.shout()

# use globals
hoge = globals()['HogeHoge']("hogedayo!")
hoge.shout()

# use get attr
import sys
hoge = getattr(sys.modules['__main__'], 'HogeHoge')("hogedayo!")
hoge.shout()

# type
def shout(self):
    print "hohgoaehgaogeag"

another_hoge = type("NewHogeHoge", (object,), dict(a=1, shout=shout))
new_hoge_hoge = another_hoge()
new_hoge_hoge.shout()

#* http://d.hatena.ne.jp/atsuoishimoto/20110402/1301709054
#* http://d.hatena.ne.jp/atsuoishimoto/20110311/1299805971
#* http://d.hatena.ne.jp/atsuoishimoto/20110215/1297742414
#* http://d.hatena.ne.jp/atsuoishimoto/20110130/1296385784
#* http://d.hatena.ne.jp/atsuoishimoto/20101218/1292674355
#* http://d.hatena.ne.jp/atsuoishimoto/20101206/1291620675
#* http://d.hatena.ne.jp/atsuoishimoto/20101113/1289746045
#* http://d.hatena.ne.jp/atsuoishimoto/20101006/1286338675
#* http://www.freia.jp/taka/blog/737/
#* http://blog.livedoor.jp/xaicron/tag/MRO
#* http://d.hatena.ne.jp/amachang/20061007/1160232763
#* http://morchin.sakura.ne.jp/effective_python/metaclass.html
#* http://python-history-jp.blogspot.jp/2010/08/mro.html -> new style は常にダイヤモンド継承になる可能性がある。
#* 動的にクラス http://www.freia.jp/taka/blog/734/
#* 動的に http://d.hatena.ne.jp/atsuoishimoto/20110213/1297560371
#* 動的にメソッドを追加 http://www.ianlewis.org/jp/python-add-class-method
#* perlでもC3 MRO http://perldoc.jp/docs/modules/mro-1.00/mro.pod
