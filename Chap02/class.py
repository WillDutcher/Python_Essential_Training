#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class Duck:
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

    def balk(self):
        print('Ducks don\'t play baseball.')

class Dog:
    sound = 'Woof!'
    walking = 'Trots like a dog.'
    activities = 'Sleeping like a dog.'

    def woof(self):
        print(self.sound)

    def walk(self):
        print(self.walking)

    def activity(self):
        print(self.activities)

def main():
    donald = Duck()
    donald.quack()
    donald.walk()
    donald.balk()
    busy = Dog()
    busy.woof()
    busy.walk()
    busy.activity()

if __name__ == '__main__': main()
