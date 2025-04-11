class person:
    x = 12

p1 = person()
print(p1.x)

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

p1 = Person("Astick", 23, "west bengal")
p2 = Person("Rittick", 21, "Kolkata")
print(p1.name)
print(p1.age)
print(p1.address)
print(p2.name)
print(p2.age)
print(p2.address)


class Person:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"Good morning! Hii my name is {self.name}, I am {self.age} years old, My salary is {self.salary}"
    
p1 = Person("Astick", 24, 45000)
print(p1)

class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname  = lastname
    
    def printname(self):
        print(f"my firstname is {self.firstname}, and my last name is {self.lastname}")

class Student(Person):
    def __init__(self, firstname, lastname):
        Person.__init__(self, firstname, lastname)
    
# p1 = Person("Astick", "Dutta")
# p1.printname()

p2 = Student("Rittick", "Dutta")
p2.printname()


class Person:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def printName(self):
        print(f"Hi my first is {self.firstName} and my last is {self.lastName}")

class Student(Person):
    def __init__(self, firstName, lastName, year):
        super().__init__(firstName, lastName)
        self.graduationYear = year

    def welcomeStudent(self):
        print(f"Welcome {self.firstName} {self.lastName} to the class of {self.graduationYear}")

p1 = Student("Astick", "Dutta", 1997)
p1.welcomeStudent()


'''
🔴 Create a class Car with attributes brand, model, and year. 
🔴 Create an object and print the attributes.
'''
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

printCar = Car("BMW", "5 series",2023)
print(printCar.brand, printCar.model, printCar.year)


'''
🔴 Create a class Rectangle with attributes length and breadth.
🔴 Add a method to calculate area.
'''

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def calculate(self):
        print(f"{self.length * self.breadth }")

printObj = Rectangle(3,4)
printObj.calculate()


'''
🔴 Class Person: Create a class with name and age. 
🔴 Create two instances and print them.
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Astick", 27)
p2 = Person("Rittick", 25)
print(p1.name, p1.age)
print(p2.name, p2.age)

'''
🔴Add __str__() to your Car class to return "Brand: <brand>, Model: <model>".
'''

class Car:
    def __init__(self,model, brand):
        self.brand = brand
        self.model = model

    def printCar(self):
        print(f"This  is the latest car of 2025, it's brand is {self.brand} and model is {self.model}")

c = Car("Audi", "R8")
c.printCar()

'''
🔴 Create a parent class Employee with name and salary. 
🔴 Inherit a class Developer that adds a programming_language field.
'''

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
class Developer(Employee):
    def __init__(self, name, salary, programming_field):
        super().__init__(name, salary)
        self.programming_field = programming_field

p1 = Developer("Rittick", 349000, "ABAP Developer")
print(p1.programming_field)

'''
🔴 Create class Animal and class Dog inheriting from Animal. 
🔴 Add method make_sound() to each class. 
🔴 Use super() in Dog class to call the parent constructor.
'''

class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Some generic sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def make_sound(self):
        return "Woof!"

dog1 = Dog("Buddy", "Labrador")
print(dog1.name, dog1.breed)
print(dog1.make_sound())

'''
🔴 Create a class BankAccount:
🔴 Attributes: account_holder, balance
🔴 Methods: deposit, withdraw, __str__
'''

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

'''
🔴 Iterator example:
'''

class Student:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1

        return x
    
myClass = Student()
myRollNumber = iter(myClass)

print(next(myRollNumber))
print(next(myRollNumber))
print(next(myRollNumber))
print(next(myRollNumber))