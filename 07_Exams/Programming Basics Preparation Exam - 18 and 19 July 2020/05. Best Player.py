import sys
command = input()
best_player = ""
max_goal = - sys.maxsize
is_made_hat_trick = False
while command != "END":
    name_of_player = command
    number_of_goal = int(input())
#    if number_of_goal < 1:
#        number_of_goal = input()
    if number_of_goal > max_goal:
        max_goal = number_of_goal
        best_player = name_of_player
        if number_of_goal >= 3:
            is_made_hat_trick = True
    if number_of_goal >= 10:
        break
    command = input()
print(f"{best_player} is the best player!")
if is_made_hat_trick:
    print(f"He has scored {max_goal} goals and made a hat-trick !!!")
else:
    print(f"He has scored {max_goal} goals.")
