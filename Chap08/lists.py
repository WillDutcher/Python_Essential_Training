#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    game = [ 'Rock', 'Paper', 'Scissors', 'Lizard', 'Spock' ]
    print(game[2:4]) # Prints items 3 and 4 in the list, above
    print(game[0:5:2])
    i = game.index('Paper')
    print(game[i])
    game.append('Computer')
    game.insert(0,'Corn')
    print_list(game)
    game.remove('Corn')
    x = game.pop() # Remove end item
    print(x)
    y = game.pop(0)
    print(y)
    del game[0:2]
    print(game)
    print(', '.join(game))
    game.append('New One A')
    game.append('New One B')
    game.append('New One C')
    print(game)
    print(len(game))


def print_list(o):
    for i in o: print(i, end=' ', flush=True)
    print()

if __name__ == '__main__': main()
