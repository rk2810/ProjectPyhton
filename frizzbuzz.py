number = raw_input("Enter a number : ")
number = int(number)

# Calc:

if number % 3 == 0 and number % 5 ==0:
    print "Frizzbuzz"
elif number % 3 ==0:
    print "Frizz"
elif number % 5 == 0:
    print "buzz"
else:
    print number

