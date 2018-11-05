#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

# Complete the maximumPerimeterTriangle function below.
def maximumPerimeterTriangle(sticks):
    sticks_s = sticks
    perimeter = 0
    lengths = [-1]
    for i, j, k in combinations(range(len(sticks_s)), 3):
        s_i = sticks_s[i]
        s_j = sticks_s[j]
        s_k = sticks_s[k]
        aux_l = sorted([s_k, s_j, s_i])
        aux = sum(aux_l)
        if aux_l[0] + aux_l[1] > aux_l[2] and aux > perimeter:
            lengths = aux_l
            perimeter = aux
            
    return lengths

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
