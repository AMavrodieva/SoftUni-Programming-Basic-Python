owned_money = float(input())
gender = input()
ages = int(input())
type_of_sport = input()
card_price = 0
if gender == "m":
    if type_of_sport == "Gym":
        card_price = 42
    elif type_of_sport == "Boxing":
        card_price = 41
    elif type_of_sport == "Yoga":
        card_price = 45
    elif type_of_sport == "Zumba":
        card_price = 34
    elif type_of_sport == "Dances":
        card_price = 51
    elif type_of_sport == "Pilates":
        card_price = 39
elif gender == "f":
    if type_of_sport == "Gym":
        card_price = 35
    elif type_of_sport == "Boxing":
        card_price = 37
    elif type_of_sport == "Yoga":
        card_price = 42
    elif type_of_sport == "Zumba":
        card_price = 31
    elif type_of_sport == "Dances":
        card_price = 53
    elif type_of_sport == "Pilates":
        card_price = 37
if ages <= 19:
    card_price *= 0.80
if card_price <= owned_money:
    print(f"You purchased a 1 month pass for {type_of_sport}.")
else:
    difference = card_price - owned_money
    print(f"You don't have enough money! You need ${difference:.2f} more.")
