name = input("Enter your name: ")


count = 0
for i in name:
    if i == "a" or i == "e" or i =="i" or i == "o" or i =="u":
        count = count + 1


print("The number of your vowels is", count)