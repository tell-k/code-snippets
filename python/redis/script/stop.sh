#!/bin/sh

redis-cli SHUTDOWN
redis-cli -p 6378 SHUTDOWN
redis-cli -p 6377 SHUTDOWN
