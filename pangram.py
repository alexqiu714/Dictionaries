numbers = {"0" : 0, "1" : 0, "2" : 0, "3" : 0, "4" : 0, "5" : 0, "6" : 0, "7" : 0, "8" : 0, "9" : 0}
x = input("Enter a number")

for i in x:
    numbers[i] += 1
print(numbers)

pangram = True
for count in numbers.values():
    if count == 0:
        pangram = False
    
if pangram == True:
    print("The number is a pangram")

else: 
    print("It is not a pangram")