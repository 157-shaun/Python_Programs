details=dict()
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
        name=input("Enter name :")
        age=int(input("Enter age :"))
        phone_no = input("Enter phone number :")
        if len(phone_no)==10 and phone_no.isdigit():
            initial_deposit = int(input("Enter initial deposit :"))
            details[phone_no]={"name":name,"age":age,"deposit":initial_deposit}
        else:
            print("Enter valid phone number")
        
    elif n==2:
        phone=input("Enter the phone number of the person to which the money is to be deposited :")
        for phone_no in details.keys():
            if phone_no==phone:
                amount=int(input("Enter the amount to be deposited :"))
                details[phone_no]["deposit"]+=amount
                print(f"the current amount in account is {details[phone_no]['deposit']}")
            
            
    elif n==3:
        phone=input("Enter phone number to withdraw amount from account :")
        for phone_no in details.keys():
            if phone_no==phone:
                amount=int(input("Enter the amount to withdraw :"))
                if amount>0:
                    if amount <= details[phone_no]["deposit"]:
                        details[phone_no]["deposit"]-=amount
                        print(f"Amount withrawed and balance = {details[phone_no]['deposit']}")
                    else:
                        print("Insufficient Balance")
                else:
                    print("Enter correct amount")
    
    elif n==4:
        phone=input("Enter phone number to delete account :")
        if phone in details:
            details.pop(phone)
            print("Account deleted")
        else:
            print("Invalid phone number")
        
    elif n==5:
        phone=input("Enter phone number to view the details of the account :")
        for phone_no in details.keys():
             if phone_no==phone:
                 print("\n")
                 print(f"Name = {details[phone_no]['name']}")
                 print(f"Age = {details[phone_no]['age']}")
                 print(f"Amount = {details[phone_no]['deposit']}")
                 print("\n")
        
    elif n==6:
        break
