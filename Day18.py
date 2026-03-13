#Object oriented Programs (Modules -> Program splits into different modules)
#Object -> Has attributes and methods
#Procedural program which depends on data and functions -> no modularity

#Classes-> it is a blue print(template) to create -> Objects

class car:
    #Attributes
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    #Methods
    def display_info(self):
        print(f"Car brand:{self.brand}\nModel:{self.model}")

#Creating an object of the class
my_car = car("Toyota","Corolla")
my_car.display_info()




