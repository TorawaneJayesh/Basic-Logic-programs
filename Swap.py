# swap two numbers.
n1 = int(input("enter number a:"))
n2 = int(input("enter number b:"))

print(f"before swaping:a = {n1}, b = {n2}")

temp = n1
n1 = n2
n2 = temp

print(f"after swaping:a = {n1}, b = {n2}")
