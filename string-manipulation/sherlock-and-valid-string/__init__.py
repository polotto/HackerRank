#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the isValid function below.
def isValid(s):
    # frequencies of all letters
    freq = Counter(s)
    # frequencies values sorted
    values = sorted(freq.values())
    # max frequencie value
    v_max = max(values)
    # min frequencie value
    v_min = min(values)
    # max frequencie value repetitions
    max_count = values.count(v_max)
    # min frequencie value repetitions
    min_count = values.count(v_min)
    # frequencie of frequencie values, made some validations more easy 
    freq_values = Counter(values)

    # more then 2 frequencies repeat, this case string can be valid, case: aaabbc
    if len(freq_values) > 2:
        return 'NO'
    # only 1 frequencie repeat, so, is a valid string, case: aabbcc
    elif len(freq_values) == 1:
        return 'YES'
    # min frequencie count is 1, so, just remove one value to turn the string valid, case: aab
    elif min_count == 1:
        return 'YES'
    # max frequencie minus your repeatitions equal min value, case: bbaaa, just remove
    # one of the same letter repeatitions to turn the strig valid
    elif v_max - max_count == v_min:
        return 'YES'
    # other cases are not valids
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