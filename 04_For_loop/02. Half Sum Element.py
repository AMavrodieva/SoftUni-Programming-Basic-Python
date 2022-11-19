import sys
n = int(input())
max_num = -sys.maxsize
sum_of_numbers = 0
for number in range(1, n+1):
    value = int(input())
    if value > max_num:
        max_num = value
    sum_of_numbers += value
if max_num == sum_of_numbers - max_num:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    print("No")
    difference = max_num - (sum_of_numbers - max_num)
    print(f"Diff = {abs(difference)}")
