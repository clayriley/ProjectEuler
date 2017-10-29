#!/usr/bin/python
'''
an implementation of the Project Euler problem 112, "Bouncy numbers":

"Working from left-to-right if no digit is exceeded by the digit to its left it 
is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a 
decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a 
"bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just over half 
of the numbers below one-thousand (525) are bouncy. In fact, the least number 
for which the proportion of bouncy numbers first reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the time we 
reach 21780 the proportion of bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly 
99%."
'''

def countDecreasing(digit1, digit2):
    '''
    returns the number of pairs of digits whose concatenation monotonically 
    decreases and is less than or equal to the concatenation of digit1 and 
    digit2
    '''
    
def bouncyHundreds(n):
    '''
    returns the count of a bouncy natural number less than 1000 by comparing 
    orders of magnitude using string comparison.
    
    A 3-digit number may decrease and then increase (high-low-high), or vice versa (low-high-low).

    With n's orders of magnitude as h, t, and o:
    for each possible hundreds place x that is less than or equal to h,
        and each possible tens place y that is greater than x but not greater than t,
            and each possible ones place z that is less than y and not greater than o,
                there is one low-high-low bouncy number;
        and each possible tens place y' that is less than x and not greater than t,
            and each possible ones place z' that is greater than y' but not greater than o,
                there is one high-low-high bouncy number.

    The mathematical constraints on these variables are as follows:

    x | 0 < x <= h
    y | x < y <= t
    z | 0 <= z <= o, z < y
    y' | 0 <= y' <= t, y' < x
    z' | y' < z' <= o
    '''
    if len(n) > 3:
        raise IOError('Do not call bouncyHundreds with an n greater than 999')
    elif len(n) < 3:
        return 0
    else:
        count = 0
        hundred, ten, one = int(n[0]), int(n[1]), int(n[2])
        # should be able to be framed as geometric sequence rather than loops
        for h in range(1, hundred+1):             # with each h | 0 < h <= hundred...
            for t in range(h+1, ten+1):           # ...and each t | h < t <= ten...
                for o in range(0, min(one+1, t)): # ......and each o | 0 <= o < t, o <= one
                    #print(h,t,o)
                    count += 1
            for t in range(0, min(ten+1, h)):     # ...and each t' | 0 <= t' < h, t' <= ten
                for o in range(t+1, one+1):       # ......and each o' | t' < o' <= one
                    #print('+', h,t,o)
                    count += 1
        return count
    

def countBouncy(number):
    '''
    returns number of bouncy natural numbers less than or equal to given number 
    '''
    count = 0
    order = len(str(number))
    pass


def main():
    pass

if __name__ == '__main__':
    main()

