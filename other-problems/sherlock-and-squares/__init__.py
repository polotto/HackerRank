#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the squares function below.
def squares(a, b):
    n = 1
    while n**2 < a:
        n = n + 1
    count = 0
    while n**2 <= b:
        count = count + 1
        n = n + 1
        
    return count

# first solution
def squares0(a, b):
    count = 0
    for i in range(a, b+1):
        if math.sqrt(i)%1 == 0:
            count = count + 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
