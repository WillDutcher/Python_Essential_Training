#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

if True:
    print('if true')
elif False:
    print('elif true')
else:
    print('neither true')

print("*"*50)

x = 3

if x == 0:
    print("zero is true")
elif x == 1:
    print("one is true")
elif x == 2:
    print("two is true")
elif x == 3:
    print("three is true")
elif x == 4:
    print("four is true")
else:
    print("none is true")

# Comparison Operators
print("Comparison Operators")
print("-"*20)
print("==\ta == b\tEqual")
print("!=\ta != b\tNot Equal")
print("<\ta < b\tLess than")
print(">\ta > b\tGreater than")
print("<=\ta <= b\tLess than or equal to")
print(">=\ta >= b\tGreater than or equal to")
print("and\tx and y\tTrue if both x and y")
print("or\tx or y\tTrue if x or y")
print("not\tnot x\tInvert state\n")
print("x is y\t\tTrue if the same object")
print("x is not y\tTrue if not the same object")
print("x is y\t\tTrue if x member of collection y")
print("x is not y\tTrue if x not member of collection y")
