needed_money = float(input())
owned_money = float(input())
count_days = 0
spending_days = 0
while owned_money < needed_money and spending_days < 5:
    action = input()
    money = float(input())
    count_days += 1
    if action == "save":
        owned_money += money
        spending_days = 0
    elif action == "spend":
        owned_money -= money
        spending_days += 1
        if owned_money < 0:
            owned_money = 0
if spending_days == 5:
    print(f"You can't save the money.")
    print(f"{count_days}")
elif owned_money >= needed_money:
    print(f"You saved the money for {count_days} days.")