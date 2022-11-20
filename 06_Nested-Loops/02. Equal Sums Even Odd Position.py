first_number = int(input())
second_number = int(input())
sum_odd = 0
sum_even = 0
is_founded_number = False
for x in range(first_number, second_number+1):
    number = str(x)
    for index, digit in enumerate(number):
        if index % 2 == 0:
            sum_even += int(digit)
        else:
            sum_odd += int(digit)
    if sum_odd == sum_even:
        is_founded_number = True
        print(number, end=" ")
    sum_odd = 0
    sum_even = 0
if not is_founded_number:
    exit()



