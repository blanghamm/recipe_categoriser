from pydantic import BaseModel
from typing import Optional, List


class RecipeCreate(BaseModel):
    url: str


class Ingredient(BaseModel):
    title: str
    quantity: dict

    class Config:
        orm_mode = True


class Recipe(BaseModel):
    id: Optional[int]
    url: str
    title: str
    ingredients: List
    instructions: str
    source: str
    image: str

    class Config:
        orm_mode = True


class RecipeResponse(BaseModel):
    recipe: Recipe
