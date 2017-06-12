# There are N coins in a pile. Player chose to remove one or two coins, alternative turn, last one to draw wins

coins = raw_input("Enter the number of coins : ")
coins = int(coins)
# The logic
if coins > 2:
    if coins % 3 is 0:
        print "Winner is Rohit"
    else:
        print "Winner is Puneet "
else:
    print "Winner is Punnet"

