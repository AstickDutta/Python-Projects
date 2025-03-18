# Python Escape Sequences Cheat Sheet with Examples

print("1. New Line (\\n):")
print("Hello\nWorld")  
print("Python\nis\nawesome!")  
print("Line1\nLine2\nLine3")  

print("\n2. Tab (\\t):")
print("Hello\tWorld")  
print("Python\tProgramming")  
print("Item1\tItem2\tItem3")  

print("\n3. Backslash (\\\\):")
print("This is a backslash: \\")  
print("C:\\Users\\Python")  
print("Path: D:\\Projects\\Code")  

print("\n4. Single Quote (\\'):")
print('It\'s a nice day!')  
print('She said, \'Hello!\'')  
print('This isn\'t difficult.')  

print("\n5. Double Quote (\\\"):")
print("He said, \"Python is awesome!\"")  
print("She replied, \"Yes, it is!\"")  
print("Quote: \"Stay positive!\"")  

print("\n6. Carriage Return (\\r):")
print("Hello\rWorld")  # Overwrites "Hello" with "World"
print("12345\rABCDE")  
print("Python\rCode")  

print("\n7. Backspace (\\b):")
print("Helloo\b World")  # Removes the extra 'o'
print("Python\bRocks!")  
print("Test\b\b\bABC")  

print("\n8. Form Feed (\\f):")
print("Hello\fWorld")  
print("Python\fCoding")  
print("Page1\fPage2")  

print("\n9. Octal Value (\\ooo):")
print("\110\145\154\154\157")  # Prints 'Hello'
print("\101\102\103")  # Prints 'ABC'
print("\117\143\164\141\154")  # Prints 'Octal'  

print("\n10. Hex Value (\\xhh):")
print("\x48\x65\x6C\x6C\x6F")  # Prints 'Hello'
print("\x50\x79\x74\x68\x6F\x6E")  # Prints 'Python'
print("\x41\x42\x43")  # Prints 'ABC'  

# print("\n11. Unicode (\\u and \\U):")
# print("\u2764")  # Prints ❤️ (heart symbol)
# print("\U0001F600")  # Prints 😀 (smiley emoji)
# print("\U0001F609")  # Prints 😉 (winking face)  

print("\n12. Raw String (r''):")
print(r"C:\Users\Python\Scripts")  # Raw string ignores escape sequences
print(r"New line character: \n is not processed")
print(r"Use \t for tabs in a normal string, but not in a raw string")
