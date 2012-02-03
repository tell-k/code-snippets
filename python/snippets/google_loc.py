#!/usr/bin/env python
#-*- coding:utf8 -*-
import re
import sys
import simplejson
from urllib import urlopen, urlencode

def verify_mac_addresses(geo):
    if not geo or len(geo) != 2:
        raise ValueError('Specify 2 mac addresses.\n')

    regex = r'[:-]'.join([r'([0-9a-fA-F]{2})'] * 6)
    for g in geo:
        if not re.match(regex, g):
            raise ValueError('Specify 2 mac addresses.\n')
    return geo

def main():
    geo = verify_mac_addresses(sys.argv[1:])
    QUERY = {
      'version':'1.1.0',
      'host':'maps.google.com',
      'request_address': 'true',
      'address_language':'ja_JP',
      'wifi_towers':
      [
        {
          'mac_address': geo[0],
          'signal_strength':8,
          'age':0
        },
        {
          'mac_address': geo[1],
          'signal_strength':8,
          'age':0
        }
      ]
    }
    print urlencode(QUERY)
    body = urlopen('http://www.google.com/loc/json', urlencode(QUERY)).read()
    print body


if __name__ == '__main__':
    try:
        main()
    except Exception, e:
        print e
