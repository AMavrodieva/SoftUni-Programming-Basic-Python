command = input()
total_money = 0
while command != "NoMoreMoney":
    money = float(command)
    if money < 0:
        print(f"Invalid operation!")
        break
    else:
        print(f"Increase: {money:.2f}")
        total_money += money

    command = input()

print(f"Total: {total_money:.2f}")
