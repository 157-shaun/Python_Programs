# program 1
class Person:
    def __init__(self,name):
        self.name=name
        
class Employee(Person):
    def __init__(self,name,employee_id):
        super().__init__(name)
        self.employee_id=employee_id
        
class Manager(Employee):
    def __init__(self,name,employee_id,department):
        super().__init__(name,employee_id)
        self.department=department
    def display(self):
        print(f"name = {self.name}, employee id = {self.employee_id}, department = {self.department}")
        

m=Manager("shaun",101,"Developer")
m.display()

# program 2
class Vehicle:
    def __init__(self,brand):
        self.brand=brand
class Car(Vehicle):
    def __init__(self,brand,model):
        super().__init__(brand)
        self.model=model
class SportsCar(Car):
    def __init__(self,brand,model,top_speed):
        super().__init__(brand,model)
        self.top_speed=top_speed
    def display(self):
        print(f"brand = {self.brand}")
        print(f"model = {self.model}")
        print(f"top speed = {self.top_speed}")
        
s=SportsCar("BMW","Z5","150 Km/hr")
s.display()