from recipe_scrapers import scrape_me
from uuid import uuid4
import re

from scraper.utils import num


def scrape_url(url) -> list:
    scraper = scrape_me('https://' + url)
    results = [{
        'url': str(url),
        'title': scraper.title(),
        'ingredients': _extract_ingredients(scraper.ingredients()),
        'instructions': scraper.instructions(),
        'source': scraper.host(),
        'image': scraper.image()
    }]
    return results


# TODO: enum of measurements and variants?
measurements = [
    "kg",
    "ml",
    "g",
    "l"
]

symbols_float_map = {
    "¼": 0.25,
    "½": 0.5,
    "¾": 0.75
}


def get_quantity_and_measurement(value):
    fraction_ints = re.findall(r'(\d+[\d. ]*|\d)', value)
    float_matches = re.findall(r'(\d+\.\d+)', value)
    symbol_half = re.findall(r'(\½)', value)
    symbol_quarter = re.findall(r'(\¼)', value)
    symbol_three_quarter = re.findall(r'(\¾)', value)
    grams = re.findall(r'(?<=[0-9])(g)', value)
    ml = re.findall(r'(?<=[0-9])(ml)', value)
    oz = re.findall(r'(\b[Oo]z\b)', value)
    tsp = re.findall(r'(\b[Tt]sp\b)', value)
    tbsp = re.findall(r'(\b[Tt]bsp\b)', value)
    large = re.findall(r'(\b[Ll]arge\b)', value)
    medium = re.findall(r'(\b[Mm]edium\b)', value)
    small = re.findall(r'(\b[Ss]mall\b)', value)
    # Can use this to convert symbols into float measurements if required
    symbols_concat = symbol_quarter + symbol_half + symbol_three_quarter
    convert_symbols = [float(symbols_float_map[s]) for s in symbols_concat]
    print(convert_symbols)
    amount = fraction_ints + float_matches + symbol_half + symbol_quarter + symbol_three_quarter
    measurement_type = grams + tsp + tbsp + ml + large + medium + small + oz
    return {
        "amount": None if len(amount) == 0 else num(amount[0]),
        "measurement": None if len(measurement_type) == 0 else measurement_type[0].lower()
    }


def _extract_ingredients(ingredients):
    return [{
        'ingredient':
            {
                'quantity': get_quantity_and_measurement(ingredient),
                'name': ingredient
            }
    } for ingredient in ingredients]
