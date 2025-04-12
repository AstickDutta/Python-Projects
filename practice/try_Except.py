"""
🔴
    Prompts the user to input a number and determines whether it is a prime number.
    
    Returns:
        str: Message indicating whether the input number is prime or not.
        
    Edge Cases:
        - Handles non-integer input gracefully.
        - Considers numbers less than 2 as non-prime.
"""

def check_prime():
    try:
        number = int(input("Enter a number: "))
        if number < 2:
            return f"Given {number} is not prime..!"
        elif number == 2:
            return f"Given number {number} is Prime number..!"
        else:
            for i in range(2, int(number ** 0.5) + 1):
                if number % i == 0:
                    return f"Given number {number} is a not Prime number..!"
            return f"Given number {number} is a Prime number..!"
    except ValueError:
        return f"Given value is not a valid value so please put a valid value"

print(check_prime())