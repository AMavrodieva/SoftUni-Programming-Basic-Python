deposited_amount = float(input())
period_of_deposit = int(input())
annual_interest_rate = float(input())
percent_rate = annual_interest_rate/100
print(deposited_amount + period_of_deposit * (deposited_amount*percent_rate)/12)