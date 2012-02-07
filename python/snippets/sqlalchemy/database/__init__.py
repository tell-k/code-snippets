#!/usr/bin/env python
#-*- coding:utf8 -*-
"""
    database/models.py
    ~~~~~~~~~~~~~~~~~~

    :author: tell-k
    :copyright: tell-k All Rights Reserved.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

dsn = 'mysql://testuser:testpass@localhost/test'
engine = create_engine(dsn, convert_unicode=True, echo=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                            autoflush=False,
                            bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()
