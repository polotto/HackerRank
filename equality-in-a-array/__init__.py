#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):
    arr_hash = {}
    max_hash =[0, 0]
    for i in arr:
        if not i in arr_hash:
            arr_hash[i] = 1
        else:
            arr_hash[i] += 1
        if arr_hash[i] > max_hash[1]:
            max_hash = [i, arr_hash[i]]
    
    ans = len(arr) - max_hash[1]
    
    return ans    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
