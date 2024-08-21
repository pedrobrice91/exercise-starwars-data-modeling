import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()
class user(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    addreess = Column(String(250), nullable=False)
    contry = Column(String(250), nullable=False)

class favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    user_Id = Column(Integer, ForeignKey('user.id'))
    user = relationship(user)

class people(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    favorite_Id = Column(Integer, ForeignKey('favorite.id'))
    films = Column(String(250))
    gender = Column(String(250))
    homeworld = Column(String(250))
    vehicles = Column(String(250))
    favorite = relationship(favorite)

class planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    climate = Column(Integer)
    gravity = Column(Integer)
    population = Column(Integer)
    favorite_id = Column(Integer, ForeignKey('favorite.id'))
    favorite = relationship(favorite)

class species(Base):
    __tablename__ = 'species'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    language = Column(String(250))
    homeworld = Column(String(250))
    classification = Column(String(250))
    favorite_Id = Column(Integer, ForeignKey('favorite.id'))
    favorite = relationship(favorite)

class vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    cargo_capacity = Column(String(250))
    length = Column(Integer)
    model = Column(String(250))
    favorite_Id = Column(Integer, ForeignKey('favorite.id'))
    favorite = relationship(favorite)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
