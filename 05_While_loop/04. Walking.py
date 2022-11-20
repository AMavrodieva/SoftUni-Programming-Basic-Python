goal = 10000
sum_step = 0
while sum_step < goal:
    step = input()
    if step == "Going home":
        step = int(input())
        sum_step += step
        break
    walking_step = int(step)
    sum_step += walking_step
difference = abs(goal - sum_step)
if sum_step >= goal:
    print(f"Goal reached! Good job!")
    print(f"{difference} steps over the goal!")
else:
    print(f"{difference} more steps to reach goal.")