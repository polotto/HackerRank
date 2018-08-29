#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the angryProfessor function below.
def angryProfessor(k, a):
    count = int(0)
    for i in a:
        if i >= 0:
            count = int(count) + int(1)
    
    if count <= k:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open('output02', 'w')
    fptrInput = open('input03.txt', 'w')
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        fptr.write(result + '\n')

    fptr.close()
