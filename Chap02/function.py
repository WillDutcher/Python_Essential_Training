#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def function(n):
    print(n)
    return n * 2

function(47)

def newFunc(*args): # Pass a non-static number of variables
    print(*args)

newFunc(1, 2, 3, 'potato')

x = function(42)
print(x)
