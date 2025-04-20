# here is simple code for num is armstrong or not.
# 153 = sum of cube of 1 , 5, 3  is 153 thats why it is armstrong.

num =  int(input("enter a number:"))
num1 = str(num)
sum = 0
for digit in num1:
    sum += int(digit) ** 3
    
if sum == num:
    print("number is armstrong.")
else:
    print("number is not armstrong.")
    