#!/usr/bin/python
'''
An implementation of Project Euler problem 22, Names Scores.

"Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?"
'''

import argparse



def main():

    filename = 'names.txt'

    ap = argparse.ArgumentParser()
    ap.add_argument('filename', nargs='?', default=filename)
    args = ap.parse_args()

    total = None
    
    print('Total for all scores:', total)


if __name__ == '__main__':
    main()



