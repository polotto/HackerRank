#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the freqQuery function below.
def freqQuery(queries):
    count_data = defaultdict(int)
    data = []
    for q in queries:
        if q[0] == 1:
            data.append(q[1])
            count_data[q[1]] += 1
        elif q[0] == 2 and (q[1] in data):
            del data[data.index(q[1])]
            count_data[q[1]] += 1
        else:
            count_data.

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
