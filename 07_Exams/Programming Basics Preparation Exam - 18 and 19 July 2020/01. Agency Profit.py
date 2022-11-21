airline = input()
number_of_tickets_for_adults = int(input())
number_of_tickets_for_kids = int(input())
net_price_of_ticket_for_adults = float(input())
service_fee = float(input())
price_of_ticket_for_adults = net_price_of_ticket_for_adults + service_fee
price_of_ticket_for_kids = 0.30 * net_price_of_ticket_for_adults + service_fee
sales = (number_of_tickets_for_adults * price_of_ticket_for_adults) + (number_of_tickets_for_kids * price_of_ticket_for_kids)
profit = 0.20 * sales
print(f"The profit of your agency from {airline} tickets is {profit:.2f} lv.")