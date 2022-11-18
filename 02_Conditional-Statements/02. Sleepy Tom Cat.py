holidays = int(input())
workdays = 365 - holidays
norm_of_games = 30000
time_for_play_holiday = holidays * 127
time_for_play_workdays = workdays * 63
all_time_for_play = time_for_play_holiday + time_for_play_workdays
hours_of_play = abs(all_time_for_play - norm_of_games) // 60
minutes_of_play = abs(all_time_for_play - norm_of_games) % 60
if all_time_for_play > norm_of_games:
    print(f"Tom will run away")
    print(f"{hours_of_play} hours and {minutes_of_play} minutes more for play")
elif all_time_for_play < norm_of_games:
    print(f"Tom sleeps well")
    print(f"{hours_of_play} hours and {minutes_of_play} minutes less for play")
