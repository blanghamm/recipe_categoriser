from pydantic import BaseModel


class RecipeCreate(BaseModel):
    url: str


class Ingredient(BaseModel):
    id: int
    title: str
    quantity: dict

    class Config:
        orm_mode = True


class Recipe(BaseModel):
    id: int
    url: str
    title: str
    ingredients: list[Ingredient] = []
    instructions: str
    source: str
    image: str

    class Config:
        orm_mode = True
