#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    ans = 0
    for passnum in range(len(arr)-1, 0, -1):
        print(passnum)
        for i in range(passnum):
            if arr[i] > arr[i+1]:
                a = arr[i]
                b = arr[i+1]
                arr[i+1] = a
                arr[i] = b
                ans += 1
                print(arr)

    return ans


if __name__ == '__main__':
    dir_scr = os.path.dirname(__file__)
    fptr = open(os.path.join(dir_scr, './output.txt'), 'w')
    input_test = open(os.path.join(dir_scr, './input0.txt'), 'r')
    n = int(input_test.readline())

    arr = list(map(int, input_test.readline().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
    
    print(res)