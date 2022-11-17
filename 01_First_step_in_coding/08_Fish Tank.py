length = int(input())
width = int(input())
height = int(input())
occupied_percentage = float(input())
aquarium_volume = length * width * height
total_litter = aquarium_volume * 0.001
print(total_litter * (1-occupied_percentage/100))
