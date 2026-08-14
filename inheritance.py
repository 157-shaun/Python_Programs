# Single Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, "is eating")


class Dog(Animal):
    def bark(self):
        print(self.name, "is barking")

d = Dog("Tommy")
d.eat()
d.bark()


#  Multiple Inheritance
class Father:
    def __init__(self):
        print("Father constructor")

    def skills(self):
        print("Father: Driving")


class Mother:
    def __init__(self):
        print("Mother constructor")

    def hobbies(self):
        print("Mother: Cooking")


class Child(Father, Mother):
    def __init__(self):
        Father.__init__(self)
        Mother.__init__(self)
        print("Child constructor")

    def study(self):
        print("Child: Studying")


c = Child()
c.skills()
c.hobbies()
c.study()


# # Multilevel Inheritance
class Grandparent:
    def __init__(self):
        print("Grandparent constructor")

    def house(self):
        print("Grandparent has a house")


class Parent(Grandparent):
    def __init__(self):
        super().__init__()
        print("Parent constructor")

    def car(self):
        print("Parent has a car")


class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child constructor")

    def bike(self):
        print("Child has a bike")



c = Child()
c.house()
c.car()
c.bike()


# # Heirarchical Inheritance
class Animal:
    def __init__(self, name):
        self.name = name
        print("Animal constructor")

    def eat(self):
        print(self.name, "is eating")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        print("Dog constructor")

    def bark(self):
        print(self.name, "is barking")


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
        print("Cat constructor")

    def meow(self):
        print(self.name, "is meowing")


d = Dog("Tommy")
d.eat()
d.bark()
print()
c = Cat("Kitty")
c.eat()
c.meow()


# # # Hybrid Inheritance
class Animal:
    def __init__(self):
        print("Animal constructor")

    def eat(self):
        print("Animal is eating")
 8

class Dog(Animal):
    def dog_sound(self):
        print("Dog says Woof")


class Cat(Animal):
    def cat_sound(self):
        print("Cat says Meow")


class Pet(Dog, Cat):
    def __init__(self):
        Animal.__init__(self)
        print("Pet constructor")

    def play(self):
        print("Pet is playing")



p = Pet()
p.eat()
p.dog_sound()
p.cat_sound()
p.play()