#!/usr/bin/env python
#-*- coding:utf8 -*-
"""
    sample for gdata.youtube
    ~~~~~~~~~~~~~~~~~~
        
    :author: tell-k
    :copyright: tell-k. All Rights Reserved.
    :ref: http://developers.facebook.com/docs/test_users/
    :ref: http://facebook-docs.oklahome.net/archives/51976670.html
    :tool: http://www.koikikukan.com/tools/facebook/TestUsers/
""" 
from pit import Pit

conf = Pit.get('gdata')

import gdata.youtube
import gdata.youtube.service

client = gdata.youtube.service.YouTubeService()
query = gdata.youtube.service.YouTubeVideoQuery()

query.vq = '2NE1'
query.max_results = 25
query.start_index = 1
query.racy = 'exclude'
query.format = '5'
query.orderby = 'relevance'

feed = client.YouTubeQuery(query)

for entry in feed.entry:
    print entry.title.text
