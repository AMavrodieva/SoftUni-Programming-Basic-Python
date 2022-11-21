number_of_group = int(input())
count_of_people = 0
people_go_to_musala = 0
people_go_to_monblan = 0
people_go_to_kalimandjaro = 0
people_go_to_k2 = 0
people_go_to_everest = 0
for group in range(1, number_of_group+1):
    number_of_people = int(input())
    count_of_people += number_of_people
    if number_of_people <= 5:
        people_go_to_musala += number_of_people
    elif 6 <= number_of_people <= 12:
        people_go_to_monblan += number_of_people
    elif 13 <= number_of_people <= 25:
        people_go_to_kalimandjaro += number_of_people
    elif 26 <= number_of_people <= 40:
        people_go_to_k2 += number_of_people
    elif number_of_people >= 41:
        people_go_to_everest += number_of_people
percentage_people_go_to_musala = people_go_to_musala / count_of_people * 100
percentage_people_go_to_monblan = people_go_to_monblan / count_of_people * 100
percentage_people_go_to_kalimandjaro = people_go_to_kalimandjaro / count_of_people * 100
percentage_people_go_to_k2 = people_go_to_k2 / count_of_people * 100
percentage_people_go_to_everest = people_go_to_everest / count_of_people * 100
print(f"{percentage_people_go_to_musala:.2f}%")
print(f"{percentage_people_go_to_monblan:.2f}%")
print(f"{percentage_people_go_to_kalimandjaro:.2f}%")
print(f"{percentage_people_go_to_k2:.2f}%")
print(f"{percentage_people_go_to_everest:.2f}%")
