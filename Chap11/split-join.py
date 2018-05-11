#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

s = 'This is a long string with a bunch of words in it.'
print(s)
print(s.split()) # Split; each element in string is now a word
print(s.split('i')) # Split on letter 'i'
l = s.split()
s2 = ':'.join(l)
print(s2)
s3 = ''.join(l)
print(s3)
