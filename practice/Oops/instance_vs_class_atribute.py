class employee():
    salary = 1234000
    language = "English"  #this is class attribute

    def getInfo(self):
        print(f"Employee's salary is {self.salary}, language is {self.language}")
    @staticmethod
    def greet():
        print("Hello, I am an employee!")

astick = employee() # this is instance atribute

astick.getInfo()
astick.greet()