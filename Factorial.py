# factorial of n numbers.
# n = 5 - 5 * 4 * 3 * 2 * 1 = 120 this is factorial of 5.

num = int(input("enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print("factorial is :", fact)


# using recursion.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
n = int(input("enter a num:"))
print(f"factorial of {n} is {factorial(n)}")