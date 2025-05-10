
import time
my_time = int(input("Enter the time in seconds: "))

for i in range(my_time, 0, -1):
    second = i % 60
    minutes = (i // 60) % 60
    hours = i // 3600
    print(f"{hours:02}:{minutes:02}:{second:02}")
    time.sleep(1)

print("Time's up!")

def countdown_timer():
    my_time = int(input("Enter the time in seconds: "))

    for second in range(my_time, 0, -1 ):
        seconds = second % 60
        minutes = ( second // 60) % 60
        hours = second // 3600
        print(f"{hours:02}:{minutes:02}:{seconds:02}")
        time.sleep(1)

    print("Time's up!")

countdown_timer()