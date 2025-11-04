passwords = {"alex123" : "alex234", "alex345" : "alex456", "alex567" : "alex678"}
x = input("What is your user?")
if x in passwords:
    y = input("What is your password?")
    if y == passwords[x]:
        print("Access granted")
    else:
        print("Access denied")
else:
    print("Sorry, user is not valid")