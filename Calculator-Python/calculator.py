# This Python code functions as a simple calculator that performs basic arithmetic operations (addition, subtraction, 
# multiplication, and division) based on user input.

# The steps involved are as follows:
# 1. The user is prompted to input an arithmetic operator (+, -, *, or /).
# 2. The user is then prompted to enter two numerical values, number1 and number2.
# 3. Depending on the chosen operator, the code performs the corresponding operation:
#    - Addition (+): Adds number1 and number2.
#    - Subtraction (-): Subtracts number2 from number1.
#    - Multiplication (*): Multiplies number1 by number2.
#    - Division (/): Divides number1 by number2.
# 4. The result of the operation is rounded to three decimal places and displayed.
# 5. If the user inputs an invalid operator, the code returns an error message stating that the operator is not valid.


operator = input("Please enter an operator (+, -, *, /): ")
number1 = float(input("Please enter the first number: "))
number2 = float(input("Please enter the second number: "))

if operator == "+":
    result = number1 + number2
    print(round(result, 3))
elif operator == "-":
    result = number1 - number2
    print(round(result, 3))
elif operator == "*":
    result = number1 * number2
    print(round(result, 3))
elif operator == "/":
    result = number1 / number2
    print(round(result, 3))
else:
    print(f"Given input {operator} is not a valid operator.")
