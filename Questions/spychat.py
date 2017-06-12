spy_name = raw_input("What's your name ? : ")
string_length = len(spy_name)

# Spy online status
spy_is_online = str("true")

# str(string_length)
if string_length <= 0:
    print("name can't be null, you cant be a spy...")
    exit()
else:
    print('the data is valid')
# Salutation
print 'Welcome ' + spy_name + '. Glad that you are back !'
spy_salutation = raw_input("What should we call you (Mr. or Ms.)? : ")
spy_name = spy_salutation + " " + spy_name
print 'Ok' + " I call you " + spy_name

# Age section
spy_age = raw_input("Enter your age : ")

# Value check for age
if spy_age <= " ":
    print("invalid age !")
    exit()

elif 1>0 :
    spy_age = int(spy_age)
    if spy_age <= 15 and spy_age >= 50:
        print("You are too small for it")
        exit()
else:
    print("Age saved !")

# Spy rating
spy_rating = raw_input("Enter your rating(0~5): ")
spy_rating = float(spy_rating)

if spy_rating >= 4.7 :
    print("You're an excellent spy mate !")
elif spy_rating >=3 and spy_rating <=4.6 :
    print("You're a good spy mate !")
else :
    print("You're a spy for sure !")

print "Ok, let's evaluate....."

print " Welcome " + spy_name + " your age is " + str(spy_age) + " and your rating is " + str(spy_rating) + ", Welcome  aboard !"
