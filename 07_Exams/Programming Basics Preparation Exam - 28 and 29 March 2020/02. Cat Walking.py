minutes_for_walking = int(input())
number_of_walking = int(input())
calories = int(input())
calories_burned = minutes_for_walking * 5 * number_of_walking
if calories_burned >= 0.50 * calories:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {calories_burned}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {calories_burned}.")