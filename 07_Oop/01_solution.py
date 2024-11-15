class Car: #This is called class . It is a blueprint for the object
    #This is called constructor. It is a special method which is called when the object is created
    total_cars = 0
    
    def __init__(self,userbrand,usermodel): #This is called parameters or arguments
       self.brand = userbrand #This is called attributes
       self.model = usermodel
       Car.total_cars += 1
    
    # def get_brand(self):
    #     return self.__brand + " !"
    
    def full_name(self):
        return f"{self.brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    @staticmethod
    def general_description():
        return "Cars are the most popular mode of transport in the world"

my_car = Car("Toyota","Corolla") #This is called arguments. we are passing the values to the parameters
print(my_car.brand,my_car.model) #This is called accessing the attributes

my_new_car = Car("Tata","Safari")
print(my_new_car.brand,my_new_car.model)

print(Car.total_cars)


class ElectricCar(Car):
    def __init__(self, userbrand, usermodel,battery_size):
        super().__init__(userbrand, usermodel)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"

my_tesla = ElectricCar("Tesla","Model S","86kWh")
# print(my_tesla.brand,my_tesla.model,my_tesla.battery_size)

# print(my_tesla.get_brand())

my_car = Car("Tata","Safari")
my_car.model = "City"
safarithree = Car("Tata","Nexon")

# print(my_car.general_description())

print(Car.general_description())
# print(safari.fuel_type())

# tesla = ElectricCar("Tesla","Model S","86kWh")
# print(tesla.fuel_type())








#oops in python . It is a way of programming which is based on objects and classes.
#Objects are instances of classes. Classes are blueprints for objects.
#Classes are created using the keyword class.
#Objects are created using the constructor __init__ method.
#Attributes are variables that belong to the object.
#Attributes are accessed using the dot operator.
#Attributes are defined in the constructor method.
#Methods are functions that belong to the object.
#Methods are defined inside the class.
#Methods are called using the dot operator.
