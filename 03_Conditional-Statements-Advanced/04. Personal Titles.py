ages = float(input())
gender = input()
if ages < 16:
    if gender == "m":
        print("Master")
    else:
        print("Miss")
elif ages >= 16:
    if gender == "m":
        print("Mr.")
    else:
        print("Ms.")
