#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    steps = n*[0]
    altitude = 0
    for i in range(n):
        if s[i] == 'U':
            altitude += 1
        else:
            altitude -= 1
        steps[i] = altitude
    
    valley = 0
    for j in range(n):
        if steps[j] == -1 and steps[j-1] == 0:
            valley += 1
    
    return valley
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
