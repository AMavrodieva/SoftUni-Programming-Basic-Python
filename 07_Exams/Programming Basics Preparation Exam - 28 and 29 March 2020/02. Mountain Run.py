from math import floor
record = float(input())
distance = float(input())
time_for_meter = float(input())
total_time = distance * time_for_meter
number_of_delays = floor(distance / 50)
time_for_delays = number_of_delays * 30
needed_time = total_time + time_for_delays
if needed_time < record:
    print(f"Yes! The new record is {needed_time:.2f} seconds.")
else:
    difference = needed_time - record
    print(f"No! He was {difference:.2f} seconds slower.")
