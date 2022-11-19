kind_of_flowers = input()
count_of_flowers = int(input())
budget = int(input())
total_price = 0
if kind_of_flowers == "Roses":
    total_price = count_of_flowers * 5
    if count_of_flowers > 80:
        total_price *= 0.9
elif kind_of_flowers == "Dahlias":  # далия
    total_price = count_of_flowers * 3.80
    if count_of_flowers > 90:
        total_price *= 0.85
elif kind_of_flowers == "Tulips":  # лалета
    total_price = count_of_flowers * 2.80
    if count_of_flowers > 80:
        total_price *= 0.85
elif kind_of_flowers == "Narcissus":  # нарцис
    total_price = count_of_flowers * 3
    if count_of_flowers < 120:
        total_price *= 1.15
elif kind_of_flowers == "Gladiolus":  # гладиола
    total_price = count_of_flowers * 2.50
    if count_of_flowers < 80:
        total_price *= 1.20
difference = abs(total_price - budget)
if budget >= total_price:
    print(f"Hey, you have a great garden with {count_of_flowers} {kind_of_flowers} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")
