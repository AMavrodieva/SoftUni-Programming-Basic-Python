price_per_baggage_over_20kg = float(input())
kg_per_baggage = float(input())
days_to_holiday = int(input())
count_baggage = int(input())
fee_for_baggage = 0
if kg_per_baggage < 10:
    fee_for_baggage = 0.20 * price_per_baggage_over_20kg
elif 10 <= kg_per_baggage <= 20:
    fee_for_baggage = 0.50 * price_per_baggage_over_20kg
elif kg_per_baggage > 20:
    fee_for_baggage = price_per_baggage_over_20kg
if days_to_holiday > 30:
    fee_for_baggage *= 1.10
elif 7 <= days_to_holiday <= 30:
    fee_for_baggage *= 1.15
elif days_to_holiday < 7:
    fee_for_baggage *= 1.40
total_price = count_baggage * fee_for_baggage
print(f"The total price of bags is: {total_price:.2f} lv. ")
