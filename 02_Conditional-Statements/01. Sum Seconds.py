first_time = int(input())
second_time = int(input())
third_time = int(input())
sum_time = first_time + second_time + third_time
# minutes = int(sum_time / 60)
minutes = sum_time//60
seconds = sum_time % 60
if seconds <= 9:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')
