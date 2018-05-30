import random

def scores(num):
    if num <= 60:
        print("Your grade is D")
    if num >= 70 and num <= 79:
        print("Your grade is C")
    if num >= 80 and num <= 89:
        print("Your grade is B")
    if num >= 90 and num <= 100:
        print("Your grade is A")

scores(random.random())
