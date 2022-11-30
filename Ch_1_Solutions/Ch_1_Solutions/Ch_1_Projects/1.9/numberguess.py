"""
Program: numberguess.py
Project 1.9

The computer guesses the user's number using the minimum
number of attempts and prevents cheating by the user.
"""

import math

low = int(input("Enter the smaller number: "))
high = int(input("Enter the larger number: "))
count = 0
maxGuesses = round(math.log(high - low + 1, 2))
while True:
    count += 1
    yourNumber = (low + high) // 2
    print("Your number is", yourNumber)
    answer = input("Enter =, <, or >: ")
    if answer == "=":
        print("Hooray, I've got it in", count, "tries!")
        break
    elif count == maxGuesses:
        print("You're cheating!")
        break
    elif answer == "<":
        high = yourNumber - 1
    else:
        low = yourNumber + 1
