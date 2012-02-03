#!/usr/bin/env perl

#http://ks0608.hatenablog.com/entry/2012/01/24/134052

#use strict;
#use warnings;
#use JSON;
#use Data::Dumper;
#use utf8;
#use Encode;
#use LWP::UserAgent;
#$Data::Dumper::Indent = 1;
#$Data::Dumper::Terse = 1;
#
#my $encoder = find_encoding(
#    $^O eq 'MSWin32' ? 'cp932' : 'utf8'
#);

my @geo = verify_mac_addresses(@ARGV);

#my $query = <<QUERY;
#{
#  "version":"1.1.0",
#  "host":"maps.google.com",
#  "request_address":true,
#  "address_language":"ja_JP",
#  "wifi_towers":
#  [
#    {
#      "mac_address":"$geo[0]",
#      "signal_strength":8,
#      "age":0
#    },
#    {
#      "mac_address":"$geo[1]",
#      "signal_strength":8,
#      "age":0
#    }
#  ]
#}
#QUERY
#$query =~ s/\n//g;
#$query =~ s/\s+//g;
#
#my $response = LWP::UserAgent->new->post(
#    'http://www.google.com/loc/json',
#    Content => $query
#);
#die $response->status_line unless $response->is_success;
#
#my $json = decode_json($response->content);
#die "Return no location data.\n" if not exists $json->{location};
#
#my $dump_json = Dumper $json;
#$dump_json =~ s/\\x{([0-9a-fA-F]+)}/chr(hex($1))/ge;
#print $encoder->encode($dump_json), "\n";
#
#print $encoder->encode("latitude(緯度) and longitude(経度) are:"), "\n";
#print "$json->{location}{latitude},$json->{location}{longitude}\n";

sub verify_mac_addresses {
    my @geo = @_;
    die "Specify 2 mac addresses.\n" if @geo != 2;
    my $regex = join("[:-]", ("([0-9a-fA-F]{2})") x 6);
    print $regex;
    for (@geo) {
        unless (s/^$regex$/$1-$2-$3-$4-$5-$6/) {
            die "Specify 2 mac addresses.\n";
        }
    }
    return @geo;
}
