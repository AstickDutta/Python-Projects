# def factorial(number):
#     fact = 1
#     for num in range(1, number + 1):
#         fact *= num
#     return fact

# def is_strong_number(number):
#     str_num = str(number)
#     sum = 0

#     for digit in str_num:
#         strong_num = factorial(int(digit))
#         sum += strong_num
#     return sum == number

# number = int(input("Please enter a number: "))
# print(is_strong_number(number))

def factorial(number):
    fact = 1
    for num in range(1, number + 1):
        fact *= num
    return fact

def strong_number(number):
    str_number = str(number)
    sum = 0
    for num in str_number:
        sum += factorial(int(num))
    return "Given number is a strong number..!" if sum == number else "Given number is not a strong number..!"

number = int(input("Please input a number: "))
print(strong_number(number))
