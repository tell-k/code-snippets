#!/usr/bin/env python
#-*- coding:utf8 -*-

import csv
import re


class PostalRow(object):

    colmuns = [
        'region_id', 'old_zip', 'zip',
        'pref_kana', 'region_kana', 'town_kana', 'pref', 'region', 'town',
        'is_multi_zip', 'has_koaza_banchi', 'has_chome', 'is_multi_town',
        'update_status', 'update_reason'
    ]

    def __init__(self, build_town, build_town_kana, row):
        self.build_town = build_town
        self.build_town_kana = build_town_kana
        self.row = row

        self._fix_region()
        self._fix_town()

    def __getattr__(self, attr_name):
        try:
           return self.row[self.colmuns.index(attr_name)]
        except ValueError:
           return None

    def _fix_region(self):
        match = re.search(r'^(.+?郡)(.+[町村])$', self.region)
        (district, town_village) = match.groups() if match else (None, None)
        if district and town_village:
            match = re.search(r'^((?:ｷﾀｸﾞﾝﾏ|.+?)ｸﾞﾝ)(.+)$', self.region_kana)
            (district_kana, town_village_kana) = match.groups() if match else (None, None)
            self.district = district
            self.town_village = town_village
            self.district_kana = district_kana
            self.town_village_kana = town_village_kana
            return

        match = re.search(r'^(.+市)(.+区)$', self.region)
        (city, ward) = match.groups() if match else (None, None)
        if city and ward:
            match = re.search(r'^((?:ﾋﾛｼﾏ|ｷﾀｷｭｳｼｭｳ|.+?)ｼ)(.+)$', self.region_kana)
            (city_kana, ward_kana) = match.groups() if match else (None, None)
            self.city = city
            self.ward = ward
            self.city_kana = city_kana
            self.ward_kana = ward_kana
        elif re.search(r'区$', self.region):
            self.ward = self.region
            self.ward_kana = self.region_kana
        else:
            self.city = self.region
            self.city_kana = self.region_kana

    def _fix_town(self):
        if self.town == '以下に掲載がない場合':
            self.town = None
            self.town_kana = None
        elif re.search(r'^(.+)の次に番地がくる場合', self.town):
            match = re.search(r'^(.+)の次に番地がくる場合', self.town)
            name = match.group()
            if self.city:
                print self.city

            if self.city and (self.city == name or re.search(r'郡%s$' % name, self.city)):
                self.town = None
                self.town_kana = None
        elif re.search(r'（その他）$', self.town):
                self.town = re.sub(r' (その他) $', '', self.town)
                self.town_kana = re.sub(r'\(ｿﾉﾀ\)$', '', self.town_kana)
        elif re.search(r'^(.+[町村])一円$', self.town):
            match = re.search(r'^(.+[町村])一円$', self.town)
            name = match.group()
            if self.city == name:
                self.town = None
                self.town_kana = None

        if self.town:
            pass
            # ?
            #self.town = re.sub(r'[〜～]', '〜')

    def _fix_subtown(self):
        pass


class PostalParser(object):

    current_build_town = ''
    current_build_town_kana = ''

    def __init__(self, filename):
        self.csv_reader = csv.reader(open(filename, 'r'))

    def __iter__(self):
        return self

    def _fetch_row(self):
        row = [r.decode('cp932').encode('utf8') for r in next(self.csv_reader)]
        if re.search(r'（.+[^）]$', row[8]):
            while (True):
                tmp = [r.decode('cp932').encode('utf8') for r in next(self.csv_reader)]
                row[5] += tmp[5]
                row[8] += tmp[8]
                if re.search(r'\）$', row[8]):
                    break

        town = row[8]
        match = re.search(r'^(.+)（次のビルを除く）$', town)
        if match:
            self.current_build_town = match.groups()[0]
            match = re.search(r'^(.+)\(', row[5])
            if match:
                self.current_build_town_kana = match.groups()[0]

        elif row[2] == '4530002' and re.search(r'^名駅\（', town):
            self.current_build_town = '名駅'
            self.current_build_town_kana = 'ﾒｲｴｷ'
        elif not re.search(r'^%s.+（.+階.*）$' % self.current_build_town, town):
            self.current_build_town = ''
            self.current_build_town_kana = ''

        return row

    def next(self):
        if self.extract_type == 0:
            return self._fetch_row()
        if self.extract_type == 1:
            return self._fetch_obj()

    def _fetch_obj(self):
        row = self._fetch_row()
        return PostalRow(
            build_town=self.current_build_town,
            build_town_kana=self.current_build_town_kana,
            row=row
        )

    def fetch_obj(self):
        self.extract_type = 1
        return iter(self)

    def fetch_row(self):
        self.extract_type = 0
        return iter(self)

if __name__ == "__main__":

    ken_all_csv_path = "ken_all.csv"
    parser = PostalParser(ken_all_csv_path)
    for t in parser.fetch_obj():
        pass


#for t in parser:
#    i += 1
#    pass
#def parse(filename):
#    with open(filename, 'r') as f:
#        reader = csv.reader(f)
#        try:
#            yield [r.decode('cp932').encode('utf8') for r in next(reader)]
#        except csv.Error, e:
#            sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))
#print next(parse(kenall))
#print next(parse(kenall))
#print next(parse(kenall))
#print next(parse(kenall))
#print next(parse(kenall))
