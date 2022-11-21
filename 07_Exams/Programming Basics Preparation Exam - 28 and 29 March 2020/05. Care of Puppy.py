quantity_of_purchased_dog_food = int(input())
quantity_into_grams = quantity_of_purchased_dog_food * 1000
command = input()
food_eaten = 0
left_food = 0
while command != "Adopted":
    food_per_day = int(command)
    food_eaten += food_per_day
    left_food = quantity_into_grams - food_eaten
    command = input()
if left_food >= 0:
    print(f"Food is enough! Leftovers: {left_food} grams.")
else:
    print(f"Food is not enough. You need {abs(left_food)} grams more.")
