n = int(input())
sum_left = 0
sum_right = 0
for number in range(1, n+1):
    value_left = int(input())
    sum_left += value_left
for number in range(1, n+1):
    value_right = int(input())
    sum_right += value_right
if sum_right == sum_left:
    print(f"Yes, sum = {sum_left}")
else:
    print(f"No, diff = {abs(sum_left - sum_right)}")

