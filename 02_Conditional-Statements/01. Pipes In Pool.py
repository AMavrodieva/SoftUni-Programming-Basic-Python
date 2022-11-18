volume = int(input())
pipe_flow_P1 = int(input())
pipe_flow_P2 = int(input())
work_hour = float(input())
volume_after_work_pipe_1 = pipe_flow_P1 * work_hour
volume_after_work_pipe_2 = pipe_flow_P2 * work_hour
total_volume = volume_after_work_pipe_1 + volume_after_work_pipe_2
all_percent_volume = total_volume / volume * 100
percent_volume_pipe_1 = volume_after_work_pipe_1 / total_volume * 100
percent_volume_pipe_2 = volume_after_work_pipe_2 /total_volume * 100
if total_volume <= volume:
    print(f"The pool is {all_percent_volume:.2f}% full. Pipe 1:"
          f" {percent_volume_pipe_1:.2f}%. Pipe 2: {percent_volume_pipe_2:.2f}%.")
else:
    print(f"For {work_hour:.2f} hours the pool overflows with {total_volume - volume:.2f} liters.")
