num = int(input("enter a number:"))
if num <= 1 :
    print("one and less than one is not prime.")
else:
    for i in range(2,num):
        if num % i == 0:
            print(f"number {num} is not prime")
            break
    else:
            print("is prime")