
principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Please enter the principle amount: "))
    if principle < 0:
        print("Invalid input. Principle cannot be less than zero. Please try again.")
    else:
        break

while True:
    rate = float(input("Please enter the annual interest rate (in %): "))
    if rate < 0:
        print("Invalid input. Interest rate cannot be less than zero. Please try again.")
    else:
        break

while True:
    time = int(input("Please enter the time in years: "))
    if time < 0:
        print("Invalid input. Time cannot be less than zero. Please try again.")
    else:
        break

total = principle * pow((1 + rate / 100), time)

print(f"Balance after {time} years: INR {total:.2f}")
