price_vegetable = float(input())
price_fruit = float(input())
quantity_vegetable = int(input())
quantity_fruit = int(input())
sales_euro = ((price_vegetable * quantity_vegetable) + (price_fruit * quantity_fruit)) / 1.94
print(f'{sales_euro:.2f}')
