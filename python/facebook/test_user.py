#!/usr/bin/env python
#-*- coding:utf8 -*-
"""
    create test account for facebook
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        
    :author: tell_k
    :copyright: tell-k. All Rights Reserved.
    :ref: http://developers.facebook.com/docs/test_users/
    :ref: http://facebook-docs.oklahome.net/archives/51976670.html
    :tool: http://www.koikikukan.com/tools/facebook/TestUsers/
""" 

import urllib
import cgi
import simplejson
import StringIO
from pit import Pit

conf = Pit.get('fb_app_info')
APP_ID = conf['app_id']
CONSUMER_SECRET = conf['consumer_secret']

#num of test user
DEFAULT_TEST_USER_NUM = 3

def get_app_access_token(app_id, consumer_secret):
    """ get access_token for facebook application  """
    url = "https://graph.facebook.com/oauth/access_token?" + urllib.urlencode(dict(
        client_id=app_id,
        client_secret=consumer_secret,
        grant_type="client_credentials",
    ))
    response = cgi.parse_qs(urllib.urlopen(url).read())
    access_token = response["access_token"][-1]
    return access_token

def _create(app_id, app_token, installed, name):
    """ create test user. """
    base_url = "https://graph.facebook.com/" + app_id + "/accounts/test-users?"
    url = base_url + urllib.urlencode(dict(
                                installed=installed,
                                name=name,
                                method='post',
                                permissions='read_stream',
                                access_token=app_token,
                                ))
    res = urllib.urlopen(url).read() 
    return simplejson.load(StringIO.StringIO(res))

def _delete(test_user_id, app_token):
    """ test user の削除"""
    base_url = "https://graph.facebook.com/" + test_user_id + "?"
    url = base_url + urllib.urlencode(dict(
                                method='delete',
                                access_token=app_token,
                                ))
    res = urllib.urlopen(url).read() 
    return simplejson.load(StringIO.StringIO(res))

def get_all(app_id, app_token):
    """ test user の取得"""
    base_url = "https://graph.facebook.com/" + app_id + "/accounts/test-users?"
    url = base_url + urllib.urlencode(dict(
                                access_token=app_token,
                                ))
    res = simplejson.load(StringIO.StringIO(urllib.urlopen(url).read()))
    return  res['data'] if res and ('data' in res) else []

def delete_all(app_id, app_token):
    """ test user の取得"""
    test_users = get_all(app_id, app_token)
    for user in test_users:
        res = _delete(user['id'], app_token)
        if res == True:
            print "delete succes. test_user: " + str(user['id'])
        else:
            print "delete fail. test_user: " + str(user['id']) + " " + res

def get_user(user_id, app_token):
    """ test user の取得"""
    base_url = "https://graph.facebook.com/%s?"
    url = (base_url % user_id) + urllib.urlencode(dict(access_token=app_token))
    res = urllib.urlopen(url).read() 
    return simplejson.load(StringIO.StringIO(res))

def _make_friends(user_id, friend_id, access_token):
    base_url = "https://graph.facebook.com/%s/friends/%s?method=post&"
    url = (base_url % (user_id, friend_id)) + urllib.urlencode(dict(access_token=access_token))
    res = urllib.urlopen(url).read() 
    return simplejson.load(StringIO.StringIO(res))

def create(app_id, app_token, installed, name_prefix, user_num, test_users):
    name_sample = ['taro', 'jiro', 'hanako', 'sabro', 'shiro', 'goro', 'rokuro']
    for i in range(user_num):
        test_user = _create(APP_ID, app_token, installed, name_prefix + name_sample[i])
        if not test_user:
            continue
        print 'create test user => ' + str(test_user)
        test_users.append(test_user)

def make_friends(test_users):
    friends = test_users[:]
    for user in test_users:
        for friend in friends:
            if user['id'] != friend['id']:
                print 'id:%s friend request to id:%s' % (user['id'], friend['id'])
                _make_friends(user['id'], friend['id'], user['access_token'])

def _create_parser():
    parser = argparse.ArgumentParser(description='command line interface for facebook test user')
    parser.add_argument('dir1')
    parser.add_argument('dir2')
    parser.add_argument('-d')
    parser.add_argument('--version', action='version', version='%(prog)s 0.1')
    return parser

def main():
    parser = _create_parser()
    print 


#    app_token = get_app_access_token(APP_ID, CONSUMER_SECRET)
#    test_users = []
#    create(APP_ID, app_token, 'true', 'liblar', TEST_USER_NUM, test_users)
#    make_friends(test_users)
#    pprint(get_all(APP_ID, app_token))
#    delete_all(APP_ID, app_token)

if __name__ == '__main__':
    main()
