operator = input("please enter( + - * /) : ")
number1 = float(input("please entyer first number1 : "))
number2 = float(input("please entyer second number2 : "))

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
    print(f"Given input {operator} is not a proper operator")
