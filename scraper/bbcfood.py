from recipe_scrapers import scrape_me


def scrape_url() -> list:
    scraper = scrape_me('https://www.bbc.co.uk/food/recipes/one_pot_dal_48517/')
    results = [{
        'title': scraper.title(),
        'ingredients': _extract_ingredients(scraper.ingredients()),
        'instructions': scraper.instructions(),
        'source': scraper.host(),
        'image': scraper.image()
    }]

    return results


# TODO: clean up
def _extract_ingredients(ingredients):
    return [{
        'ingredient':
            {
                'quantity': [float(s) for s in ingredient.split() if s.isdigit()],
                'ingredient': ingredient
            }
    } for ingredient in ingredients]
