number_of_jury = int(input())
command = input()
score = 0
counter_grade = 0
avg_score_per_presentation = 0
sum_of_avg_score = 0
counter_presentation = 0
while command != "Finish":
    name_of_presentation = command
    counter_presentation += 1
    grade = float(input())
    while counter_grade != number_of_jury:
        score += grade
        counter_grade += 1
        if counter_grade == number_of_jury:
            avg_score_per_presentation = score / number_of_jury
            sum_of_avg_score += avg_score_per_presentation
            print(f"{name_of_presentation} - {avg_score_per_presentation:.2f}.")
            counter_grade = 0
            score = 0
            avg_score_per_presentation = 0
            break
        grade = float(input())
    command = input()
avg_score = sum_of_avg_score / counter_presentation
print(f"Student's final assessment is {avg_score:.2f}.")
