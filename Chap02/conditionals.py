#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = 12
y = 42

if x < y:
    print('x < y: x is {} and y is {}'.format(x, y))

# Above is same as this:
print("Another way: On one line\n")
print('if x < y: print(\'x < y: x is {} and y is {}\'.format.(x, y))')
if x < y: print('x < y: x is {} and y is {}'.format(x, y)) # Frowned upon to do it this way

print('\n' + '*'*50 + '\n')

if x > y:
    print('x > y: x is {} and y is {}'.format(x, y))
elif x < y:
    print('x < y: x is {} and y is {}'.format(x, y))
elif x == y:
    print('x == y: x is {} and y is {}'.format(x, y))
else:
    print('Do something else.')
