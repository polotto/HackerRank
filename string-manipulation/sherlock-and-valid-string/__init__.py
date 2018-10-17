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
    freq_values = Counter()
    
    for i in freq.values():
        freq_values[i] += 1

    print(freq)
    print(freq.most_common())
    print(freq_values)
    print(freq_values.most_common())
    
    if len(freq_values) == 1:
        return 'YES'
    elif len(freq_values) > 2:
        return 'NO'
    else:
        most = freq_values.most_common()
        most_freq_kv = most[0]
        less_freq_kv = most[-1]
        print(most_freq_kv)
        print(less_freq_kv)

        if less_freq_kv[0] - less_freq_kv[1] == most_freq_kv[0] or less_freq_kv[0] - less_freq_kv[1] == 0:
            return 'YES'
        return 'NO'
    
if __name__ == '__main__':
    # tests = ['00', '01', '03', '04', '18']
    tests = ['00']
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