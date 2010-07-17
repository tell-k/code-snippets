#!/usr/bin/perl

use strict;
use warnings;

my $test = 'http://buzzurl.jp/entry/http://anond.hatelabo.jp/20090112011703';
$test =~ s/^http\:\/\/buzzurl.jp\/entry\///g;

print $test;
