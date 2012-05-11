#!/usr/bin/env python
#-*- coding:utf8 -*-

from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Date
from sqlalchemy.types import TypeDecorator
from sqlalchemy import DateTime
import time

from sqlalchemy import func
from sqlalchemy.sql.expression import select, text

dsn = 'mysql://xxxxx:xxxx@localhost/xxxxx?charset=utf8'
engine = create_engine(dsn, convert_unicode=True, echo=False)
db_session = scoped_session(sessionmaker(autocommit=False,
                                 autoflush=False,
                                 bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

if __name__ == "__main__":

    r = db_session.execute(select([(func.utc_timestamp() - text("INTERVAL 2 DAY"))])).first()
    print r[0].strftime("%Y/%m/%d %H:%I:%S")

    # func => SQLの関数
    # text => SQLの文
