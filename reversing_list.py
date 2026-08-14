# reversing the list using index value

# numbers = [10,8,20,11,5,2]
# start=0
# end=len(numbers)-1
# while start < end:
#     numbers[start],numbers[end]=numbers[end],numbers[start]
#     start+=1
#     end-=1
# print(numbers)

# sorting a list without using built-in function

numbers = [10,8,20,11,5,2]
s=len(numbers)
for i in range(s-1,0,-1):
    for j in range(s-1,)