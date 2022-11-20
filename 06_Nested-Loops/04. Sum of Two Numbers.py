first_number = int(input())
second_number = int(input())
magical_number = int(input())
combination = 0
x = 0
y = 0
counter = 0
is_founded_combinations = False
for x in range(first_number, second_number+1):
    for y in range(first_number, second_number+1):
        combination = x + y
        counter += 1
        if combination == magical_number:
            is_founded_combinations = True
            break
    if is_founded_combinations:
        break
    if first_number == second_number:
        counter += 1
if is_founded_combinations:
    print(f"Combination N:{counter} ({x} + {y} = {magical_number})")
else:
    print(f"{counter} combinations - neither equals {magical_number}")
