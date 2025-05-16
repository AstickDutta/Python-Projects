# class person:
#     x = 12

# p1 = person()
# print(p1.x)

# class Person:
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address

# p1 = Person("Astick", 23, "west bengal")
# p2 = Person("Rittick", 21, "Kolkata")
# print(p1.name)
# print(p1.age)
# print(p1.address)
# print(p2.name)
# print(p2.age)
# print(p2.address)


# class Person:
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary

#     def __str__(self):
#         return f"Good morning! Hii my name is {self.name}, I am {self.age} years old, My salary is {self.salary}"
    
# p1 = Person("Astick", 24, 45000)
# print(p1)

# class Person:
#     def __init__(self, firstname, lastname):
#         self.firstname = firstname
#         self.lastname  = lastname
    
#     def printname(self):
#         print(f"my firstname is {self.firstname}, and my last name is {self.lastname}")

# class Student(Person):
#     def __init__(self, firstname, lastname):
#         Person.__init__(self, firstname, lastname)
    
# # p1 = Person("Astick", "Dutta")
# # p1.printname()

# p2 = Student("Rittick", "Dutta")
# p2.printname()


# class Person:
#     def __init__(self, firstName, lastName):
#         self.firstName = firstName
#         self.lastName = lastName

#     def printName(self):
#         print(f"Hi my first is {self.firstName} and my last is {self.lastName}")

# class Student(Person):
#     def __init__(self, firstName, lastName, year):
#         super().__init__(firstName, lastName)
#         self.graduationYear = year

#     def welcomeStudent(self):
#         print(f"Welcome {self.firstName} {self.lastName} to the class of {self.graduationYear}")

# p1 = Student("Astick", "Dutta", 1997)
# p1.welcomeStudent()


# '''
# 🔴 Create a class Car with attributes brand, model, and year. 
# 🔴 Create an object and print the attributes.
# '''
# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year

# printCar = Car("BMW", "5 series",2023)
# print(printCar.brand, printCar.model, printCar.year)


# '''
# 🔴 Create a class Rectangle with attributes length and breadth.
# 🔴 Add a method to calculate area.
# '''

# class Rectangle:
#     def __init__(self, length, breadth):
#         self.length = length
#         self.breadth = breadth

#     def calculate(self):
#         print(f"{self.length * self.breadth }")

# printObj = Rectangle(3,4)
# printObj.calculate()


# '''
# 🔴 Class Person: Create a class with name and age. 
# 🔴 Create two instances and print them.
# '''

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# p1 = Person("Astick", 27)
# p2 = Person("Rittick", 25)
# print(p1.name, p1.age)
# print(p2.name, p2.age)

# '''
# 🔴Add __str__() to your Car class to return "Brand: <brand>, Model: <model>".
# '''

# class Car:
#     def __init__(self,model, brand):
#         self.brand = brand
#         self.model = model

#     def printCar(self):
#         print(f"This  is the latest car of 2025, it's brand is {self.brand} and model is {self.model}")

# c = Car("Audi", "R8")
# c.printCar()

# '''
# 🔴 Create a parent class Employee with name and salary. 
# 🔴 Inherit a class Developer that adds a programming_language field.
# '''

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
    
# class Developer(Employee):
#     def __init__(self, name, salary, programming_field):
#         super().__init__(name, salary)
#         self.programming_field = programming_field

# p1 = Developer("Rittick", 349000, "ABAP Developer")
# print(p1.programming_field)

# '''
# 🔴 Create class Animal and class Dog inheriting from Animal. 
# 🔴 Add method make_sound() to each class. 
# 🔴 Use super() in Dog class to call the parent constructor.
# '''

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def make_sound(self):
#         return "Some generic sound"

# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)
#         self.breed = breed

#     def make_sound(self):
#         return "Woof!"

# dog1 = Dog("Buddy", "Labrador")
# print(dog1.name, dog1.breed)
# print(dog1.make_sound())

# '''
# 🔴 Create a class BankAccount:
# 🔴 Attributes: account_holder, balance
# 🔴 Methods: deposit, withdraw, __str__
# '''

# class BankAccount:
#     def __init__(self, bankHolderName, balance = 0):
#         self.bankHolderName = bankHolderName
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         return self.balance
    
#     def WithDraw(self, amount):
#         if self.balance < amount:
#             return "Insufficient Balance"
#         self.balance -= amount
#         return self.balance
    
#     def __str__(self):
#         return f"This Account details of name {self.bankHolderName}, and Balance is {self.balance}"
    

# account = BankAccount("Astick", 600000)
# account.deposit(90000)
# account.WithDraw(89000)
# print(account)

# '''
# 🔴 Iterator example:
# '''

# class Student:
#     def __iter__(self):
#         self.a = 1
#         return self
    
