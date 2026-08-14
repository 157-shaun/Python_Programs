# Single Inheritance
# program 1
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# class Student(Person):
#     def __init__(self,name,age,course):
#         super().__init__(name,age)
#         self.course=course
#     def display(self):
#         print(f"name = {self.name}, age = {self.age}, course = {self.course}")
        
# s=Student("shaun",23,"computer science")
# s.display()


# program 2
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department
    
    def display(self):
        print(f"name  = {self.name}, salary = {self.salary}, department = {self.department}")
        
m=Manager("shaun",50000,"Software Developer")
m.display()
        

# Multilevel Inheritance
