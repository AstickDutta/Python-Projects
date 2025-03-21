# loop_with_continue.py

# Problem 1: Print numbers from 1 to 10, but skip 5.
for num in range(1, 11):
    if num == 5:
        continue
    print(num)

# Problem 2: Print even numbers from 1 to 20.
for num in range(1, 21):
    if num % 2 != 0:
        continue
    print(num)

# Problem 3: Iterate over a string and skip vowels.
string = "Hello World"
for char in string:
    if char.lower() in "aeiou":
        continue
    print(char, end="")
