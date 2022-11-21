days = int(input())
total_quantity_of_food = float(input())
eaten_food_from_dog = 0
eaten_food_from_cat = 0
count_days = 0
count_biscuits_dog = 0
count_biscuits_cat = 0
for current_day in range(1, days + 1):
    eaten_food_from_dog_daily = int(input())
    eaten_food_from_cat_daily = int(input())
    eaten_food_from_dog += eaten_food_from_dog_daily
    eaten_food_from_cat += eaten_food_from_cat_daily
    if current_day % 3 == 0:
        count_biscuits_dog += 0.10 * eaten_food_from_dog_daily
        count_biscuits_cat += 0.10 * eaten_food_from_cat_daily
total_eaten_food = eaten_food_from_dog + eaten_food_from_cat
total_eaten_biscuits = count_biscuits_dog + count_biscuits_cat
percentage_eaten_food = total_eaten_food / total_quantity_of_food * 100
percentage_eaten_food_from_dog = eaten_food_from_dog / total_eaten_food * 100
percentage_eaten_food_from_cat = eaten_food_from_cat/ total_eaten_food * 100
print(f"Total eaten biscuits: {round(total_eaten_biscuits)}gr.")
print(f"{percentage_eaten_food:.2f}% of the food has been eaten.")
print(f"{percentage_eaten_food_from_dog:.2f}% eaten from the dog.")
print(f"{percentage_eaten_food_from_cat:.2f}% eaten from the cat.")
