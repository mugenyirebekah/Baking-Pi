import random

colour = random.choice(["red", "orange", "green", "pink", "blue"])


print("Colour options: red, orange, green, pink, and blue")

print(colour)

answer = input("Pick one!: ")


if answer == colour:
    print("Well Done!")

while answer != colour:

    if answer == "red":
        print("Don't be red with anger, try again")
        

    elif answer == "orange":
        print("Orange you glad you tried?")

    elif answer == "blue":
        print("Don't be blue, try again")

    elif answer == "green":
        print("Don't be green with envy, try again")    


    elif answer == "pink":
        print("Well I'm tickled pink that you tried...but try again")    

    elif answer == "blue":
        print("Don't be blue, try again")

    answer = input("Pick one!: ")


print("Corrreeect!!")