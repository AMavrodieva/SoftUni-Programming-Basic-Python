length_square = int(input())
width_tile = float(input())
length_tile = float(input())
width_bench = int(input())
length_bench = int(input())
size_bench = width_bench * length_bench
square_free_space = (length_square ** 2) - size_bench
area_tile = width_tile * length_tile
print(f'{square_free_space / area_tile:.2f}')
print(f'{square_free_space / area_tile * 0.2:.2f}')
# или закръгляваме с round
#print(round(square_free_space / area_tile, 2))
#print(round(square_free_space / area_tile * 0.2, 2))
