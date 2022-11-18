trip_price = float(input())
num_puzzles = int(input())
num_doles = int(input())
num_teddy_bear = int(input())
num_minion = int(input())
num_track = int(input())
count_toys = num_puzzles + num_doles \
             + num_teddy_bear + num_minion + num_track
sum_of_sales = (num_puzzles * 2.60) + (num_doles * 3) + \
               (num_teddy_bear * 4.10) + (num_minion * 8.20) \
               + (num_track * 2)
if count_toys >= 50:
    sum_of_sales = (sum_of_sales * 0.75)
left_money = (sum_of_sales * 0.9)
if left_money >= trip_price:
    print(f"Yes! {left_money - trip_price:.2f} lv left.")
else:
    print(f"Not enough money! {trip_price - left_money:.2f} lv needed.")


