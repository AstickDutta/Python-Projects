class OverloadExample:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):  # + operator
        return OverloadExample(self.value + other.value)

    def __sub__(self, other):  # - operator
        return OverloadExample(self.value - other.value)

    def __mul__(self, other):  # * operator
        return OverloadExample(self.value * other.value)

    def __truediv__(self, other):  # / operator
        return OverloadExample(self.value / other.value)

    def __floordiv__(self, other):  # // operator
        return OverloadExample(self.value // other.value)

    def __mod__(self, other):  # % operator
        return OverloadExample(self.value % other.value)

    def __pow__(self, other):  # ** operator
        return OverloadExample(self.value ** other.value)

    def __eq__(self, other):  # == operator
        return self.value == other.value

    def __ne__(self, other):  # != operator
        return self.value != other.value

    def __gt__(self, other):  # > operator
        return self.value > other.value

    def __lt__(self, other):  # < operator
        return self.value < other.value

    def __ge__(self, other):  # >= operator
        return self.value >= other.value

    def __le__(self, other):  # <= operator
        return self.value <= other.value

    def __str__(self):  # String representation
        return str(self.value)

# Example usage
a = OverloadExample(10)
b = OverloadExample(5)

print("Addition:", a + b)  # Calls __add__()
print("Subtraction:", a - b)  # Calls __sub__()
print("Multiplication:", a * b)  # Calls __mul__()
print("Division:", a / b)  # Calls __truediv__()
print("Floor Division:", a // b)  # Calls __floordiv__()
print("Modulus:", a % b)  # Calls __mod__()
print("Power:", a ** b)  # Calls __pow__()
print("Equal:", a == b)  # Calls __eq__()
print("Not Equal:", a != b)  # Calls __ne__()
print("Greater Than:", a > b)  # Calls __gt__()
print("Less Than:", a < b)  # Calls __lt__()
print("Greater or Equal:", a >= b)  # Calls __ge__()
print("Less or Equal:", a <= b)  # Calls __le__()
