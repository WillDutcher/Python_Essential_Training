#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = 42
y = 73

if x < y:
    z = 112
    print('x < y: x is {} and y is {}'.format(x, y))
    print('line 2') # Only prints if 'if' statement is true
    print('line 3') # Only prints if 'if' statement is true
    print('line 4') # Only prints if 'if' statement is true
print('line 5') # Prints automatically because it's not part of block, above, now

print('Something else.')
print('z is equal to: {}'.format(z))
