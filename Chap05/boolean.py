#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# Completed Chap05: Lesson 23 - Comparison operators

print("\nand\t\tAnd")
print("or\t\tOr")
print("not\t\tNot")
print("in\t\tValue in set")
print("not in\t\tValue not in set")
print("is\t\tSame object identity")
print("is not\t\tNot same object identity\n")
print("*"*50,"\n")

a = True
b = False
x = ( 'bear', 'bunny', 'tree', 'sky', 'rain' )
y = 'tree'

if a and b:
    print('expression is true')
else:
    print('expression is false')

if y in x:
    print("Yep, it is.")
else:
    print("Nope, it's not.")

if y is x[0]:
    print("Yes, that's the same.")
else:
    print("No, they're different.")
