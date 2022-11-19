number_tab = int(input())
salary = int(input())
remaining_salary = 0
for tab in range(1, number_tab+1):
    name_tab = input()
    if name_tab == "Facebook":
        salary -= 150
    if name_tab == "Instagram":
        salary -= 100
    if name_tab == "Reddit":
        salary -= 50
    if salary == 0:
        break
if salary == 0:
    print(f"You have lost your salary.")
else:
    print(salary)