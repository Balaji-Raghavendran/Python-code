year = int(input("enter a year:"))
if year % 400 == 0:
    print("it is a leap year")         #divisible by 400 is considered as leap year.
elif year % 100 == 0:                  #not all the century years are considered as leap year.
    print("it is not a leap year")
elif year % 4 == 0:                    #divisible by 4 is considered as leap year.
    print("it is a leap year")
else:
    print("it is not a leap year")