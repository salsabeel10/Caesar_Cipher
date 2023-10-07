def days_in_month(year,num):
   if year%400==0 or year%4==0 and  year%100!=0:
      month_day=[31,29,31,30,31,30,31,31,30,31,30,31]
      return month_day[num-1]
   else:
      month_day=[31,28,31,30,31,30,31,31,30,31,30,31]
      return month_day[num-1]

        
year=int(input("enter a year:"))
month=int(input("enter a Month:"))

days=days_in_month(year,month)
print(days)