#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the palindromeIndex function below.
def palindromeIndex(s):
    N = len(s)
    N_i = N - 1
    s_i = s[::-1]
    if s == s_i:
        return -1
    
    for i in range(N):
        test = s[:i] + s[i+1:]
        test_i = s_i[:N_i-i] + s_i[N_i-i+1:]
        if test == test_i:
            return i
        
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
