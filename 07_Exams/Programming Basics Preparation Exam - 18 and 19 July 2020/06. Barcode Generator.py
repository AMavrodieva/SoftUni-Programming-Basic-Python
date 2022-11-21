start_number = int(input())
finish_number = int(input())
for number in range(start_number, finish_number + 1):
    current_number = str(number)
    start_number = str(start_number)
    finish_number = str(finish_number)
    for index, digit in enumerate(current_number):
        if index == 0:
            value = int(digit)
            if value == 0 or value % 2 == 0:
                break
            first = int(start_number[0])
            second = int(finish_number[0])
            if value in range(first, second+1):
                continue
            else:
                break
        elif index == 1:
            value = int(digit)
            if value == 0 or value % 2 == 0:
                break
            first = int(start_number[1])
            second = int(finish_number[1])
            if value in range(first, second + 1):
                continue
            else:
                break
        elif index == 2:
            value = int(digit)
            if value == 0 or value % 2 == 0:
                break
            first = int(start_number[2])
            second = int(finish_number[2])
            if value in range(first, second + 1):
                continue
            else:
                break
        elif index == 3:
            value = int(digit)
            if value == 0 or value % 2 == 0:
                break
            first = int(start_number[3])
            second = int(finish_number[3])
            if value in range(first, second + 1):
                print(current_number, end=" ")
            else:
                break

