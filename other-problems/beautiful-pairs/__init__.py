#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulPairs function below.
def beautifulPairs(A, B):
    A = list(A)
    B = list(B)
    pairs = 0
    i = 0
    while i < len(A):
        aux = A[i]
        if aux in B:
            A.pop(i)
            j = B.index(aux)
            B.pop(j)
            pairs += 1
        else:
            i += 1
    
    print(len(A), len(B), pairs)
    if len(B) > 0:
        pairs += 1
    elif len(A) == len(B):
        pairs -= 1
    
    return pairs
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    A = list(map(int, input().rstrip().split()))

    B = list(map(int, input().rstrip().split()))

    result = beautifulPairs(A, B)

    fptr.write(str(result) + '\n')

    fptr.close()
