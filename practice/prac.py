# import os

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

# n = int(input("enter a number: "))

# for i in range(1, 11):
#     print(f"{n} x {i} = {i * n}")

# n = int(input("enter a number: "))
# i = 1

# while i <= 10:
#     print(f"{n} x {i} = {i * n}")
#     i += 1

# l = ["Astick", "Rittick", "Sattick", "Sukannya", "Souvik", "Tattick"]

# for name in l:
#     if(name.startswith("S")):
#         print(f"hello {name}")

# # Check Prime number or not

# num = int(input("Enter a number: "))

# for i in range(2 , num):
#     if(num % i) == 0:
#         print(f"{num} is not a prime number")
#         break
# else:
#     print(f"{num} is a prime number")

# n = int(input("Enter a number: "))

# i = 1
# sum = 0

# while i <= n:
#     sum += i
#     i += 1
# print(sum)

# # 5! = 1 x 2 x 3 x 4 x 5

# n = int(input("Enter a number: "))
# product = 1

# for i in range(1, n+1):
#     product *= i
# print(f" The factorial of {n} is {product}")

# n = int(input("Enter a number: "))

# for i in range(1, n+1):
#     print(" " * (n - i), end = "")
#     print("*" * (2*i - 1), end = "")
#     print("")


# n = int(input("Enter a number: "))

# for i in range(1, n+1):
#     print("*" * i, end = "")
#     print("")

# n = int(input("enter a number: "))

# for i in range (1, n+1):
#     if(i == 1 or i == n ):
#         print("*" * n, end = "")
#     else:
#         print("*", end = "")
#         print(" " * (n -2), end = "")
#         print("*", end = "")
#     print("")

# n = int(input("enter a number: "))

# for i in range(1, 11):
#     print(f"{n} x {11 - i} = { n *( 11 - i)}")

# def grt(name, value):
#     print(f"Hii {name},Good day , how are you?, {value}")

#     return "fine"
# a = grt("Astick", "your roll number is 5")
# print(a)

# def greatest(a, b, c):
#     if a > b and a > c:
#         return a
#     elif b > a and b > c:
#         return b
#     else:
#         return c
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# c = int(input("Enter the third number: "))


# print("the greatest number the list is", greatest(a, b, c))

# def f_c (f):
#     return 5*(f-32)/9
# f = int(input("Enter a number: "))
# c  = f_c(f)

# print(f"{f}\u00B0 Fahrenheit is equal to {round(c, 2)}\u00B0 Celsius")

# def sum(n):
#     if n == 1 or n == 0:
#         return 1
#     else:
#         return n + sum(n-1)

# n = int(input("Enter a number: "))
# print(f"sum of natural number {n} is {sum(n)}")

# def pattern(n):
#     if(n == 0):
#         return
#     print("*" * n)
#     pattern(n -1)
# n = int(input("Enter a number: "))
# pattern(n)


# def inc_to_cm(n):
#     return n * 2.54

# n = int(input("Enter a value in inches: "))

# print(f"{n} inches is converted to {inc_to_cm(n)} centimeters")


# def rem(l, word):
#     n = []
#     for item in l:
#         if not(item == word):
#             n.append(item.strip(word))
#     return n

# l = ["apple", "banana", "cherry", "apple", "an"]

# print(rem(l , "an"))

# def mul(n):
#     for i in range(1, 11):
#         print(f"{n} x {i} = {n*i}")
#     return n

# n = int(input("Enter a number: "))

# mul(n)

# with open("poem.txt", "w") as f:
#     data = f.write("This is a poem\n twinkle twinkle little star")
#     print(data)


# with open("poem.txt", "r") as f:
#     data = f.read()
#     if("twinkle" in data):
#         print("The word 'twinkle' is present in the poem")
#     else:
#         print("The word 'twinkle' is not present in the poem")

# os.remove("poem.txt")

# import random

# def game():
#     print("Welcome to the number guessing game!")
#     score = random.randint(1, 100)

#     with open("hiScore.txt", "r") as f:
#         hiScore = f.read()
#         if(hiScore != ""):
#             hiScore = int(hiScore)
#         else:
#             hiScore = 0
#     print(f"your score is {score}")

#     if(hiScore < score):
#         with open("hiScore.txt", "w") as f:
#             f.write(str(score))

#     return score

# game()
    

