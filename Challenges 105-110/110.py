file = open("Names.txt", "r")
print(file.read())
file.close()

file = open("Names.txt","r")
name = input("Enter one of the names: ")
name = name + "\n"

for row in file:

    if row!= name:
        file = open("Names2.txt","a")
        newrecord = row
        file.write(newrecord)
        file.close()

file.close()