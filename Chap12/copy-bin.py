#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    infile = open('berlin.jpg', 'rb') # Would get error if try 'rt' as this is binary and not text file
    outfile = open('berlin-copy.jpg', 'wb')
    while True:
        buf = infile.read(10240) # reading in 10k byte chunks; not wise to read entire file at once
        if buf:
            outfile.write(buf)
            print('.', end='', flush=True)
        else: break
    outfile.close()
    print('\ndone.')

if __name__ == '__main__': main()
