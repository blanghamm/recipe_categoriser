from sqlalchemy.orm import Session
from app.scraper.services import scrape_url

from . import models, schemas


def create_recipe(db: Session, recipe: schemas.RecipeCreate):
    scraped_recipe = scrape_url(url=recipe.url)[0]
    db_recipe = models.Recipe(
        title=scraped_recipe["title"],
        url=recipe.url,
        ingredients=scraped_recipe["ingredients"],
        instructions=scraped_recipe["instructions"],
        source=scraped_recipe["source"],
        image=scraped_recipe["image"])

    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe
