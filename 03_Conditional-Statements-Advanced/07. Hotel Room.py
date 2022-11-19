month = input()
night = int(input())
price_per_apartment = 0
price_per_studio = 0
if month == "May" or month == "October":
    price_per_studio = 50
    price_per_apartment = 65
    if 7 < night <= 14:
        price_per_studio *= 0.95
    elif night > 14:
        price_per_studio *= 0.70
        price_per_apartment *= 0.90
elif month == "June" or month == "September":
    price_per_studio = 75.20
    price_per_apartment = 68.70
    if night > 14:
        price_per_studio *= 0.80
        price_per_apartment *= 0.90
elif month == "July" or month == "August":
    price_per_studio = 76
    price_per_apartment = 77
    if night > 14:
        price_per_apartment *= 0.90
total_price_apartment = price_per_apartment * night
total_price_studio = price_per_studio * night
print(f"Apartment: {total_price_apartment:.2f} lv.")
print(f"Studio: {total_price_studio:.2f} lv.")
