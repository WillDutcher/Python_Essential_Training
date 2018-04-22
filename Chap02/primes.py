#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def isprime(n):
    if n <= 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True

def list_primes():
    for y in range(101):
        if isprime(y):
            print(y, end = ' ', flush = True)

def isprime2(x):
    if x <= 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    else:
        return True

n = 5
x = int(input("Give me a number: "))
if isprime(n):
    print(f'{n} is prime')
else:
    print(f'{n} not prime')

if isprime2(x):
    print(f'{x} is prime')
else:
    print(f'{x} not prime')

list_primes()
