# coding: utf-8
import csv

filename = "sample/pool/201207200183050/1234567_offer.csv"
writecsv = csv.writer(file(filename, 'w'))
writecsv.writerow(['1234567', '0', '010', 'タイトル', '1', '2012-08-01 00:00:00', '2012-08-10 00:00:00', '2012-08-31 23:59:59', 'オファー説明文\r\n\r\nオファー説明文', 'http://www.united-arrows.co.jp/index.html', 'オファー注意文\r\nオファー注意文', '画像注意文\r\n画像注意文'])

filename = "sample/1234567_offer_min.csv"
writecsv = csv.writer(file(filename, 'w'))
writecsv.writerow(['1234567', '0', '010', 'タイトル', '1', '2012-08-01 00:00:00', '2012-08-10 00:00:00', '2012-08-31 23:59:59', 'オファー説明文\r\n\r\nオファー説明文', '', '', ''])

filename = "sample/pool/201207200183050/1234567_delivery.csv"
writecsv = csv.writer(file(filename, 'w'))

for i in range(5):
    writecsv.writerow(['1234567', str(2110000020 + i)])

#writecsv.writerow(['1234567', '2110000021'])
#writecsv.writerow(['1234567', '2110000022'])
#writecsv.writerow(['1234567', '2110000023'])
#writecsv.writerow(['1234567', '2110000024'])
#writecsv.writerow(['1234567', '2110000025'])

filename = "sample/result/201207200183050.csv"
writecsv = csv.writer(file(filename, 'w'))
writecsv.writerow(["1234567_offer.csv", "0000", "取り込み成功"])
writecsv.writerow(["1234567_delivery.csv", "0000", "取り込み成功"])

filename = "sample/201207200183050_success.csv"
writecsv = csv.writer(file(filename, 'w'))
writecsv.writerow(["1234567_offer.csv", "0000", "取り込み成功"])
writecsv.writerow(["1234567_delivery.csv", "0000", "取り込み成功"])

filename = "sample/201207200183050_failure1.csv"
writecsv = csv.writer(file(filename, 'w'))
writecsv.writerow(["1234567_offer.csv", "0010", "オファーIDがありません。"])
writecsv.writerow(["1234567_offer.csv", "0110", "見出し画像がありません。"])
writecsv.writerow(["1234567_delivery.csv", "1000", "offer.csvの取り込みに失敗しました。配信リストの取り込みをスキップします"])

filename = "sample/201207200183050_failure2.csv"
writecsv = csv.writer(file(filename, 'w'))
writecsv.writerow(["1234567_offer.csv", "0000", "取り込み成功"])
writecsv.writerow(["1234567_delivery.csv", "1003", "10行目のハウスカード番号が数値10桁ではありません。取り込みをスキップします。"])
writecsv.writerow(["1234567_delivery.csv", "1003", "15行目のハウスカード番号が数値10桁ではありません。取り込みをスキップします。"])
writecsv.writerow(["1234567_delivery.csv", "1003", "20行目のハウスカード番号が数値10桁ではありません。取り込みをスキップします。"])


#import tarfile
#import os
#_tar = tarfile.open('sample/pool/201207200183050.tar.gz','w:gz')
#for _root, _dirs, _files in os.walk("sample/pool/201207200183050"):
#    for _file in _files:
#        _tar.add(os.path.join(_root, _file))
#_tar.close()
