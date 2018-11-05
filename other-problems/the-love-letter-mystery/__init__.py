#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the theLoveLetterMystery function below.
def theLoveLetterMystery(s):
    N = len(s)
    N_h = N//2
    changes = 0
    if s == s[::-1]:
        return changes
    
    for i in range(N_h):
        start = s[i]
        end = s[-1+(-1*i)]
        if start != end:
            changes += abs(ord(start)-ord(end))
    
    return changes

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()
