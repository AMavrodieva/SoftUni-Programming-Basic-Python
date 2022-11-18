time_record = float(input())
distance = float(input())
need_time_for_one_meter = float(input())
delay = int(distance / 15) * 12.5
need_time = (distance * need_time_for_one_meter) + delay
if need_time < time_record:
    print(f" Yes, he succeeded! The new world record is {need_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {need_time - time_record:.2f} seconds slower.")