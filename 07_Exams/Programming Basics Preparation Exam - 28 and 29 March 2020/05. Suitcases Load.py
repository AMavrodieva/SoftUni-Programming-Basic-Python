capacity = float(input())
command = input()
counter = 0
taken_space = 0
count_of_suitcase = 0
no_more_space = False
while command != "End":
    area_of_suitcase = float(command)
    taken_space += area_of_suitcase
    counter += 1
    count_of_suitcase += 1
    if counter != 0 and counter % 3 == 0:
        area_of_suitcase *= 0.10
        taken_space += area_of_suitcase
    if taken_space <= capacity:
        command = input()
    else:
        count_of_suitcase -= 1
        no_more_space = True
        print(f"No more space!")
        print(f"Statistic: {count_of_suitcase} suitcases loaded.")
        break
#if no_more_space:
 #   print(f"No more space!")
 #   print(f"Statistic: {count_of_suitcase} suitcases loaded.")
else:
    print(f"Congratulations! All suitcases are loaded!")
    print(f"Statistic: {count_of_suitcase} suitcases loaded.")
