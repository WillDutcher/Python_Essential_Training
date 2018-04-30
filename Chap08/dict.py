#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    animals = { 'kitten': 'meow', 'puppy': 'ruff!', 'lion': 'grrr',
        'giraffe': 'I am a giraffe!', 'dragon': 'rawr' }
    # Above is same as this:
    animals2 = dict(kitten = 'meow', puppy = 'ruff', lion = 'grrr',
        giraffe = 'I am a giraffe!', dragon = 'rawr')
    animals['lion'] = 'I am a lion'
    animals['monkey'] = 'haha'
    for k, v in animals.items():
        print(f'{k}: {v}')
    print('\n')

    print('*'*25, '\n')
    for i in animals2.items(): print(i)
    print('\n')

    print('*'*25, '\n')
    for k in animals2.keys(): print(k)
    print('\n')

    print('*'*25, '\n')
    for v in animals2.values(): print(v)
    print('\nFound!\n' if 'lion' in animals else '\nNot found!\n')
    print_dict(animals)
    print('\n')
    if print(animals.get('godzilla')) == None:
        print("I didn't find it. Sorry.")
    elif print(animals.get('godzilla')) == True:
        print("You got a true.")
    else:
        print("You got a false.")


def print_dict(y):
    # for x in y: print(f'{x}: {y[x]}')
    for k, v in y.items(): print(f'Key = {k}: \t\tValue = {v}')

if __name__ == '__main__': main()
