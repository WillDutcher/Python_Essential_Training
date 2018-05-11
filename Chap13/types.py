#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# Numeric Functions
x = '47'
y = int(x)
z = float(x)
zz = abs(y) # Needs to be y, lest I change to 'abs(int(x))'
zzz = divmod(y, 3) # Same as above, re: y vice x
zzzz = complex(y, 72)

print(f'x is {type(x)}')
print(f'x is {x}')
print(f'y is {type(y)}')
print(f'y is {y}')
print(f'z is {type(z)}')
print(f'z is {z}')
print(f'zz is {type(zz)}')
print(f'zz is {zz}')
print(f'zzz is {type(zzz)}')
print(f'zzz is {zzz}')
print(f'zzzz is {type(zzzz)}')
print(f'zzzz is {zzzz}')

# String Functions
print('\n')
s = 'Hello, World.'
print(repr(s)) # repr = representation; raw string, itself

class bunny:
    # The way this works:
        # Prints the __str__ version if you do print(s), otherwise
        # Will print __repr__ version, if print(repr(s)), otherwise
        # Will print memory address of the object
    def __init__(self, n):
        self._n = n
    def __repr__(self):
        return f'repr: The number of bunnies is {self._n}'
    def __str__(self):
        return f'str: The number of bunnies is {self._n}'

s = bunny(47)
print(repr(s)) # Prints the bunny object memory address, *UNLESS* repr method defined (__repr__)
print(s) # Same as if I'd put print(str(s))
print(ascii(s)) # Works just like repr, but will escape special characters for unicode emojis (as example)
# print(chr(128406)) # Live long and prosper emoji hand; won't display in cygwin
# ord = number of a character (emoji) whereas chr gives you character (emoji) of a number

# Container Functions
print('\n')


# Object and Class Functions
print('\n')
