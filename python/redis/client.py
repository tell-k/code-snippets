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

master.set('hoge', 'hoge')
#for i in range(1000000):
#    master.set('m_key_%s' % str(i), 'm_value_%s' % str(i))
#    master.set('j_key_%s' % str(i), '日本語テスト-%s' % str(i))
