num_of_bitcoin = int(input())
num_of_chinese_yuan = float(input())
commission = float(input())
convert_bitcoin_to_euro = (num_of_bitcoin * 1168 / 1.95)
convert_chinese_yuan_to_euro = num_of_chinese_yuan * 0.15 * 1.76 / 1.95
sum_of_euro = convert_bitcoin_to_euro + convert_chinese_yuan_to_euro
commission_tax = sum_of_euro * (commission / 100)
print(f'{sum_of_euro - commission_tax:.2f}')
# друг вариант за форматиране
#print("%.2f" % (sum_of_euro - commission_tax))