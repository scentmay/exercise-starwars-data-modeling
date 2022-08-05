import os
import sys
from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class user(Base):
    __tablename__ = "usuarios"
    userID = Column (Integer, primary_key = True)
    name = Column (String (50), nullable = False)
    lastname = Column (String(50), nullable = False)
    password = Column (String(50), nullable = False)
    created_at = Column (DateTime(), default = datetime.now())

# Personajes-----------------------------------

class personaje(Base):
    __tablename__="personajes"
    personajeID = Column (Integer, primary_key = True)
    name = Column (String(50), nullable = False, unique = True)
    eyed_color = Column(String(50), nullable = False)
    birth_year = Column(String(50), nullable = False)
    gender = Column(String(50), nullable = False)

class favCharacter(Base):
    __tablename__ = "favChars"
    favCharID= Column (Integer, primary_key = True)
    user_ID = Column (Integer, ForeignKey("usuarios.userID"))
    char_ID = Column (Integer, ForeignKey ("personajes.personajeID"))
    personaje_relation = relationship("personajes")
    user_relation = relationship("usuarios", back_populates="favChars")

# Vehículos------------------------------------

class vehiculo(Base):
    __tablename__= "vehiculos"
    vehiculoID = Column (Integer, primary_key = True)
    name = Column(String(50), nullable = False, unique = True)
    model = Column(String(50), nullable = False)

class favVehicle(Base):
    __tablename__ = "favVehicles"
    favVehicleID= Column (Integer, primary_key = True)
    user_ID = Column (Integer, ForeignKey("usuarios.userID"))
    vehicle_ID = Column (Integer, ForeignKey ("vehiculos.vehiculoID"))
    vehicle_relation = relationship("vehiculos")
    user_relation = relationship("usuarios", back_populates="favVehicles")

# Planetas------------------------------------

class planeta(Base):
    __tablename__= "planetas"
    planetaID = Column (Integer, primary_key = True)
    name = Column(String(50), nullable = False, unique = True)
    rotated_period = Column(Integer)
    diameter = Column(Integer)
    climate = Column(Integer)

class favPlanet(Base):
    __tablename__ = "favPlanets"
    favPlanetID= Column (Integer, primary_key = True)
    user_ID = Column (Integer, ForeignKey("usuarios.userID"))
    planet_ID = Column (Integer, ForeignKey ("planetas.planetaID"))
    planet_relation = relationship("planetas")
    user_relation = relationship("usuarios", back_populates="favPlanets")


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')