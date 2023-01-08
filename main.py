from fastapi import FastAPI
from scraper.bbcfood import scrape_url

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/recipe/")
async def get_recipe():
    return scrape_url()
