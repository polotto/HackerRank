#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxMin function below.
def maxMin(k, arr):
    ans = 10**9
    arr_s = sorted(arr)
    for i in range(len(arr) - k + 1):
        sub_arr_min = arr_s[i]
        sub_arr_max = arr_s[i+k-1]
        ans = min(sub_arr_max - sub_arr_min, ans)
    return ans

if __name__ == '__main__':
    scr_dir = os.path.dirname(__file__)
    fp_in = open(os.path.join(scr_dir, './input/input16.txt'), 'r')

    n = int(fp_in.readline())

    k = int(fp_in.readline())

    arr = []

    for _ in range(n):
        arr_item = int(fp_in.readline())
        arr.append(arr_item)

    result = maxMin(k, arr)

    print(result)
