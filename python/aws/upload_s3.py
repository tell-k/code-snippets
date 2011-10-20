#!/usr/bin/env python
#-*- coding:utf8 -*-

from pit import Pit
from boto.s3.connection import S3Connection
from boto.s3.key import Key

conf = Pit.get('aws')
conn = S3Connection(conf['key'], conf['secret'])
bucket = conn.get_bucket('tellkbucket')

k = Key(bucket)
k.key = 'test/'
k.set_contents_from_string('')

k = Key(bucket)
k.key = 'hoge.txt'
k.set_contents_from_string('hogehoge')

k = Key(bucket)
k.key = 'test.txt'
k.set_contents_from_filename('test.txt')
k.set_acl('public-read')
#http://tellkbucket.s3.amazonaws.com/test.txt

k = Key(bucket)
k.key = 'tell-k.png'
k.set_contents_from_filename('tell-k.png')
k.set_acl('public-read')
#http://tellkbucket.s3.amazonaws.com/tell-k.png

k = Key(bucket)
k.key = 'test/tell-k2.png'
with open('tell-k.png') as f:
    k.set_contents_from_file(f)
    k.set_acl('public-read')
#http://tellkbucket.s3.amazonaws.com/tell-k2.png

for l in bucket:
    print l
