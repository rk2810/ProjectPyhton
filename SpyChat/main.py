# Imports


print "Welcome to SpyChat !"
print "Setting up environment and getting things ready ... "
print "Done !"
spy_credentials = {
    'username': ['admin'],
    'password': ['password']
    }
username_count = 1
password_count = 1


def chat():
    ans = True
    while ans:
        print """
            1.Send a message
            2.Set status
            3.View chats
            """
        ans = raw_input("What would you like to do? ")
        if ans == "1":
            print "Send message control line > "
            ans = False

        elif ans == "2":
            print "Set status control line > "
            ans = False

        elif ans == "View chat control line >":
            ans = False

        elif ans != "":
            print "Not Valid Choice Try again"


def existing():
    spy_username = raw_input("Enter your username : ")
    spy_pass = raw_input("Enter password : ")
    if spy_username in spy_credentials['username']:
        x = spy_credentials['username'].index(spy_username)
        if spy_pass is spy_credentials['password'][x]:
            print "Welcome " + spy_username + ", Good to have you back !"
            chat()
        else:
            print "Incorrect password... Exiting!"


def password():
    new_password = raw_input("Enter a password for your account ( 6 char min) : ")
    if len(new_password) < 6:
        print "password too short, try again..."
        password()
    else:
        print "password saved !"
        spy_credentials['password'].append(new_password)
        print "redirecting you to main page, login as existing user."
        main()


def new_user():
    new_username = str(raw_input("Enter a username for yourself (make it unique) : "))
    if new_username in spy_credentials['username']:
        print "username already exists.... try again "
        new_user()
    else:
        print "Adding username...."
        spy_credentials['username'].append(new_username)
        password()


def main():
    ans = True
    while ans:
        print """
        1.Existing user login
        2.New user
        3.Exit/Quit
        """
        ans = raw_input("What would you like to do? ")
        if ans == "1":
            print "Loading login form > "
            existing()
            ans = False

        elif ans == "2":
            print "Loading new user form > "
            new_user()
            ans = False

        elif ans == "3":
            print "Good bye mate..."
            exit()

        elif ans != "":
            print "Not Valid Choice Try again"


main()

