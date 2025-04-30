# def check_prime_number(number):
#     if number < 2:
#         return False
    
#     for num in range(3, number):
#         if number % num == 0:
#             return False
#     return True

# number = int(input("Please enter a number: "))
# print(check_prime_number(number))


def check_prime_number(number):
    if number < 2:
        return False

    for num in range(2, number):
        if number % num == 0:
            return False
    return True

def find_prime_numbers_range(firstNumber, lastNumber):
    prime_numbers = []
    for num in range(firstNumber, lastNumber + 1):
        if check_prime_number(num):
            prime_numbers.append(num)
    print("Prime numbers in the given range are:", prime_numbers)

firstNumber = int(input("Please input the first number: "))
lastNumber = int(input("Please input the second number: "))

find_prime_numbers_range(firstNumber, lastNumber)