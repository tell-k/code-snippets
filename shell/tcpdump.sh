
#http://subtech.g.hatena.ne.jp/secondlife/20110916/1316142314
tcpdump -i eth0 port 80 -s 0 -l -w - | strings
