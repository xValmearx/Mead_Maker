# recipes.py


 # each recepie will contain a ingredient and data about that ingredient

# an example of this will be honey, 
# honey then contains the amount of honey needed for 1,3 and 5 gallons of mead
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

SACK_MEAD = {
    "honey": {
        "amount": {1: 4, 3: 12, 5: 20},
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
        "amount": {1: 1.5, 3: 4.5, 5: 7.5},
        "unit": "tsp",
    },
}

BRAGGOT_MEAD = {
    "honey": {
        "amount": {1: 2, 3: 6, 5: 10},
        "unit": "lbs",
    },
    "light malt extract": {
        "amount": {1: 3, 3: 9, 5: 15},
        "unit": "lbs",
    },
    "water": {
        "amount": {1: 1, 3: 3, 5: 5},
        "unit": "gallons",
    },
    "brewing yeast": {
        "amount": {1: 1, 3: 3, 5: 5},
        "unit": "packet",
    },
}

SPICED_MEAD = {
    "honey": {
        "amount": {1: 3, 3: 9, 5: 15},
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
    "cinnamon sticks": {
        "amount": {1: 1, 3: 3, 5: 5},
        "unit": "stick",
    },
    "whole cloves": {
        "amount": {1: 4, 3: 12, 5: 20},
        "unit": "cloves",
    },
}


BLUEBERRY_MEAD = {
    "honey": {
        "amount": {1: 3, 3: 9, 5: 15},
        "unit": "lbs",
    },
    "blueberries": {
        "amount": {1: 3, 3: 9, 5: 15},
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
}

BLACKBERRY_MEAD = {
    "honey": {
        "amount": {1: 3, 3: 9, 5: 15},
        "unit": "lbs",
    },
    "blackberries": {
        "amount": {1: 3, 3: 9, 5: 15},
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
}

STRAWBERRY_MEAD = {
    "honey": {
        "amount": {1: 3, 3: 9, 5: 15},
        "unit": "lbs",
    },
    "strawberries": {
        "amount": {1: 3, 3: 9, 5: 15},
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
}

GRAPE_MEAD = {
    "honey": {
        "amount": {1: 2.5, 3: 7.5, 5: 12.5},
        "unit": "lbs",
    },
    "grape juice": {
        "amount": {1: 1, 3: 3, 5: 5},
        "unit": "gallons",
    },
    "wine yeast": {
        "amount": {1: 1, 3: 3, 5: 5},
        "unit": "packet",
    },
}

ORANGE_MEAD = {
    "honey": {
        "amount": {1: 3, 3: 9, 5: 15},
        "unit": "lbs",
    },
    "oranges": {
        "amount": {1: 3, 3: 9, 5: 15},
        "unit": "whole",
    },
    "water": {
        "amount": {1: 1, 3: 3, 5: 5},
        "unit": "gallons",
    },
    "yeast": {
        "amount": {1: 1, 3: 3, 5: 5},
        "unit": "packet",
    },
}

LAVENDER_MEAD = {
    "honey": {
        "amount": {1: 3, 3: 9, 5: 15},
        "unit": "lbs",
    },
    "lavender buds": {
        "amount": {1: 2, 3: 6, 5: 10},
        "unit": "tbsp",
    },
    "water": {
        "amount": {1: 1, 3: 3, 5: 5},
        "unit": "gallons",
    },
    "yeast": {
        "amount": {1: 1, 3: 3, 5: 5},
        "unit": "packet",
    },
}

CHERRY_MEAD = {
    "honey": {
        "amount": {1: 3, 3: 9, 5: 15},
        "unit": "lbs",
    },
    "cherries": {
        "amount": {1: 3, 3: 9, 5: 15},
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
}

CIDER_MEAD = {
    "honey": {
        "amount": {1: 3, 3: 9, 5: 15},
        "unit": "lbs",
    },
    "apple cider": {
        "amount": {1: 1, 3: 3, 5: 5},
        "unit": "gallons",
    },
    "wine yeast": {
        "amount": {1: 1, 3: 3, 5: 5},
        "unit": "packet",
    },
}




RECIPES = {
    "traditional": TRADITIONAL_MEAD,
    "sack": SACK_MEAD,
    "braggot": BRAGGOT_MEAD,
    "spiced": SPICED_MEAD,
    "blueberry": BLUEBERRY_MEAD,
    "blackberry": BLACKBERRY_MEAD,
    "strawberry": STRAWBERRY_MEAD,
    "grape": GRAPE_MEAD,
    "orange": ORANGE_MEAD,
    "lavender": LAVENDER_MEAD,
    "cherry": CHERRY_MEAD,
    "cider": CIDER_MEAD,
}


def build_ingredients_dict(recipe, gallons):
    """
    Build an ingredients dictionary for a given recipe and batch size.
    """

    # blank dictionary
    dict = {}

    # loop over each ingredient and that ingredients data from the recepie
    for ingredient, data in recipe.items():

        #example of this would be honey: amount = [1,3,5] units = lbs(pounds)

        # add a new ingredient to the dictionary (like honey)
        dict[ingredient] = {

            # then get the amount of that ingrediant based on the gallon paremeter
            "amount": data["amount"][gallons],
            "unit": data["unit"],
        }

    return dict