# import pickle
# students=[{"name":"shaun","age":23},{"name":"John","age":25}]
# with open("students.pkl", "wb") as file:
#     pickle.dump(students,file)

# with open("students.pkl","rb") as file:
#     loaded_students = pickle.load(file)
#     print(loaded_students)


#modules
# import math
# print(math.sqrt(25))

# from math import sqrt
# print(sqrt(25)) 

# import my_module
# print(my_module.add(10,15))

# from my_module import add,subtract
# print(add(10,16))
# print(subtract(20,15))


# packages


# from mathoperations.mymdule import add

# ****** map, filter,reduce ******

# def square(x):
#     return x*x
# numbers=[1,2,3,4,5]
# squared=list(map(square,numbers))
# print(squared)

# def iseven(n):
#     return n%2==0

numbers=[1,2,3,4,5]
# even_numbers=list(filter(iseven,numbers))
# print(even_numbers)

# from functools import reduce
# def multiply(a,b):
#     return a*b

# product=reduce(multiply,numbers)
# print(product)


from functools import reduce
price = [100,200,300,400,500]
def apply_discount(price):
    return price * 0.9
def is_affordable(price):
    return price<350
def total_cost(a,b):
    return a+b

discounted_prices = list(map(apply_discount,price))
print(discounted_prices)
affordable_prices = list(filter(is_affordable,price))
print(affordable_prices)
total = reduce(total_cost,affordable_prices)

print(total)