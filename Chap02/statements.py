#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import platform

new = "\nLook, I added something else to this!"
version = platform.python_version()

def myFunc():
    global new
    print(new)

print('This is python version {}'.format(version))
myFunc()
