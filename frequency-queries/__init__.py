#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
from timeit import default_timer as timer

# Complete the freqQuery function below.
def freqQuery(queries):
    # count_data = defaultdict(int)
    data = defaultdict(int)
    output = []
    for q in queries:
        if q[0] == 1:
            data[q[1]] += 1
        elif q[0] == 2 and (q[1] in data):
            data[q[1]] -= 1
        elif q[0] == 3:
            if q[1] in data.values():
                output.append(1)
            else:
                output.append(0)
    return output

if __name__ == '__main__':
    start = timer()
    scr_dir = os.path.dirname(__file__)
    fptr = open(os.path.join(scr_dir, './output/output.txt'), 'w')
    fptr_input = open(os.path.join(scr_dir, './input/input09.txt'), 'r')

    q = int(fptr_input.readline().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, fptr_input.readline().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()

    # print(ans)
    print(timer() - start)
