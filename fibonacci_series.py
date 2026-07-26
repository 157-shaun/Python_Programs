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