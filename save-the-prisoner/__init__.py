#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the saveThePrisoner function below.
def saveThePrisoner(n, m, s):
    # n prinsioners
    # m sweets
    # s start seat
    return math.ceil(m/n + s)

if __name__ == '__main__':
    scr_dir = os.path.dirname(__file__)
    fptr_in = open(os.path.join(scr_dir, './input03.txt'), 'r')
    fptr = open(os.path.join(scr_dir, './output03.txt'), 'w')

    t = int(fptr_in.readline())

    for t_itr in range(t):
        nms = fptr_in.readline().split()

        n = int(nms[0])

        m = int(nms[1])

        s = int(nms[2])

        result = saveThePrisoner(n, m, s)
        output = str(result) + '\n'
        print(output)
        fptr.write(output)

    fptr.close()
