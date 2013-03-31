#!/usr/bin/env python
#-*- coding:utf8 -*-

from pit import Pit
import boto
from boto import dynamodb, connect_dynamodb

conf = Pit.get('aws')
conn = connect_dynamodb(conf['key'], conf['secret'], host="dynamodb.ap-northeast-1.amazonaws.com")

print conn.list_tables()

message_table_schema = conn.create_schema(
        hash_key_name='forum_name',
        hash_key_proto_value='S',
        range_key_name='subject',
        range_key_proto_value='S'
    )

print message_table_schema

try:
    table = conn.create_table(
            name='messages',
            schema=message_table_schema,
            read_units=10,
            write_units=10
        )
    print table
except boto.exception.DynamoDBResponseError as e:
    print "already create this table."

print conn.list_tables()
print conn.describe_table('messages')

table = conn.get_table('messages')
print table
item_data = {
        'Body': 'http://url_to_lolcat.gif',
        'SentBy': 'User A',
        'ReceivedTime': '12/9/2011 11:36:03 PM',
    }
item = table.new_item(
        # Our hash key is 'forum'
        hash_key='LOLCat Forum',
        # Our range key is 'subject'
        range_key='Check this out!',
        # This has the
        attrs=item_data
    )
item['a_new_key'] = 'testing'
del item['a_new_key']
print item
print item.put()

item_ret = table.get_item(
        # Your hash key was 'forum_name'
        hash_key='LOLCat Forum',
        # Your range key was 'subject'
        range_key='Check this out!'
    )

if item_ret == item:
    print "same object"

item_ret = table.get_item(
        # Your hash key was 'forum_name'
        hash_key='LOLCat Forum',
        # Your range key was 'subject'
        range_key='Check this out!'
    )
item_ret['SentBy'] = 'User B'
print item_ret.put()

item_ret = table.get_item(
        # Your hash key was 'forum_name'
        hash_key='LOLCat Forum',
        # Your range key was 'subject'
        range_key='Check this out!'
    )
print item_ret

#print conn.delete_table(table)
