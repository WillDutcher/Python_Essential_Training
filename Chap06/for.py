#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

animals = ( 'bear', 'bunny', 'dog', 'cat', 'velociraptor' )

for pet in animals:
    print(pet)

x = len(animals)
print("That's all of them. There are", len(animals), "pets.")
print(f'That\'s all {x} pets.')
print("To repeat, we've named a total of {} pets.".format(len(animals)))
