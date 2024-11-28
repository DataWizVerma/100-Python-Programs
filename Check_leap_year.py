'''year--- 365 day's 
but
In leap year-- 366 day's
Once in 4 Year '''

year=int(input("Enter Your Year: "))

if (year%400==0) and (year%100==0):
    print("It is a leap year"),
elif (year%4==0) and (year % 100 !=0):
    print("It is a leap year")
else:
    print("Not a leap")