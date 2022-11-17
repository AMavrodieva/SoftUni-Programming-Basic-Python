number_of_days = int(input())
number_of_participants = int(input())
number_of_cake = int(input())
number_of_waffles = int(input())
number_of_pancake = int(input())
sum_of_sold_cake_per_day = number_of_participants * number_of_cake * 45
sum_of_sold_waffles_per_day = number_of_participants * number_of_waffles * 5.80
sum_of_sold_pancake_per_day = number_of_participants * number_of_pancake * 3.20
amount_collected = (sum_of_sold_cake_per_day +
                    sum_of_sold_waffles_per_day +
                    sum_of_sold_pancake_per_day) * number_of_days
print((amount_collected * 7) / 8)