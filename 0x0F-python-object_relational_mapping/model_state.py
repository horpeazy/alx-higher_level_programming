#!/usr/bin/python3
"""
Connect to a database using SQLAlchemy
"""
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql://root:root@localhost:3306/hbtn_0e_6_usa')
Base = declarative_base()

class State(Base):
    __tablename__ = "states"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

Base.metadata.create_all(engine)
