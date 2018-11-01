#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

def swaps(arr_e):
    vis = defaultdict(bool)
    ans = 0
    j = 0
    for i in range(len(arr_e)):
        if vis[i]:
            continue

        j = i
        cycles = 0
        while not vis[j]:
            vis[j] = True
            j = arr_e[j][0]
            cycles += 1
        
        if cycles > 0:
            ans += cycles - 1
    
    return ans

# Complete the lilysHomework function below.
def lilysHomework(arr):
    arr_e = list(enumerate(arr))
    arr_s = sorted(arr_e, key=lambda x: x[1])
    ans1 = swaps(arr_s)
    arr_s = sorted(arr_e, key=lambda x: x[1], reverse = True)
    ans2 = swaps(arr_s)

    return min(ans1, ans2)

if __name__ == '__main__':
    test_case = '01'
    scr_dir = os.path.dirname(__file__)
    fp_in = open(os.path.join(scr_dir, './input/input%s.txt' % test_case), 'r')
    fp_out = open(os.path.join(scr_dir, './output/output%s.txt' % test_case), 'r')

    n = int(fp_in.readline().rstrip())

    arr = list(map(int, fp_in.readline().rstrip().split()))

    result = lilysHomework(arr)

    result_test = int(fp_out.readline().rstrip())
    print(result, result_test, result == result_test)
