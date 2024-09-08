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
