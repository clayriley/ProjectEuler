#!/usr/bin/python
'''
an implementation of the Project Euler problem 85, "Counting rectangles":

"By counting carefully it can be seen that a rectangular grid measuring 3 by 2 
contains eighteen rectangles.

Although there exists no rectangular grid that contains exactly two million 
rectangles, find the area of the grid with the nearest solution."
'''

def subRectangles(length, width):
    '''
    returns the number of rectangles with integer dimensions that the rectangle 
    of the given dimensions consists of.

    Each dimension D produces (sum of integers from 1 to D) subrectangles for each unit of the other dimension.
    The sum of the first n natural numbers excluding 0 = n*(n+1)/2.
    So, L x W = (L*(L+1)/2) x (W*(W+1)/2) = (L*W*(L+1)*(W+1))/4 
    '''
    pass

def main():
    pass

if __name__ == '__main__':
    main()

