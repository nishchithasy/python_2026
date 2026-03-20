#Object oriented programming
#Constructor,self.....

class movie:
      def __init__(self,title,ratings):
            self.title = title
            self.ratings = ratings

      def display_info(self):
            print(f"Movie title:{self.title}\n-->>>>>>>>>Ratings={self.ratings}")

The_movie = movie("Seeta Ramam","9.0")
The_movie.display_info()

#Employee
class employee:
      def __init__(self,name,designation,salary="30,000"):
            self.name = name
            self.designation = designation
            self.salary = salary

      def display_info(self):
            print(f"Employee1 >>>{self.name}\nDesignation >>>{self.designation}\nSalary >>>{self.salary}")
            print("-----------------------------------------------------------------------")

employee1 = employee("Ram","Fresher","15,000")
employee1.display_info()

employee2 = employee("Dev","Experienced")
employee2.display_info()

employee3 = employee("Ajay","Older","25,000")
employee3.display_info()


class laptop:
      def __init__(self,brand,price):
            self.brand = brand
            self.price = price

      def display_info(self):
            print(f"Brand:{self.brand}\nModel:{self.price}")

my_laptop1 = laptop("Lenova","30,000")
my_laptop1.display_info()
my_laptop2 = laptop("HP","52,000")
my_laptop2.display_info()
