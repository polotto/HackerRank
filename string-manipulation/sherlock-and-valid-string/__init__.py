#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the isValid function below.
def isValid(s):
    freq = Counter(s)
    values = sorted(freq.values())
    v_max = max(values)
    v_min = min(values)
    max_count = values.count(v_max)
    min_count = values.count(v_min)

    print(values)
    print(v_max, v_min)
    print(max_count, min_count)

    if min_count == 1:
        return 'YES'
    elif v_max - max_count == v_min:
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    tests = ['00', '01', '03', '04', '18', '06']
    # tests = ['00']
    for test in tests:
        print(test)
        scr_dir = os.path.dirname(__file__)
        fptr = open(os.path.join(scr_dir, './output/output.txt'), 'w')
        fptr_input = open(os.path.join(scr_dir, './input/input%s.txt' % test), 'r')
        fptr_result = open(os.path.join(scr_dir, './output/output%s.txt' % test), 'r')

        s = fptr_input.readline().rstrip()

        result = isValid(s)

        fptr.write(result + '\n')

        fptr.close()
        test_result = fptr_result.readline().rstrip()
        print(result, test_result, result == test_result)