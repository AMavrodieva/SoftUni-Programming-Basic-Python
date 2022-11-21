number_of_cats = int(input())
eaten_food = 0
small_cats = 0
big_cats = 0
huge_cats = 0
for cats in range(1, number_of_cats + 1):
    quantity_food = float(input())
    eaten_food += quantity_food
    if 100 <= quantity_food < 200:
        small_cats += 1
    elif 200 <= quantity_food < 300:
        big_cats += 1
    elif 300 <= quantity_food < 400:
        huge_cats += 1
total_price = (eaten_food / 1000) * 12.45
print(f"Group 1: {small_cats} cats.")
print(f"Group 2: {big_cats} cats.")
print(f"Group 3: {huge_cats} cats.")
print(f"Price for food per day: {total_price:.2f} lv.")
