from recipe_scrapers import scrape_me
import re


def scrape_url() -> list:
    scraper = scrape_me('https://www.bbc.co.uk/food/recipes/chickpea_spinach_and_egg_50755')
    results = [{
        'title': scraper.title(),
        'ingredients': _extract_ingredients(scraper.ingredients()),
        'instructions': scraper.instructions(),
        'source': scraper.host(),
        'image': scraper.image()
    }]

    return results


measurements = [
    "kg",
    "ml",
    "g",
    "l"
]


def get_quantity_and_measurement(value):
    int_single = re.findall(r'^\D*(\d+)', value)
    grams = re.findall(r'(?<=[0-9])(g)', value)
    ml = re.findall(r'(?<=[0-9])(ml)', value)
    float_matches = re.findall(r'(\d+\.\d+)', value)
    tsp = re.findall(r'(\btsp\b)', value)
    tbsp = re.findall(r'(\btbsp\b)', value)
    large = re.findall(r'(\blarge\b)', value)
    medium = re.findall(r'(\bmedium\b)', value)
    small = re.findall(r'(\bsmall\b)', value)
    symbol_half = re.findall(r'(\½)', value)
    symbol_quarter = re.findall(r'(\¼)', value)
    symbol_three_quarter = re.findall(r'(\¾)', value)
    amount = int_single + float_matches + symbol_half + symbol_quarter + symbol_three_quarter
    measurement_type = grams + tsp + tbsp + ml + large + medium + small
    return {"amount": None if len(amount) == 0 else _num(amount[0]), "measurement": None if len(measurement_type) == 0 else measurement_type[0]}


def _num(s):
    if not s.isnumeric():
        return s.strip()
    try:
        return int(s)
    except ValueError:
        return float(s)


# TODO: clean up
def _extract_ingredients(ingredients):
    return [{
        'ingredient':
            {
                'quantity': get_quantity_and_measurement(ingredient),
                'ingredient': ingredient
            }
    } for ingredient in ingredients]
