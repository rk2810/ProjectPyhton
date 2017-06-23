# This contains all functions as a backend framework for spychat app

# Imports:

from steganography.steganography import Steganography
from termcolor import colored
# Static variable
current_username = []
temp_recipient = []
friend_list = ['Trenton', 'Romero', 'Darlene', 'Elliot']
appended_friend_list = []

# Dictionaries
spy_credentials = {
    'username': ['admin', 'secondary'],
    'password': ['password', 'pass'],
    'name': ['fSociety', 'No Name'],
    'spy rating': ['5', '5'],
    'spy salutation': ['Mr.', 'Master'],
    'spy status': ['Working !', 'Alive']
    }
chats = {
    'sender': [],
    'recipient': [],
    'message': []
}

# Functions


def view_messages_received():    # function to view received messages
    print "Received messages > "
    for i in range(0, len(chats['recipient'])):
        if chats['recipient'][i] == current_username[0]:
            print "Sender : " + chats['sender'][i]
            print "Chat : " + chats['message'][i]
            view_message_options()
        else:
            print "No chats found !"
            view_message_options()


def view_messages_sent():   # function to view sent messages
    print "Sent messages >"
    for i in range(0, len(chats['recipient'])):
        if chats['sender'][i] == current_username[0]:
            print "Sent to : " + chats['recipient'][i]
            print "Chat : " + chats['message'][i]
        else:
            print "No chats found !"
            view_message_options()


def view_message_options():     # message options
    ans = True
    while ans:
        print """
                1.Sent messages 
                2.Received messages
                3.back
                """
        ans = raw_input("What would you like to do ? ")
        if ans == "1":
            view_messages_sent()
        elif ans == "2":
            view_messages_received()
        elif ans == "3":
            chat()
        elif ans != "":
            print "Invalid choice... try again!"


def send_message():     # send message control function
    message = raw_input("Enter the message to encode : ")
    path_image = "input.jpg"
    output_path = "message.jpg"
    Steganography.encode(path_image, output_path, message)
    user_index = spy_credentials['username'].index(current_username[0])
    chats['sender'].append(spy_credentials['username'][user_index])
    chats['recipient'].append(temp_recipient[0])
    chats['message'].append(message)
    print "Message sent..."
    print "Clearing traces and temporary files..."
    temp_recipient.pop(0)
    print "Done ! All set..."
    chat()


def send_message_validation():      # username validator for chats
    get_user = raw_input("Username of recipient : ")
    if get_user in spy_credentials['username']:
        temp_recipient.append(get_user)
        send_message()
    else:
        print "Wrong username"
        print "Moving back ..."
        chat()


def view_profile_fancy():       # not so fancy view profile zone
    print "your current profile > "
    index = spy_credentials['username'].index(current_username[0])
    print "Name : " + spy_credentials['name'][index]
    print "Salutation : " + spy_credentials['spy salutation'][index]
    print "Status : " + spy_credentials['spy status'][index]
    print "DATA FETCHED !"
    print "moving back..."
    edit_profile()


def add_friend():    # add friend controls
    friend_added_username = raw_input("Enter username of your friend : ")
    if friend_added_username in spy_credentials['username']:
        x = spy_credentials['username'].index(friend_added_username)
        question = raw_input("Are you sure you want to add " + " " + spy_credentials['name'][x] + " ? (y/n)")
        if question is "y" or "Y":
            print "Adding..."
            spy_credentials['appended_friend_list'].append(spy_credentials['name'][x])
            print "Your new friend list : "
            print ", ".join(friend_list) + " ," + " , ".join(appended_friend_list)
            chat()
        else:
            print "friend not added."
            chat()
    else:
        question = raw_input("friend not found, try again ?(y/n)")
        if question is "y" or "Y":
            add_friend()
        else:
            print("going back to chat menu >")
            chat()


def remove_friend():    # remove friend controls
    print "Your current friends are > "
    print friend_list + appended_friend_list
    friend_remove_user = raw_input("Enter name of friend to be removed ")
    if friend_remove_user in friend_list or appended_friend_list:
        remove = friend_list.index(friend_remove_user)
        friend_list.pop(remove)
        print "Your friend list is now >"
        print friend_list
        question = raw_input("Remove more friends ? (y/n) ")
        if question is "Y" or "y":
            remove_friend()
        else:
            print "Moving back to chat menu >"
            chat()


