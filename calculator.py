print(" "*3,"Calculator")
while True:
    num1=int(input("enter a number :"))
    num2=int(input("enter a number :"))
    operator = input("choose the operator (+,-,//,*) :")
    if operator=='+':
        print(num1,"+",num2,"=",num1+num2)
    elif operator=='-':
        if num1>num2:
           print(num1,"-",num2,"=",num1-num2)
        else:
            print(num2,"-",num1,"=",num2-num1)
    elif operator=='//':
        print(num1,"//",num2,"=",num1//num2)
    else:
        print(num1,"x",num2,"=",num1*num2)
    d=int(input("if you want to exit enter 5 :"))
    if d==5:
        break