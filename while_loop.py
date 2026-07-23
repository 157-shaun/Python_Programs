# i=0
# while i<=10:
#     print(i)
#     i+=1

# a="shaun"
# b=len(a)
# i=0
# while i<b:
#     print(a[i],end="")
#     i+=1
# print(b)
# for i in a:
#     print(i,end=" ")

# reverse order of numbers from 1 to 10
# i=10
# while i>0:
#     print(i,end=" ")
#     i-=1
    
# even numbers from 1 to 50
# i=0
# a=int(input("enter a number :"))
# while i<=a:
#     print(i,end=" ")
    # i+=2
    # if i%2==0:
    #     print(i,end=" ")
    # i+=1
# choice =""
# while choice!="quit":
#     choice=input("Enter type quit to exit :")
# print("Goodbye")

# s=""
# total=0
# while s!=0:
#     s = int(input("Enter a number :"))
#     total+=s
# print(total)

# row=1
# while row<=3:
#     col=1
#     while col<=3:
#         print(f"({row},{col})",end=" ")
#         col+=1
#     print()
#     row+=1

while True:
    a=int(input("enter your firt number :"))
    b=int(input("enter your second number :"))
    c=a+b
    print(c)
    if a==0:
        break