#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    d = []
    for i in range(1, len(q) + 1):
        for j in range(1, len(q) + 1):
            p = q[j-1]
            if p == i and j < i:
                d.append(abs(j - i))
    
    for k in d:
        if k > 2:
            print('Too chaotic')
    ans = sum(d)
    print(ans)
                

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
