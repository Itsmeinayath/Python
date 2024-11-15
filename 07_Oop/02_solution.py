
# Here we are importing the Car class from the main.py file
from main import Car
def full_name(self):
    return f"{self.brand} {self.model}" #This is called method

# Creating an instance of the Car class
info_car = Car("Toyota","Corolla") 
print(full_name(info_car))