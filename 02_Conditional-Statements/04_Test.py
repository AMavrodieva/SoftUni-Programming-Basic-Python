number = float(input())
unit_in = input()
unit_out = input()
convert_out = 0
if unit_in == 'm' and unit_out == 'mm':
    convert_out = f"{number * 1000:.3f}"
elif unit_in == 'm' and unit_out == 'cm':
    convert_out = f"{number * 100:.3f}"
elif unit_in == 'cm' and unit_out == 'mm':
    convert_out = f"{number * 10:.3f}"
elif unit_in == 'cm' and unit_out == 'm':
    convert_out = f"{number / 100:.3f}"
elif unit_in == 'mm' and unit_out == 'm':
    convert_out = f"{number / 1000:.3f}"
elif unit_in == 'mm' and unit_out == 'cm':
    convert_out = f"{number / 10:.3f}"
print(convert_out)
