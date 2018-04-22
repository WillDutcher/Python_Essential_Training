#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# OVERVIEW

x = 7
print('x is {}'.format(x))
print(type(x))

x = 7.0
print('x is {}'.format(x))
print(type(x))

x = '7.0'
print('x is {}'.format(x))
print(type(x))

x = True
print('x is {}'.format(x))
print(type(x))

x = None
print('x is {}'.format(x))
print(type(x))

x = [1,2,3]
print('x is {}'.format(x))
print(type(x))

x = (1,2,3)
print('x is {}'.format(x))
print(type(x))

x = {"A":1,"B":2,"C":3}
print('x is {}'.format(x))
print(type(x))

print("*"*100)

# THE STRING TYPE

a = 8
b = 9
c = f'seven {a} {b}'
print("c = ", c)
x = 'seven {1} {0}'.format('first option', 'second option')
z = 'seven "{1:<9}" "{0:>9}"'.format(10,3)
zz = 'seven "{1:<09}" "{0:>09}"'.format(145680,3)
y = 'seven'.upper()
print('x is {}'.format(x))
print('y is {}'.format(y))
print('z is {}'.format(z))
print('zz is {}'.format(zz))
print(type(x))
print(type(y))

print("*"*100)

# NUMERIC TYPES

x = 7 * 3.14159
y = 7 / 3
z = 7 // 3

print('x is {}'.format(x))
print(type(x))
print(type(y))
print(type(z))

a = .1 + .1 + .1 - .3 # Returns bad number
print(a)
# DO NOT USE FLOATING POINT NUMBERS WITH MONEY!
# DO THIS INSTEAD!
from decimal import *
b = Decimal('.10')
c = Decimal('.30')
d = b + b + b - c
print(d)

print("*"*100)

# THE BOOL TYPE

x = True
y = 7 < 5
z = None # None, zero, and empty string values evaluate to False; all else is true
print('x is {}'.format(x))
print('y is {}'.format(y))
print('z is {}'.format(z))
print(type(x))

if z:
    print("True")
else:
    print("False")

print("*"*100)
