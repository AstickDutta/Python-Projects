# def check_prime_number(number):
#     if number < 2:
#         return False
    
#     for num in range(3, number):
#         if number % num == 0:
#             return False
#     return True

# number = int(input("Please enter a number: "))
# print(check_prime_number(number))


# def check_prime_number(number):
#     if number < 2:
#         return False

#     for num in range(2, number):
#         if number % num == 0:
#             return False
#     return True

# def find_prime_numbers_range(firstNumber, lastNumber):
#     prime_numbers = []
#     for num in range(firstNumber, lastNumber + 1):
#         if check_prime_number(num):
#             prime_numbers.append(num)
#     print("Prime numbers in the given range are:", prime_numbers)

# firstNumber = int(input("Please input the first number: "))
# lastNumber = int(input("Please input the second number: "))

# find_prime_numbers_range(firstNumber, lastNumber)


def check_prime_number(number):
    if number < 2:
        return "given number cant not be prime"
    for num in range(2, int(number ** 0.5) +1):
        if number % num == 0:
            return "given number is not a prime number"
    return "given number is a prime number"

number = int(input("Please input a number: "))
print(check_prime_number(number))