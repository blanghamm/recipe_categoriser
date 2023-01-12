from fastapi import FastAPI
from scraper.services import scrape_url

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/recipe/")
async def get_recipe(url: str):
    return scrape_url(url)
