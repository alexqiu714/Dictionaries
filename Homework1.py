error = {"100" : "Continue", "101" : "Switching Protcols", "102" : "Processing"}
x = int(input("Enter error code"))
if x in error:
    print(error[x])
else:
    print("Sorry, error code is not valid")