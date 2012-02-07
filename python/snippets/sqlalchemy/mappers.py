#!/usr/bin/env python
#-*- coding:utf8 -*-
"""
    test.py
    ~~~~~~~~~~~~~~~~~~

    :author: tell-k
    :copyright: tell-k All Rights Reserved.
"""
import json
from datetime import datetime

from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

from bpmappers import Mapper, RawField, ListDelegateField


# create base
engine = create_engine('sqlite://', convert_unicode=True, echo=False)
db_session = scoped_session(sessionmaker(autocommit=False,
                            autoflush=False,
                            bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

# declare models
class Entry(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    text = Column(String)
    created_at = Column(DateTime, default=datetime.now, nullable=False)

    comments = relationship('Comment')

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    entry_id = Column(Integer, ForeignKey('entries.id'), nullable=False)
    text = Column(String)
    created_at = Column(DateTime, default=datetime.now, nullable=False)

class CommentMapper(Mapper):
    id = RawField()
    entry_id = RawField()
    text = RawField()
    created_at = RawField()

    def filter_created_at(self, value):
        return str(value)

class EntryMapper(Mapper):
    id = RawField()
    text = RawField()
    created_at = RawField()

    def filter_created_at(self, value):
        return str(value)

    comments = ListDelegateField(CommentMapper)

# insert data
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

db_session.add(Entry(text='entry text'))
db_session.commit()
db_session.add(Comment(entry_id=1, text='comment1 text'))
db_session.add(Comment(entry_id=1, text='comment2 text'))
db_session.commit()

# select data
print '-' * 10
entries = Entry.query.all()
for entry in entries:
    print 'entry.id: ' + str(entry.id)
    print 'entry.text: ' + entry.text
    print 'entry.creted_at: ' + str(entry.created_at)
    for comment in entry.comments:
        print ' ' + ('-' * 9)
        print ' comment.id: ' + str(comment.id)
        print ' comment.text: ' + comment.text
        print ' comment.created_at: ' + str(comment.created_at)

# convert to json
print '-' * 10
print json.dumps(EntryMapper(entries).as_dict(), indent=2)
