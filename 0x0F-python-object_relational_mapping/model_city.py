#!/usr/bin/python3
'''Write a python file that contains the class definition of a City
   and an instance Base = declarative_base()
'''

from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    '''A city'''
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True,
                unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
