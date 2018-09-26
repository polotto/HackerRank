#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    position = 0
    jumps = 0
    
    while position < len(c) - 1:
        print(position)
        jumps += 1
        if position + 2 < len(c) and c[position+2] == 0:
            position += 2
        else:
            position += 1
    
    return jumps
            

if __name__ == '__main__':
    scr_dir = os.path.dirname(__file__)
    fptr = open(os.path.join(scr_dir, './output.txt'), 'w')
    fptr_input = open(os.path.join(scr_dir, './input00.txt'))

    n = int(fptr_input.readline())

    c = list(map(int, fptr_input.readline().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()

    print(result)
