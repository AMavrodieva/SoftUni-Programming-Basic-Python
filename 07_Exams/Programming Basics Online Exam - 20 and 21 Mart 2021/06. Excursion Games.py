number_of_players = int(input())
count_win = 0
count_lost = 0
for game_continue in range(1, number_of_players + 1):
    destination = input()
    sum_of_number = 0
    count_of_number = int(len(destination))
    for number in range(1, count_of_number + 1):
        current_number = int(input())
        sum_of_number += current_number
    if sum_of_number % count_of_number == 0:
        print(f"Win")
        count_win += 1
    else:
        print("Lost")
        count_lost += 1
percentage_win = count_win / number_of_players * 100
percentage_lost = count_lost / number_of_players * 100
print(f"Win: {percentage_win:.2f}%")
print(f"Lost: {percentage_lost:.2f}%")

