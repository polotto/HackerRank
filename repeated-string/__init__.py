#!/bin/python3

import math
import os
import random
import re
import sys
from timeit import default_timer as timer

# Complete the repeatedString function below.
def repeatedString(s, n):
    count_a = s.count('a')
    n_s = math.floor(n / len(s))
    n_s_reamain = n % len(s)

    count_a_reamain = 0
    for i in range(n_s_reamain):
        if s[i] == 'a':
            count_a_reamain += 1
    
    ans = count_a * n_s + count_a_reamain
    
    return ans

if __name__ == '__main__':
    start = timer()
    scr_dir = os.path.dirname(__file__)
    fptr = open(os.path.join(scr_dir, './output.txt'), 'w')
    fptr_input = open(os.path.join(scr_dir, './input01.txt'), 'r')

    s = fptr_input.readline().rstrip()

    n = int(fptr_input.readline())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
    print(result)
    print(timer()-start)
