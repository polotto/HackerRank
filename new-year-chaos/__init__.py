#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    r = list(range(1, len(q) + 1))
    d = []
    for i in range(len(q)):
        if r[i] != q[i]:
            print(r)
            ir = r.index(q[i], q[i] - 1)
            print(ir, q[i] - 1)
            a = r.pop(ir)
            r.insert(i, a)
            d.append(abs(ir - i))
            print(q)
            print(r)
            print()
    if max(d) > 2:
        print('Too chaotic')
        return
    ans = sum(d)
    print(ans)
    
##    d = []
##    for i in range(1, len(q) + 1):
##        for j in range(1, len(q) + 1):
##            p = q[j-1]
##            if p == i and j < i:
##                d.append(abs(j - i))
##            elif p == i and len(q) > j and q[j] < p :
##                print(i, p, j)
##                d.append(abs(j - i))
##    
##    print(d)
##
##    for k in d:
##        if k > 2:
##            print('Too chaotic')
##            return
##    ans = sum(d)
##    print(ans)
                

if __name__ == '__main__':
    dir_scr = os.path.dirname(__file__)
    input_tests = open(os.path.join(dir_scr, './input09.txt'), 'r')
    
    
    t = int(input_tests.readline())

    for _ in range(t):
        n = int(input_tests.readline())

        q = list(map(int, input_tests.readline().rstrip().split()))

        minimumBribes(q)
