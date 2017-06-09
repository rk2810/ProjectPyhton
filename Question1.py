# given a number N the player must subtract 1,2 & 3 from n in order to make it divisible by 4
number_n = raw_input("Enter a number")
number_n = int(number_n)

# the magic
if ((number_n - 3) % 4 == 0 or (number_n - 2) % 4 == 0 or (number_n -1) % 4 ==0 ):
    print "Player 1 wins"
else:
    print "Player 2 wins "