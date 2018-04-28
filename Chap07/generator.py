#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    for i in inclusive_range(25):
        print(i, end = ' ')
    print()

def inclusive_range(*args):
    numargs = len(args)
    start = 0
    step = 1

    # initialize parameters
    if numargs < 1:
        raise TypeError(f'expected at least 1 argument, got {numargs}')
    elif numargs == 1:
        stop = args[0]
    elif numargs == 2:
        (start, stop) = args
    elif numargs == 3:
        (start, stop, step) = args
    else: raise TypeError(f'expected at most 3 arguments, got {numargs}')

    # generator
    i = start
    while i <= stop:
        yield i # Works like a return, but for a generator
        i += step

if __name__ == '__main__': main()

def main():
    for x in my_range(10,100,10):
        print(x, end = ' ')
    print()

def my_range(*args):
    totalArgs = len(args)
    myStart = 0
    mySkip = 1

    # Initialize all parameters
    if totalArgs < 1:
        raise TypeError(f'\nI expected you to give me at least one argument. You gave me {totalArgs}')
    elif totalArgs == 1:
        myStop = args[0]
    elif totalArgs == 2:
        (myStart, myStop) = args
    elif totalArgs == 3:
        (myStart, myStop, mySkip) = args
    else: raise TypeError(f'\nI expected you to give me at most three arguments. You gave me {totalArgs}')

    # generator
    i = myStart
    while i <= myStop:
        yield i
        i += mySkip

if __name__ == '__main__': main()
