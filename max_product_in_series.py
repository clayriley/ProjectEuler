#!/usr/bin/python
'''
"The four adjacent digits in the 1000-digit number that have the greatest 
product are 9 × 9 × 8 × 9 = 5832.

[...]

Find the thirteen adjacent digits in the 1000-digit number that have the 
greatest product. What is the value of this product?"
'''

sequence = '73167176531330624919225119674426574742355349194934\
            96983520312774506326239578318016984801869478851843\
            85861560789112949495459501737958331952853208805511\
            12540698747158523863050715693290963295227443043557\
            66896648950445244523161731856403098711121722383113\
            62229893423380308135336276614282806444486645238749\
            30358907296290491560440772390713810515859307960866\
            70172427121883998797908792274921901699720888093776\
            65727333001053367881220235421809751254540594752243\
            52584907711670556013604839586446706324415722155397\
            53697817977846174064955149290862569321978468622482\
            83972241375657056057490261407972968652414535100474\
            82166370484403199890008895243450658541227588666881\
            16427171479924442928230863465674813919123162824586\
            17866458359124566529476545682848912883142607690042\
            24219022671055626321111109370544217506941658960408\
            07198403850962455444362981230987879927244284909188\
            84580156166097919133875499200524063689912560717606\
            05886116467109405077541002256983155200055935729725\
            71636269561882670428252483600823257530420752963450'

def findMaxA(sequence, window, function):
    '''
    Find the maximum result of applying to the given function each digit (and 
    the previous result) within a window that is slid across the input number.
    The window is not padded, so the window is always full.  The function should 
    take two integers as input and return an integer.

    For example, with sequence=12345, window=3, function=lambda x,y: x+y; we see

    [((1 + 2) + 3) = 6]45 -> 1[((2 + 3) + 4) = 9]5 -> 12[(3 + 4) + 5) = 12]

    The maximum result of adding each element in the window places the window 
    over the subsequence [3, 4, 5].
    '''
    if type(sequence) is int:
        sequence = str(sequence)

    if len(sequence) > window:
        raise IOError('Window is larger than sequence.')

    for span in range(0, len(sequence) + 1 - window):
        current = sequence[span:span+window]
        pass


findMaxB(sequence, window, function):
    '''
    Uses list comprehension to find the maximum product within a window over an 
    integer.  This is the same as calling findMax().  It makes an additional 
    pass over the sequence in order to use the max() function, but is still O(n) 
    and may be more readable.
    
    However, here the function should take a list of integers as input and 
    return one integer.
    '''

    if type(sequence) is int:
        sequence = str(sequence)

    if len(sequence) > window:
        raise IOError('Window is larger than sequence.')

    # returns the maximum of the list created by calling function 
    # on each window after mapping its elements to integers
    return max([function(map(int, sequence[i:i+window]))
                for i in range(0, len(sequence) + 1 - window)])
    







