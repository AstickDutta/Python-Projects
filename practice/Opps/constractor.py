class employee():
    salary = 1234000
    language = "English"  #this is class attribute

    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language    #dunder mathod which is automatically called
        print("Hi I am A employee")

    # def getInfo(self):
    #     print(f"Employee's salary is {self.salary}, language is {self.language}")
    # @staticmethod
    # def greet():
    #     print("Hello, I am an employee!")

astick = employee("xyz", 123401, "Python") # this is instance atribute
print(astick.name, astick.salary, astick.language)

# astick.getInfo()
# astick.greet()