#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# A set is like a list that does not allow duplicate elements
# Example: Below will return a result of the string,but it won't repeat letters
# Default to return unordered set
def main():
    a = set("We're gonna need a bigger boat.")
    b = set("I'm sorry, Dave. I'm afraid I can't do that.")
    print_set(a)
    print_set(sorted(a)) # Prints same as above, but sorted
    print_set(b)
    print_set(sorted(b)) # Prints same as above, but sorted
    print_set(a - b) # In set A, but NOT in set B
    print_set(b - a) # In set B, but NOT in set A
    print_set(a | b) # In set A OR B
    print_set(a & b) # In set A AND B
    print_set(a ^ b) # In set A or B but NOT both


def print_set(o):
    print('{', end = '')
    for x in o: print(x, end = '')
    print('}')

if __name__ == '__main__': main()
