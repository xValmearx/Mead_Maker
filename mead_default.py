# recipes.py


TRADITIONAL_MEAD = {
    "honey": {
        "amount": {1: 3, 3: 9, 5: 15}, # 1 gallon = 3lbs of honey, 3 gallons = 9lbs of honey etc
        "unit": "lbs",
    },
    "water": {
        "amount": {1: 1, 3: 3, 5: 5},
        "unit": "gallons",
    },
    "yeast": {
        "amount": {1: 1, 3: 3, 5: 5},
        "unit": "packet",
    },
    "yeast nutrient": {
        "amount": {1: 1, 3: 3, 5: 5},
        "unit": "tsp",
    },
}



RECIPES = {
    "traditional": TRADITIONAL_MEAD
}
