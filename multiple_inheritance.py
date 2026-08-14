# program 1
class Father:
    def __init__(self,name1):
        self.name1=name1
    def display1(self):
        print(f"Father's name = {self.name1}")

class Mother:
    def __init__(self,name2):
        self.name2=name2
    def display2(self):
        print(f"Mother's name = {self.name2}")

class Child(Father,Mother):
    def __init__(self,name1,name2,name3):
        Father.__init__(self,name1)
        Mother.__init__(self,name2)
        self.name3=name3
    def display3(self):
        print(f"Child's name = {self.name3}")
        
c=Child("John","Sarah","Sam")
c.display1()
c.display2()
c.display3()


# program 2
# class Phone:
#     def make_call(self):
#         print("Make a call")
    
# class Camera:
#     def take_photo(self):
#         print("Take a photo")
        
# class Smartphone(Phone,Camera):
#     pass
        
# s=Smartphone()
# s.make_call()
# s.take_photo()