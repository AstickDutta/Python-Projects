# Most Important File Handling Functions in Python

# 1. Open a file
txt_file = open("example.txt", "w")  # Modes: r, w, a, r+

# 2. Write to a file
txt_file.write("Hello, World!\n")

# 3. Read from a file
txt_file.close()
txt_file = open("example.txt", "r")
content = txt_file.read()
print(content)

# 4. Read lines from a file
txt_file.seek(0)  # Reset pointer
txt_file.readlines()

# 5. Append to a file
with open("example.txt", "a") as txt_file:
    txt_file.write("Appending new content.\n")

# 6. Check if file exists
import os
if os.path.exists("example.txt"):
    print("File exists")

# 7. Delete a file
os.remove("example.txt")
