from math import pi
kind_of_figure = input()
if kind_of_figure == "square":
    length_side = float(input())
    print(f'{length_side * length_side:.3f}')
elif kind_of_figure == "rectangle":
    length_side = float(input())
    width_side = float(input())
    print(f"{length_side * width_side:.3f}")
elif kind_of_figure == "circle":
    radios = float(input())
    print(f"{(pi * radios ** 2):.3f}")
elif kind_of_figure == "triangle":
    length_side = float(input())
    length_high = float(input())
    print(f"{length_side * length_high / 2:.3f}")
