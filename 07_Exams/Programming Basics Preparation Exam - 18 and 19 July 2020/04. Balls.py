from math import floor
number_of_balls = int(input())
score = 0
count_of_red_balls = 0
count_of_orange_balls = 0
count_of_yellow_balls = 0
count_of_white_balls = 0
count_of_other_color_balls = 0
count_of_black_balls = 0
for balls in range(1, number_of_balls + 1):
    color = input()
    if color == "red":
        score += 5
        count_of_red_balls += 1
    elif color == "orange":
        score += 10
        count_of_orange_balls += 1
    elif color == "yellow":
        score += 15
        count_of_yellow_balls += 1
    elif color == "white":
        score += 20
        count_of_white_balls += 1
    elif color == "black":
        score /= 2
        count_of_black_balls += 1
    else:
        count_of_other_color_balls += 1
        continue
print(f"Total points: {floor(score)}")
print(f"Points from red balls: {count_of_red_balls}")
print(f"Points from orange balls: {count_of_orange_balls}")
print(f"Points from yellow balls: {count_of_yellow_balls}")
print(f"Points from white balls: {count_of_white_balls}")
print(f"Other colors picked: {count_of_other_color_balls}")
print(f"Divides from black balls: {count_of_black_balls}")
