# Python String Methods Cheat Sheet

s = "  Hello, World!  "

print("Original String:", s)

# Basic string operations
print("Length:", len(s))
print("Lowercase:", s.lower())
print("Uppercase:", s.upper())
print("Title Case:", s.title())
print("Capitalized:", s.capitalize())

# Trimming whitespace
print("Stripped:", s.strip())
print("Left Stripped:", s.lstrip())
print("Right Stripped:", s.rstrip())

# Replace and split
print("Replaced:", s.replace("World", "Python"))
print("Split:", s.split(","))

# Joining strings
words = ["Python", "is", "awesome"]
print("Joined:", " ".join(words))

# Finding substrings
print("Find 'o':", s.find("o"))
print("RFind 'o':", s.rfind("o"))
print("Index of 'o':", s.index("o"))
print("Count of 'l':", s.count("l"))

# Checking string properties
print("Starts with '  Hello':", s.startswith("  Hello"))
print("Ends with '!  ':", s.endswith("!  "))
print("Is Alpha:", "Hello".isalpha())
print("Is Digit:", "12345".isdigit())
print("Is Alphanumeric:", "Hello123".isalnum())
print("Is Space:", "   ".isspace())

# Swapping case
print("Swap Case:", s.swapcase())

# Zero Fill
print("ZFill:", "42".zfill(5))

# F-String Formatting
name = "John"
age = 25
print(f"My name is {name} and I am {age} years old.")

