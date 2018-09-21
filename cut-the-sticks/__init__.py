#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    lenths = []
    while len(arr) > 0:
        shortest = min(arr)
        print(shortest)
        lenths.append(len(arr))
        i = 0
        while i < len(arr):
            arr[i] = arr[i] - shortest
            i += 1
        
        arr[:] = (x for x in arr if x != 0)
        
        # i = 0
        # while i < len(arr):
        #     if arr[i] <= 0:
        #         arr.pop(i)
        
        print(arr)
        print()
    
    return lenths

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
