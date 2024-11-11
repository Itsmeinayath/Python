year = int(input("Provide the year : \n"))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 ==0):
    print(year,"ist a leap year")
else:
    print(year,"its not a leap year")