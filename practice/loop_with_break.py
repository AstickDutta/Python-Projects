# loop_with_break.py

# Problem 1: Find the first number divisible by 7 in a range.
for num in range(1, 20):
    if num % 7 == 0:
        print("Found:", num)
        break

# Problem 2: Stop a loop when a negative number is encountered.
numbers = [1, 3, 5, -1, 7, 9]
for num in numbers:
    if num < 0:
        print("Negative number found, stopping loop.")
        break
    print(num)

# Problem 3: Break out of an infinite loop when a condition is met.
count = 0
while True:
    print("Count:", count)
    count += 1
    if count == 5:
        break
