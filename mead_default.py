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
traditional_equipment = {
    "Airlock": "https://www.amazon.com/Molovee-Fermentation-Silicone-Sauerkraut-transparency/dp/B095BXVM7Y/ref=sr_1_4_sspa?dib=eyJ2IjoiMSJ9.SQg5bFZfZBFPqjj-Js5D3ViN9mir9erZftIzkJLXBXFg0cX4SD6tjFPll-yYtW3mbO6J-ERbqov0lECsucAhQTVhe8KlzDZo3Tn_pb4Oh8ARB0wjDKIicJXzCqY-pBS_UyCab1dhBZXWWzzS-u3p9z0cJuYO_fzD4Z9mRewPLxisBB4w-A3NwC8A01sVy-blbbhuCb-jnn49hxWcVqMC118gU3BDxXt9RlLEYguWvfA3KXJEVkcjGxRQbQ_QgbU9fouwp02d_I9XNyHNqslSr1dH-xtinnldwhsBwYlK2o8.6ab9trJLKVwDT9cTPkSF52WzxjYRUHX4sfPL9sY5BVA&dib_tag=se&keywords=3+piece+fermentation+airlock+homebrew&qid=1786944811&sr=8-4-spons&utm_source=chatgpt.com&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1",
    "Hydrometer": "https://www.amazon.com/Brewers-Elite-Hydrometer-Kombucha-Hardcase/dp/B01CITP03W/ref=sr_1_3?crid=1Z90ASM1HSMF0&dib=eyJ2IjoiMSJ9.ZwxmB5TMoJxSObgl61kDJAB4L-G3rF3wpqcm1Heo07_IFa_e8_llOOoBq0dMyY1e2FrML5vSlABt4GTfk3aYlSmQNVKFMOYjYH4HVBOc-Zj_BPC7JM0O8sggB6jqNi18G2JR_rkjK1m78qdI2N1fl58mkFYWaUI_tgT8gYWcYGFoVnivF7o-l789PsQ4UCB9H4CW7qO8l7TBpc-mdq3iwt-8JTdbDzxhWl6XR0juVnQ.5FVgsrdM35ZCC1uyLgCwCzwY7LCnHAKKfpr9IMAzY58&dib_tag=se&keywords=hydrometer+for+fermenting&qid=1786944995&sprefix=hydrometer+ferm%2Caps%2C150&sr=8-3",
    "Auto Siphon": "https://www.amazon.com/gp/aw/d/B00CIXXM8O/?_encoding=UTF8&pd_rd_plhdr=t&aaxitk=8c376a06928251a1d7f4f8dcaf4ed06a&hsa_cr_id=0&qid=1786945032&sr=1-2-9e67e56a-6f64-441f-a281-df67fc737124&i=aps&aref=bduVvzmLO0&ref_=sbx_s_sparkle_sbtcd_asin_1_rating&pd_rd_w=cn8aC&content-id=amzn1.sym.8de9b3d5-f5c5-40e9-9b39-d65f08d6ea68%3Aamzn1.sym.8de9b3d5-f5c5-40e9-9b39-d65f08d6ea68&pf_rd_p=8de9b3d5-f5c5-40e9-9b39-d65f08d6ea68&pf_rd_r=QKYK1TRVTCZT4Q9M8HCW&pd_rd_wg=Lt9SD&pd_rd_r=9425146d-36f4-43cc-a074-cdd609ab3a13#customerReviews",
    "Star San Sanitizer": "https://www.amazon.com/C-Kraus-Star-San-oz/dp/B0114ARHGO/ref=pd_day0_d_sccl_1_4/140-7761712-6668319?pd_rd_w=lXatk&content-id=amzn1.sym.de286d99-05f6-43bf-9d9c-b57de9652232&pf_rd_p=de286d99-05f6-43bf-9d9c-b57de9652232&pf_rd_r=SGKE6E63WXQWRJQFE8Q6&pd_rd_wg=GYWek&pd_rd_r=d080d8d9-f6b2-4f56-bc5a-abf744aa6c23&pd_rd_i=B0114ARHGO&psc=1",
    "Spray Bottle": "https://www.amazon.com/Chemical-Guys-ACC151-Secondary-Container/dp/B06X6NN4XL/ref=sr_1_16?crid=3PKG2VY3CWYGL&dib=eyJ2IjoiMSJ9.OD_znyUn9fj8eoywJqNX4R1pVSbO-EJ0QdfQswPoxbVtui8xZxH2BKkoXmkzH0qImdLSgMSnJrzyPVC7gMkl2rkxjwJ0lkUl36Pll0h-yLIeImw6e6W2pTMNqTJKDu4hvmeUJPFvELk7dYwoGBCsF63xxchKjYDG0dxnIGW474oiib86fKw82FHskKtrXmQYExR6OThuKW2He_rcQ-I4fUuwK7nr8qMps8u07SGtf24Gk8438oCWDjluk4PyuvZvOGXMf4ArO6LHMLTSMBgj2KOz4iNdZFMPuYh1SziD0Mo._m1AOUEhMUYSJT3c_RyEdklwL2uMwaSd-xTuPNiOEx4&dib_tag=se&keywords=16%2Boz%2Bspray%2Bbottles%2Bmist%2Bsprayer%2Bsingle%2Bpact&nsdOptOutParam=true&qid=1786945328&sprefix=16%2Boz%2Bspray%2Bbottles%2Bmist%2Bsprayer%2Bsingle%2Bpact%2Caps%2C185&sr=8-16&th=1",
    "Large Stir Spoon": "https://www.amazon.com/Winco-BSON-13-Stainless-Basting-Commercial/dp/B07C5MBRCK/ref=sr_1_8?crid=AV1JYUCADOBS&dib=eyJ2IjoiMSJ9.fr2iHEacn3ycRXAjUB1tgI_K5lPukTtt-aVZLSESG-ITjbzxBQIM7QYHc0-ApE4MU2ELjtns_9U8JKD9ENt4SwWKvscVGqiw2u2BTmEnN6aLhv3sNzc3B0bMRyr07o_yoXMiGILw2qmN1B69-cmCFGfgGX-M-kbolO3WQgxD0B9m4ZryTZpYrxK0_j9kUO91FunJSibfQ0dvQVXjiaTvi81agIltkiOAh7lFSV6SDw7hv4wdDr8td74KzfWd_mm1tPa3od8OQu6Gr-XRP2RKi_3daFYmgXaknuPzDyZgvV0.ICss4Z7mlX018xIixdoVyfFKFnPqT3vSpq1ULmtSCmQ&dib_tag=se&keywords=12+inch+spoon&qid=1786945847&sprefix=12+inch+spoon%2Caps%2C183&sr=8-8",
}

