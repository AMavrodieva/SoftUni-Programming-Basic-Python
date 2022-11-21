from math import ceil
football_fan = input()
budget = float(input())
number_of_bottle_beer = int(input())
number_of_packet_of_chips = int(input())
total_price_for_beers = number_of_bottle_beer * 1.20
price_one_chips = 0.45 * total_price_for_beers
total_price_for_chips = ceil(price_one_chips * number_of_packet_of_chips)
expenses = total_price_for_beers + total_price_for_chips
difference = abs(budget - expenses)
if budget >= expenses:
    print(f"{football_fan} bought a snack and has {difference:.2f} leva left.")
else:
    print(f"{football_fan} needs {difference:.2f} more leva!")

