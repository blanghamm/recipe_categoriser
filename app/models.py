from sqlalchemy import Boolean, Column, PickleType, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Recipe(Base):
    __tablename__ = "app"

    # id = Column(Integer, primary_key=True, index=True)
    url = Column(String, unique=True, index=True)
    title = Column(String)
    instructions = Column(String)
    source = Column(String)
    image = Column(String)
    ingredients = relationship("Ingredient")


class Ingredient(Base):
    __tablename__ = "ingredients"

    # id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    quantity = Column(PickleType)
