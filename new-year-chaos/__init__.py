#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    r = list(range(1, len(q) + 1))
    d = 0
    for i in range(len(q)):
        if r[i] != q[i]:
            #print(r)
            ir = r.index(q[i], q[i] - 1, q[i] + 10)
            #print(ir, q[i] - 1)
            a = r.pop(ir)
            r.insert(i, a)
            
            if abs(ir - i) > 2:
                print('Too chaotic')
                return
            d = d + abs(ir - i)
    print(d)

if __name__ == '__main__':
    dir_scr = os.path.dirname(__file__)
    input_tests = open(os.path.join(dir_scr, './input08.txt'), 'r')
    
    t = int(input_tests.readline())

    for _ in range(t):
        n = int(input_tests.readline())

        q = list(map(int, input_tests.readline().rstrip().split()))

        minimumBribes(q)
