#!/usr/bin/env python
#-*- coding:utf8 -*-

#http://wiki.apache.org/solr/SolPython
#http://stackoverflow.com/questions/6728944/solr-best-documented-easy-to-use-stable-python-apis
#http://stackoverflow.com/questions/6466188/django-python-and-apache-solr-pysolr-or-solrpy
#http://packages.python.org/sunburnt/installation.html#using-pip
#https://github.com/toastdriven/pysolr/blob/master/pysolr.py
#http://blog.timetric.com/2010/02/08/sunburnt-a-python-solr-interface/
#http://opensource.timetric.com/sunburnt/queryingsolr.html
#http://www.mwsoft.jp/programming/munou/lucene_gosen.html

from pprint import pprint

#solr api
SOLR_API_URL = 'http://localhost:8983/solr'
word = u'アパッチ'

#print 'solrpy' + '--' * 50
#import solr
#s = solr.SolrConnection(SOLR_API_URL)
#for r in s.query(word):
#    pprint(r)
#
#print 'pysolr' + '--' * 50
#import pysolr
#s = pysolr.Solr(SOLR_API_URL)
#for r in s.search(word):
#    pprint(r)

print 'sunburnt' + '--' * 50
import sunburnt
s = sunburnt.SolrInterface(SOLR_API_URL)
for r in s.query(word).execute():
    pprint(r)
