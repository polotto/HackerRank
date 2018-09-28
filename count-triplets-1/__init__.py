#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    gp_hash = {}
    arr_max = max(arr)
    i = 0
    pg = min(arr)
    while pg < arr_max:
        pg = r * pg
        gp_hash[pg] = i
        i += 1
    for j in range(len(arr)):
        



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
