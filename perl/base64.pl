#!/usr/bin/perl

use strict;

use MIME::Base64 qw(encode_base64);
my $buzzurl_id = 'ffk2005@gmail.com';
my $pass       = "ksdve5645";

print sprintf("Authorization: Basic %s", encode_base64($buzzurl_id . ":" . $pass));

