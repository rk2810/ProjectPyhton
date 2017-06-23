# This is the file to trigger the backend framework that contains all functions

# basic imports
from backend import *
from datetime import datetime

# start screen
current_time = datetime.now()
print "System time > " + current_time.strftime("%a, %d %b %Y | %l:%M")
print "Welcome to SpyChat !"
print "Setting up environment and getting things ready ... "
print "Done !"

# initiate spychat framework

main()
