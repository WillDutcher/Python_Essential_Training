#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

words = ['one', 'two', 'three', 'four', 'five']

n = 0
while(n < 5):
    print(words[n])
    n += 1

moreWords = ["ten", "nine", "eight", "seven", "six", "five", "four", "three", "two", "one", "zero"]
x = 10
while(x < 11):
    print('x = ', moreWords[x])
    x -= 1
    if x == 0:
        break

ageList = [37, 38, 39, 40, 41, 42]
age = 36
year = 2015
while age < 44:
    if year > 2018:
        print("In the year", year, "\b, I will be", age, "years old.")
    else:
        print("In the year", year, "\b, I was", age, "years old.")
    age +=1
    year += 1
