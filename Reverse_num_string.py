# reverse of the number.
rev = 0
n = 321
while(n>0):
    rem = n % 10
    rev = rev * 10 + rem
    n = int(n//10)
print(rev)

# here is easiast way to reverse a num.
import string
n = 567
x = str(n)
n = x[::-1]
print(n)

# now reverse a string.
str = "python"
n = str[::-1]
reversed_string = ''.join(reversed(str))
print(reversed_string)

# using slicing
str = "slice"
reversed_string = str[::-1]
print("reversed string is: ",reversed_string)