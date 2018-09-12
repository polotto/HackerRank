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
            print(i, p, j)
            if p == i and j < i:
                d.append(abs(j - i))
    
    print(d)

    for k in d:
        if k > 2:
            print('Too chaotic')
            return
    ans = sum(d)
    print(ans)
                

if __name__ == '__main__':
    inp = '''2
5
2 1 5 3 4
5
2 5 1 3 4

8

5 - 2
7 - 2
8 - 2
6 - 1
1 2 3 4 5 6 7 8

1 2 5 3 4 6 7 8
1 2 5 3 7 4 6 8
1 2 5 3 7 8 4 6

1 2 5 3 7 8 6 4
    '''

    t = int(1)

    for t_itr in range(t):
        n = int(8)

        q = list(map(int, '1 2 5 3 7 8 6 4'.rstrip().split()))

        minimumBribes(q)
