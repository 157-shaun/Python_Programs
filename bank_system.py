# Registration
account=[]
num=int(input("Enter the total number of people to be registered :"))
for i in range(num):
    name=input("Enter name :")
    age=int(input("Enter age :"))
    while True:
        phone=input("Enter phone number :")
        if len(phone)!=10 or not phone.isdigit():
            print("Enter valid phone number")
            continue
        found=False
        for i in account:
            if i["phone"]==phone:
                found=True
                print("phone number already exists")
                break
        if found==False:
            break
    while True:
        username=input("Enter username :")
        found=False
        for i in account:
            if i["username"]==username:
                print("Username already exists")
                found=True
                break
        if found==False:
            break
    
    password=input("Enter password :")
    deposit=int(input("Enter initial deposit :"))
    user={"name":name,"age":age,"phone":phone,"username":username,"password":password,"deposit":deposit}
    account.append(user)
    print("\n Registration Successful\n")
    

# Login
print("Please enter username and password to login\n")
username=input("Enter username :")
password=input("Enter password :")
for user in account:
    if user["username"]==username and user["password"]==password:
        print("User Logged in successful")
        break
    
while True:
    print("1. Deposit")
    print("2 . Withdraw")
    print("3. Profile view")
    print("4. Logout\n")
    n=int(input("Enter your choice :"))
    
    if n==1:
        amount=int(input("Enter the amount to deposit :"))
        if amount>0:
            for user in account:
                if amount < user["deposit"]:
                    user["deposit"]+=amount
                else:
                    print("Insufficient balance")
        else:
            print("Enter valid amount")
    
    if n==2:
        amount=int(input("Enter the amount to withdraw"))
        if amount>0:
            for user in account