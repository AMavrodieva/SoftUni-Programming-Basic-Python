from math import floor
kind_of_year = input()
number_of_holiday = int(input())
number_of_weekend_with_family = int(input())
number_of_play_in_holidays = number_of_holiday * 2 / 3
number_of_play_with_old_friends = number_of_weekend_with_family
weekend_of_sofia = 48 - number_of_weekend_with_family
number_of_play_in_sofia = weekend_of_sofia * 3 / 4
total_play_normal_year = number_of_play_in_sofia + number_of_play_with_old_friends \
                            + number_of_play_in_holidays
total_play_leap_year = total_play_normal_year * 1.15
if kind_of_year == "normal":
    print(floor(total_play_normal_year))
elif kind_of_year == "leap":
    print(floor(total_play_leap_year))

