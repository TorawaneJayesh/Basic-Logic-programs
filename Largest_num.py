# find largest number from given three num.
a = 2
b = 7
c = 5
if a > b:
    print(f"{a} is greater than {b} and {c}")
elif b > c:
    print(f"{b} is greater than {a} and {c}")
elif c > a:
    print(f"{c} is greater than {b} and {a}")
else:
    print("all are same")

# here is another alternative way.
large_element = max(a,b,c)
print(large_element)

# largest num in list.
list = [4,6,3,8,6]
ans = max(list)
print(f"{ans} is largest element in this list{list}.")

# code for largest number given by user.
n  = int(input("enter how many numbers."))
list = []
for i in range(1, n+1):
    num = int(input("enter a num:"))
    list.append(num)
ans = max(list)
print(ans,"is big number.")