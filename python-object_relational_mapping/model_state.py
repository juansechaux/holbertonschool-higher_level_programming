#!/usr/bin/python3
"""A script to list states from database hbtn_0e_0_usa."""
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    '''Class States'''
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, primary_key=True,
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)
