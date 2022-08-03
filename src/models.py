import os
import sys
from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = "usuarios"
    userID = Column (Integer, primary_key = True)
    name = Column (String (50), nullable = False)
    lastname = Column (String(50), nullable = False)
    password = Column (String(50), nullable = False)
    created_at = Column (DateTime(), default = datetime.now())
    favorite_relation = relationship("favorites", back_populates="usuarios")


class Favorite(Base):
    __tablename__="favorites"
    favID= Column (Integer, primary_key = True)
    user_ID = Column (Integer, ForeignKey("usuarios.userID"))
    user_relation = relationship("usuarios", back_populates="favorites")
    personaje_relation = relationship("personajes")
    planet_relation = relationship("planetas")
    vehicle_relation = relationship("vehiculos")
    personaje_ID = Column (Integer, ForeignKey ("personajes.personajeID"))
    planeta_ID = Column (Integer, ForeignKey("planetas.planetaID"))
    vehiculo_ID = Column (Integer, ForeignKey("vehiculos.vehiculoID"))
    

class Personaje(Base):
    __tablename__="personajes"
    personajeID = Column (Integer, primary_key = True)
    name = Column (String(50), nullable = False, unique = True)
    eyed_color = Column(String(50), nullable = False)
    birth_year = Column(String(50), nullable = False)
    gender = Column(String(50), nullable = False)
    favorite_relation = relationship("favorites")


class Planeta(Base):
    __tablename__="planetas"
    planetaID = Column (Integer, primary_key = True)
    name = Column(String(50), nullable = False, unique = True)
    rotated_period = Column(Integer)
    diameter = Column(Integer)
    climate = Column(Integer)
    favorite_relation = relationship("favorites")


class Vehiculo(Base):
    __tablename__= "vehiculos"
    vehiculoID = Column (Integer, primary_key = True)
    name = Column(String(50), nullable = False, unique = True)
    model = Column(String(50), nullable = False)
    favorite_relation = relationship("favorites")

    
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')