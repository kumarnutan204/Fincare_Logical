import time
def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  print(f"Time Lapsed = {int(hours)}.{int(mins)}.{sec}")

input("Press Enter to start the timer")
start_time=time.time()

input("Press Enter to stop the timer")
end_time=time.time()

time_diff= end_time-start_time
print(time_convert(time_diff))
