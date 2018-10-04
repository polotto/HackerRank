#!/bin/python3

import math
import os
import random
import re
import sys

def inverse(n):
    i = str(int(n))
    return int(i[::-1])

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    print('k %d' % k)
    b_days = int(0)
    for day in range(i, j+1):
        aux = abs(int(day) - inverse(day))
        print(aux)
        if not aux % k:
            b_days = b_days + 1
            print('b_day: %d' % b_days)
    return b_days

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = '13 45 3'.split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    #fptr.write(str(result) + '\n')
    print(str(result) + '\n')
    #fptr.close()
