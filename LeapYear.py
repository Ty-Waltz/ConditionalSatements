year = int(input("What year were you born? "))

if year % 4 == 0 and not year % 100 == 0:
    print("it's a leap year!")
elif year % 400 == 0 :
    print("it's a leap year!")
else:
    print("it's not a leap year!")
