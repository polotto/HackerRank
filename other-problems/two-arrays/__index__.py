#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the twoArrays function below.
def twoArrays(k, A, B):
    N = len(A)
    
    a_sum = sum(A)
    b_sum = sum(B)
    k_sum = k*N
    
    if a_sum > k_sum * b_sum or b_sum > k_sum * a_sum:
        return 'NO'
    
    if a_sum + b_sum >= k_sum:
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        A = list(map(int, input().rstrip().split()))

        B = list(map(int, input().rstrip().split()))

        result = twoArrays(k, A, B)

        fptr.write(result + '\n')

    fptr.close()
