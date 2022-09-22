import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    
    id = Column(Integer, primary_key = True)
    name = Column(String(250), nullable = False)
    lastName = Column(String(250), nullable = False)
    email = Column(String(20), nullable = False)
    password = Column(String(20), nullable = False)

class Planeta(Base):
    __tablename__ = 'planeta'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable = False)
    rotationPeriod = Column(Integer, nullable = False)
    orbitalPeriod = Column(Integer, nullable = False)
    diameter = Column(Integer, nullable = False)
    climate = Column(String(250), nullable = False)
    gravity = Column(String(250), nullable = False)
    terrain = Column(String(250), nullable = False)
    surfaceWater = Column(Integer, nullable = False)
    population = Column(Integer, nullable = False)
    residents = Column(String(250), nullable = False)

    user_id = Column(Integer, ForeignKey('usuario.id'))
    user = relationship(Usuario)

class Personaje(Base):
    __tablename__ = 'personaje'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable = False)
    height = Column(Integer, nullable = False)
    mass = Column(Integer, nullable = False)
    hairColor = Column(String(250), nullable = False)
    skinColor = Column(String(250), nullable = False)
    eyeColor = Column(String(250), nullable = False)
    birthYear = Column(String(250), nullable = False)
    gender = Column(String(250), nullable = False)
    homeworld = Column(String(250), nullable = False)

    user_id = Column(Integer, ForeignKey('usuario.id'))
    user = relationship(Usuario)

class Vehiculos(Base):
    __tablename__ = 'vehiculos'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable = False)
    model = Column(String(250), nullable = False)
    manufacturer = Column(String(250), nullable = False)
    costInCredits = Column(Integer, nullable = False)
    length = Column(Integer, nullable = False)
    maxAtmospheringSpeed = Column(Integer, nullable = False)
    crew = Column(Integer, nullable = False)
    passengers = Column(Integer, nullable = False)
    cargoCapacity = Column(Integer, nullable = False)
    consumables = Column(String(250), nullable = False)
    vehicleClass = Column(String(250), nullable = False)
    homeworld = Column(String(250), nullable = False)

    character_id = Column(Integer, ForeignKey('personaje.id'))
    character = relationship(Personaje)

class Starships(Base):
    __tablename__ = 'starships'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable = False)
    model = Column(String(250), nullable = False)
    manufacturer = Column(String(250), nullable = False)
    costInCredits = Column(Integer, nullable = False)
    length = Column(Integer, nullable = False)
    maxAtmospheringSpeed = Column(Integer, nullable = False)
    crew = Column(Integer, nullable = False)
    passengers = Column(Integer, nullable = False)
    cargoCapacity = Column(Integer, nullable = False)
    hyperdriveRating = Column(Integer, nullable = False)
    mglt = Column(Integer, nullable = False)
    starshipClass = Column(String(250), nullable = False)

    character_id = Column(Integer, ForeignKey('personaje.id'))
    character = relationship(Personaje)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')