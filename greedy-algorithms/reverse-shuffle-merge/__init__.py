#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import permutations

def reverse(s):
    return s[::-1]

def diff(s, r):
    ans = s
    for j in r:
        ans = ans.replace(j,'', 1)
    return ans

def rotate(s, n):
    return s[-n:] + s[:-n]

# Complete the reverseShuffleMerge function below.
def reverseShuffleMerge(s):
    N = len(s)
    s1 = s[:N//2]
    # print(s1, s2)
    r_s1 = reverse(s1)
    d_s = diff(s, r_s1)
    print(r_s1, d_s)
    # perms = [''.join(p) for p in permutations(s1)]
    # perms = sorted(perms)
    # print(perms)
    ans = r_s1
    while ans >= s1:
        print(ans)
        ans = rotate(ans, 1)
    return ans

if __name__ == '__main__':
    test_case = '15'
    sc_dir = os.path.dirname(__file__)
    fp_in = open(os.path.join(sc_dir, './input/input%s.txt' % test_case), 'r')
    fp_test = open(os.path.join(sc_dir, './output/output%s.txt' % test_case), 'r')

    s = fp_in.readline().rstrip()

    result = reverseShuffleMerge(s)
    test_result = fp_test.readline().strip()

    print(result, test_result, result == test_result)
