class Car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    def display_details(self):
        print(f"Car Brand = {self.brand} , Car Model = {self.model} , Car year = {self.year}")
        
car1=Car("Benz","c_class",1998)
car2=Car("Lamborghini","Aventador",2002)
# car1.display_details()
# car2.display_details()


class Student:
    def __init__(self):
        print("first constructor")
    def __init__(self):
        print("second constructor")
    def display(self,name):
        print(name)

s1=Student()
s1.display("shaun")



