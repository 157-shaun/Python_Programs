print("1. Pyramid star pattern")
print("2. Inverted Number Pattern")
print("3. Sum of First N Natural Numbers")
print("4. Power of a Number")
print("5. Exit")

while True:
    choice=int(input("Enter your choice :"))
    if choice==1:
        n=4
        for i in range(1,n+1):
            for p in range(n-i):
                 print(" ",end=" ")
            for j in range(2*i-1):
                print("*",end=" ")
            print()
            

    if choice==2:
        n=4
        for i in range(n,0,-1):
            for j in range(1,i+1):
                print(j,end=" ")
            print()
        
    if choice==3:
      def sum_numbers(n):
        if n==0:
            return 0
        return n+sum_numbers(n-1)
    
      n=int(input("Enter a number :"))
      print(sum_numbers(n))
    
    if choice==4:
        power=lambda x,y:x**y
    
        x=int(input("Enter a number"))
        y=2
        print(power(x,y))
    
    if choice==5:
       break

