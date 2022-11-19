fruit = input()
day_of_week = input()
quantity = float(input())
price = 0
workday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekend = ["Saturday", "Sunday"]
kind_of_fruit = ["banana", "apple", "orange", "grapefruit", "kiwi", "pineapple", "grapes"]
if fruit == "banana":
    if day_of_week in workday:
        price = 2.50
    elif day_of_week in weekend:
        price = 2.70
elif fruit == "apple":
    if day_of_week in workday:
        price = 1.20
    elif day_of_week in weekend:
        price = 1.25
elif fruit == "orange":
    if day_of_week in workday:
        price = 0.85
    elif day_of_week in weekend:
        price = 0.90
elif fruit == "grapefruit":
    if day_of_week in workday:
        price = 1.45
    elif day_of_week in weekend:
        price = 1.60
elif fruit == "kiwi":
    if day_of_week in workday:
        price = 2.70
    elif day_of_week in weekend:
        price = 3.00
elif fruit == "pineapple":
    if day_of_week in workday:
        price = 5.50
    elif day_of_week in weekend:
        price = 5.60
elif fruit == "grapes":
    if day_of_week in workday:
        price = 3.85
    elif day_of_week in weekend:
        price = 4.20
total_price = quantity * price
if (day_of_week in weekend or day_of_week in workday) and fruit in kind_of_fruit:
    print(f"{total_price:.2f}")
else:
    print("error")
