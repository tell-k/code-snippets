#!/usr/bin/perl

use strict;
use warnings;

use Data::Dumper;
use Encode;

my $str = 'abcde';
print Dumper(scalar reverse($str));

$str = '日本語表示';
print Dumper(str_reverse($str));

sub str_reverse {
    my ($str) = shift;
    utf8::decode($str); # utf8フラグをつける
    my @str = map {utf8::encode($_); $_} split //, $str;
    my $b   = @str;
    for (my $a = 0; $a <= --$b; $a++) {
      ($str[$a], $str[$b]) = ($str[$b], $str[$a]);
    }
    join('', @str);
}
__END__
