# Most Asked If-Elif Problems in Python

# 1. Check if a number is positive, negative, or zero
number = int(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# 2. Grade Calculator
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F (Failed)")

# 3. Check if a year is a Leap Year
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a Leap Year.")
else:
    print(f"{year} is not a Leap Year.")

# 4. Determine if a person is a Child, Teen, or Adult
age = int(input("Enter your age: "))
if age < 13:
    print("You are a Child.")
elif 13 <= age < 20:
    print("You are a Teenager.")
else:
    print("You are an Adult.")

# 5. Even or Odd Checker
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is Even.")
else:
    print("The number is Odd.")

# 6. Largest of Three Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a >= b and a >= c:
    print(f"{a} is the largest number.")
elif b >= a and b >= c:
    print(f"{b} is the largest number.")
else:
    print(f"{c} is the largest number.")

# 7. Check if a Character is a Vowel or Consonant
char = input("Enter a single character: ").lower()
if char in "aeiou":
    print("It's a Vowel.")
else:
    print("It's a Consonant.")

# 8. Check if a Number is Divisible by 5 and 11
num = int(input("Enter a number: "))
if num % 5 == 0 and num % 11 == 0:
    print("The number is divisible by both 5 and 11.")
else:
    print("The number is not divisible by both 5 and 11.")
