#!/usr/bin/env python
#-*- coding:utf8 -*-
"""
    test.py
    ~~~~~~~~~~~~~~~~~~

    :author: tell-k
    :copyright: tell-k All Rights Reserved.
"""
from database import engine, db_session, Base
from database.models import Entry

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

db_session.add(Entry())
db_session.commit()

e = db_session.query(Entry).first()
print e.datetime
