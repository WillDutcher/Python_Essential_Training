#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import sys
import os
import random
import datetime

def main():
    v = sys.version_info
    x = sys.platform
    y = os.name
    z = os.getenv('PATH')
    a = os.getcwd()
    b = os.urandom(25) # Random number 25 bytes long
    bb = os.urandom(25).hex() # Random number 25 bytes long
    c = random.randint(1, 1000)
    d = list(range(25))
    now = datetime.datetime.now()
    print('Python version {}.{}.{}'.format(*v))
    print(x)
    print(y)
    print(z)
    print('\n', a)
    print(b)
    print(bb)
    print(c)
    print('d: {}'.format(d))
    random.shuffle(d)
    print(d)
    print(now)
    print(now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond)


if __name__ == '__main__': main()