fruit_equipment = {
    "Airlock": "https://www.amazon.com/Molovee-Fermentation-Silicone-Sauerkraut-transparency/dp/B095BXVM7Y/ref=sr_1_4_sspa?dib=eyJ2IjoiMSJ9.SQg5bFZfZBFPqjj-Js5D3ViN9mir9erZftIzkJLXBXFg0cX4SD6tjFPll-yYtW3mbO6J-ERbqov0lECsucAhQTVhe8KlzDZo3Tn_pb4Oh8ARB0wjDKIicJXzCqY-pBS_UyCab1dhBZXWWzzS-u3p9z0cJuYO_fzD4Z9mRewPLxisBB4w-A3NwC8A01sVy-blbbhuCb-jnn49hxWcVqMC118gU3BDxXt9RlLEYguWvfA3KXJEVkcjGxRQbQ_QgbU9fouwp02d_I9XNyHNqslSr1dH-xtinnldwhsBwYlK2o8.6ab9trJLKVwDT9cTPkSF52WzxjYRUHX4sfPL9sY5BVA&dib_tag=se&keywords=3+piece+fermentation+airlock+homebrew&qid=1786944811&sr=8-4-spons&utm_source=chatgpt.com&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1",
    "Hydrometer": "https://www.amazon.com/Brewers-Elite-Hydrometer-Kombucha-Hardcase/dp/B01CITP03W/ref=sr_1_3?crid=1Z90ASM1HSMF0&dib=eyJ2IjoiMSJ9.ZwxmB5TMoJxSObgl61kDJAB4L-G3rF3wpqcm1Heo07_IFa_e8_llOOoBq0dMyY1e2FrML5vSlABt4GTfk3aYlSmQNVKFMOYjYH4HVBOc-Zj_BPC7JM0O8sggB6jqNi18G2JR_rkjK1m78qdI2N1fl58mkFYWaUI_tgT8gYWcYGFoVnivF7o-l789PsQ4UCB9H4CW7qO8l7TBpc-mdq3iwt-8JTdbDzxhWl6XR0juVnQ.5FVgsrdM35ZCC1uyLgCwCzwY7LCnHAKKfpr9IMAzY58&dib_tag=se&keywords=hydrometer+for+fermenting&qid=1786944995&sprefix=hydrometer+ferm%2Caps%2C150&sr=8-3",
    "Auto Siphon": "https://www.amazon.com/gp/aw/d/B00CIXXM8O/?_encoding=UTF8&pd_rd_plhdr=t&aaxitk=8c376a06928251a1d7f4f8dcaf4ed06a&hsa_cr_id=0&qid=1786945032&sr=1-2-9e67e56a-6f64-441f-a281-df67fc737124&i=aps&aref=bduVvzmLO0&ref_=sbx_s_sparkle_sbtcd_asin_1_rating&pd_rd_w=cn8aC&content-id=amzn1.sym.8de9b3d5-f5c5-40e9-9b39-d65f08d6ea68%3Aamzn1.sym.8de9b3d5-f5c5-40e9-9b39-d65f08d6ea68&pf_rd_p=8de9b3d5-f5c5-40e9-9b39-d65f08d6ea68&pf_rd_r=QKYK1TRVTCZT4Q9M8HCW&pd_rd_wg=Lt9SD&pd_rd_r=9425146d-36f4-43cc-a074-cdd609ab3a13#customerReviews",
    "Star San Sanitizer": "https://www.amazon.com/C-Kraus-Star-San-oz/dp/B0114ARHGO/ref=pd_day0_d_sccl_1_4/140-7761712-6668319?pd_rd_w=lXatk&content-id=amzn1.sym.de286d99-05f6-43bf-9d9c-b57de9652232&pf_rd_p=de286d99-05f6-43bf-9d9c-b57de9652232&pf_rd_r=SGKE6E63WXQWRJQFE8Q6&pd_rd_wg=GYWek&pd_rd_r=d080d8d9-f6b2-4f56-bc5a-abf744aa6c23&pd_rd_i=B0114ARHGO&psc=1",
    "Spray Bottle": "https://www.amazon.com/Chemical-Guys-ACC151-Secondary-Container/dp/B06X6NN4XL/ref=sr_1_16?crid=3PKG2VY3CWYGL&dib=eyJ2IjoiMSJ9.OD_znyUn9fj8eoywJqNX4R1pVSbO-EJ0QdfQswPoxbVtui8xZxH2BKkoXmkzH0qImdLSgMSnJrzyPVC7gMkl2rkxjwJ0lkUl36Pll0h-yLIeImw6e6W2pTMNqTJKDu4hvmeUJPFvELk7dYwoGBCsF63xxchKjYDG0dxnIGW474oiib86fKw82FHskKtrXmQYExR6OThuKW2He_rcQ-I4fUuwK7nr8qMps8u07SGtf24Gk8438oCWDjluk4PyuvZvOGXMf4ArO6LHMLTSMBgj2KOz4iNdZFMPuYh1SziD0Mo._m1AOUEhMUYSJT3c_RyEdklwL2uMwaSd-xTuPNiOEx4&dib_tag=se&keywords=16%2Boz%2Bspray%2Bbottles%2Bmist%2Bsprayer%2Bsingle%2Bpact&nsdOptOutParam=true&qid=1786945328&sprefix=16%2Boz%2Bspray%2Bbottles%2Bmist%2Bsprayer%2Bsingle%2Bpact%2Caps%2C185&sr=8-16&th=1",
    "Large Stir Spoon": "https://www.amazon.com/Winco-BSON-13-Stainless-Basting-Commercial/dp/B07C5MBRCK/ref=sr_1_8?crid=AV1JYUCADOBS&dib=eyJ2IjoiMSJ9.fr2iHEacn3ycRXAjUB1tgI_K5lPukTtt-aVZLSESG-ITjbzxBQIM7QYHc0-ApE4MU2ELjtns_9U8JKD9ENt4SwWKvscVGqiw2u2BTmEnN6aLhv3sNzc3B0bMRyr07o_yoXMiGILw2qmN1B69-cmCFGfgGX-M-kbolO3WQgxD0B9m4ZryTZpYrxK0_j9kUO91FunJSibfQ0dvQVXjiaTvi81agIltkiOAh7lFSV6SDw7hv4wdDr8td74KzfWd_mm1tPa3od8OQu6Gr-XRP2RKi_3daFYmgXaknuPzDyZgvV0.ICss4Z7mlX018xIixdoVyfFKFnPqT3vSpq1ULmtSCmQ&dib_tag=se&keywords=12+inch+spoon&qid=1786945847&sprefix=12+inch+spoon%2Caps%2C183&sr=8-8",
}


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

