import sys
max_floor = - sys.maxsize
floors = int(input())
rooms = int(input())
for number_of_floors in range(floors, 0, -1):
    for number_of_rooms in range(0, rooms):
        if floors == 1:
            print(f"L{number_of_floors}{number_of_rooms}", end=" ")
            number_of_rooms += 1
            continue
        if max_floor <= number_of_floors:
            max_floor = number_of_floors
            print(f"L{max_floor}{number_of_rooms}", end=" ")
            number_of_rooms += 1
        elif number_of_floors % 2 == 0:
            print(f"O{number_of_floors}{number_of_rooms}", end=" ")
            number_of_rooms += 1
        else:
            print(f"A{number_of_floors}{number_of_rooms}", end=" ")
            number_of_rooms += 1
    print()
    number_of_floors -= 1
