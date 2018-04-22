#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = [ 1, 2, 3, 4, 5 ]
x[2] = 42 # Changes third item in list from 3 to 42
# x = (1, 2, 3, 4, 5)
# x[2] = 42 # This will not work because it's a tuple; tuple values can't be changed
for i in x:
    print('i is {}'.format(i))

x = range(5, 51, 5)
# x[2] = 42 # THIS WILL NOT WORK BECAUSE RANGE IS A TUPLE!
    # Specify one number, iterates up to, but NOT INCLUDING, that number (i.e. range 3 = 0, 1, 2)
    # Specify two numbers, iterates from first up to, but NOT INCLUDING, second number (i.e. range(1,4) = 1, 2, 3)
    # Specify three numbers, iterates from and to and steps by that amount, i.e. (range(1,10,3) = 1, 4, 7)
for i in x:
    print('i is {}'.format(i))

print("*"*50)

x = list(range(1,101,10))
x[3] = "Apples"
for i in x:
    print('i is {}'.format(i))

x = { 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
x['three'] = "Pineapples"
for k, v in x.items():
    print('k: {}, v: {}'.format(k, v))