BRAGGOT_MUST_STEPS = {
    "Add the Honey":
        "Pour the required amount of honey into the sanitized fermenter.",

    "Add the Malt Extract":
        "Add the required amount of light malt extract to the fermenter.",

    "Add Water":
        "Add the required amount of clean water to the fermenter.",

    "Mix Thoroughly":
        "Stir thoroughly until the honey and malt extract are completely dissolved and evenly mixed throughout the must.",

    "Take an Original Gravity Reading (optional)":
        "Use a sanitized hydrometer to measure and record the original gravity (OG).",

    "Aerate the Must":
        "Stir or shake the must vigorously for 1 to 2 minutes to introduce oxygen for the yeast.",

    "Pitch the Yeast":
        "Sprinkle or pour the required brewing yeast into the must according to the manufacturer's instructions. Gently stir if recommended for the selected yeast strain.",
}

SPICED_MUST_STEPS = {
    "Add the Honey":
        "Pour the required amount of honey into the sanitized fermenter.",

    "Prepare the Spices":
        "Place the required cinnamon sticks and whole cloves into a sanitized fermentation mesh bag. Secure the bag so the spices remain contained during fermentation.",

    "Add Water":
        "Add the required amount of clean water to the fermenter.",

    "Add the Spices":
        "Place the sealed fermentation mesh bag containing the cinnamon sticks and whole cloves into the fermenter.",

    "Mix Thoroughly":
        "Stir thoroughly until the honey is completely dissolved and evenly mixed throughout the must.",

    "Take an Original Gravity Reading (optional)":
        "Use a sanitized hydrometer to measure and record the original gravity (OG).",

    "Aerate the Must":
        "Stir or shake the must vigorously for 1 to 2 minutes to introduce oxygen for the yeast.",

    "Pitch the Yeast":
        "Sprinkle or pour the required yeast into the must according to the manufacturer's instructions. Gently stir if recommended for the selected yeast strain.",
}

