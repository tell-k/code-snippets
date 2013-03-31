# -*- coding: utf-8 -*-

import base64


from urllib2 import unquote
src = u"%E3%83%8C%E3%83%A1%E3%83%AD%E3%83%8B%E3%82%A6"
unicode_string = unquote(str(src)).decode('utf-8')
print unicode_string
