#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# simple fibonacci series
# the sum of two elements defines the next set

a, b = 0, 1
while b < 1000:
    print(b, end = ' ', flush = True)
    a, b = b, a + b

print('\n') # line ending

x, y = 0, 1
while y < 11000:
    print(y, end = ' ', flush = True)
    x, y = y, x + y
