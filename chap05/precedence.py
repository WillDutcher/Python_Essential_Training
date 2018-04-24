#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# Completed Chap05: Lesson 24 - Operator precedence

# Precedence order is:
print("**\n\tExponent\n")
print("+x, -x\n\tPositive, negative\n")
print("*, /, //, %\n\tMultiplication, division, remainder\n")
print("+, -\n\tAddition and subtraction\n")
print("<<, >>\n\tBitwise shifts\n")
print("&\n\tBitwise AND\n")
print("^\n\tBitwise OR\n")
print("|\n\tExponent\n")
print("in, not in, is, is not, <, <=, >, >=, !=, ==\n\tComparisons, including membership tests and identity tests\n")
print("not x\n\tBoolean NOT\n")
print("and\n\tBoolean AND\n")
print("or\n\tBoolean OR\n")

z = 2 + 4 * 5
print(z)
