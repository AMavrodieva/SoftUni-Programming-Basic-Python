bought_food = int(input())
food_in_grams = bought_food * 1000
command = input()
total_eaten_food = 0
is_left_food = True
while command != "Adopted":
    eaten_food = int(command)
    total_eaten_food += eaten_food
    if food_in_grams >= total_eaten_food:
        is_left_food = True
    else:
        is_left_food = False
    command = input()
if is_left_food:
    difference = food_in_grams - total_eaten_food
    print(f"Food is enough! Leftovers: {difference} grams.")
else:
    difference = total_eaten_food - food_in_grams
    print(f"Food is not enough. You need {difference} grams more.")
