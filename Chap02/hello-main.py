#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import platform

def main():
    message()

def message():
    print('This is python version {}'.format(platform.python_version()))
    new()

def new():
    print('\nI just wanted to have something to add. So here it is.')
    last()

def last():
    if True:
        print("This is a true statement.")
    else:
        print("This statement is a false one.")

# By having this conditional statement, below, that calls main
# it actually forces the interpreter to read the entire script
# before it executes any of the code.
if __name__ == '__main__': main()
