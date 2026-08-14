# def greet():
#     print("shaun")

# greet()
# greet()

# def greet():
#     return "shaun"
# # print(greet())
# a=greet()
# print(a)

# def add(a):
#     b=10
#     return a+b

# result = add(20)
# print(result)

# def add(p,q):
#     return p+q

# a=int(input("Enter a number :"))
# b=int(input("Enter a number :"))
# result = add(a,b)
# print(result)

# def even(num1,num2):
#     for i in range(num1,num2+1):
#         if i%2==0:
#             print(i,end=" ")




# num1=int(input('enter a number :'))
# num2 = int(input("enter a number :"))
# print("even numbers are")
# even(num1,num2)

# with arguments with return type
# def add(a,b):
#     return a+b

# a=int(input("enter a number :"))
# b=int(input("enter a  number :"))
# result=add(a,b)
# print(result)

# # with argument without return type
# def add(a,b):
#     print(a+b)

# a=int(input("enter a number :"))
# b=int(input("enter a  number :"))
# add(a,b)

# # without argument without return type
# def add():
#     a=int(input("enter a number :"))
#     b=int(input("enter a number :"))
#     result=a+b
#     print(result)

# add()

# # without argument with return type
# def add():
#     a=int(input("enter a number :"))
#     b=int(input("enter a number :"))
#     return a+b

# result=add()
# print(result)


# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n*factorial(n-1)
    
# print(factorial(5))

# def Sum(n):
#     if n==0:
#         return 0
#     else:
#        return n+Sum(n-1)

# n=int(input("enter a number :"))
# print(Sum(n))

# add=lambda a,b:a+b
# print(add(2,3))

# numbers = [1,2,3,4,5]
# even_numbers = list(filter(lambda x:x%2==0,numbers))
# print(even_numbers)

numbers=[1,3,2]
sorted_numbers=sorted(numbers,key=lambda x:-x)
print(sorted_numbers)
