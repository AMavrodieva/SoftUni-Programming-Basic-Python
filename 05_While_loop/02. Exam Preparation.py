number_of_low_score = int(input())
count_task = 0
grades_sum = 0
count_bad_score = 0
last_problem = ""
is_bad_score = True
while count_bad_score < number_of_low_score:
    name_of_task = input()
    if name_of_task == "Enough":
        is_bad_score = False
        break
    grade = int(input())
    if grade <= 4:
        count_bad_score += 1
    count_task += 1
    grades_sum += grade
    last_problem = name_of_task
average_score = grades_sum / count_task
if not is_bad_score:
    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {count_task}")
    print(f"Last problem: {last_problem}")
else:
    print(f"You need a break, {number_of_low_score} poor grades.")

