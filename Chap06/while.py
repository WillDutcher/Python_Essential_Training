#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

secret = 'swordfish'
pw = ''

while pw != secret:
    pw = input("What's the secret word? ")
    if pw == secret:
        print("You got it!")
    else:
        print("That's not it. Try again.\n")
