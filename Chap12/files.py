#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    f = open('lines.txt') # Default to open in read-only mode ('r')
    # w: If you open in write mode, it will empty/clear the file and start anew
    # a: If you open in append mode, it will begin writing at the end of last line
    # +: Read and write mode (ex: r+)
    # b or t: Binary or text mode (ex: r+b or r+t)
    for line in f:
        print(line.rstrip()) # This strips any whitespace and newlines for each line

if __name__ == '__main__': main()
