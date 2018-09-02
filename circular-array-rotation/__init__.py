#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the circularArrayRotation function below.
def circularArrayRotation(a, k, queries):
    # right rotation in python, based in
    # https://stackoverflow.com/a/46846544/7468664
    # https://stackoverflow.com/a/9457923/7468664
    if len(a) >= k :
        result = a[-k:] + a[:-k]
    else:
        # for big k, rotate one by one
        result = a
        for _ in range(k):
            for i in range(len(a)):
                j = i + 1
                if j == len(a):
                    result[0] = a[i]
                else:
                    result[j] = a[i]
    
    q_result = []
    for q in queries:
        q_result.append(result[q])
    return q_result

if __name__ == '__main__':
    scr_dir = os.path.dirname(__file__)

    fpIn = open(os.path.join(scr_dir, './input04.txt'), 'r')
    
    fptr = open(os.path.join(scr_dir, './output.txt'), 'w')

    nkq = fpIn.readline().split()

    n = int(nkq[0])

    k = int(nkq[1])

    q = int(nkq[2])

    a = list(map(int, fpIn.readline().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(fpIn.readline())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
