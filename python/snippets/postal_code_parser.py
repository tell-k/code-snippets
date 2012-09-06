#!/usr/bin/env python
#-*- coding:utf8 -*-

import csv
import re


class PostalCodeRow(object):

    _colmuns = [
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
            return self.row[self._colmuns.index(attr_name)]
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
            name = match.groups()[0]
            if self.city and (self.city == name or re.search(r'郡%s$' % name, self.city)):
                self.town = None
                self.town_kana = None
        elif re.search(r'（その他）$', self.town):
                self.town = re.sub(r' (その他) $', '', self.town)
                self.town_kana = re.sub(r'\(ｿﾉﾀ\)$', '', self.town_kana)
        elif re.search(r'^(.+[町村])一円$', self.town):
            match = re.search(r'^(.+[町村])一円$', self.town)
            name = match.groups()[0]
            if self.city == name:
                self.town = None
                self.town_kana = None

        if self.town:
            pass
            # ?
            #self.town = re.sub(r'[〜～]', '〜')

    def _fix_subtown(self):

        if not self.town:
            return

        subtown = []
        subtown_kana = []

        if re.search(r'（([\d〜、]+)丁目）$', self.town):
            match = re.search(r'^(.+)の次に番地がくる場合', self.town)
            #num = self.alnum_z2h(match.groups())
            self.town = re.sub(r'（([\d〜、]+)丁目）$', '', self.town)
            #TODO なにやってるか分からん


class PostalCodeParser(object):

    def __init__(self, filename, mode=1, encoding='utf8'):
        self._reader = csv.reader(open(filename, 'r'))
        self._encoding = encoding
        self._current_build_town = ''
        self._current_build_town_kana = ''
        self._mode = mode

    def __iter__(self):
        return self

    def _get_line(self):
        row = [r.decode('cp932').encode(self._encoding) for r in next(self._reader)]
        if re.search(r'（.+[^）]$', row[8]):
            while (True):
                tmp = [r.decode('cp932').encode(self._encoding) for r in next(self._reader)]
                row[5] += tmp[5]
                row[8] += tmp[8]
                if re.search(r'\）$', row[8]):
                    break

        match = re.search(r'^(.+)（次のビルを除く）$', row[8])
        if match:
            self._current_build_town = match.groups()[0]
            match = re.search(r'^(.+)\(', row[5])
            if match:
                self._current_build_town_kana = match.groups()[0]

        elif row[2] == '4530002' and re.search(r'^名駅\（', row[8]):
            self._current_build_town = '名駅'
            self._current_build_town_kana = 'ﾒｲｴｷ'

        elif not re.search(r'^%s.+（.+階.*）$' % self._current_build_town, row[8]):
            self._current_build_town = ''
            self._current_build_town_kana = ''

        return row

    def _fetch_obj(self):
        row = self._get_line()
        return PostalCodeRow(
            build_town=self._current_build_town,
            build_town_kana=self._current_build_town_kana,
            row=row
        )

    def get_line(self):
        self._mode = 1
        return self

    def fetch_obj(self):
        self._mode = 2
        return self

    def next(self):
        if self._mode == 1:
            return self._get_line()
        if self._mode == 2:
            return self._fetch_obj()

    def __next__(self):
        return self.next()


if __name__ == "__main__":

    ken_all_csv = "KEN_ALL.csv"
    parser = PostalCodeParser(ken_all_csv)

    for t in parser:
        print t[3]
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
