# fibonacci series.
x, y = 0, 1
sum = 0
num = int(input("enter a number:"))
for i in range(num):
    print(x)
    sum += x
    x, y = y, x + y
print("total of fibonacci:",sum)