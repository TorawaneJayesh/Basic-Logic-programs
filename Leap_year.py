year =  int(input("enter a year:"))
if year % 4 == 0 and year % 100 != 0:
    print(f"year {year} is leap.")
else:
    print(f"year {year} is Not-leap.")