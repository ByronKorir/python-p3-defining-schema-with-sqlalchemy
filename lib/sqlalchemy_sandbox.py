#!/usr/bin/env python3

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = column(integer(), primary_key=True)
    name = column(string())

if __name__ == '__main__':
    engine = create_engine('sqlite:///students.db')
    base.metadata.create_all(engine)