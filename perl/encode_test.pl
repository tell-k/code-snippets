#!/usr/bin/perl

use warnings;
use strict;

use Data::Dumper;
use Encode;

my $octets = encode("euc-jp", "ああ");

Dumper print decode("euc-jp", $octets);

#my $octets2 = encode("utf8", $octets);
#
#Dumper print $octets2;
