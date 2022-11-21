number_of_bitcoin = int(input())
number_of_chinese_yuan = float(input())
commission = float(input())
convert_bgn_from_bitcoin = number_of_bitcoin * 1168
convert_bgn_from_chinese_yuan = number_of_chinese_yuan * 0.15 * 1.76
money_in_euro = (convert_bgn_from_bitcoin + convert_bgn_from_chinese_yuan) / 1.95
current_commission = (money_in_euro * commission) / 100
left_money = money_in_euro - current_commission
print(f"{left_money:.2f}")