BLUEBERRY_MUST_STEPS = {
    "Prepare the Blueberries":
        "Wash the required amount of blueberries and place them into a sanitized fermentation mesh bag. Secure the bag so the fruit remains contained during fermentation.",

    "Add the Blueberries":
        "Place the sealed fermentation mesh bag containing the blueberries into the sanitized fermenter.",

    "Add the Honey":
        "Pour the required amount of honey into the sanitized fermenter.",

    "Add Water":
        "Add the required amount of clean water to the fermenter.",

    "Mix Thoroughly":
        "Stir thoroughly until the honey is completely dissolved and evenly mixed throughout the must.",

    "Take an Original Gravity Reading (optional)":
        "Use a sanitized hydrometer to measure and record the original gravity (OG).",

    "Aerate the Must":
        "Stir or shake the must vigorously for 1 to 2 minutes to introduce oxygen for the yeast.",

    "Pitch the Yeast":
        "Sprinkle or pour the required yeast into the must according to the manufacturer's instructions. Gently stir if recommended for the selected yeast strain.",
}

BLACKBERRY_MUST_STEPS = {
    "Prepare the Blackberries":
        "Wash the required amount of blackberries and place them into a sanitized fermentation mesh bag. Secure the bag so the fruit remains contained during fermentation.",

    "Add the Blackberries":
        "Place the sealed fermentation mesh bag containing the blackberries into the sanitized fermenter.",

    "Add the Honey":
        "Pour the required amount of honey into the sanitized fermenter.",

    "Add Water":
        "Add the required amount of clean water to the fermenter.",

    "Mix Thoroughly":
        "Stir thoroughly until the honey is completely dissolved and evenly mixed throughout the must.",

    "Take an Original Gravity Reading (optional)":
        "Use a sanitized hydrometer to measure and record the original gravity (OG).",

    "Aerate the Must":
        "Stir or shake the must vigorously for 1 to 2 minutes to introduce oxygen for the yeast.",

    "Pitch the Yeast":
        "Sprinkle or pour the required yeast into the must according to the manufacturer's instructions. Gently stir if recommended for the selected yeast strain.",
}

