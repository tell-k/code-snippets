#!/usr/bin/env python

import facebook

APP_ID =""
API_KEY =""
CONSUMER_SECRET =""
MY_ACCESS_TOKEN =""

graph = facebook.GraphAPI(MY_ACCESS_TOKEN)
profile = graph.get_object("me")
friends = graph.get_connections("me", "apprequests")

#ret = graph.put_object("me", "feed", message="hello world")
print ret
