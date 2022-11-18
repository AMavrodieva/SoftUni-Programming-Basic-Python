from math import ceil, floor
vineyard_area = int(input())
grapes_per_one_sq_meter = float(input())
needed_liters_of_wine = int(input())
staff = int(input())
grapes_for_wine = 0.40 * (vineyard_area * grapes_per_one_sq_meter)
produced_liters_of_wine = grapes_for_wine / 2.50
if int(produced_liters_of_wine) < needed_liters_of_wine:
    print(f"It will be a tough winter! More "
          f"{floor(needed_liters_of_wine - produced_liters_of_wine)} liters wine needed.")
elif int(produced_liters_of_wine) > needed_liters_of_wine:
    print(f"Good harvest this year! Total wine: {floor(produced_liters_of_wine)} liters.")
    print(f"{ceil(produced_liters_of_wine - needed_liters_of_wine)} liters left -> "
          f"{ceil((ceil(produced_liters_of_wine) - needed_liters_of_wine) / staff)} liters per person.")
