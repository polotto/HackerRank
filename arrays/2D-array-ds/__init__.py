#!/bin/python3

import math
import os
import random
import re
import sys

def mult_sum(a, b):
    res = []
    for i in range(len(a)):
        row = []
        for j in range(len(a)):
            row.append(a[i][j]*b[i][j])
        res.append(row)
        
    sum = 0
    for i in range(len(res)):
        for j in range(len(res)):
            if res[i][j] == 0:
                continue
            else:
                sum = sum + res[i][j]
            
    return sum

def hourglass(kr, kc):
    hg = [[1, 1, 1, 0, 0, 0], 
          [0, 1, 0, 0, 0, 0], 
          [1, 1, 1, 0, 0, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0]]
    hg_rot = []
    for r in hg:
        hg_rot.append(r[-kr:] + r[:-kr])
    
    hg_rot = hg_rot[-kc:] + hg_rot[:-kc]
    
    return hg_rot

# Complete the hourglassSum function below.
def hourglassSum(arr):
    max_sum = -10**9
    for i in range(4):
        for j in range(4):
            hg = hourglass(i, j)
            ans = mult_sum(hg, arr)
            max_sum = ans if ans > max_sum else max_sum
            
    return max_sum            

if __name__ == '__main__':
    path = os.path.dirname(__file__)
    fptr = open(os.path.join(path, './output.txt'), 'w')

    test = '''-1 -1 0 -9 -2 -2
-2 -1 -6 -8 -2 -5
-1 -1 -1 -2 -3 -4
-1 -9 -2 -4 -4 -5
-7 -3 -3 -2 -9 -9
-1 -3 -1 -2 -4 -5'''.split('\n')
    
    arr = []

    for i in range(6):
        arr.append(list(map(int, test[i].rstrip().split())))

    print(arr)
    result = hourglassSum(arr)

    print(result)
    fptr.write(str(result) + '\n')

    fptr.close()
