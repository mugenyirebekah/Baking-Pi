import csv
import random
score = 0
name = input("What's your name: ")

q1_num1 = random.randint(10,50)
q1_num2 = random.randint(10,50)

question1 = str(q1_num1)+ " + " + str(q1_num2) + " = "
ans1 = int(input(question1))

realans1 = q1_num1+q1_num2

if ans1 == realans1:
    score = score + 1

q2_num1 = random.randint(10,50)
q2_num2 = random.randint(10,50)

question2 = str(q2_num1) + "+" + str(q2_num2) + "="
ans2 = int(input(question2))
realans2 = q2_num1+q2_num2
if ans2 ==