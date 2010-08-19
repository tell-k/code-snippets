#!/usr/bin/perl

use strict;
use warnings;

my @hoge = qw(
        key1
        key2 
        key3 
        key4 
        key5 
        key6 
        key7 
        key8 
        key9 
        key10
        );
my $pointer = \(@hoge)[3];
print $pointer;

__END__
