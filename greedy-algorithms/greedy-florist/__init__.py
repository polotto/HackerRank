#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    c_len = len(c)
    total = sum(c)
    if k >= c_len:
        return total
    
    c_s = sorted(c, reverse=True)
    total = sum(c_s[:k])
    c_diff = c_s[k:]
    i = 1
    j = 1
    for c_i in c_diff:
        total += c_i * (1 + i)
        if j < k:
            j += 1
        else:
            i += 1
            j = 1
    
    return total
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
