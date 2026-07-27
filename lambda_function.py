# square of a number
n=int(input("enter a number :"))
square=lambda x:x**2
print(square(n))


# largest among two numbers
num1=int(input("enter first number :"))
num2=int(input("enter second numberv :"))
largest=lambda num1,num2: num1 if num1>num2 else num2
print(largest(num1,num2))


# using lambda function to create a list of even numbers using filter() from a given list of numbers
numbers = [1,2,3,4,5]
even_numbers = list(filter(lambda x:x%2==0,numbers))
print(even_numbers)


# using lambda function with map to create a list of square of each numbers from a given list of numbers
numbers = [1,2,3,4]
square_numbers=list(map(lambda x:x**2,numbers))
print(square_numbers)


# use lambda function with sorted to sort students name and marks based on the descending order of marks
student_details=[
                   {"name" : "John","marks":95}, 
                   {"name" : "Sam","marks":89},
                   {"name" : "Philip","marks":91},
                ]
sorted_details=sorted(student_details,key= lambda x:-x["marks"] )
print(sorted_details)

