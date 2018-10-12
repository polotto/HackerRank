#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
from timeit import default_timer as timer

# Complete the commonChild function below.
# function LCSLength(X[1..m], Y[1..n])
#     C = array(0..m, 0..n)
#     for i := 0..m
#        C[i,0] = 0
#     for j := 0..n
#        C[0,j] = 0
#     for i := 1..m
#         for j := 1..n
#             if X[i] = Y[j]
#                 C[i,j] := C[i-1,j-1] + 1
#             else
#                 C[i,j] := max(C[i,j-1], C[i-1,j])
#     return C[m,n]
# https://pypy.org/download.html#default-with-a-jit-compiler
# https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
# https://www.martinkysel.com/hacker-rank-common-child-solution/
def commonChild(s1, s2):
    common = [[0 for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]
    for i, s_i in enumerate(s1):
        for j, s_j in enumerate(s2):
            if s_i == s_j:
                common[i + 1][j + 1] = common[i][j] + 1
            else:
                common[i + 1][j + 1] = max(common[i + 1][j], common[i][j + 1])
    return  common[-1][-1]

if __name__ == '__main__':
    start = timer()
    scr_dir = os.path.dirname(__file__)
    fptr = open(os.path.join(scr_dir, './output/output.txt'), 'w')
    fptr_input = open(os.path.join(scr_dir, './input/input05.txt'), 'r')
    
    s1 = fptr_input.readline().rstrip()

    s2 = fptr_input.readline().rstrip()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()

    print(result)
    print(timer() - start)
