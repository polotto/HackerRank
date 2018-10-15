#!/bin/python3

import math
import os
import random
import re
import sys
from timeit import default_timer as timer

def number_needed(a, b):
    count = 0
    for i in range(97, 123):
        ia = sum(letter == chr(i) for letter in a)
        ib = sum(letter == chr(i) for letter in b)
        count += abs(ia-ib)
    return count

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    a_s = list(a)
    b_s = list(b)
    
    if len(a_s) > len(b_s):
        a_s, b_s = b_s, a_s

    i = 0
    while i < len(a_s):
        n_i = a_s[i]
        if n_i in b_s:
            j = b_s.index(n_i)
            del b_s[j]
            j = a_s.index(n_i)
            del a_s[j]
            i -= 1
        i += 1
    total = len(a_s) + len(b_s)
    return total

if __name__ == '__main__':
    start = timer()
    test_n = '01'
    scr_dir = os.path.dirname(__file__)
    fptr = open(os.path.join(scr_dir, './output/output.txt'), 'w')
    fptr_input = open(os.path.join(scr_dir, './input/input%s.txt' % test_n), 'r')
    fptr_resp = open(os.path.join(scr_dir, './output/output%s.txt' % test_n), 'r')

    a = fptr_input.readline().rstrip()

    b = fptr_input.readline().rstrip()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
    res_exp = int(fptr_resp.readline().rstrip())
    print(res, res_exp, res_exp == res)
    print(timer() - start)