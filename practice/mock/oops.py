# class Person:
#     person_count = 0

#     def __init__(self, name, age, password):
#         self.name = name
#         self._age = age
#         self.__password = password
#         Person.person_count += 1

#     def get_details(self):
#         return f"Name: {self.name}, Age: {self._age}"

#     def _get_protected_details(self):
#         return f"Age: {self._age} (Accessed from protected method)"

#     def __get_private_password(self):
#         return self.__password

#     @classmethod
#     def get_person_count(cls):
#         return cls.person_count

#     @staticmethod
#     def is_adult(age):
#         return age >= 18

#     @property
#     def password(self):
#         return self.__password


# class Employee(Person):
#     def __init__(self, name, age, password, employee_id, salary):
#         super().__init__(name, age, password)
#         self.employee_id = employee_id  # Public
#         self._salary = salary  # Protected

#     def get_details(self):
#         #! Overridden method with more details
#         base_details = super().get_details()
#         return f"{base_details}, Employee ID: {self.employee_id}, Salary: ${self._salary}"

#     def get_salary(self):
#         return self._salary

#     def _raise_salary(self, amount):
#         self._salary += amount
#         return self._salary


# # * Creating Person instance
# p1 = Person("Alice", 30, "alice_pass123")
# print(p1.get_details())
# print("Password (via property):", p1.password)
# print("Is Adult:", Person.is_adult(p1._age))
# print("Total Persons:", Person.get_person_count())

# p2 = Person("astick", 30, "astick_pass123")
# print(p1.get_details())
# print("Password (via property):", p2.password)
# print("Is Adult:", Person.is_adult(p1._age))
# print("Total Persons:", Person.get_person_count())

# # * Creating Employee instance
# e1 = Employee("Bob", 28, "bob_pass456", "EMP123", 50000)
# print(e1.get_details())
# print("Salary:", e1.get_salary())
# e1._raise_salary(5000)
# print("New Salary after raise:", e1.get_salary())
# print("Total Persons (including employees):", Person.get_person_count())


class Vehicle:
    count = 0
    def __init__(self,brand,engine_type,c_number):
        self.brand=brand
        self._engine_type=engine_type
        self.__c_number=c_number
        Vehicle.count+=1

    def get_details(self):
        return f'This is car deatils {self.__c_number}'
    
    def _get_protected_engine_details(self,msg):
        return f'{self._engine_type} , {msg}'


    def __get_pri_ch_methods(self):
        return self.__c_number

    @classmethod
    def get_Vehicle_count(cls):
        return Vehicle.count

    @staticmethod
    def is_electric(type_):
        if type_ == 'electric':
            return 'yes, its electric car'
        return 'no, its not'
    
    @property
    def pro_meth(self):
        return self.__c_number


class Car(Vehicle):
    def __init__(self ,model, milage, brand, engine_type, c_number):
        super().__init__(brand, engine_type, c_number)
        self.milage = milage
        self.model = model

    def get_details(self):
        old_record = super().get_details()
        return f"this is old record {old_record} and {self.milage}, and {self.model}"

    def get_milage(self):
        return f"milage of of that car {self.milage}"

    def __increase_car_milage(self, increase_milage):
        total_milage = self.milage + increase_milage
        return f"this is total milage {total_milage}"


obj = Vehicle('TATA','petrol','12165')
print(obj.get_details())
print(obj._Vehicle__get_pri_ch_methods())
print(obj._get_protected_engine_details("this is al details about car"))

obj2= Car('punch',15,'TATA','electric',9999)
print(obj2.get_details())