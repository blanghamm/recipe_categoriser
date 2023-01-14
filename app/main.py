from fastapi import FastAPI
from sqlalchemy.orm import Session

from . import models, schemas
from .database import SessionLocal, engine

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
async def root():
    return {"message": "Hello World"}


@app.post("/recipe/", response_model=schemas.Recipe)
async def create_recipe(db: Session, url: str):
    # TODO: add search query for already categorised recipe
    db_recipe = models.Recipe(url=url)

    return
