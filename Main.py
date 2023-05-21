UserDB = {
    "User1": "Login",
    "User2": 'Suepr',
    '1': '1',
    '3': '3',
    'admin': 'admin'
}
attemptsJust = 0
while attemptsJust <3:
    UserQ = input("What is your username?")
    try:
        if UserDB[UserQ]:
            Passis = UserDB[UserQ]
            question = input("Whats your pass?")
            if Passis == question:
                print("Succesfull logged in.")
                break
            else:
                print("Login Failed, Try again")
                attemptsJust= attemptsJust+1
    except:
         print("User has not been found,please try again")
    