# def generate(n):
#     table = ""
#     for i in range(1, 11):
#         row = f"{i} x {n} = {i*n}\n"
#         table += row
#     with open(f"tables/table_{n}.txt", "w") as f:
#         f.write(table)

# for i in range(2, 21):
#     generate(i)

# word = "Python"

# with open("file.txt", "r") as f:
#     content = f.read()

# contentNew = content.replace(word, "*****")

# with open("file.txt", "w") as f:
#     f.write(contentNew)


# words = ["Astick", "Python", "to", "basically", "practice"]

# with open("file.txt", "r") as f:
#     content = f.read()

#     for word in words:
#         content = content.replace(word, "#" *len(word))

# with open("file.txt", "w") as f:
#     f.write(content)


# with open("log.txt", "r") as f:
#     data = f.read()

#     if("Python" in data):
#         print("The word 'Python' is present in the file")
#     else:
#         print("The word 'Python' is not present in the file")


# with open("log.txt") as f:
#     lines = f.readlines()

# lineNo = 1
# for line in lines:
#     if "python" in line:
#         print(f"The word 'Python' is present in the file and is available in line no: {lineNo}")
#         break
#     lineNo += 1
# else:
#     print("The word 'Python' is not present in the file")


# class employee():
#     salary = 1234000
#     language = "English"  #class attribute

# astick = employee()
# astick.name = "harry" #instance atribute
# print(astick.salary, astick.language, astick.name)

# class programmer:
#     company = "Microsoft"

#     def __init__(self, name, salary, pincode):
#         self.name = name
#         self.salary = salary
#         self.pincode = pincode

# p = programmer("Astick", 1234000, 894749)

# print(p.name, p.company, p.salary, p.pincode)

# class claculator:
#     def __init__(self, n):
#         self.n = n
        
#     def square(self):
#         print(f"the square of given number is {self.n * self.n}")

#     def cube(self):
#         print(f"the cube of given number is {self.n * self.n * self.n}")

#     def root(self):
#         print(f"the root of given number is {self.n ** 1/2}")

#     @staticmethod
#     def greet():
#         print("Hii there")

# a = claculator(4)

# a.greet()
# a.square()
# a.cube()
# a.root()

# from random import randint

# class train:
#     def __init__(self, trainNo):
#         self.trainNo = trainNo
    
#     def book(self, fro, to):
#         print(f"ticket is booked in train number: {self.trainNo} from {fro} to {to}")

#     def getStatus(self):
#         print(f"train number {self.trainNo} in running on time")

#     def getFare(self, fro, to):
#         print(f"Ticket fare in train number: {self.trainNo} from {fro} to {to} is {randint(222, 555)}")


# t = train(1234)
# t.book("Durgapur", "Kolkata")
# t.getStatus()
# t.getFare("Durgapur", "Kolkata")

# class twoVector:
#     def __init__(self, i, j):
#         self.i = i
#         self.j = j

#     def show(self):
#         print(f"two vector values are {self.i}i and {self.j}j")

    
# class threeVector(twoVector):
#     def __init__(self, i, j , k):
#         super().__init__(i, j)
#         self.k = k
        

#     def show(self):
#         print(f"three vector values are {self.i}i and {self.j}j and {self.k}k")


# a = twoVector(1, 2)
# a.show()

# b = threeVector(5, 2, 3)
# b.show()


# class Animal:
#     pass

# class Pet(Animal):
#     pass

# class dog(Pet):
#     @staticmethod
#     def bark():
#         print("Bow, Bow")

# e = dog()
# e.bark()


# class employee:
#     salary = 5000
#     increment = 20

#     @property
#     def salaryAfterIncrement(self):
#         return (self.salary + self.salary * (self.increment/100))
    

#     @salaryAfterIncrement.setter
#     def salaryAfterIncrement(self, salary):
#         self.increment = ((salary / self.salary) - 1 ) * 100

# e = employee()
# e.salaryAfterIncrement = 10000
# print(e.increment)

# def sum(a: int, b:int) -> int:
#     return (a+b)

# result = sum(1, 5)

# print(result)


# dict1 = {"a" : 2, "b" : 3}
# dict3= {"e" : 4, "k": 9}

# marged = dict1 | dict3

# print(marged)

# try:
#     a = int(input("Please put a number : "))
#     print(a)
# except Exception as e:
#     print(e)


# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello, World!")

# say_hello()

# age = 79
# discount = 5 if age < 65 else 10

# print(discount)


