class employee:
    def __init__(self):
        print("employee constructor")
    a = 1

class programmer(employee):
    def __init__(self):
        print("programmer constructor")
    b = 2

class manager(programmer):
    def __init__(self):
        super().__init__()
        print("manager constructor")
    c = 3


o = manager()

print(o.a, o.b, o.c)


class employee:
    company = "ITC"
    def lang(self):
        print(f"this employe's company name is {self.company}")

class programmer(employee):
    company = "ITC Infotech"
    def __init__(self, language):
        self.language = language

    def showLanguage(self):
        print(f"Employee's language is {self.language}")

a = programmer("Python")

print(a.company, a.language)

a.showLanguage()


class Parent1:
    def feature1(self):
        print("Feature 1 is from Parent1")

class Parent2:
    def feature2(self):
        print("Feature 2 is from Parent2")

class Child(Parent1, Parent2):  # Inheriting from both Parent1 and Parent2
    def feature3(self):
        print("Feature 3 is from Child")

# Creating an object of Child class
obj = Child()
obj.feature1()  # Accessing method from Parent1
obj.feature2()  # Accessing method from Parent2
obj.feature3()  # Accessing method from Child

class employee:
    a = 10

    @classmethod
    def show(cls):
        print(f"class attribute value is {cls.a}")
        

e = employee()
e.a = 45

e.show()