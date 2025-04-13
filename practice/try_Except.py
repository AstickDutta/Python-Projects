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

"""
🔴 16. A school has following rules for grading system: 
    a. Below 25 - F 
    b. 25 to 45 - E 
    c. 45 to 50 - D 
    d. 50 to 60 - C 
    e. 60 to 80 - B 
    f. Above 80 - A Ask user to enter marks and print the corresponding grade..!
"""

def grade_system():
    marks = int(input("Enter marks of a student in between 0 to 100: "))

    if marks < 0 or 100 < marks:
        print("Given marks should in between 0 to 100..!!")
    else:
        if marks < 25:
            grade = "F"
        elif marks < 45:
            grade = "E"
        elif marks < 50:
            grade = "D"
        elif marks < 60:
            grade = "C"
        elif marks < 80:
            grade = "B"
        else:
            grade = "A"
    return f"Grade is {grade}"

print(grade_system())