hour_of_exam = int(input())
minute_of_exam = int(input())
hour_of_arriving = int(input())
minute_of_arriving = int(input())
time_of_exam = hour_of_exam * 60 + minute_of_exam
time_of_arriving = hour_of_arriving * 60 + minute_of_arriving
if time_of_arriving > time_of_exam:
    print("Late")
elif time_of_exam - 30 <= time_of_arriving <= time_of_exam:
    print("On time")
else:
    print("Early")
if time_of_exam - 60 < time_of_arriving < time_of_exam:
    print(f"{time_of_exam - time_of_arriving} minutes before the start")
elif time_of_arriving <= time_of_exam - 60:
    minutes = (time_of_exam - time_of_arriving) % 60
    hours = (time_of_exam - time_of_arriving) // 60
    if minutes < 10:
        print(f"{hours}:0{minutes} hours before the start")
    else:
        print(f"{hours}:{minutes} hours before the start")
elif time_of_exam < time_of_arriving < time_of_exam + 60:
    print(f"{time_of_arriving - time_of_exam} minutes after the start")
elif time_of_exam + 60 <= time_of_arriving:
    minutes = (time_of_arriving - time_of_exam) % 60
    hours = (time_of_arriving - time_of_exam) // 60
    # print(f"{hours}:{minutes:0>2d} hours after the start"")
    if minutes < 10:
        print(f"{hours}:0{minutes} hours after the start")
    else:
        print(f"{hours}:{minutes} hours after the start")
