weight = int(input())
length = int(input())
height = int(input())
area = weight * length * height
command = input()
count_box = 0
while command != "Done":
    number_box = int(command)
    count_box += number_box
    if area <= count_box:
        break
    command = input()
difference = abs(area - count_box)
if area <= count_box:
    print(f"No more free space! You need {difference} Cubic meters more.")
else:
    print(f"{difference} Cubic meters left.")
