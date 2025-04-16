import random

def menu():
    ans = int(input("1) Addition \n2) Subtraction \nEnter 1 or 2:"))

    if ans == 1:
        one()
    if ans == 2:
        two()

def one():
    num_1 = random.randint(5,20)
    num_2 = random.randint(5,20)
    add_ans = int(input("What is", num_1,"+",num_2,"?: "))
    correct_add_ans =num_1+num_2
    addition_data_tuple = (add_ans, correct_add_ans)
    return addition_data_tuple

def two():
    num1 = random.randint(25,50)
    num2 = random.randint(1,25)

    sub_ans = int(input("What is",num1,"-",num2,"?: "))
    correct_sub_ans = num1-num2

    subtraction_data_tuple = (sub_ans, correct_sub_ans)
    return subtraction_data_tuple

def check():
    
