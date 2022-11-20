change = float(input())
change_in_pennies = int(change * 100)
count_pennies = 0
while change_in_pennies != 0:
    if change_in_pennies // 200:
        count_pennies += 1
        change_in_pennies -= 200
    elif change_in_pennies // 100:
        count_pennies += 1
        change_in_pennies -= 100
    elif change_in_pennies // 50:
        count_pennies += 1
        change_in_pennies -= 50
    elif change_in_pennies // 20:
        count_pennies += 1
        change_in_pennies -= 20
    elif change_in_pennies // 10:
        count_pennies += 1
        change_in_pennies -= 10
    elif change_in_pennies // 5:
        count_pennies += 1
        change_in_pennies -= 5
    elif change_in_pennies // 2:
        count_pennies += 1
        change_in_pennies -= 2
    if change_in_pennies == 1:
        count_pennies += 1
        change_in_pennies -= 1
print(count_pennies)
