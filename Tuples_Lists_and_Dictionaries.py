#NOTES
# 
# Once a tuple is defined you cannot change what is stored in it.

#The contents of a list can be changed while the program is 
# running and lists are one of the most common ways to store a
# collection of data under one variable name in Python.


#The contents of a dictionary can also be changed while the program is running.

#EXAMPLE CODE

fruit_tuple = ("apple", "banana", "strawberry", "orange")

print(fruit_tuple.index("strawberry"))

print(fruit_tuple[2])

names_list = ["John", "Tim", "Sam"]

del names_list[1]

names_list.append(input("Add a name: "))

print(names_list)

names_list.append(input("Enter another name: "))

print("Names in alphabetical order:", sorted(names_list))

