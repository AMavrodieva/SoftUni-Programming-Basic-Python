name = input()
score = 0
school_class = 0
fail = 0
while True:
    grade = float(input())
    score += grade
    school_class += 1
    if grade < 4:
        fail += 1
        if fail == 2:
            print(f"{name} has been excluded at {school_class - 1} grade")
            break
    if school_class == 12:
        average_grade = score / school_class
        print(f"{name} graduated. Average grade: {average_grade:.2f}")
        break
