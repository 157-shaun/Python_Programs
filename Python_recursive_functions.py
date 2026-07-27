# factorial of a number
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
    
n=int(input("enter a number :"))
print(factorial(n))


# sum of first n natural numbers
def Sum(n):
    if n==0:
        return 0
    else:
       return n+Sum(n-1)

n=int(input("enter a number :"))
print(Sum(n))


# fibonacci series upto the nth term
def fibonacci(num):
    global first,second,i
    if num>2:
        third=first+second
        print(third,end=" ")
        first=second
        second=third
        return fibonacci(num-1)
    

num=int(input("Enter a number :"))
first=0
second=1
if num<0 or num==0:
    print("Enter a positive integer")
else:
    print(first,second,end=" ")
    fibonacci(num)


# reversing a string
def reverse(s):
    return s[1:]+s[0]

s=input("enter a string :")
print(reverse(s))


# calculate the power of a number
def power(base,exponent):
    if exponent==0:
        return 1
    else:
        return base*power(base,exponent-1)

base=int(input("enter base number :"))
exponent = int(input("enter exponent :"))
result = power(base,exponent)
print(result)