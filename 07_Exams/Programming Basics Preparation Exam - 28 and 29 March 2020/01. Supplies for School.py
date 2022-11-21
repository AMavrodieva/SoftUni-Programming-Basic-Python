number_of_pencil = int(input())
number_of_marker = int(input())
cleaning_detergent = float(input())
discount = int(input())
needed_money_for_pencil = number_of_pencil * 5.80
needed_money_for_marker = number_of_marker * 7.20
needed_money_for_cleaning_detergent = cleaning_detergent * 1.20
needed_money = needed_money_for_pencil + needed_money_for_marker + needed_money_for_cleaning_detergent
total_needed_money = needed_money - (needed_money * discount / 100)
print(f"{total_needed_money:.3f}")
