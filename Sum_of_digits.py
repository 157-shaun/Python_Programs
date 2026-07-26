# Sum of the digits of a number until it becomes a single digit

def sum_digits(num):
    temp=0
    Sum=0
    while num>0:
        temp=num%10
        Sum+=temp
        num//=10
    if Sum>=0 and Sum<10:
        return Sum
    else:
        return sum_digits(Sum)


num=int(input("Enter a number :"))
if num<0 or num==0 or (num>0 and num<10):
    print("Enter a multidigit number")
else:
    result = sum_digits(num)
    print(f"sum of digits of {num} until it becomes a single digit = {result}")