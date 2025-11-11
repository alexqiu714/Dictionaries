vowels = {"a" : 0, "e" : 0, "i" : 0, "o" : 0, "u" : 0}
x = input("Enter a word")
for i in x:
    if i in vowels:
        vowels[i] += 1
        print(vowels)