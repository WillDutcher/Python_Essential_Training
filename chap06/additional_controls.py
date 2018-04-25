#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

print("There are three additional controls:")
print("\t-Continue\t[Short-cut a loop and start it again]")
print("\t-Break\t\t[Break out of a loop prematurely]")
print("\t-Else\t\t[Executes only if loop ends normally or an if condition is not met]")
print('*'*100,'\n')

secret = 'swordfish'
pw = ''
auth = False
count = 0
max_attempt = 5

while pw != secret:
    count += 1
    if count > max_attempt: break
    if count == 3: continue
    pw = input(f'{count}: What\'s the secret word? ')
else:
    auth = True

print("\nAuthorized" if auth else "Calling the FBI...")
print('*'*100,'\n')

animals = ('bear', 'bunny', 'dog', 'cat', 'velociraptor')
for pet in animals:
    if pet == 'dog': continue
    if pet == 'velociraptor': break
    print(pet)
else:
    print('That is all of the animals.')
