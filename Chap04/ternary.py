#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

count = 0
hungry = True
x = 'Feed the bear now!' if hungry else 'Do not feed the bear.'
print(x)

while count < 5:
    hungry = True
    if hungry == False:
        print("You've fed the bear enough. It is full.")
    elif count == 4:
        print("You've fed the bear enough. It is full.")
    else:
        print("You're feeding the bear.")
    count += 1
