#!/usr/bin/env python
#-*- coding:utf8 -*-
"""
    create test account for facebook
    ~~~~~~~~~~~~~~~~~~
        
    :author: tell-k
    :copyright: tell-k. All Rights Reserved.
""" 

import urllib
import simplejson
import StringIO


app_id = current_app.config['FACEBOOK_APP_ID']
fb = FacebookAPI(app_id, current_app.config['FACEBOOK_CONSUMER_SECRET'])
app_token = fb.get_app_access_token()

url = "https://graph.facebook.com/" + app_id + "/accounts/test-users?" + urllib.urlencode(dict(
                            installed='false',
                            name='testbucho3',
                            method='post',
                            access_token=app_token,
                            ))
res = simplejson.load(StringIO.StringIO(urllib.urlopen(url).read()))
    for k in res.keys():
        print k + ': ' + res[k]

