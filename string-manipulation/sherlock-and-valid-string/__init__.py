#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the isValid function below.
def isValid(s):
    freq = Counter()
    freq_v = Counter()
    for i in s:
        freq[i] += 1
        
    for i in freq.values():
        freq_v[i] += 1
    
    print(freq)
    print(freq_v)
    
    if len(freq_v) == 1:
        return 'YES'
    else:
        v = list(freq_v.values())
        for i in range(1, len(v)):
            if v[i] > 1:
                return 'NO'
        return 'YES'
    
if __name__ == '__main__':
    test = '03'
    scr_dir = os.path.dirname(__file__)
    fptr = open(os.path.join(scr_dir, './output/output.txt'), 'w')
    fptr_input = open(os.path.join(scr_dir, './input/input%s.txt' % test), 'r')
    fptr_result = open(os.path.join(scr_dir, './output/output%s.txt' % test), 'r')

    s = fptr_input.readline().rstrip()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()

    print(result, result == fptr_result.readline())