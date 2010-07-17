#!/usr/bin/perl 

use strict;

use Pod::Usage;
my %argv;
use App::Options(
    values => \%argv,
    print_usage => sub { pod2usage(2) },
    option => {
        name  => "type=string;  required; default=Unknown;",
        age   => "type=integer; required; ",
        debug => "type=boolean; default=0;",
    },
);

# 値は %App::options ハッシュの中に入ります
print "Hello $argv{name}.\n";
print "Your age is $argv{age}.\n";
print "debug flag is $argv{debug}.\n";
print "app is $argv{app}.pl\n";
print "host is $argv{host}\n";
print "prefix is $argv{prefix}\n";
print "hostname is $argv{hostname}\n";

__END__

=head1 SYNOPSIS

test.pl --date=2006-02-28

brah brah brah brah brah brah...

=cut
