# hollow square pattern
# row = int(input("enter number of rows :"))
# colm = int(input("enter number of columns :"))
# for i in range(row):
#     for j in range(colm):
#         if i == 0 or i == row - 1:
#             print("*", end=" ")
#         elif j == 0 or j == colm - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# Number triangular
# rows=int(input("enter number of rows :"))
# for i in range(1,rows+1):
#     print(" "*(rows-i),end=" ")
#     for j in range(i):
#         print(i,end=" ")
#     print()

# number increasing pyramid
# row=int(input("Enter number of rows :"))
# for i in range(1,row+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# number increasing reverse pyramid
# row=int(input("enter number of rows :"))
# for i in range(row,0,-1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# number changing pyramid
# row=int(input("Enter number of rows :"))
# n=1
# for i in range(1,row+1):
#     for j in range(i):
#         print(n,end=" ")
#         n+=1
#     print()

# zero-one triangle
# row=int(input("enter number of rows :"))
# a=int(input("enter first number :"))
# b=int(input("enter second number :"))
# for i in range(1,row+1):
#     for j in range(i):
#         if (i+j)%2!=0:
#             print(b,end=" ")
#         else:
#             print(a,end=" ")
#     print()

# Palindrome triangular
row = int(input("enter number of rows :"))
for i in range(1,row+1):
    print(" "*(row-i),end=" ")
    