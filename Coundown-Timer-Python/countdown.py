import time

# my_time1 = int(input("enter the time: "))

# for i in range(0, my_time1):
#     print(f"{my_time1 - i} seconds remaining...")
#     time.sleep(1)
# print("times up!!")

my_time = int(input("enter the time: "))

for i in range(my_time, 0, -1):
    seceond = i % 60
    minutes = int(i/60) % 60
    hours = int(i/3600)
    print(f"{hours:02}:{minutes:02}:{seceond:02}")
    time.sleep(1)
print("times up!!")

