#!/usr/bin/perl

my $str = 'a';
$str++ for (1..285075);

print $str;  #=> ・・・・？
