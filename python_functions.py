# to check whether a given number is odd or even
def odd_or_even(n):
    if n==0:
        print(f"{n} is neither odd or even")
    elif n%2==0:
        print(f"{n} is an even number")
    else:
        print(f"{n} is an odd number")

# n=int(input("enter a number :"))
odd_or_even(n)

# Largest number among three numbers
def largest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
    
num1=int(input("enter first number :"))
num2=int(input("enter first number :"))
num3=int(input("enter first number :"))
result=largest(num1,num2,num3)
print(f"{result} is the largest number")

# fnction to count the number of vowels in a string
def vowels_count(s):
    count=0
    vowels=['a','e','i','o','u']
    for i in s:
        if i in vowels:
            count+=1
    return count

s=input("enter a string :")
result = vowels_count(s)
print(result)

# factorial of a number
def factorial(n):
    fact=1
    if n==0 or n==1:
        return 1
    else:
        while n>0:
            fact*=n
            n-=1
    return fact

n=int(input("enter a number :"))
result=factorial(n)
print(f"factorial of {n} is {result}")

# sum and average of a list of numbers
def sum_average(list):
    sum=0
    avg=0
    size=len(list)
    for i in list:
        sum+=i
    avg=sum/size
    print (f"sum = {sum}")
    print(f"Average = {avg}")
    
list=[]
s=int(input("enter the size of list :"))
for i in range(s):
    n=int(input("enter a number :"))
    list.append(n)
sum_average(list)