STRAWBERRY_MUST_STEPS = {
    "Prepare the Strawberries":
        "Wash and prepare the required amount of strawberries, then place them into a sanitized fermentation mesh bag. Secure the bag so the fruit remains contained during fermentation.",

    "Add the Strawberries":
        "Place the sealed fermentation mesh bag containing the strawberries into the sanitized fermenter.",

    "Add the Honey":
        "Pour the required amount of honey into the sanitized fermenter.",

    "Add Water":
        "Add the required amount of clean water to the fermenter.",

    "Mix Thoroughly":
        "Stir thoroughly until the honey is completely dissolved and evenly mixed throughout the must.",

    "Take an Original Gravity Reading (optional)":
        "Use a sanitized hydrometer to measure and record the original gravity (OG).",

    "Aerate the Must":
        "Stir or shake the must vigorously for 1 to 2 minutes to introduce oxygen for the yeast.",

    "Pitch the Yeast":
        "Sprinkle or pour the required yeast into the must according to the manufacturer's instructions. Gently stir if recommended for the selected yeast strain.",
}

GRAPE_MUST_STEPS = {
    "Add the Honey":
        "Pour the required amount of honey into the sanitized fermenter.",

    "Add the Grape Juice":
        "Add the required amount of grape juice to the sanitized fermenter.",

    "Mix Thoroughly":
        "Stir thoroughly until the honey is completely dissolved and evenly mixed with the grape juice.",

    "Take an Original Gravity Reading (optional)":
        "Use a sanitized hydrometer to measure and record the original gravity (OG).",

    "Aerate the Must":
        "Stir or shake the must vigorously for 1 to 2 minutes to introduce oxygen for the yeast.",

    "Pitch the Yeast":
        "Sprinkle or pour the required wine yeast into the must according to the manufacturer's instructions. Gently stir if recommended for the selected yeast strain.",
}

ORANGE_MUST_STEPS = {
    "Prepare the Oranges":
        "Wash the required oranges thoroughly. Cut or prepare them as needed and place them into a sanitized fermentation mesh bag. Secure the bag so the oranges remain contained during fermentation.",

    "Add the Honey":
        "Pour the required amount of honey into the sanitized fermenter.",

    "Add the Oranges":
        "Place the sealed fermentation mesh bag containing the oranges into the sanitized fermenter.",

    "Add Water":
        "Add the required amount of clean water to the fermenter.",

    "Mix Thoroughly":
        "Stir thoroughly until the honey is completely dissolved and evenly mixed throughout the must.",

    "Take an Original Gravity Reading (optional)":
        "Use a sanitized hydrometer to measure and record the original gravity (OG).",

    "Aerate the Must":
        "Stir or shake the must vigorously for 1 to 2 minutes to introduce oxygen for the yeast.",

    "Pitch the Yeast":
        "Sprinkle or pour the required yeast into the must according to the manufacturer's instructions. Gently stir if recommended for the selected yeast strain.",
}

LAVENDER_MUST_STEPS = {
    "Prepare the Lavender":
        "Place the required amount of lavender buds into a sanitized fermentation mesh bag. Secure the bag so the lavender remains contained.",

    "Brew the Lavender":
        "Place the sealed fermentation mesh bag containing the lavender buds into the required amount of water. Allow the lavender to steep in the water to extract its flavor and aroma.",

    "Remove the Lavender":
        "Remove the fermentation mesh bag containing the lavender from the water. Allow the lavender-infused water to cool before continuing.",

    "Add the Honey":
        "Pour the required amount of honey into the lavender-infused water.",

    "Mix Thoroughly":
        "Stir thoroughly until the honey is completely dissolved and evenly mixed throughout the must.",

    "Take an Original Gravity Reading (optional)":
        "Use a sanitized hydrometer to measure and record the original gravity (OG).",

    "Aerate the Must":
        "Stir or shake the must vigorously for 1 to 2 minutes to introduce oxygen for the yeast.",

    "Pitch the Yeast":
        "Sprinkle or pour the required yeast into the must according to the manufacturer's instructions. Gently stir if recommended for the selected yeast strain.",
}

