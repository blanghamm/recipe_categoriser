import random

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from . import models
from .auth import api_key_auth
from .schemas import RecipeCreate, RecipeResponse
from .database import SessionLocal, engine

from app.scraper.services import scrape_url

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def get_version():
    return {"version": "0.1.0"}


@app.post("/recipe/", response_model=RecipeResponse, dependencies=[Depends(api_key_auth)])
def create_recipe(url: str, db: Session = Depends(get_db)) -> RecipeResponse:
    scraped_recipe: dict = scrape_url(url=url)[0]
    db_recipe = models.Recipe(
        id=random.randint(1, 200),
        title=scraped_recipe["title"],
        url=scraped_recipe["url"],
        ingredients=scraped_recipe["ingredients"],
        instructions=scraped_recipe["instructions"],
        source=scraped_recipe["source"],
        image=scraped_recipe["image"],
    )

    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return RecipeResponse(recipe=db_recipe)


@app.get("/recipe/{recipe_id}", response_model=RecipeResponse)
def get_recipe_by_id(recipe_id: int, db: Session = Depends(get_db)) -> RecipeResponse:
    db_recipe = db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()
    return RecipeResponse(recipe=db_recipe)
