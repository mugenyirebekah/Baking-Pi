num = 10

while num>0:
    print("There are", num, "green bottles hanging on the wall.")
    print(num, "green bottles hanging on the wall.")
    print("And if 1 green bottle should accidentally fall,")

    num = num-1
    answer = int(input("How many green bottles will be hanging on the wall?"))

    if answer == num:
        print("There will be", num, "green bottles hanging on the wall.")
    else:
        while answer != num:
            answer = int(input("No, try again: "))
print("There are no more green bottles hanging on the wall.")