#5. Guess the Number
#Write a program that asks the user to guess a number between 1 and 10 and tells them if they are correct or not.

import random

gn = int(input("Guess a number between 1 and 10 : "))

rn = random.randint(1, 10)

if(gn == rn) :
    print("Win!")
else :
    print("Lose!")