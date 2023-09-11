total=float(input("what was the total Bill?$ "))
people=int(input("how many people to split the Bill? "))
tip=int(input("what percentage tip to give ? 10,12or 15? "))
sum=total+(total*tip/100)
result=sum/people
print('Each person should pay:$',round(result,2))
