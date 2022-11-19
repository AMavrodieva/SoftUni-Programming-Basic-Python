n = int(input())
p1 = 0
p2 = 0
p3 = 0
for i in range(1, n+1):
    number = int(input())
    if number % 2 == 0:
        p1 += 1
    if number % 3 == 0:
        p2 += 1
    if number % 4 == 0:
        p3 += 1
group_1 = p1 / n * 100
group_2 = p2 / n * 100
group_3 = p3 / n * 100
print(f"{group_1:.2f}%")
print(f"{group_2:.2f}%")
print(f"{group_3:.2f}%")