from sqlalchemy import Boolean, Column, PickleType, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Recipe(Base):
    __tablename__ = "recipe"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, unique=True, index=True)
    title = Column(String)
    instructions = Column(String)
    source = Column(String)
    image = Column(String)
    ingredients = Column(PickleType)


# class Ingredient(Base):
#     __tablename__ = "ingredients"
#
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String)
#     quantity = Column(PickleType)
#     recipe_id = Column(Integer, ForeignKey("recipe.id"))
#
#     recipe = relationship("Recipe", back_populates="ingredients")
