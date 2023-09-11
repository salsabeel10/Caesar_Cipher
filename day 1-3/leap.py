year=int(input("enter the Year: "))

if (year%4==0 and year%100!=0) or (year%400==0):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is Not Leap Year")    