#     def __next__(self):
#         x = self.a
#         self.a += 1

#         return x
    
# myClass = Student()
# myRollNumber = iter(myClass)

# print(next(myRollNumber))
# print(next(myRollNumber))
# print(next(myRollNumber))
# print(next(myRollNumber))

# """
# 🔴 Inventory System:

# Base class Product with attributes name and price

# Subclass Electronics, Clothing with their own attributes (warranty, size)

# Print inventory using __str__

# """

# class Product:
#     def __init__(self , name, price):
#         self.name = name
#         self.price = price

#     def __str__(self):
#         return f"{self.price} - {self.name}"
    
# class Electronics(Product):
#     def __init__(self, name, price, warranty):
#         super().__init__(name, price)
#         self.warranty = warranty

#     def __str__(self):
#         return super().__str__() + f", Warranty: {self.warranty} years"
    
# class Cloth(Product):
#     def __init__(self, name, price, size):
#         super().__init__(name, price)
#         self.size = size
    
#     def __str__(self):
#         return super().__str__() + f"Size: {self.size}"

# items = [
#     Electronics("SmartPhone", 34578, 2),
#     Cloth("Jeans", 1000, "M")
# ]

# for item in items:
#     print(item)

# """
# 🔴 Student Report System:

# Class Student with name, roll number

# Method to add subjects and marks

# Method to calculate average and grade
# """

# class Student:
#     def __init__(self, name, roll_no):
#         self.name = name
#         self.roll_no = roll_no
#         self.marks = {}

#     def add_subject(self, subject, mark):
#         self.marks[subject] = mark

#     def calculate_average(self):
#         return sum(self.marks.values()) / len(self.marks)

#     def get_grade(self):
#         avg = self.calculate_average()
#         if avg >= 90:
#             return "A"
#         elif avg >= 75:
#             return "B"
#         elif avg >= 60:
#             return "C"
#         else:
#             return "D"

#     def __str__(self):
#         return f"Name: {self.name}, Roll No: {self.roll_no}, Grade: {self.get_grade()}"

# student = Student("Arjun", 101)
# student.add_subject("Math", 95)
# student.add_subject("Science", 88)
# student.add_subject("English", 92)

# print(student)

"""
Entities:

· Item: Represents a product with a name and price.

· Cart: Holds the list of items and manages the checkout process.

· Discount: Represents various types of discounts.

Steps:

1. Item Class:

a. Attributes: name, price.

b. Methods: get_price(), which returns the price of the item.

2. Cart Class:

a. Attributes: items (a list of Item objects), discount.

b. Methods:

i. add_item(item): Adds an item to the cart.

ii. set_discount(discount): Sets a discount strategy for the cart.

iii. calculate_total(): Calculates the total price, applying the discount if available.

3. Discount Class:

a. Methods: apply_discount(total): Abstract method to be implemented by subclasses.

b. Subclasses:

i. PercentageDiscount: Reduces the total by a percentage.

ii. FixedDiscount: Reduces the total by a fixed amount.

4. Polymorphism:

a. The apply_discount() method in Cart is called based on the type of discount selected.

Example Problem:

· Create a cart, add items, apply a discount, and calculate the total amount"""

"1."

# class Item:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def get_price(self):
#         return self.price
    

# from abc import ABC, abstractmethod

# class Discount(ABC):
#     @abstractmethod
#     def apply_discount(self, total):
#         pass
    
# class Permanent_discount(Discount):
#     def __init__(self, percent):
#         self.percent = percent

#     def apply_discount(self, total):
#         return total - (total * self.percent / 100)

# class FixedDiscount(Discount):
#     def __init__(self, amount):
#         self.amount = amount

#     def apply_discount(self, total):
#         return max(0, total - self.amount)
    
class Cart:
    def __init__(self):
        self.items = []
        self.discount = None

    def add_items(self, item):
        self.items.append(item)

    def set_discount(self ,discount):
        self.discount = discount

    def calculate_total(self):
        total = sum(item.get_price() for item in self.items)
        if self.discount:
            total = self.discount.apply_discount(total)
        return total
    


# item1 = Item("Laptop", 1000)
# item2 = Item("Mouse", 50)
# item3 = Item("Keyboard", 100)

# cart = Cart()
# cart.add_items(item1)
# cart.add_items(item2)
# cart.add_items(item3)


# percent_discount = Permanent_discount(10)
# cart.set_discount(percent_discount)


# total_amount = cart.calculate_total()
# print(f"Total amount after discount: ${total_amount:.2f}")

# fixed_discount = FixedDiscount(200)
# cart.set_discount(fixed_discount)
# print(f"Total with fixed discount: ${cart.calculate_total():.2f}")
