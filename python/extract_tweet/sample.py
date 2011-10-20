#!/usr/bin/env python
# -*- encoding:utf-8 -*-

#https://twitter.com/#!/kyokaworld/following
#http://blog.kzfmix.com/entry/1298707690
#http://d.hatena.ne.jp/ymotongpoo/20081123/1227430671

import urllib
import simplejson
from mechanize import Browser
from pyquery import PyQuery as pq
from pprint import pprint

SCREEN_NAME = "hogehoge"
FOLLOW_LIST_URL = "https://twitter.com/#!/kyokaworld/following"
TL_JSON_URL = "http://api.twitter.com/1/statuses/user_timeline.json?screen_name=%s"

def main():

    users = []
    except_users = []
    with open("follow.txt") as f:
        index = 0
        flag = False
        for line in f:
            if flag: 
                data = line.strip("\n\r").split(' ')
                users.append(data[0].strip(' '))

            flag = True if line.strip("\n\r") == " フォロー" else False

    with open("except.txt") as f:
        except_users = [line.strip("\n\r") for line in f]

    for user in users:
        if user == '' or user in except_users:
            continue
        print "-" * 100
        ret = simplejson.load(urllib.urlopen(TL_JSON_URL % user))
        for r in ret:
            pprint(r)

if __name__ == '__main__':
    main();
