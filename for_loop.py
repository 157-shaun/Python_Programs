# for loop to print even numbers from 1 to 50
# for i in range(1,51):
#     if i%2==0:
#         print(i,end = " ")
        
# sum of numbers
# n=int(input("Enter a number :"))
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print(sum) 

# Multiplication table of a number
# n=int(input("enter a number :"))
# print("Multiplication table of",n,"are")
# for i in range(1,11):
#     print(n,"x",i,"=",n*i)
    
# Count vowels in a string
# s=input("enter a string :")
# count=0
# v=['a','e','i','o','u']
# for i in s:
#     if i in v:
#         count+=1
# print(count)

# factorial of a number
# n=int(input("enter a number :"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print("Factorial of",5,"is",fact)


def sum_digits(num):
    temp=0
    Sum=0
    if num<0 or (num>=0 and num<10):
        print("Enter a multidigit number")
        return None
    else:     
        while num>0:
           temp=num%10
           Sum+=temp
           num//=10
    if Sum>=0 and Sum<10:
        return Sum
    else:
        return sum_digits(Sum)


num=int(input("Enter a number :"))
result=sum_digits(num)
if result is not None:
    print(f"Sum of the digits of {num} until it becomes a single digit = {result}")