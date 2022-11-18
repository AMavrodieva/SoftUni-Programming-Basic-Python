budget = float(input())
extra = int(input())
price_for_clothing_of_one_extra = float(input())
decor_price = 0.10 * budget
expenses_for_clothing = extra * price_for_clothing_of_one_extra
if extra >= 150:
    expenses_for_clothing *= 0.9
total_expenses = decor_price + expenses_for_clothing
if total_expenses > budget:
    print(f"Not enough money!")
    print(f"Wingard needs {total_expenses - budget:.2f} leva more.")
else:
    print(f"Action!")
    print(f"Wingard starts filming with {budget - total_expenses:.2f} leva left.")
