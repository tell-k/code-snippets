# -*- coding: utf-8 -*-

from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):

    replace_data = ""

    def __init__(self):
        HTMLParser.__init__(self)
        self.replace_data = ""

    def handle_starttag(self, tag, attrs):
        self.replace_data += "<%s%s>" % (tag, self._attrs_str(tag, attrs))

    def handle_startendtag(self, tag, attrs):
        self.replace_data += "<%s%s />" % (tag, self._attrs_str(tag, attrs))

    def handle_endtag(self, tag):
        self.replace_data += "</%s>" % tag
        return tag

    def handle_data(self, data):
        self.replace_data += data
        return data

    def _attrs_str(self, tag, attrs):
        if not attrs:
            return ""

        tmp = []
        for attr in attrs:
            attr_var = attr[1]

            # imgタグのwidthを9999に置換
            if tag == "img" and attr[0] == "width":
                attr_var = "9999"

            # imgタグのheightを6666に置換
            if tag == "img" and attr[0] == "height":
                attr_var = "6666"

            tmp.append('%s="%s"' % (attr[0], attr_var))

        return " " + " ".join(tmp)


if __name__ == "__main__":

    html = '''
<br />
<strong>Salon de Communication 5月号</strong>
<a href="http://www.odette-e-odile.jp/salon/" target="_blank">
http://www.odette-e-odile.jp/salon/
</a>
<p>
テスト
</p>
ほげ
<a href="http://www.odette-e-odile.jp/salon/" target="_blank">
<img alt="oeo120510news_01.jpg" src="http://www.odette-e-odile.jp/news/uploads/oeo120510news_01.jpg" width="200" height="200" />
</a>
　<a href="http://www.odette-e-odile.jp/salon/" target="_blank">
<img alt="oeo120510news_02.jpg" src="http://www.odette-e-odile.jp/news/uploads/oeo120510news_02.jpg" width="200" height="200" />
</a>
　<a href="http://www.odette-e-odile.jp/salon/" target="_blank">
<img alt="oeo120510news_03.jpg" src="http://www.odette-e-odile.jp/news/uploads/oeo120510news_03.jpg" width="200" height="200" />
</a><br />
'''
    MyHTMLParser.replace_data = "ほげほげ"
    parser = MyHTMLParser()
    parser.feed(html)
    print parser.replace_data
