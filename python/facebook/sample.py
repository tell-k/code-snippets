#!/usr/bin/env python

import facebook

APP_ID = "155480204512923"
API_KEY = "b0ce6cbdc7944d345f64fe07588bda81"
CONSUMER_SECRET = "653d278e3a72405c3ac4398b92706420"
MY_ACCESS_TOKEN = "155480204512923|d2f1a35af1e5a33264d6b5ce.1-100001210518636|zYwbtMHo5Sia7JgIq7Hg1Lg0JSk"

graph = facebook.GraphAPI(MY_ACCESS_TOKEN)
profile = graph.get_object("me")
friends = graph.get_connections("me", "apprequests")

#ret = graph.put_object("me", "feed", message="hello world")
print ret
