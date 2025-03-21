# # repalce prac

# letter = '''hii |name| you are 
# seleted for developer position on |date|'''

# print(letter.replace("|name|", "Astick").replace("|date|", "23 september"))

# # detect double space

# progr = "Hii I am astick I am here to learn python"

# print(progr.find("  "))

# marks = []

# f1 = input("Enter marks name:")
# marks.append(f1)
# f2 = input("Enter marks name:")
# marks.append(f2)
# f3 = input("Enter marks name:")
# marks.append(f3)
# f4 = input("Enter marks name:")
# marks.append(f4)
# f5 = input("Enter marks name:")
# marks.append(f5)
# f6 = input("Enter marks name:")
# marks.append(f6)
# f7 = input("Enter marks name:")
# marks.append(f7)

# print("Your marks are:", marks)

# marks = []

# f1 = int(input("Enter marks name:"))
# marks.append(f1)
# f2 = int(input("Enter marks name:"))
# marks.append(f2)
# f3 = int(input("Enter marks name:"))
# marks.append(f3)
# f4 = int(input("Enter marks name:"))
# marks.append(f4)
# f5 = int(input("Enter marks name:"))
# marks.append(f5)
# f6 = int(input("Enter marks name:"))
# marks.append(f6)
# f7 = int(input("Enter marks name:"))
# marks.append(f7)

# marks.sort()
# print("Your marks are:", marks)

# marks = int(input("Enter your marks: "))

# if marks >= 90:
#     print("Your grade is A")
# elif marks >= 80:
#     print("Your grade is B")
# elif marks >= 75:
#     print("Your grade is C")
# else:
#     print("You failed")

# num1 = int(input("given number n1: "))
# num2 = int(input("given number n2: "))
# num3 = int(input("given number n3: "))
# num4 = int(input("given number n4: "))

# if(num1 > num2 and num1 > num3 and num1 > num4):
#     print("The largest number is", num1)
# elif(num2 > num1 and num2 > num3 and num2 > num4):
#     print("The largest number is", num2)
# elif(num3 > num1 and num3 > num2 and num3 > num4):
#     print("The largest number is", num1)
# elif(num4 > num2 and num4 > num3 and num4 > num1):
#     print("The largest number is", num4)

# marks1 = int(input("your marks m1: "))
# marks2 = int(input("your marks m2: "))
# marks3 = int(input("your marks m3: "))

# total_percentage = (100*(marks1 + marks2 + marks3))/300

# if(total_percentage > 40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33):
#     print("you are passed", total_percentage)
# else:
#     print("you are failed", total_percentage)

# p1 = "buy now"
# p2 = "make a lot of money"
# p3 = "subscribe this"
# p4 = "click in this"

# message = input("enter a comment here:")

# if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
#     print("Warning: Suspicious comment detected!")
# else:
#     print("Comment accepted")

# name = input("Enter a name: ")

# if(len(name) < 10 ):
#     print("Name is too short, this name is not contained 10 chars")
# else :
#     print("Name is valid")

# l = ["Astick", "Riju", "Batash", "Riju"]

# name = input("Enter a name: ")

# if(name in l):
#     print("Name already exists")
# else:
#     print("Name is not exists")


# for i in range(1, 4):
#     print(i)

# i = 1

# while i < 6:
#     print(i)
#     i+= 1

# l = [2,4,7,9]

# for i in l:
#     print(i)
# else:
#     print("loop completed")

# for i in range(100):
#     if i % 2 == 0:
#         continue
#     print(i)

# for i in range(100):
#     if i == 56:
#         continue
#     print(i)