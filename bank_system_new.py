account=[]
while True:
   print("1. Register")
   print("2.Login")
   n=int(input("Enter your choice :"))
   if n==1:
      name=input("Enter name :")
      age=int(input("Enter age :"))
      while True:
         found=False
         phone=input("Enter phone number :")
         if len(phone)!=10 or not phone.isdigit():
            print("Enter valid phone number")
            continue
         else:
            for user in account:
               if user["phone"]==phone:
                  print("phone number already exists, enter a new one")
                  found=True
                  break
         if found==False:
            break
      while True:
         username=input("Enter username :")
         found=False
         for user in account:
            if user["username"]==username:
               print("Username already exists, try new one")
               found=True
               break
         if found==False:
            break
      password=input("Enter password :")
      deposit=int(input("Enter initial deposit :"))
      account.append({"name":name,"age":age,"phone":phone,"username":username,"password":password,"deposit":deposit})
      print("\nRegistration Successfull\n")
   
   if n==2:
      while True:
         username=input("Enter username :")
         found=False
         for user in account:
            if user["username"]==username:
               found=True
               print("username matched.")
               break
            
           
            