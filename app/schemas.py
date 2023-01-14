from pydantic import BaseModel
from typing import Optional


class RecipeCreate(BaseModel):
    url: str


class Ingredient(BaseModel):
    # id: Optional[int]
    title: str
    quantity: dict

    class Config:
        orm_mode = True


class Recipe(BaseModel):
    # id: Optional[int]
    url: str
    title: str
    ingredients: list[Ingredient] = []
    instructions: str
    source: str
    image: str

    class Config:
        orm_mode = True


class RecipeResponse(BaseModel):
    recipe: list[Recipe]
