#!/bin/python3

import math
import os
import random
import re
import sys
from timeit import default_timer as timer

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    maximum = 0
    q_previous = [0,n]
    for q in queries:
        if q[0] >= q_previous[0] and q[1] <= q_previous[1]:
            maximum += q[2]
            q_previous = q
    
    return maximum

def arrayManipulationBruteForce(n, queries):
    arr = [0]*n
    maximum = 0
    
    for q in queries:
        for i in range(q[0] - 1, q[1]):
            arr[i] += q[2]
            maximum = max(maximum, arr[i])
    
    return maximum

if __name__ == '__main__':
    start = timer()
    scr_dir = os.path.dirname(__file__)
    fptr = open(os.path.join(scr_dir, './output.txt'), 'w')
    fptr_in = open(os.path.join(scr_dir, './input00.txt'), 'r')

    nm = fptr_in.readline().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, fptr_in.readline().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()

    print(result)
    print(timer() - start)
