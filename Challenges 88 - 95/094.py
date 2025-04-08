from array import *

nums = ('i', [12,13,14,15,11])

select = int(input("Enter one of the numbers: "))

if select in nums:
    print(nums.index(select))
else:
    test = False
    while test == False:
        print("not in array.")
        select = int(input("Enter one of the numbers: "))
        if select in nums:
            print(nums.index(select))
            test = True
