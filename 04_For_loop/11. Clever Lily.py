ages = int(input())
price_laundry = float(input())
price_toy = int(input())
count_toy = 0
saved_money = 0
for birthday in range(1, ages+1):
    if birthday % 2 == 0:
        saved_money += (birthday * 5) - 1
    else:
        count_toy += 1
total_money = (count_toy * price_toy) + saved_money
difference = abs(total_money - price_laundry)
if total_money >= price_laundry:
    print(f"Yes! {difference:.2f}")
else:
    print(f"No! {difference:.2f}")