CHERRY_MUST_STEPS = {
    "Prepare the Cherries":
        "Wash and prepare the required amount of cherries and place them into a sanitized fermentation mesh bag. Secure the bag so the fruit remains contained during fermentation.",

    "Add the Honey":
        "Pour the required amount of honey into the sanitized fermenter.",

    "Add the Cherries":
        "Place the sealed fermentation mesh bag containing the cherries into the sanitized fermenter.",

    "Add Water":
        "Add the required amount of clean water to the fermenter.",

    "Mix Thoroughly":
        "Stir thoroughly until the honey is completely dissolved and evenly mixed throughout the must.",

    "Take an Original Gravity Reading (optional)":
        "Use a sanitized hydrometer to measure and record the original gravity (OG).",

    "Aerate the Must":
        "Stir or shake the must vigorously for 1 to 2 minutes to introduce oxygen for the yeast.",

    "Pitch the Yeast":
        "Sprinkle or pour the required yeast into the must according to the manufacturer's instructions. Gently stir if recommended for the selected yeast strain.",
}

CIDER_MUST_STEPS = {
    "Add the Honey":
        "Pour the required amount of honey into the sanitized fermenter.",

    "Add the Apple Cider":
        "Add the required amount of apple cider to the sanitized fermenter.",

    "Mix Thoroughly":
        "Stir thoroughly until the honey is completely dissolved and evenly mixed with the apple cider.",

    "Take an Original Gravity Reading (optional)":
        "Use a sanitized hydrometer to measure and record the original gravity (OG).",

    "Aerate the Must":
        "Stir or shake the must vigorously for 1 to 2 minutes to introduce oxygen for the yeast.",

    "Pitch the Yeast":
        "Sprinkle or pour the required wine yeast into the must according to the manufacturer's instructions. Gently stir if recommended for the selected yeast strain.",
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

sack_steps = {
    "Sanitize Equipment":
        SANITIZE_STEPS,

    "Create the Must":
        MUST_STEPS,

    "Fermenting the Mead":
        FERMENTATION_STEPS,
}

braggot_steps = {
    "Sanitize Equipment":
        SANITIZE_STEPS,

    "Create the Must":
        BRAGGOT_MUST_STEPS,

    "Fermenting the Mead":
        FERMENTATION_STEPS,
}

spiced_steps = {
    "Sanitize Equipment":
        SANITIZE_STEPS,

    "Create the Must":
        SPICED_MUST_STEPS,

    "Fermenting the Mead":
        FERMENTATION_STEPS,
}

blueberry_steps = {
    "Sanitize Equipment":
        SANITIZE_STEPS,

    "Create the Must":
        BLUEBERRY_MUST_STEPS,

    "Fermenting the Mead":
        FERMENTATION_STEPS,
}

blackberry_steps = {
    "Sanitize Equipment":
        SANITIZE_STEPS,

    "Create the Must":
        BLACKBERRY_MUST_STEPS,

    "Fermenting the Mead":
        FERMENTATION_STEPS,
}

strawberry_steps = {
    "Sanitize Equipment":
        SANITIZE_STEPS,

    "Create the Must":
        STRAWBERRY_MUST_STEPS,

    "Fermenting the Mead":
        FERMENTATION_STEPS,
}

grape_steps = {
    "Sanitize Equipment":
        SANITIZE_STEPS,

    "Create the Must":
        GRAPE_MUST_STEPS,

    "Fermenting the Mead":
        FERMENTATION_STEPS,
}

lavender_steps = {
    "Sanitize Equipment":
        SANITIZE_STEPS,

    "Create the Must":
    LAVENDER_MUST_STEPS,

    "Fermenting the Mead":
        FERMENTATION_STEPS,
}

orange_steps = {
    "Sanitize Equipment":
        SANITIZE_STEPS,

    "Create the Must":
        ORANGE_MUST_STEPS,

    "Fermenting the Mead":
        FERMENTATION_STEPS,
}

cherry_steps = {
    "Sanitize Equipment":
        SANITIZE_STEPS,

    "Create the Must":
        CHERRY_MUST_STEPS,

    "Fermenting the Mead":
        FERMENTATION_STEPS,
}

cider_steps = {
    "Sanitize Equipment":
        SANITIZE_STEPS,

    "Create the Must":
        CIDER_MUST_STEPS,

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

def get_equipment(mead_type: str, gallons: int):

    if mead_type == "traditional":
        equipment = traditional_equipment

    elif mead_type == "sack":
        equipment = traditional_equipment

    else:
        equipment =  fruit_equipment

    if gallons == 1:
        bucket = {
            "1 Gallon Fermentation Bucket": "https://www.amazon.com/FastRack-Fermonster-Airtight-Drilled-Fermenter/dp/B0GCWKNWZL/ref=sr_1_1?crid=3DIMXX9UPJW2J&dib=eyJ2IjoiMSJ9.R12q1np4DC9IRhawmxaeu62HaWw2Wa9gsFLKJIerWU9Gs8pEqzC9HrVek8tTVX7rcYrikxW1kEPXwKkrIGrDUo-XQUdYaWgaHfdAgT9KyMrWe6HWAJvywqhxJsNx3hIYbN5cbraa4eqdVQgcbwB0UHxsiPRlMzBZp-gK1CzkfCY7jU_BWrg9RT01Q6tK5de_VcTJb-wk-iIsVZLgGFLHOutSzQsu6aZR2RT1X_twht0KxTSyQ0N78C97KoQz-14gEP_2iDVQN8tleltrgdRYwWBiNy2klMwDsDUj97Qr1TA.ZUt5w1NvYWEY4cGZdobs88sndH7gxR9JkLIhkR7itoI&dib_tag=se&keywords=fermonster+1+gallon+fermenter&qid=1786949455&sprefix=fermonster+1+gallon%2Caps%2C372&sr=8-1"
        }
    elif gallons == 3:
        bucket = {
            "3 Gallon Fermentation Bucket": "https://www.amazon.com/FastRack-Fermonster-Airtight-Food-Grade-Fermenter/dp/B07BQ7JTDJ/ref=sr_1_1?crid=2OYH06Y1ZIXH6&dib=eyJ2IjoiMSJ9.PZH-x6LiqCr7CUrLzUyuHXzT7cmQLsPfYz_hjQor2V-mCJGwfrzkuh-jp3oK-LcQhYWpwtgWDeelu0gytfiPbaIcUTWjhEfpa_fzUiwCnMgxEgp34lw_g6hG3jkcByajqEMgXt6vPv5YU8yBx5K7PSlaWwaR5gnZZp8ZQYw7JqBIokuV5dxElpUJyK0Y2J1D_9Mn7oHHB893WlNppW5p8weOYhNU5Kc23Bl6m3FrUiNv2KFPvfxU-PyGrKU7fM89teUMnCFtvt-_aCcY6XciKSDPynMqqtegfECovrsF-04.8Lbgh6_8JBauonQZ1Y-5F49TRDDdtnIcMI-aDqcCoLg&dib_tag=se&keywords=fermonster+3+gallon+fermenter&qid=1786949484&sprefix=fermonster+gallon+fermenter%2Caps%2C246&sr=8-1"
        }
    else:
        bucket = {
            "6 Gallon Fermentation Bucket": "https://www.amazon.com/FerMonster-Fermenter-Econolock-Drilled-Stopper/dp/B07FV2BMR4/ref=sr_1_2?crid=305MJS6EV8QD4&dib=eyJ2IjoiMSJ9.K2aV9LGwFz94WIwWJBNp7-QtiKRdN4QK2YVkHkE_7uV0kpKa_UfDs3HlAPO3CNf1VLkjg53CMCxTWCSqgsjF7xlj_KR3fGs_j6gbDG3OjUs7Q2aP3qqNYqqdpkx23224Or642VieMR_bNT3K1WhR_lNWrEvjZnbktHtqv9C_SP52fE1Lhgu4iaQiTYoDc7fu6QIVgz7xI_PCU7nQa-kitClmiuVQP9LEQuFlids0zNWuH_PsQyThclLvjoNXs9IFomlKxcVXICR4sjUA1OzDLeIFaOxNYhfOTSRiuDGz93I.CsqZIZmKVrKloqk5yB3Pw376fjYF6bZwq08lDkcJW9k&dib_tag=se&keywords=fermonster+6+gallon+fermenter&qid=1786949504&sprefix=fermonster+6+gallon+fermenter%2Caps%2C194&sr=8-2"
        }

    return {**bucket, **equipment}