class Person:
    person_count = 0

    def __init__(self, name, age, password):
        self.name = name
        self._age = age
        self.__password = password
        Person.person_count += 1

    def get_details(self):
        return f"Name: {self.name}, Age: {self._age}"

    def _get_protected_details(self):
        return f"Age: {self._age} (Accessed from protected method)"

    def __get_private_password(self):
        return self.__password

    @classmethod
    def get_person_count(cls):
        return cls.person_count

    @staticmethod
    def is_adult(age):
        return age >= 18

    @property
    def password(self):
        return self.__password


class Employee(Person):
    def __init__(self, name, age, password, employee_id, salary):
        super().__init__(name, age, password)
        self.employee_id = employee_id  # Public
        self._salary = salary  # Protected

    def get_details(self):
        #! Overridden method with more details
        base_details = super().get_details()
        return f"{base_details}, Employee ID: {self.employee_id}, Salary: ${self._salary}"

    def get_salary(self):
        return self._salary

    def _raise_salary(self, amount):
        self._salary += amount
        return self._salary


# Demonstration

# * Creating Person instance

p1 = Person("Alice", 30, "alice_pass123")
print(p1.get_details())
print("Password (via property):", p1.password)
print("Is Adult:", Person.is_adult(p1._age))
print("Total Persons:", Person.get_person_count())

p2 = Person("astick", 30, "astick_pass123")
print(p1.get_details())
print("Password (via property):", p2.password)
print("Is Adult:", Person.is_adult(p1._age))
print("Total Persons:", Person.get_person_count())

# * Creating Employee instance
e1 = Employee("Bob", 28, "bob_pass456", "EMP123", 50000)
print(e1.get_details())
print("Salary:", e1.get_salary())
e1._raise_salary(5000)
print("New Salary after raise:", e1.get_salary())
print("Total Persons (including employees):", Person.get_person_count())