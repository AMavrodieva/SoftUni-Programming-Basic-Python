number = int(input())
is_special_number = False
first_number = 0
second_number = 0
third_number = 0
forth_number = 0
for digit in range(1111, 10000):
    current_number = str(digit)
    for index, value in enumerate(current_number):
        if index == 0:
            first_number = int(value)
        elif index == 1:
            second_number = int(value)
        elif index == 2:
            third_number = int(value)
        elif index == 3:
            forth_number = int(value)
    if first_number != 0 and number % first_number == 0:
        if second_number != 0 and number % second_number == 0:
            if third_number != 0 and number % third_number == 0:
                if forth_number != 0 and number % forth_number == 0:
                    is_special_number = True
                    print(current_number, end=" ")
    digit += 1

if not is_special_number:
    exit()
