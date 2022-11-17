price_strawberries = float(input())
quantity_bananas = float(input())
quantity_oranges = float(input())
quantity_raspberries = float(input())
quantity_strawberries = float(input())
price_raspberries = 0.5 * price_strawberries
price_oranges = 0.6 * price_raspberries
price_bananas = 0.2 * price_raspberries
sum_of_strawberries = quantity_strawberries * price_strawberries
sum_of_bananas = quantity_bananas * price_bananas
sum_of_raspberries = quantity_raspberries * price_raspberries
sum_of_oranges = quantity_oranges * price_oranges
print(sum_of_strawberries + sum_of_raspberries + sum_of_bananas + sum_of_oranges)
