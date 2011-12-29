# -*- coding: utf-8 -*-
from sqlalchemy.orm import mapper, relationship
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from bartendro.utils import session, metadata

Base = declarative_base(metadata=metadata)
class Dispenser(Base):
    """
    Information about a dispenser
    """

    __tablename__ = 'dispenser'
    id = Column(Integer, primary_key=True)
    booze_id = Column(Integer, ForeignKey('booze.id'), nullable=False)

    query = session.query_property()
    def __init__(self, booze):
        self.booze = booze
        self.booze_id = booze.id

    def json(self):
        return { 
                 'id' : self.id, 
                 'booze' : self.booze_id
               }

    def __repr__(self):
        return "<Dispenser('%s','%s')>" % (self.id, self.booze_id)