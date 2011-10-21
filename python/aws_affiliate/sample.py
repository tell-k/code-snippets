#!/usr/bin/env python
# -*- encoding:utf-8 -*-

# kzfm <kerolinq@gmail.com>

from mechanize import Browser
import smtplib
from email.MIMEText import MIMEText
from email.Header import Header
from email.Utils import formatdate
from pyquery import PyQuery as pq

# email = ''
# password = ''
# aws_email = ''
# aws_password = ''

amazon_url = 'https://affiliate.amazon.co.jp/'

def get_amazon_data():
    br = Browser()
    br.set_handle_robots(False)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; \
     rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

    br.open(amazon_url)

    br.select_form(name="sign_in")
    br["email"] = aws_email
    br["password"] = aws_password

    response = br.submit()

    d = pq(response.get_data())
    return [data.text for data in d('div').filter('.data')]

def send_mail(data):


    for d in data:
        print type(d)

    return 
    from_addr = email
    to_addr   = email
    subject   = u'Amazonアフィリエイト'
    body      = u"""
発送済み商品合計: %s
売上合計: %s
注文済み商品: %s
クリック数: %s
あなたのコンバージョン: %s
""" % tuple([d.encode('ascii') if type(d) == unicode else d for d in data])

    print body
    msg = MIMEText(body.encode("utf-8"),'plain','utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Date'] = formatdate()

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(email, password)
    s.sendmail(from_addr, to_addr, msg.as_string())
    s.close()

if __name__ == '__main__':
    amazon_data = get_amazon_data();
    send_mail(amazon_data)
