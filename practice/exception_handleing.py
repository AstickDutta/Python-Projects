# Example 1: Basic try-except
try:
    num = int(input("Enter a number: "))
    print(f"You entered: {num}")
except ValueError:
    print("Invalid input! Please enter a valid integer.")

# Example 2: Handling Multiple Exceptions
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    result = a / b
    print(f"Result: {result}")
except ValueError:
    print("Invalid input! Please enter numeric values.")
except ZeroDivisionError:
    print("Error! Division by zero is not allowed.")

# Example 3: Using finally
try:
    file = open("file.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found!")
finally:
    print("Execution completed, closing file if opened.")
    if 'file' in locals() and not file.closed:
        file.close()

try:
    a = int(input("Enter your first number: "))
    b = int(input("Enter your second number: "))

    if b == 0:
        raise ZeroDivisionError("You can't divide a number by 0")
    
    print(f"Division of given numbers is {a / b}")

except ValueError:
    print("Invalid input! Please enter a valid integer.")
except ZeroDivisionError as e:
    print(e)
