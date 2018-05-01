#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import sys

def main():
    try:
        x = a5/2
    except ValueError:
        print("I caught a ValueError.")
    except ZeroDivisionError:
        print('Don\'t divide by zero!')
    except:
        print(f'Unknown error: {sys.exc_info()[1]}')
    else:
        print("No errors found.")
        print(x)

if __name__ == '__main__': main()
