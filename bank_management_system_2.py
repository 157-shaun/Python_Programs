details=[]
while True:
    print("-------Bank Management System--------")
    print("1. Create Account")
    print("2 . Deposit Money")
    print("3. withdraw Money")
    print("4. Delete Account")
    print("5. View Account")
    print("6. Exit")
    n=int(input("Select Option :"))
    
    if n==1:
        found=False
        name=input("Enter name :")
        age=int(input("Enter age :"))
        phone_no = input("Enter phone number :")
        if len(phone_no)==10 and phone_no.isdigit():
            for person in details:
                if person[2]==phone_no:
                  found=True
                  break
            if not found:
                deposit = int(input("Enter initial deposit :"))
                details.append([name,age,phone_no,deposit])
            else:
                print("Enter diferent number")
        else:
            print("Enter valid phone number")
    elif n==2:
        phone=input("Enter the phone number of the person to which the money is to be deposited :")
        for phone_no in range(len(details)):
            if details[phone_no][2]==phone:
                amount=int(input("Enter the amount to be deposited :"))
                details[phone_no][3]+=amount
                print(f"the current amount in account is {details[phone_no][3]}")
            
            
    elif n==3:
        phone=input("Enter phone number to withdraw amount from account :")
        for phone_no in range(len(details)):
            if details[phone_no][2]==phone:
                amount=int(input("Enter the amount to withdraw :"))
                if amount>0:
                    if amount <= details[phone_no][3]:
                        details[phone_no][3]-=amount
                        print(f"Amount withrawed and balance = {details[phone_no][3]}")
                    else:
                        print("Insufficient Balance")
                else:
                    print("Enter correct amount")
    
    elif n==4:
        length=len(details)
        phone=input("Enter phone number to delete account :")
        for phone_no in range(len(details)):
            if details[phone_no][2]==phone:
               details.pop(phone_no)
               print("Account deleted")
        if length==len(details):
            print("Enter valid phone number")
    elif n==5:
        phone=input("Enter phone number to view the details of the account :")
        for phone_no in range(len(details)):
             if details[phone_no][2]==phone:
                print("\n")
                print(f"Name = {details[phone_no][0]}")
                print(f"Age = {details[phone_no][1]}")
                print(f"phone_number = {details[phone_no][2]}")
                print(f"Amount = {details[phone_no][3]}")
                print("\n")
        
    elif n==6:
        break





