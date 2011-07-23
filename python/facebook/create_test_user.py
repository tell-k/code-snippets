#!/usr/bin/env python
#-*- coding:utf8 -*-
"""
    create test account for facebook
    ~~~~~~~~~~~~~~~~~~
        
    :author: tell-k
    :copyright: tell-k. All Rights Reserved.
""" 

import urllib
import cgi
import simplejson
import StringIO

#set your app_id, consumer_secret
APP_ID = ""
CONSUMER_SECRET = ""

#num of test user
TEST_USER_NUM = 2

def get_app_access_token(app_id, consumer_secret):
    """ 登録Facebookアプリ自体のアクセストークンを取得 """
    url = "https://graph.facebook.com/oauth/access_token?" + urllib.urlencode(dict(
        client_id=app_id,
        client_secret=consumer_secret,
        grant_type="client_credentials",
    ))
    response = cgi.parse_qs(urllib.urlopen(url).read())
    access_token = response["access_token"][-1]
    return access_token

def get_test_user(app_id, app_token, installed, name):
    """ test user の取得"""
    base_url = "https://graph.facebook.com/" + app_id + "/accounts/test-users?"
    url = base_url + urllib.urlencode(dict(
                                installed=installed,
                                name=name,
                                method='post',
                                access_token=app_token,
                                ))
    return simplejson.load(StringIO.StringIO(urllib.urlopen(url).read()))

def make_friends(app_id, app_token, installed, name):
    pass

if __name__ == '__main__':
    test_user_ids = {}

    app_token = get_app_access_token(APP_ID, CONSUMER_SECRET)

    for i in range(TEST_USER_NUM):
        test_user = get_test_user(APP_ID, app_token, 'false', 'testbucho' + str(i))
        for k in test_user.keys():
            print k + ': ' + test_user[k]
            if k == 'id':
                test_user_ids.append(test_user[k])
