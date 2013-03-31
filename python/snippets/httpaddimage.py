#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

def get_image_url(path):
    if re.match(r'^\/\/', path):
        return 'http:' + path
    return path

print get_image_url("//hogehoge.com")
print get_image_url("/hogehoge.com")
print get_image_url("http://hogehoge.com")
print get_image_url("https://hogehoge.com")
