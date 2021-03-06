#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    kitten()
    y = kitten()
    print("KJ")
    print(y)
    puppy(3)

def kitten():
    print('Meow.')
    return 'Return statement is: meow'

def puppy(x):
    print(f'A puppy says \'arf\'. Also, the paramter I passed was a {x}.')

# If only one line function, can all exist on same line seperated by colon
# Below means if this module is running as the main unit of execution, call main()
# i.e. if another module used import statement to bring in this module, below = False then
# But since it is being run by typing 'python function.py' it will run as __main__
if __name__ == '__main__': main()
print("*"*100,"\n")

def main():
    x = 10
    dog(x)
    print(f'in main: x is {x}')
    kitten(5, 6, 7)
    dog(5)

def kitten(a, b, c, d = 'potato'):
    print("Meow.")
    print(a, b, c, d)

def dog(x):
    x = 3
    print('Arf.')
    print(x)

if __name__ == '__main__': main()
print("*"*100,"\n")

def main():
    x = kitten()
    print(type(x), x)

def kitten():
    print('Meow.')
    y = dict(a = 1, b = 2, c = 3)
    return y, [43,2,54]


if __name__ == '__main__': main()
