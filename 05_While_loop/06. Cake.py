weight = int(input())
length = int(input())
area = weight * length
count_cake = 0
piece_of_cake = input()
is_left_cakes = True
while piece_of_cake != "STOP":
    piece_of_cake = int(piece_of_cake)
    count_cake += piece_of_cake
    if count_cake >= area:
        is_left_cakes = False
        break
    piece_of_cake = input()
difference = abs(area - count_cake)
if is_left_cakes:
    print(f"{difference} pieces are left.")
else:
    print(f"No more cake left! You need {difference} pieces more.")

