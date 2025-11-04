capitals = {"UK" : "London", "Switzerland" : "Bern"}
print(capitals)
capitals["USA"] = "Washington. DC"
print(capitals)
print(capitals["Switzerland"])
if "Switzerland" in capitals:
    print("yes")
else:
    print("no")