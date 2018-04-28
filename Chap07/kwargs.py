#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    kitten(Buffy = 'meow', Zilla = 'grr', Angel = 'rawr')
    dog(Rex = "woof", Spot = "ruff", Daisy = "arf")
    x = dict(Birdie = "tweet", Tweety = "tweep", Canary = "gleep")
    bird(**x)

def kitten(**kwargs):
    if len(kwargs):
        for k in kwargs:
            print('Kitten {} says {}'.format(k, kwargs[k]))
    else: print('Meow.')

def dog(**kwargs):
    print('\n')
    if len(kwargs):
        for k in kwargs:
            print("The dog named {} says {}!".format(k, kwargs[k]))
    else: print("Yip!")

def bird(**kwargs):
    print('\n')
    if len(kwargs):
        for k in kwargs:
            print("The bird named {} says {}!".format(k, kwargs[k]))
    else: print('Caw!')

if __name__ == '__main__': main()
