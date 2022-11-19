days_stay = int(input())
room_type = input()
opinion = input()
night = days_stay - 1
price_per_night = 0
if room_type == "apartment":
    price_per_night = 25.00
    if night < 10:
        price_per_night *= 0.7
    elif 10 <= night <= 15:
        price_per_night *= 0.65
    elif night > 15:
        price_per_night *= 0.50
elif room_type == "president apartment":
    price_per_night = 35.00
    if night < 10:
        price_per_night *= 0.9
    elif 10 <= night <= 15:
        price_per_night *= 0.85
    elif night > 15:
        price_per_night *= 0.80
elif room_type == "room for one person":
    price_per_night = 18.00
if opinion == "positive":
    price_per_night *= 1.25
elif opinion == "negative":
    price_per_night *= 0.90
total_price = price_per_night * night
print(f"{total_price:.2f}")

