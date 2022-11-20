number = int(input())
sum_of_numbers = 0
counter = 0
for first_number in range(0, number+1):
    for second_number in range(0, number + 1):
        for third_number in range(0, number + 1):
            sum_of_numbers = first_number + second_number + third_number
            if sum_of_numbers == number:
                counter += 1
print(counter)