def view_friends():     # view friends control
    print "This is your current friend list > "
    print friend_list
    question = raw_input("Would you like to edit friends ? (y/n) ")
    if question is "y" or "Y":
        ans = True
        while ans:
            print """
                        1.Add a friend
                        2.Remove a friend
                        3.Back
                        4.Exit
                        """
            ans = raw_input("What would you like to do ? ")
            if ans == "1":
                add_friend()
                ans = False
            if ans == "2":
                remove_friend()
                ans = False
            if ans == "3":
                chat()
                ans = \
                    False
            if ans == "4":
                while len(current_username) > 0:
                    current_username.pop()
                print "Destroying data and clearing cache..."
                exit()
            if ans != "":
                print "Invalid selection, try again"


def edit_profile_name():    # editing profile: name
    print "your current name is > "
    index = spy_credentials['username'].index(current_username[0])
    print "Name : " + spy_credentials['name'][index]
    new_name = raw_input("Enter new name : ")
    spy_credentials['name'][index] = new_name
    print "New name set to > " + new_name
    print "Saved ! Moving back..."
    edit_profile()


def edit_status():  # editing profile: status
    index = spy_credentials['username'].index(current_username[0])
    print "Current status : " + spy_credentials['spy status'][index]
    new_status = raw_input("Enter new status(1~50 length) : ")
    spy_credentials['spy status'][index] = new_status
    print "New status set to > " + new_status
    print "Saved ! Moving back..."
    edit_profile()


def edit_salutation():  # editing profile: salutation
    print "Your current salutation in use is > "
    index = spy_credentials['username'].index(current_username[0])
    print spy_credentials['spy salutation'][index]
    new_salutation = raw_input("Enter new salutation : ")
    spy_credentials['spy salutation'][index] = new_salutation
    print "Saved ! Moving back..."
    edit_profile()


def edit_profile():     # editing profile options
    ans = True
    while ans:
        print """
                1.Name
                2.Salutation
                3.Status
                4.Nothing at all/ Keep as it is...
                """
        ans = raw_input("What would you like to edit ? ")
        if ans == "1":
            edit_profile_name()
        if ans == "2":
            edit_salutation()
        if ans == "3":
            edit_status()
        if ans == "4":
            chat()
        if ans != "":
            "Invalid selection..."


def edit_profile_options():     # edit profile lead control
    ans = True
    while ans:
        print """
                1.Edit profile options
                2.Back
                """
        ans = raw_input("Select an option : ")
        if ans == "1":
            edit_profile()
        if ans == "2":
            chat()
        if ans != "":
            print "invalid selection ...."


def chat():     # chat options and main interface maneuver from main()
    ans = True
    while ans:
        print """
            1.Send a message
            2.View messages
            3.View profile
            4.Edit Profile
            5.Set status
            6.view friend(s)
            7.Exit
            """
        ans = raw_input("What would you like to do? ")
        if ans == "1":
            print "Send message control line > "
            ans = False
            send_message_validation()

        elif ans == "2":
            print "Messages options : > "
            ans = False
            view_message_options()

        elif ans == "3":
            print "View profile control line >"
            ans = False
            view_profile_fancy()

        elif ans == "4":
            print "Edit profile control line >"
            ans = False
            edit_profile()

        elif ans == "5":
            print "Set status control line >"
            ans = False
            edit_status()

        elif ans == "6":
            print "View friend control line >"
            ans = False
            view_friends()

        elif ans == "7":
            print "Exiting"
            print "Destroying data and clearing cache..."
            while len(current_username) > 0:
                current_username.pop()
            exit()

        elif ans != "":
            print "Not Valid Choice Try again"


def existing():     # credential check for existing users
    spy_username = raw_input("Enter your username : ")
    spy_pass = raw_input("Enter password : ")
    if spy_username in spy_credentials['username']:
        x = spy_credentials['username'].index(spy_username)
        print x
        if spy_pass == spy_credentials['password'][x]:
            print "Welcome " + spy_username
            current_username.append(spy_username)
            print "Current user added to session is > "
            print current_username[0]
            chat()
        else:
            print "Incorrect password... Exiting!"


def password():     # password validator
    new_password = raw_input("Enter a password for your account ( 6 char min) : ")
    if len(new_password) < 6:
        print "password too short, try again..."
        password()
    else:
        print "password saved !"
        spy_credentials['password'].append(new_password)
        spy_credentials['name'].append("")
        spy_credentials['spy salutation'].append("")
        spy_credentials['spy status'].append("")
        spy_credentials['spy rating'].append("")
        print "redirecting you to main page, login as existing user."
        main()


def new_user():     # add new user controls
    new_username = str(raw_input("Enter a username for yourself (make it unique) : "))
    if new_username in spy_credentials['username']:
        print "username already exists.... try again "
        new_user()
    else:
        print "Adding username...."
        spy_credentials['username'].append(new_username)
        password()


def main():     # the home of it all
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
