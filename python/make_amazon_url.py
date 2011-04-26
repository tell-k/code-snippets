#!/usr/local/bin/python
#-*- coding:utf8 -*-


def amazonurl(country='jp'):
    aws_base_url = 'http://webservices.amazon.%s/onca/xml'
    aws_tld = {
                'jp': 'co.jp',
                'us': 'com'
               }
    tld = aws_tld[country] if country in aws_tld else aws_tld['jp']
    return aws_base_url % tld

print amazonurl('us')
