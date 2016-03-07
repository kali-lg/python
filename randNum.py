#!/usr/bin/python

import random

num = random.randint(0, 100)

while True:
    try:
    	guess = int(raw_input("Please Enter number 1~100:\n"))
    except ValueError, e:
        print "Please Enter correct number, your number is wrong type."
        continue

    if guess > num:
        print "Guess Bigger:", guess
    elif guess < num:
        print "Gusee Smaller:", guess
    else:
        print "Guess OK, Game Over:"
        break
    print "\n"
