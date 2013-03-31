# coding:utf8

# http://key2.jp/~yskhashi/wordpress/?p=427
# http://0xcc.net/blog/archives/000191.html
# http://d.hatena.ne.jp/CortYuming/20080717/p4

from unicodedata import normalize
import htmlentitydefs

hoge1 = u"ガ"
print hoge1

hoge2 = u"ガ"
print hoge2

nfd_str = normalize('NFD', hoge1)
print nfd_str
#nfd_str_encode = nfd_str.encode('utf8')

nfc_str = normalize('NFC', hoge1)
#nfc_str_encode = nfc_str.encode('utf8')
print nfc_str

assert hoge1 == nfd_str
assert hoge2 == nfc_str

print hoge2
