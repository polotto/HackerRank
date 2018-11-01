#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the toys function below.
def toys(w):
    w_s = sorted(w)
    N = len(w_s)
    containers = 1
    base = w_s[0] + 4
    while True:
        # w_s = list(filter(lambda x: x > base, w_s))
        w_s = [x for x in w_s if x > base]
        if not w_s:
            break
        else:
            containers += 1
            base = w_s[0] + 4
            
    return containers

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    w = list(map(int, input().rstrip().split()))

    result = toys(w)

    fptr.write(str(result) + '\n')

    fptr.close()
