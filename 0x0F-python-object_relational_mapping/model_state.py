#!/usr/bin/python3
"""
This module contains the class definition of a State and an instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base


# Creating an instance of declarative_base
Base = declarative_base()


class State(Base):
    """
    Class representing the states table.
    Linked to MySQL table "states"
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True)
    name = Column(String(128), nullable=False)
