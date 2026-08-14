# program 1
# class Animal:
#     def __init__(self,name):
#         self.name=name
#     def eat(self):
#         print(f"{self.name} is eating")

# class Dog(Animal):
#     def __init__(self,name,name1):
#         super().__init__(name)
#         self.name1=name1
#     def bark(self):
#         print(f"{self.name1} is barking")

# class Cat(Animal):
#     def __init__(self,name2):
#         self.name2=name2
#     def meow(self):
#         print(f"{self.name2} is meowing")
    
# class Bird(Animal):
#     def __init__(self,name3):
#         self.name3=name3
#     def sound(self):
#         print(f"{self.name3} is making sound ")
        
# d=Dog("Lion","Bruno")
# d.eat()
# d.bark()
# c=Cat("Kitty")
# c.meow()
# b=Bird("sparrow")
# b.sound()


# program 2
class Employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        print(f"name = {self.name}")
        print(f"salary = {self.salary}")

class Developer(Employee):
    def __init__(self,name,salary,programming_language):
        super().__init__(name,salary)
        self.programming_language=programming_language
        print(f"Programming Language = {self.programming_language}")
        print()
        

class Designer(Employee):
    def __init__(self,name,salary,design_tool):
        super().__init__(name,salary)
        self.design_tool=design_tool
        print(f"Design Tool = {self.design_tool}")
        print()
        
d=Developer("shaun",40000,"Python")
designer=Designer("Sam",30000,"Photoshop")