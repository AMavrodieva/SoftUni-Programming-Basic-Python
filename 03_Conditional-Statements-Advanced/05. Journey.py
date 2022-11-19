budget = float(input())
season = input()
destination = ""
type_of_accommodation = ""
price = 0
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        type_of_accommodation = "Camp"
        price = 0.30 * budget
    elif season == "winter":
        type_of_accommodation = "Hotel"
        price = 0.70 * budget
elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        type_of_accommodation = "Camp"
        price = 0.40 * budget
    elif season == "winter":
        type_of_accommodation = "Hotel"
        price = 0.80 * budget
else:
    destination = "Europe"
    type_of_accommodation = "Hotel"
    price = 0.90 * budget
print(f"Somewhere in {destination}")
print(f"{type_of_accommodation} - {price:.2f}")

