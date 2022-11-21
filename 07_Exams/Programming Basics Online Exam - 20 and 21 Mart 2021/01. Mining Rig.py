from math import ceil
price_video_game = int(input())
price_adapter = int(input())
price_amperage = float(input())
profit_per_day = float(input())
total_price_video_game = price_video_game * 13
total_price_adapter = price_adapter * 13
other_components = 1000
spend_money = total_price_video_game + total_price_adapter + other_components
profit_from_game = profit_per_day - price_amperage
total_profit_per_day = profit_from_game * 13
days = spend_money / total_profit_per_day
print(f"{spend_money}")
print(f"{ceil(days)}")