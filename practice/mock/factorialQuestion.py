"""
* Find the Factorial of a Number using while loop
"""

# def factorial_number(number):
#     factorial = 1

#     while number > 0:
#         factorial *= number
#         number -= 1
#     return factorial

# number = int(input("please enter a number: "))
# print(factorial_number(number))


def factorial(number):
    fact = 1
    while number > 0:
        fact *= number
        number -= 1
    return fact

number = int(input("Please input a number: "))
print(factorial(number))