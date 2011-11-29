#!/bin/sh
#http://www.smipple.net/snippet/IanLewis/init.d%20script%20for%20redis

CONF_PATH=$(cd $(dirname $0) && pwd)/../conf
redis-server $CONF_PATH/master.conf
redis-server $CONF_PATH/slave.conf
redis-server $CONF_PATH/slave2.conf
