#!/usr/bin/python
'''
An implementation of Project Euler problem 22, Names Scores.

"Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?"
'''

import argparse

def scoreName(name, weight=1):
    '''
    produces a score for a name, weighted by a given value.
    '''
    char_scores = dict(zip('abcdefghijklmnopqrstuvwxyz', range(1, 27)))  
    return weight * sum(map(char_scores.get, name.lower()))
  

def readNames(filename):
    '''
    Reads names from the Project Euler file "names.txt" format.
    Returns a list of names.
    '''
    with open(filename, 'r') as f:
        names = f.read().split(',')
    # map object can be sorted, but has no len()!
    return list(map(lambda x: x.strip('"'), names))


def weightNames(names):
    '''
    Sorts names alphanumerically and returns a dictionary that maps them to a 
    weight according to their sorted position.
    
    Does not ignore case!
    '''
    return dict(zip(sorted(names),  # hybrid of merge sort and insertion sort 
                    range(1, len(names)+1)))


def main():

    filename = 'names.txt'

    ap = argparse.ArgumentParser()
    ap.add_argument('filename', nargs='?', default=filename)
    args = ap.parse_args()

    weights = weightNames(readNames(args.filename))
    total = sum([scoreName(name, weight) for name, weight in weights.items()])
    
    print('Total for all scores:', total)


if __name__ == '__main__':
    main()



