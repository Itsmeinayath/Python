class Car: #This is called class . It is a blueprint for the object
    #This is called constructor. It is a special method which is called when the object is created
    def __init__(self,userbrand,usermodel): #This is called parameters or arguments
       self.brand = userbrand #This is called attributes
       self.model = usermodel

# my_car = Car("Toyota","Corolla") #This is called arguments. we are passing the values to the parameters
# print(my_car.brand) #This is called accessing the attributes
# print(my_car.model)
# my_new_car = Car("Tata","Safari")
# print(my_new_car.brand)
# print(my_new_car.model)