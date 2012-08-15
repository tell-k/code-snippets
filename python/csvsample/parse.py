# -*- coding: utf-8 -*-

import re
import tarfile
import csv
from StringIO import StringIO

with tarfile.open('201207200183050.tar.gz', "r:gz") as tar:
    members = [tar_file for tar_file in tar.getmembers()]
    for m in members:
        if re.search(r'_offer.csv$', m.name):
            offer_txt = m
        if re.search(r'_delivery.csv$', m.name):
            delivery_txt = m
        if re.search(r'_main.png$', m.name):
            main_png = m
        if re.search(r'_heading.png$', m.name):
            heading_png = m

    f = tar.extractfile(offer_txt)
    tmp = f.readlines()
    for row in csv.reader(StringIO("\r\n".join(tmp))):
#        print row[0]  # オファーID
#        print row[1]  # オファーカテゴリ
#        print row[2]  # タイトル
#        print row[3]  #
#        print row[4]  #
#        print row[5]  #
#        print row[6]  #
        print row[7].replace('\r\n', '\n')
#        print row[8]
        print row[9].replace('\r\n', '\n')
        print row[10].replace('\r\n', '\n')
