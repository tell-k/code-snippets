#!/bin/sh

sh $(cd $(dirname $0) && pwd)/stop.sh
sh $(cd $(dirname $0) && pwd)/start.sh

