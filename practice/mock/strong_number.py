def factorial(number):
    fact = 1
    for num in range(1, number + 1):
        fact *= num
    return fact

def is_strong_number(number):
    str_num = str(number)
    sum = 0

    for digit in str_num:
        strong_num = factorial(int(digit))
        sum += strong_num
    return sum == number

number = int(input("Please enter a number: "))
print(is_strong_number(number))