'''
🔴 Polymorphism:
🔴 For example, say we have three classes: Car, Boat, and Plane, and they all have a method called move()..:
'''


class Car:
    def __init__(self, brand, model):
        self.brand =  brand
        self.model = model

    def move(self):
        print("Drive")

class Boat:
    def __init__(self, brand, model):
        self.brand =  brand
        self.model = model
    
    def move(self):
        print("Swim")

class Plane:
    def __init__(self, brand, model):
        self.brand =  brand
        self.model = model

    def move(self):
        print("Fly")

car1 = Car("BMW", "5 Series")
boat1 = Boat("Titanic", "T9400")
plane1 = Plane("Jet", "5 Series")

for i in (car1, boat1, plane1):
    i.move()