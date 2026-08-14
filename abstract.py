# abstract method
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
    
# concrete method
from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
    def move(self):
        return "moving"
class Dog(Animal):
    def make_sound(self):
        return "Bark"

dog=Dog()
print(dog.move())

# abstract properties
from abc import ABC, abstractmethod
class Animal(ABC):
    @property
    @abstractmethod
    def species(self):
        pass

class Dog(Animal):
    @property
    def species(self):
        return "canine"
    
dog=Dog()
print(dog.species)
        
# self instantiation
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
animal=Animal()
    