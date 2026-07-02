class Car:
    def __init__(self, make, model, year, mileage, condition, color):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.condition = condition
        self.color = color
        self.engine_running = False  # New attribute to track engine state
    
    def start(self) -> None:

        self.engine_running = True
        print("The engine has started.")

    def get_info(self):
        return f"{self.year} {self.make} {self.model}"

    def start_engine(self):
        return "Vroom! The engine is running."

    def stop_engine(self):
        return "The engine is off."
    
    class car:
        def __init__(self, make="jeep", model="Wrangler", year=2020, mileage=0, condition="New", color="Black"):
            self.make = make
            self.model = model
            self.year = year
            self.mileage = mileage
            self.condition = condition
            self.color = color

        def get_info(self):
            return f"{self.year} {self.make} {self.model}"

        def start_engine(self):
            return "Vroom! The engine is running."

        def stop_engine(self):
            return "The engine is off."
        

my_car = Car("Toyota", "Camry", 2020, 15000, "Good", "Blue")

print("This is another class file.")

print(my_car.get_info())

# Solution:  
# 2020 Toyota Camry


# 5th video - Using methods in classes

my_car = Car("Toyota", "Camry", 2020, 15000, "Good", "Blue")

my_string = my_car.get_info()

print(my_string)  # Output: 2020 Toyota Camry

print(my_car.start_engine())  # Output: Vroom! The engine is running.

print(my_car.get_info().upper())

# 2020 TOYOTA CAMRY

print(my_string.strip().capitalize()) # Output: 2020 toyota camry

#===================================================================================


# Next video - building my own methods in classes
