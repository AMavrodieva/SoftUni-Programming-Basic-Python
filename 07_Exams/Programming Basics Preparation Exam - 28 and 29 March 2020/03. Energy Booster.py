fruit = input()
type_of_set = input()
count_of_set = int(input())
price = 0
if type_of_set == "small":
    if fruit == "Watermelon":
        price = 56
    elif fruit == "Mango":
        price = 36.66
    elif fruit == "Pineapple":
        price = 42.10
    elif fruit == "Raspberry":
        price = 20
    price = 2 * price
elif type_of_set == "big":
    if fruit == "Watermelon":
        price = 28.70
    elif fruit == "Mango":
        price = 19.60
    elif fruit == "Pineapple":
        price = 24.80
    elif fruit == "Raspberry":
        price = 15.20
    price = 5 * price
total_price = count_of_set * price
if 400 <= total_price <= 1000:
    total_price *= 0.85
elif total_price > 1000:
    total_price *= 0.50
print(f"{total_price:.2f} lv.")
