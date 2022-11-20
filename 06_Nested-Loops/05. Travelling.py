destination = input()
min_budget = 0
total_saved_money = 0
is_going_holiday = False
while destination != "End":
    min_budget = float(input())
    while total_saved_money < min_budget:
        current_saved_money = float(input())
        total_saved_money += current_saved_money
        if total_saved_money >= min_budget:
            is_going_holiday = True
            print(f"Going to {destination}!")
            total_saved_money = 0
            destination = input()
            if destination == "End":
                break
            min_budget = float(input())
if destination == "End":
    exit()
