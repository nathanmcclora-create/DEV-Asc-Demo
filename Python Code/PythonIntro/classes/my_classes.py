# Building a class in Python is a way to create a blueprint for objects. 
# A class defines the properties and behaviors that the objects created from it will have. 
# In Python, you can define a class using the `class` keyword, followed by the class name and a colon. 
# Inside the class, you can define methods (functions) and attributes (variables) that belong to the class.

class Car:
    def __init__(self, make: str, model: str, year: int, mileage: int, condition: str, color: str) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.condition = condition
        self.color = color



my_car = Car(make="Toyota", model="Camry", year=2020, mileage=15000, condition="Good", color="Blue")

my_wife_car = Car(make="Honda", model="Civic", year=2018, mileage=30000, condition="Excellent", color="Red")

from classes.my_classes import Car