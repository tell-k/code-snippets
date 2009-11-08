#!/usr/bin/ruby

str1 = "string"
str2 = "string"
p str1.object_id #=> object_idは実行毎に違うらしい。
p str2.object_id 
p str1 == str2   #=> true; 内容は同じ
p str1.equal?(str2) #=> false; 内容は同じでもオブジェクトとしては異なる。


