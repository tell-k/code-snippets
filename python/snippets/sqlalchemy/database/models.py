#!/usr/bin/env python
#-*- coding:utf8 -*-
"""
    database/database.py
    ~~~~~~~~~~~~~~~~~~

    :author: tell-k
    :copyright: tell-k All Rights Reserved.
"""
from datetime import datetime
from sqlalchemy import Column, Integer, DateTime
from database.types import DateTime
from database import Base

class Entry(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    text = Column(Text)
    comment_id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.now, nullable=False)

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    text = Column(Text)
