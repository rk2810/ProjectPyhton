# Leap year
year = raw_input("Enter the year to check : ")
year = int(year)

# Calculations

if year % 100 == 00:
    if year % 400 is 0:
      print"It's a leap year !"
    else:
        print"Not a leap year !"
elif year % 4 is 0:
    print"it's a leap year !"
else:
    print"Not a leap year !"