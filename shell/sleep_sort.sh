#!/bin/bash  

#http://d.hatena.ne.jp/gfx/20110519/1305810786

function f() {
    sleep "$1"
    echo "$1"
}
while [ -n "$1" ]
do
    f "$1" &
    shift
done
wait

# example usage:
# ./sleepsort.bash 5 3 6 3 6 3 1 4 7
