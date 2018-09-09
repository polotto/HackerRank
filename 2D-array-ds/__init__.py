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

def hourglass(pos):
    if pos == 0:
        hg = [[1, 1, 1, 0, 0, 0], 
              [0, 1, 0, 0, 0, 0], 
              [1, 1, 1, 0, 0, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0]]
        
    

# Complete the hourglassSum function below.
def hourglassSum(arr):
    
    
    print(mult_sum(hg, arr))
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
