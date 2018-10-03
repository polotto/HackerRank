#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
from timeit import default_timer as timer

# Complete the freqQuery function below.
def freqQuery(queries):
    data = Counter()
    counter = Counter()
    output = []

    for q in queries:
        op = q[0]
        value = q[1]
        if op == 1:
            counter[data[value]] -= 1
            data[value] += 1
            counter[data[value]] += 1
        elif op == 2:
            if data[value] > 0:
                counter[data[value]] -= 1
                data[value] -= 1
                counter[data[value]] += 1
        elif op == 3:
            # print(counter[value], value)
            if counter[value] > 0:
                output.append(1)
            else:
                output.append(0)
    return output

if __name__ == '__main__':
    start = timer()
    scr_dir = os.path.dirname(__file__)
    fptr = open(os.path.join(scr_dir, './output/output.txt'), 'w')
    fptr_input = open(os.path.join(scr_dir, './input/input07.txt'), 'r')

    q = int(fptr_input.readline().strip())
    queries = []
    for _ in range(q):
        queries.append(list(map(int, fptr_input.readline().rstrip().split())))

    ans = freqQuery(queries)
    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')
    fptr.close()
    print(timer() - start)

def freqQueryForum(queries):
    freq = Counter()
    cnt = Counter()
    arr = []
    for q in queries:
        if q[0]==1:
            cnt[freq[q[1]]]-=1
            freq[q[1]]+=1
            cnt[freq[q[1]]]+=1
        elif q[0]==2:
            if freq[q[1]]>0:
                cnt[freq[q[1]]]-=1
                freq[q[1]]-=1
                cnt[freq[q[1]]]+=1
        else:
            if cnt[q[1]]>0:
                arr.append(1)
            else:
                arr.append(0)
    return arr

def freqQuery1Solution(queries):
    data = Counter()
    output = []
    for q in queries:
        op = q[0]
        value = q[1]
        if op == 1:
            data[value] += 1
        elif op == 2 and (value in data):
            data[value] -= 1
        elif op == 3:
            if value in data.values():
                output.append(1)
            else:
                output.append(0)
    return output