print("Welcome to Sam's Login Page")
usernames = ['sam']
passwords = ['sam']

while True:
    response = input("Would you like to Login or Register? [l/r]\nType here: ")

    if response.lower() == "l":
        while True:
            username = input("Enter your username: ")
            if username not in usernames:
                print("That isn't a registered username, please try again")
            else:
                print("sweet, let's get started " + str(username))
                break

        while True:
            password = input("Enter your password: ")
            if password not in passwords:
                print('Incorrect password, please try again')
            else:
                print("You are now logged in")
                break

        while True:
            action = input("Type 'exit' to return to main menu  ")
            if action == "exit":
                print("You are now logged out")
                break
            else:
                print("Still here ")


    elif response.lower() == "r":
        while True:
            newname = input("Please make a USERNAME with ONLY letters and numbers: ")
            if newname.isalnum():
                break
        usernames.append(newname)

        while True:
            newpass = input("Please make a PASSWORD with ONLY letters and numbers: ")
            if newpass.isalnum():
                break
        passwords.append(newpass)

        print("Registration successful! You are now logged in.")
        print(usernames)

        while True:
            mesreg = input("Type 'exit' to return to main menu  ")
            if mesreg == "exit":
                print("You are now logged out")
                print(usernames)
                break
            else:
                print("Still here")

    else:
        print("sorry I didn't understand that")

