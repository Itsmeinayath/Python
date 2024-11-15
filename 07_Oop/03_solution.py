from main import Car

class ElectricCar(Car):
    def __init__(self, userbrand, usermodel,battery_size):
        super().__init__(userbrand, usermodel)
        self.battery_size = battery_size

my_tesla = ElectricCar("Tesla","Model S","86kWh")
print(my_tesla.brand,my_tesla.model,my_tesla.battery_size)

# This is called inheritance. It is a way of creating a new class using the existing class.
# The new class is called the child class and the existing class is called the parent class.
# The child class inherits the attributes and methods of the parent class.
# The child class can have its own attributes and methods.
# The child class can override the attributes and methods of the parent class.
# The child class can also have its own constructor.
# The child class can call the constructor of the parent class using the super() function.
# The super() function is used to call the constructor of the parent class.
# The super() function is used to call the methods of the parent class.

