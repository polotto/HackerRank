#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the fairRations function below.
def fairRations(B):
    breads = 0
    i = 0
    while i < len(B) - 1:
        b = B[i]
        if b % 2 != 0:
            B[i] = B[i] + 1
            B[i+1] = B[i+1] + 1
            breads += 2
        i += 1
    
    for b in B:
        if b % 2 != 0:
            return 'NO'

    return breads

if __name__ == '__main__':
    scr_dir = os.path.dirname(__file__)

    fptr = open(os.path.join(scr_dir, './output.txt'), 'w')
    fptr_input = open(os.path.join(scr_dir, './input00.txt'), 'r')

    N = int(fptr_input.readline())

    B = list(map(int, fptr_input.readline().rstrip().split()))

    result = fairRations(B)

    fptr.write(str(result) + '\n')

    fptr.close()

    print(result)
