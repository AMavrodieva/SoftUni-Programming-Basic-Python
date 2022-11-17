length = float(input())
weight = float(input())
length_cm = length * 100
weight_cm = weight * 100
number_by_row = (weight_cm -100) // 70
number_by_column = length_cm // 120
count_seat = (number_by_row * number_by_column) - 3
print(count_seat)