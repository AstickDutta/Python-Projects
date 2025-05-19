n = int(input("Enter a number: "))

# 1. Right-Angled Triangle
for i in range(1, n+1):
    print("*" * i)

# 2. Inverted Right-Angled Triangle
for i in range(n, 0, -1):
    print("*" * i)

# 3. Pyramid Pattern
for i in range(1, n+1):
    print(" " * (n-i) + "*" * (2*i - 1))

# 4. Inverted Pyramid
for i in range(n, 0, -1):
    print(" " * (n-i) + "*" * (2*i - 1))

# 5. Hollow Square
print("*" * n)
for i in range(n-2):
    print("*" + " " * (n-2) + "*")
print("*" * n)

# 6. Diamond Pattern
for i in range(1, n+1):
    print(" " * (n-i) + "*" * (2*i - 1))
for i in range(n-1, 0, -1):
    print(" " * (n-i) + "*" * (2*i - 1))

# 7. Hollow Pyramid
for i in range(1, n):
    if i == 1:
        print(" " * (n-i) + "*")
    else:
        print(" " * (n-i) + "*" + " " * (2*i - 3) + "*")
print("*" * (2*n - 1))

# 8. Pascal's Triangle
from math import factorial
for i in range(n):
    print(" " * (n-i-1), end="")
    for j in range(i+1):
        print(factorial(i) // (factorial(j) * factorial(i-j)), end=" ")
    print()

# 9. Cross (X) Pattern
for i in range(n):
    for j in range(n):
        if j == i or j == n-i-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# 10. Hollow Diamond
for i in range(1, n+1):
    if i == 1:
        print(" " * (n-i) + "*")
    else:
        print(" " * (n-i) + "*" + " " * (2*i - 3) + "*")
for i in range(n-1, 0, -1):
    if i == 1:
        print(" " * (n-i) + "*")
    else:
        print(" " * (n-i) + "*" + " " * (2*i - 3) + "*")

