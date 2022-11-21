days = int(input())
saved_money = 0
count_win_days = 0
count_loss_days = 0
for contest in range(1, days + 1):
    command = input()
    saved_money_per_day = 0
    count_wins = 0
    count_loss = 0
    while command != "Finish":
        name_of_sport = command
        result = input()
        if result == "win":
            saved_money_per_day += 20
            count_wins += 1
        elif result == "lose":
            count_loss += 1
        command = input()
    if count_wins > count_loss:
        saved_money_per_day *= 1.10
        count_win_days += 1
    else:
        count_loss_days += 1
    saved_money += saved_money_per_day
if count_win_days > count_loss_days:
    saved_money *= 1.20
    print(f"You won the tournament! Total raised money: {saved_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {saved_money:.2f}")
