price_mackerel = float(input())
price_sprat = float(input())
quantity_bonito = float(input())
quantity_scad = float(input())
quantity_mussels = int(input())
price_bonito = price_mackerel * 1.6
price_scad = price_sprat * 1.8
total_sales = (price_bonito * quantity_bonito) \
              + (price_scad * quantity_scad) + \
              (7.5 * quantity_mussels)
print(f'{total_sales:.2f}')




