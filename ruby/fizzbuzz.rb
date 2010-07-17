#!/usr/bin/ruby

#for i in 1..100 do
#puts((i%15>0)?(i%5>0)?(i%3>0)?i:"Fizz":"Buzz":"FizzBuzz");
#end;

(1..100).each{|i| puts((i%15>0)?(i%5>0)?(i%3>0)?i:"Fizz":"Buzz":"FizzBuzz")};
