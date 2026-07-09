# Q Keep asking user to guess a number (1-10) until they get it right
import random

guessing_no = random.randint(1,10)

while True:
    i = int(input("enter no. between 1-10:"))

    if(i == guessing_no):
        print("correct")
        break
    else:
        print("wrong ,try again!")