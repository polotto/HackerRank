#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
from itertools import combinations

def sum_i(a, b):
    c = bin(int(a, 2) | int(b, 2))
    total = c.count('1')
    return total

# Complete the acmTeam function below.
def acmTeam(topic):
    N = len(topic)
    ans = Counter()

    for i, j in combinations(range(N), 2):
        total = sum_i(''.join(topic[i]), ''.join(topic[j]))
        ans[total] += 1
    
    max_ans = max(ans)
    return [max_ans, ans[max_ans]]
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
