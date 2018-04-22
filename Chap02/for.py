#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

words = ['one', 'two', 'three', 'four', 'five']

j = 0
for i in words:
    if j == 0:
        print('The first word is ', i)
    elif j == 4:
        print('The last word is ', i)
    else:
        print('The next word is ', i)
    j += 1
