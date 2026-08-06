# recipes.py



# ============================
# INGREDIENTS
# ============================

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



# ============================
# EQUIPMENT
# ============================
traditional_equipment = [
    "Fermentation Bucket",
    "Airlock",
    "Hydrometer",
    "Auto Siphon",
    "Star San Sanitizer",
    "Spray Bottle",
    "Large Stir Spoon",
]


# ============================
# Instructions
# ============================


SANITIZE_STEPS = {
    "Prepare the Sanitizer":
        "Mix Star San Sanitizing Solution according to the manufacturer's instructions. Fill a clean 16 oz spray bottle with the mixed solution. Do not rinse after applying, as Star San is a no-rinse sanitizer.",

    "Clean the Equipment":
        "Wash all brewing equipment with warm water and a mild, unscented cleaner to remove dirt, dust, or residue. Rinse thoroughly before sanitizing.",

    "Spray All Surfaces":
        "Spray the inside and outside of all equipment that will come into contact with the mead. This includes the fermenter, lid, airlock, bung, funnel, hydrometer, stirring spoon, measuring cups, scissors, siphon, and any other tools.",

    "Allow Contact Time":
        "Let the Star San solution remain on the equipment for at least 1 to 2 minutes. This contact time allows the sanitizer to effectively kill bacteria and wild yeast.",

    "Drain Excess Sanitizer":
        "Pour out any excess sanitizer remaining inside the equipment. A small amount of foam is completely normal and safe. Do not rinse the equipment with water after sanitizing.",

    "Keep Equipment Sanitary":
        "Once sanitized, avoid touching any surfaces that will come into contact with the mead. If an item becomes contaminated or is left exposed for an extended period, sanitize it again before use.",
}

MUST_STEPS = {
    "Add the Honey":
        "Pour the honey into the sanitized fermenter.",

    "Add Water":
        "Add clean distilled water until you reach the desired batch volume.",

    "Mix Thoroughly":
        "Stir until all of the honey is completely dissolved and no honey remains on the bottom of the fermenter.",

    "Take an Original Gravity Reading (optional)":
        "Use a sanitized hydrometer to measure and record the original gravity (OG).",

    "Aerate the Must":
        "Stir or shake the must vigorously for 1 to 2 minutes to introduce oxygen for the yeast.",

    "Add the Yeast Nutrient":
        "Add the required amount of yeast nutrient to the must and stir until evenly mixed.",

    "Pitch the Yeast":
        "Sprinkle or pour the yeast into the must according to the manufacturer's instructions. Gently stir if recommended for the selected yeast strain.",
}

FERMENTATION_STEPS = {
    "Install the Airlock":
        "Secure the lid on the fermenter and install the airlock. Place the fermenter in a cool, dark location with a stable temperature.",

    "Primary Fermentation":
        "Allow the mead to ferment for approximately 4 weeks. During this time, the yeast will convert the sugars into alcohol.",

    "Wait Until Clear":
        "Leave the mead in the fermenter until it becomes clear. As the yeast finishes its work, it will naturally settle to the bottom of the fermenter, leaving the mead above it clear.",

    "Do Not Disturb the Fermenter":
        "Avoid moving or shaking the fermenter while the mead is clearing. Keeping it still allows the yeast and other sediment to settle to the bottom.",

    "Check for Clarity":
        "When the mead is clear and you can easily see through it, it is ready to be bottled. This process may take several weeks or months depending on the recipe.",

         "Take a Final Gravity Reading (optional)":
        "Once the mead is clear, use a sanitized hydrometer to measure the final gravity (FG).",

    "Bottle the Mead":
        "Carefully siphon the clear mead into clean, sanitized bottles, leaving the sediment behind in the fermenter. Seal the bottles with corks or caps and store them in a cool, dark place.",
}


traditional_steps = {
    "Sanitize Equipment":
        SANITIZE_STEPS,

    "Create the Must":
        MUST_STEPS,

    "Fermenting the Mead":
        FERMENTATION_STEPS,
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


def build_ingredient_dict(recipe, gallons):
    """
    Build a complete recipe dictionary for the selected batch size.
    """

    ingredients = {}

    for ingredient, data in recipe.items():
        ingredients[ingredient] = {
            "amount": data["amount"][gallons],
            "unit": data["unit"],
        }

    return ingredients


def get_instructions(mead_type:str):
     return globals().get(f"{mead_type}_steps")

def get_equipment(mead_type:str):
    return globals().get(f"{mead_type}_equipment")