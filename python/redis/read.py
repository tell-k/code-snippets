#!/usr/bin/env python
# -*- encoding:utf-8 -*-

#refs
#-http://redis.io/commands
#-http://tech.dclog.jp/2010/10/nosql-redismysql.html
#-http://symfoware.blog68.fc2.com/blog-entry-521.html
#-http://redis.shibu.jp/
#-http://redis.shibu.jp/admin/config.html

import redis

master = redis.Redis(connection_pool=redis.ConnectionPool(host='localhost', port=6379, db=0))
slave = redis.Redis(connection_pool=redis.ConnectionPool(host='localhost', port=6378, db=0))
slave2 = redis.Redis(connection_pool=redis.ConnectionPool(host='localhost', port=6377, db=0))

for i in range(1000000):

    #slave -> master
    if slave.get('m_key_%s' % str(i)) != 'm_value_%s' % str(i):
        print "false"
    else:
        print "true"

    #slave2 -> slave
    if slave2.get('m_key_%s' % str(i)) != 'm_value_%s' % str(i):
        print "false"
    else:
        print "true"
