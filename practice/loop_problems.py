# Commonly Asked Loop Problems in Python

# 1. Print numbers from 1 to 10 using a for loop
for i in range(1, 11):
    print(i)

# 2. Print even numbers from 1 to 20 using a while loop
num = 2
while num <= 20:
    print(num)
    num += 2

# 3. Calculate the sum of all numbers from 1 to n (user input)
n = int(input("Enter a number: "))
sum_n = sum(range(1, n+1))
print("Sum of numbers from 1 to", n, "is:", sum_n)

# 4. Print the multiplication table of a given number
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# 5. Find the factorial of a number using a loop
n = int(input("Enter a number: "))
factorial = 1
for i in range(1, n+1):
    factorial *= i
print("Factorial of", n, "is:", factorial)

# 6. Reverse a given number
num = int(input("Enter a number: "))
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num //= 10
print("Reversed number is:", rev)

# 7. Check if a number is prime
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")

# 8. Print Fibonacci series up to n terms
n = int(input("Enter number of terms: "))
a, b = 0, 1
print("Fibonacci sequence:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()

# 9. Count digits in a number
num = int(input("Enter a number: "))
digit_count = len(str(num))
print("Number of digits:", digit_count)

# 10. Print a pattern using nested loops
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
