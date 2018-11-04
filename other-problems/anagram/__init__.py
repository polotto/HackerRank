#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the anagram function below.
def anagram(s):
    N = len(s)
    if N % 2 != 0:
        return -1
    N_h = N // 2
    sub1 = list(s[:N_h])
    sub2 = list(s[N_h:])
    i = 0
    while i < len(sub1):
        aux = sub1[i]
        if aux in sub2:
            sub1.pop(i)
            j = sub2.index(aux)
            sub2.pop(j)
        else:
            i += 1
    
    return len(sub1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
