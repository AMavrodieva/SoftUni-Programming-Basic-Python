degrees = float(input())

if degrees <= 11.9 and degrees >= 5:
    print("Cold")
elif degrees <= 14.9 and degrees >=12.00:
    print("Cool")
elif degrees <= 20 and degrees >= 15:
    print("Mild")
elif degrees <= 25.9 and degrees >= 20.1:
    print("Warm")
elif degrees <= 35 and degrees >= 26:
    print("Hot")
else:
    print("unknown")
