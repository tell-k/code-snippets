
from unicodedata import normalize

import sys, codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout)

with open('./templates/core/index.html') as f:

    hoge = f.readlines()
    hoge_body = "".join(hoge)
    hoge_nfc = normalize('NFC', hoge_body.decode('utf8'))
    print hoge_nfc
