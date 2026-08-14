# public 
# class Student:
#     def __init__(self,name):
#         self.name=name

# student=Student("shaun")
# print(student.name)

# protected
class Student:
    def __init__(self,name):
        self._name=name
    
student=Student("shaun")
print(student._name)

# private
class BankAccount:
    def __init__(self,balance):
        self.__balance=balance
    
    def deposit(self,amount):
        self.__balance=amount
    
    def withdraw(self,amount):
        if amount <=self.__balance:
            self.__balance-=amount
        else:
            print("Insufficient balnce")
    def get_balance(self):
        return self.__balance
    
        
    
account=BankAccount(5000)
account.deposit(2000)
account.withdraw(1000)
print(f"Balance = {account.get_balance()}")
