#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the luckBalance function below.
def luckBalance(k, contests):
    # extract values from 2d array
    L = list(map(lambda x: x[0], contests))
    T = list(map(lambda x: x[1], contests))
    
    total_L = sum(L) # get the total of luck
    total_T = Counter(T)[1] # get how many important question have in the array
    
    # in this case, she can loses all the question to preserve the luck
    if k >= total_T:
        return total_L
    
    # filter all important contests, value == 1 
    contests_i = list(filter(lambda x: x[1] == 1, contests))
    # sort the values of important contest and get until N
    # where N is difference between k and total of important contests
    # this represent the min values that she needs win
    contests_i = sorted(contests_i, key = lambda x: x[0])[:abs(k-total_T)]
    
    # calculate the total points
    for c in contests_i:
        # need the 2* because we sum the value at begining
        total_L -= 2*c[0]
    
    # return the total
    return total_L

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
