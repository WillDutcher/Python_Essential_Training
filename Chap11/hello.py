#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

print('Hello, World.')
print('Hello, World.'.upper())
print('Hello, World.'.swapcase())
print('Hello, World.{}'.format(42 * 7))
print("""
    Hello,
    World.

    {}""".format(1+2))

class MyString(str):
    def __str__(self):
        return self[::-1]

s = MyString('Hello, World.')
print(s)

print('\n')
################################################
print('\n')

print('Hello, World.'.upper())
print('Hello, World.'.lower())
print('Hello, World.'.capitalize())
print('Hello, World.'.swapcase())
print('Hello, World.'.casefold())

s1 = "Hello, World."
s2 = s1.upper()
print(id(s1))
print(id(s2))

t1 = 'Hi'
t2 = ', how are ya?'
t3 = 'this string' ' that string'
print(t1 + t2)
print(t3)

print('\n')
################################################
print('\n')

x = 42
y = 73
print("the number is: {} {}".format(x, y))
print("the number is: {abc} {defg}".format(abc = x, defg = y))
print("the number is: {1} {0}".format(x, y))
print("the number is: {0:<5} {1:>5}".format(x, y))
z = 43 * 4234
print("The number is {:,}".format(z))
print("The number is {:,}".format(z).replace(',','.'))
print("The number is {:.3f}".format(z))
a = 42
print("the number is: {:x}".format(x)) # HEXADECIMAL
print("the number is: {:o}".format(x)) # OCTAL
print("the number is: {:b}".format(x)) # BINARY
print(f'The number is: {x}')
print(f'The number is: {x:.3f}')
