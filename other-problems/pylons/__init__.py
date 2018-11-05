#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pylons function below.
def pylons(k, arr):
    n = len(arr)
    i, j, trans, flag, loc = 0, 0, 0, 0, 0
    while(i < n):
        trans += 1
        j = i + k - 1
        if(j > n):
            j = n - 1
        while(loc <= j < n and arr[j] == 0):
            j -= 1
        if(j < loc):
            return -1
        else:
            loc = j + 1
            j += k
            i = j
            
    if(flag == 0):      
        return trans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pylons(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
