#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):
    y = []
    for x in range(1, len(p) + 1):
        index_x = p.index(x) + 1
        index_y = p.index(index_x) + 1
        y.append(index_y)
    return y

if __name__ == '__main__':
    scr_dir = os.path.dirname(__file__)
    
    fptr = open(os.path.join(scr_dir, './output.txt'), 'w')
    '''
    3
    2 3 1
    '''
    n = 5 # int(input())

    p = list(map(int, '5 2 1 3 4'.rstrip().split()))

    result = permutationEquation(p)
    
    print('\n'.join(map(str, result)))
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
