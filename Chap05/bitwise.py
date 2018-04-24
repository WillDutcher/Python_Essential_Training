#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# Completed Chap05: Lesson 21 - Bitwise operators

x = 0x0a
y = 0x02
z = x & y

# 02x gives two-character string, hexadecimal, with leading zero
# 0 = leading zero
# 2 = two characters wide
# x = hexadecimal display of integer value
# 08b gives eight-character string, binary, with leading zeroes
# 0 = leading zeroes, where applicable
# 8 = 8 characters wide
# b = binary display of integer value
print(f'(hex) x is {x:02x}, y is {y:02x}, z is {z:02x}')
print(f'(bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')

print("&\tAnd")
print("|\tOr")
print("^\tXor")
print("<<\tShift left")
print(">>\tShift right")