# for i in range(10):
#     if i == 7:
#         break
#     print(i , end=",")
    
# for i in range(10):
#     if i == 7:
#         continue
#     print(i , end = ",")

# def myFync():
#     print("hii there , I frm before the pass statment")
#     pass
# myFync()

# class person:
#     def  __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f"Hii my name is {self.name}, and I am {self.age} years old")

# c = person("Astick", 27)
# c.info()


# # count

# a = [7,3, 3, 4,25, 5]

# print(a.count(3))

# # index
# my_list =  [7, 3, 3, 4, 25, 5]

# print(my_list.index(5))

# # pop
# my_list =  [7, 3, 3, 4, 25, 5]
# print(my_list.pop(2))
# print(my_list)

# def is_prime(n):
#     if n <= 1:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False
    
#     for i  in range (3, int(n ** 0.5) + 1, 2):
#         if n % i == 0:
#             return False
#         return True
    
# try:
#     number = int(input("Enter a number :"))
#     if is_prime(number):
#         print(f"given number {number} is a prime number")
#     else:
#         print(f"given number {number} is not a prime number")

# except ValueError:
#     print("Invalid input, please enter a number")


# list_1 =[1,2,'fhuy',3,4]
# list_2 =[1,2,3,7]

# common = []

# for num in list_1:
#     if num in list_2:
#         common.append(num)

# print(common)

# num = int(input("Please enter a number : "))

# if num < 2:
#     print("Number is not prime")

# elif num == 2:
#     print("Number is prime")

# else:
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             print(f"Given Number {num} is not a prime number")
#         else:
#             print(f"Given Number {num} is prime")


# num = int(input("Enter a number : "))

# sum = 0
# temporary = num

# while temporary > 0:
#     digit = temporary % 10
#     cube = digit ** 3
#     sum += cube
#     temporary //= 10

# if sum == num:
#     print("Given number is armstrong number")
# else:
#     print("given number is not an armstrong number")

# num = int(input("Enter a number: "))
# x = num
# reverse = 0

# while num > 0:
#     reverse = (reverse*10) + num % 10
#     num //= 10

# if(x == reverse):
#     print("Given Number is Palindrome")
# else:
#     print("Given number is not a Palindrome")

# num = int(input("Enter a number: "))

# fact = 1
# i = 1

# while i <= num:
#     fact *= i
#     i+=1

# print("Given value's factorial value is", fact)

# num = int(input("Enter a number: "))

# fact = 1
# i = 1

# while i <= num:
#     fact *= i
#     i+=1

# print("Given value's factorial value is", fact)

# ls = [1,1,2,2,2,2,2,5,9,4]

# el = []

# for i in ls:
#     if i not in el:
#         el.append(i)
# print(el)

# student = { "history": 50, "geography": 9, "english": 12 }
# di = {}
# for item in student:
#     if student[item] >= 10:
#         di[item] = student[item]

# print(di)

# dubNumbers = [3,4,5,2,6,2,7,4,5]
# uniqueNumbers = []

# for i in dubNumbers:
#     if i not in uniqueNumbers:
#         uniqueNumbers.append(i)

# print("unique numbers list", uniqueNumbers)


# number = int(input("Enter a number: "))

# fact = 1
# i = 1

# while i <= number:
#     fact*=i
#     i+=1

# print(fact)

# number = int(input("Enter a number: "))

# if number < 2:
#     print("it In not a prime number")

# elif number == 2:
#     print("it is prime number")

# else:
#     for  i in range(2, int(number ** 0.5) + 1):
#         if number % i == 0:
#             print(f"Given number is {number} id not prime number")
#         else:
#             print(f"Given number is prime number")


"""
🔴 Create a program to find and print the first 5 pairs of consecutive prime numbers using a while loop
"""

# def is_prime(number):

#     if number < 2:
#         return False

#     for num in range(2, int(number ** 0.5) + 1):
#         if number % num == 0:
#            return False
#         else:
#             return True
# def find_consecutive_prime_pairs():
#     count = 0
#     current = 2

#     while count < 5:
#         if is_prime(current) and is_prime(current + 2):
#             print(f"Pair {count + 1}: ({current}, {current + 2})")
#             count += 1
#         current += 1

# find_consecutive_prime_pairs()

def star_prob():
    i = 1
    while i <= 5:
        j = 1
        while j <= i:
            print("*", end = "")
            j += 1
        print()
        i += 1

star_prob()
