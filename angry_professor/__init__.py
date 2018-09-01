#!/bin/python3

import math
import os
import random
import re
import sys

from os import path


# Complete the angryProfessor function below.
def angryProfessor(k, a):
    count = int(0)
    print('a length: %i' % len(a))
    for i in a:
        if i <= 0:
            count = int(count) + int(1)
    print('count: %i' % count)
    print('k: %i' % k)
    if count < k:
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    script_dir = os.path.dirname(__file__)

    fptrInput = open(os.path.join(script_dir, './input01.txt'), 'r')
    fptr = open(os.path.join(script_dir, './output03.txt'), 'w')
    
    t = int(fptrInput.readline()) # int(input())

    for t_itr in range(t):
        nk = fptrInput.readline().split()

        n = int(nk[0])

        k = int(nk[1])

        a = list(map(int, fptrInput.readline().rstrip().split()))

        result = angryProfessor(k, a)
        print('Result: %s' % result)
        fptr.write(result + '\n')

    fptr.close()
