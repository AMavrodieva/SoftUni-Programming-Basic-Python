budget = int(input())
season = input()
number_of_fishermen = int(input())
price_for_boat_rental = 0
if season == "Spring":
    price_for_boat_rental = 3000
elif season == "Summer" or season == "Autumn":
    price_for_boat_rental = 4200
elif season == "Winter":
    price_for_boat_rental = 2600
if number_of_fishermen <= 6:
    price_for_boat_rental *= 0.9
elif 7 <= number_of_fishermen <= 11:
    price_for_boat_rental *= 0.85
elif number_of_fishermen > 12:
    price_for_boat_rental *= 0.75
if number_of_fishermen % 2 == 0 and season != "Autumn":
    price_for_boat_rental *= 0.95
difference = abs(budget - price_for_boat_rental)
if budget >= price_for_boat_rental:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")

