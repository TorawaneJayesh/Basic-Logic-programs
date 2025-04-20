# here is simple patterns program

n = 5
# x = int(input("how many stars in colums:"))
# y = int(input("how many stars in rows:"))
for i in range(n):
    print("*" * n)
    
    
# star tringle
n = 5
for  i in range(1, n+1):
    print("*" * i)

# pyramid tringle
n = 5
for i in range(n):
    print(" " * (n - i - 1) + "*" *( 2*i+1))
    
# inverted pyramid
n  = 5
for i in range(n):
    print(" "*i + "*" *( 2*(n-i)-1))

# number pattern 
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end= "")
    print()


# floyd's tringle
n = 4
num = 1
for i in range (1, n + 1):
    for h in range(1, i + 1):
        print(num, end=" ")
        num += 1
    print()

# here are some more patterns by my logic

n = 4
val = 1
for i in range(1, n + 1):
    for j in range(1, i+1):
        print(val , end = " ")
    print()
    val += 1


n = 5
for i in range(n):
    space = n - i - 1
    star = i + 1
    print(" " * space, "*" * star)
    

n = 5
for i in range(1,n+1):
    for j in range(n,1):
        print("*" , end=" ")
