from math import floor
species_cat = input()
gender_of_cat = input()
years_of_life = 0
is_cat_name_valid = True
if gender_of_cat == "m":
    if species_cat == "British Shorthair":
        years_of_life = 13
    elif species_cat == "Siamese":
        years_of_life = 15
    elif species_cat == "Persian":
        years_of_life = 14
    elif species_cat == "Ragdoll":
        years_of_life = 16
    elif species_cat == "American Shorthair":
        years_of_life = 12
    elif species_cat == "Siberian":
        years_of_life = 11
    else:
        is_cat_name_valid = False
elif gender_of_cat == "f":
    if species_cat == "British Shorthair":
        years_of_life = 14
    elif species_cat == "Siamese":
        years_of_life = 16
    elif species_cat == "Persian":
        years_of_life = 15
    elif species_cat == "Ragdoll":
        years_of_life = 17
    elif species_cat == "American Shorthair":
        years_of_life = 13
    elif species_cat == "Siberian":
        years_of_life = 12
    else:
        is_cat_name_valid = False
months_of_cat_life = years_of_life * 2
if is_cat_name_valid:
    print(f"{floor(months_of_cat_life)} cat months")
else:
    print(f"{species_cat} is invalid cat!")

