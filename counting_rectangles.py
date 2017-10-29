#!/usr/bin/python
'''
an implementation of the Project Euler problem 85, "Counting rectangles":

"By counting carefully it can be seen that a rectangular grid measuring 3 by 2 
contains eighteen rectangles.

Although there exists no rectangular grid that contains exactly two million 
rectangles, find the area of the grid with the nearest solution."
'''

import math
import argparse

def subRectangles(length, width):
    '''
    returns the number of rectangles with integer dimensions that the rectangle 
    of the given dimensions consists of.

    Each dimension D produces (sum of integers from 1 to D) subrectangles for each unit of the other dimension.
    The sum of the first n natural numbers excluding 0 = n*(n+1)/2.
    So, L x W = (L*(L+1)/2) x (W*(W+1)/2) = (L*W*(L+1)*(W+1))/4.
    '''
    return (length*width*(length+1)*(width+1))/4

def getLargestDimension(goal):
    '''
    returns the least integer that when treated as a rectangular dimension 
    with 1, yields at least the goal number of rectangles.  This is the largest
    possible dimension of the rectangle whose area solves this problem.

    (x*y*(x+1)*(y+1))/4 
    = (x*1*(x+1)*(1+1))/4 
    = (x*(x+1)*(2))/4 
    = (x*(x+1))/2

    Checks via brute force, starting at the square root of the goal.
    '''
    current = int(math.sqrt(goal))
    while subRectangleS(current, 1) < goal:
        current += 1
    return current

def search(goal):
    '''
    given the goal, finds the rectangular area of the dimensions resulting in 
    the number of subrectangles nearest to goal.
    
    By starting with the largest possible difference between the two dimensions
    L and W, the goal can be approached by decrementing L or by incrementing W.
    This descends the gradient toward the goal by bringing the number of LxW's 
    subrectangles in its direction, whether it has been "skipped over" or not.
    
    Because incrementing and decrementing the dimensions affects the count of
    subrectangles differently, checks must continue until a square rectangle 
    is reached, and each new best area must be stored.
    '''
    L = getLargestDimension(args.goal)
    W = 1
    nearest_distance = float('inf')
    area = L*W
    while True:
        subs = subRectangles(L, W)
        distance = math.abs(subs - goal) 
        if distance < nearest_distance:  # then update best area
            area = L*W
            nearest_distance = distance
        # stop right here if goal has been struck
        # decrement larger dimension if goal is still below
        if goal < 
        # increment smaller dimension if goal is now above
    if L < W:  # once L < W, we've crossed the square and are repeating work!
        break
    return area
    

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('goal', type='int', nargs='?', default=2000000)
    args = ap.parse_args()

if __name__ == '__main__':
    main()

