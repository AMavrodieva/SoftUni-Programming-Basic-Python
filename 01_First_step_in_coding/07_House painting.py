height_house = float(input())
length = float(input())
height_ceiling = float(input())
area_front_and_back_wall = ((height_house * height_house) * 2 - (2 * 1.2))
area_lateral_wall = ((height_house * length) * 2 - (1.5 * 1.5) * 2)
area_front_back_ceiling = (0.5 * height_house * height_ceiling) * 2
area_lateral_ceiling = 2 * (height_house * length)
need_green_paint = (area_front_and_back_wall + area_lateral_wall) / 3.4
need_red_paint = (area_front_back_ceiling + area_lateral_ceiling) / 4.3
print(f'{need_green_paint:.2f}')
print(f'{need_red_paint:.2f}')
