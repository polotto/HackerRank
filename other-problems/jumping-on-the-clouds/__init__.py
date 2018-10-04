#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    n = len(c)
    jumps = []
    e = 100
    i = 0
    # while don't reach the array size n
    while i <= n-1:
        # jumps calc
        j = (i+k)%n
        # to limit the loop
        i = i+k
        # add to the list of jumps
        jumps.append(j)
    print(jumps)
    # jumps throught the clouds and calc the energy
    for jump in jumps:
        if c[jump] == 1:
            e = e - 1 - 2
        else:
            e = e - 1    
    return e

if __name__ == '__main__':
    d_path = os.path.dirname(__file__)
    fptr = open(os.path.join(d_path,'./output.txt'), 'w')

    nk = '8 2'.split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, '0 0 1 0 0 1 1 0'.rstrip().split()))

    result = jumpingOnClouds(c, k)
    print(result)
    fptr.write(str(result) + '\n')

    fptr.close()
